import json, os, time, urllib.request, urllib.error

BASE = "https://henjb.com/design/asset/"
with open("collection.json", encoding="utf-8") as f:
    designs = json.load(f)["designs"]

total = done = skipped = errors = 0
os.makedirs("design/asset", exist_ok=True)

for i, d in enumerate(designs, 1):
    did = str(d["id"])
    folder = os.path.join("design", "asset", did)
    os.makedirs(folder, exist_ok=True)

    files = ["nav.png"] if did == "default" else ["nav.png", "icon.png"]

    for name in files:
        total += 1
        path = os.path.join(folder, name)
        if os.path.exists(path) and os.path.getsize(path) > 0:
            skipped += 1
            continue

        url = BASE + did + "/" + name
        for attempt in range(3):
            try:
                req = urllib.request.Request(
                    url, headers={"User-Agent": "Mozilla/5.0"}
                )
                with urllib.request.urlopen(req, timeout=20) as r:
                    data = r.read()
                if not data.startswith(b"\x89PNG\r\n\x1a\n"):
                    raise ValueError("الملف ليس PNG صالح")
                with open(path, "wb") as out:
                    out.write(data)
                done += 1
                break
            except Exception as e:
                if attempt == 2:
                    errors += 1
                    print("تعذر:", did, name, str(e)[:100])
                else:
                    time.sleep(2)

    if i % 25 == 0:
        print(f"التصاميم: {i}/{len(designs)} | نزل: {done} | موجود: {skipped} | أخطاء: {errors}")
    time.sleep(0.08)

print("\nكمل التحميل.")
print("ملفات جديدة:", done, "| موجودة مسبقًا:", skipped, "| أخطاء:", errors)
