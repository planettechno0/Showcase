## 2024-05-23 - DOM Manipulation
**Learning:** In vanilla JS projects without a build step, simple DOM batching (DocumentFragment) yields significant wins (~65% faster rendering) with minimal code change.
**Action:** Always look for loops appending to DOM and replace with DocumentFragment.
