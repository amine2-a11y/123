# AMINE PS4 — Offline Cache Stability Report

Date: 2026-10-12

## Confirmed project defects fixed
- Corrected missing AppCache manifest references in the 7.00 and 9.00 cache pages (they referenced filenames that did not exist).
- Restored the expected `goldhen.bin` file for the 7.00 host and aligned the GoldHEN payload filenames in the 5.05, 6.72, and 7.00 folders with the project's newer bundled payload (SHA-256 prefix `df3f27c1b35bc7c4`). This keeps the cache targets present and avoids shipping the older payload under the legacy filename.
- Removed the invalid `core.js?v=10` AppCache entry from the 13.00 manifest; the file is already listed as `core.js`.
- Bumped manifest version comments so AppCache can detect the updated manifests.
- Dedicated cache pages now stay open after success/failure instead of automatically navigating away.

## Validation
- Local manifest-reference audit is run when packaging; see result in the final response.
- ZIP integrity is checked after packaging.

## Limitations
- This is a static file/path audit, not a real PS4 browser test. AppCache can still fail if the host server does not serve manifest files with a compatible MIME type, if the browser's cache is corrupt/full, or if a particular firmware/browser does not support the expected cache behavior.
- GoldHEN compatibility is firmware-specific; a shared version label or file cannot guarantee execution on every PS4 firmware.


## Zombie theme visibility fix (2026-10-12)
- Added a CSS override to 27 HTML pages so the bundled `zombie-bg.jpg` is actually referenced as the page background.
- Copied the image beside each HTML file to make relative paths work inside nested firmware folders.
- Static archive/path validation only; the background and offline cache still require testing in the PS4 browser and hosting environment.
