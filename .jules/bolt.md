## 2024-05-22 - DocumentFragment Batching
**Learning:** This vanilla JS codebase relies heavily on manual DOM manipulation. Appending elements in loops directly to the DOM causes massive reflow overhead.
**Action:** Always buffer DOM insertions into a `DocumentFragment` before appending to the live document, especially in the `render` function.
