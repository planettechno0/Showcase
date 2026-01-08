## 2024-05-23 - Batch DOM updates in Vanilla JS
**Learning:** `DocumentFragment` significantly reduces reflows when appending multiple elements in a loop, even in small applications.
**Action:** Always verify if a loop appending to the DOM can be batched using `DocumentFragment` or by building a single string.
