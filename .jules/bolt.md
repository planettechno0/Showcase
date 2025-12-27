# Bolt's Journal

## 2024-05-22 - [Optimizing DOM Updates]
**Learning:** Batching DOM updates using `DocumentFragment` significantly reduces reflows compared to appending elements one by one in a loop.
**Action:** Always use `DocumentFragment` when rendering lists of items.

## 2024-05-23 - [Image Loading Strategy]
**Learning:** Relying solely on `onerror` for image fallbacks can cause layout shifts and "broken image" icons to flash.
**Action:** Implement a skeleton loader or placeholder strategy to handle the loading state gracefully.
