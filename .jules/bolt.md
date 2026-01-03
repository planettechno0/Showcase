## 2024-05-22 - Batching DOM Updates
**Learning:** In this Vanilla JS SPA, the `render` function directly appended elements to the DOM inside a `forEach` loop. This caused N reflows (where N is product count) immediately upon load or filter change.
**Action:** Always use `DocumentFragment` to batch DOM nodes in memory and append them in a single operation to minimize layout thrashing in this specific architecture.
