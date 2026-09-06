# Prototype implementation workflow

Use this reference when converting visual prototypes or screenshots into an existing functional application.

## Evidence hierarchy

Resolve conflicts in this order unless the user says otherwise:

1. Explicit current user instruction.
2. Product requirements and required interactions.
3. Approved reference screenshot for that route and state.
4. Exported prototype HTML/CSS and design-system files.
5. Existing UI conventions.

The screenshot is not permission to copy fake numbers, dead controls, or placeholder content into production. Preserve real data and make intentional empty states visually consistent with the reference.

## Page-state matrix

Before editing, create a compact matrix with route, stable state ID, business-facing state name, reference file, current implementation file, real data source, primary action, known mismatch, and verification status. Preserve machine state IDs exactly when the application already defines them; translate them in a separate business-name field.

For a workflow product, typical states include empty, in progress, waiting for approval, failed with local retry, completed with final artifact, and archived or superseded.

## Reference extraction

From the visual and exported code, capture canvas width, content max-width, header dimensions, grid columns, card aspect ratios, font ladder, colors, borders, shadows, buttons, media fitting, and responsive breakpoints.

Do not copy generated markup wholesale into a mature application. Map reference components onto the application's real components and data flow.

## Implementation strategy

- Establish design tokens and the shared shell first.
- Work route by route and state by state.
- Keep edits localized when existing behavior is correct.
- Reuse real API/database queries and mutation handlers.
- Keep destructive or costly actions behind existing confirmation boundaries.
- Preserve versioning, retry, and rollback behavior when redesigning workflow controls.
- Make the final artifact or main result visually dominant on completed pages.
- Show a live node or step preview while work is underway when previews exist.

## Avoid these failure modes

- Declaring the redesign complete after changing only the homepage.
- Using one generic layout for reference pages with materially different modules.
- Replacing real records with attractive fake dashboard data.
- Hiding functions without providing a secondary location.
- Making technical status the main language for a nontechnical operator.
- Testing only source code instead of the rendered browser result.
- Fixing one local overflow by shrinking all text.
