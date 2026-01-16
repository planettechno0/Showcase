# BOLT'S JOURNAL ⚡

## 2024-05-22 - [DOM Batching with DocumentFragment]
**Learning:** Direct DOM manipulation in loops causes layout thrashing (repeated reflows). Using `DocumentFragment` allows batching these updates into a single reflow, significantly improving rendering performance for lists.
**Action:** Always use `DocumentFragment` when appending multiple elements to the DOM in vanilla JS.
