## 2026-01-09 - Single File Application DOM Strategy
**Learning:** This codebase is a Single File Application (Vanilla JS) without a framework. Direct DOM manipulation in loops causes significant reflow/repaint overhead.
**Action:** Always use `DocumentFragment` for batching DOM insertions in this specific codebase, as there is no Virtual DOM to handle this automatically.
