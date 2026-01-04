# Bolt's Journal

## 2024-05-23 - [DOM Batching with DocumentFragment]
**Learning:** In a vanilla JS Single File Application without a Virtual DOM, manual DOM manipulation in loops causes significant reflows. Using `DocumentFragment` to batch appends effectively mitigates this.
**Action:** When inspecting vanilla JS `render` loops, always check if elements are appended one-by-one. If so, refactor to use `DocumentFragment`.
