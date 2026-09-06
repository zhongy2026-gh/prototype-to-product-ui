# Page-state matrix

> Copy this file into the target project. Keep one row for every route and materially different state that must be implemented or verified.

## Project facts

- Product:
- Application root:
- Framework:
- Primary operator:
- Reference location:
- Data source:
- Start command:
- Validation commands:
- Target viewport(s):
- Constraints and actions requiring approval:

## Matrix

| Route or entry | State ID | Business state | Reference | Implementation | Real data source | Primary user action | Current mismatch | Status |
|---|---|---|---|---|---|---|---|---|
| `/` | `default` | 默认首页 | `references/home.png` | `app/page.tsx` | project query | Open current work | Header and card density differ | Not started |
| `/items/new` | `empty_form` | 空白创建表单 | `references/create.png` | `app/items/new/page.tsx` | form schema | Create item | Missing guidance panel | Not started |
| `/items/:id` | `awaiting_approval` | 等待确认 | `references/detail-review.png` | `app/items/[id]/page.tsx` | item and approval queries | Approve or request revision | Preview is not prominent | Not started |

Allowed status values: `Not started`, `In progress`, `Needs review`, `Verified`, `Blocked`.

## Shared design decisions

| Area | Decision | Evidence | Applies to |
|---|---|---|---|
| Typography | 15px body, 11px meaningful minimum | approved reference and readability review | all desktop routes |
| Primary action | one dominant action per state | product requirement | workflow pages |

## Open decisions

| Decision needed | Why it matters | Safe default | Owner |
|---|---|---|---|
|  |  |  |  |

## Verification log

| Date | Route/state | Viewport | Visual result | Functional result | Evidence | Remaining issue |
|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |
