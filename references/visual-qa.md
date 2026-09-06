# Visual QA and readability

Use this reference for screenshot comparison, typography changes, responsive checks, and final UI acceptance.

## Compare at the same conditions

- Use the reference viewport or match its aspect ratio closely.
- Compare the same route, state, data, and scroll position.
- Prefer actual browser screenshots over mental comparison with source code.
- Check representative desktop and narrow layouts when responsive behavior matters.

## Review order

1. Global composition: page width, header, major columns, vertical rhythm.
2. Information hierarchy: what the eye sees first, primary action, current status.
3. Component geometry: card size, padding, alignment, border radius, media crop.
4. Typography: size, weight, line height, wrapping, contrast.
5. State fidelity: empty, pending, failure, completed, selected, disabled.
6. Interaction visibility: buttons, tabs, filters, preview controls, download links.
7. Overflow and clipping: horizontal scroll, truncated labels, hidden sticky controls.

## Readable type ladder

Use as a starting point for a desktop business interface, not an absolute design law:

- page title: 28-36px;
- section title: 18-24px;
- card title: 14-18px;
- body and form input: 14-16px;
- buttons and ordinary metadata: 12-14px;
- compact labels, badges, timestamps, and audit facts: at least 11px.

Raise small text selectively. Do not uniformly scale every element: it often breaks the original hierarchy and grid. After changing the lower end of the scale, inspect navigation, card headers, badges, tables, action bars, and narrow breakpoints.

## Observable checks

For each required route, confirm there are no console errors, unintended horizontal overflow, undersized meaningful text, unexpected button wrapping, card collisions, obscuring sticky elements, broken media previews, or misleading empty states.

Treat automated pixel comparison as supporting evidence, not the sole acceptance criterion. Real data often changes text length and requires human judgment.

