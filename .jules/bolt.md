## 2024-05-22 - [DOM Batching with DocumentFragment]
**Learning:** In Vanilla JS applications, appending elements directly to the DOM in a loop causes a reflow/repaint for every iteration. This is a significant bottleneck compared to frameworks like React/Vue that handle batching automatically.
**Action:** Always use `DocumentFragment` to batch DOM insertions when rendering lists in Vanilla JS. This reduces N reflows to 1.
