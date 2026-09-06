# Example: Stitch prototype to an existing content-review app

This fictional example demonstrates the expected reasoning and deliverables. It contains no production data and does not prescribe a framework.

## User request

> I have an existing content-review dashboard with real projects and approvals. The Stitch folder contains reference screens for Home, New Project, Project Detail, Approval Center, Assets, and Settings. Redesign the existing UI to match the references. I am a nontechnical editor, so keep database and system tools out of my daily workflow. Do not replace real records with sample data. Run locally and do not enable automatic startup.

## Inputs discovered

- Existing routes: `/`, `/projects/new`, `/projects`, `/projects/:id`, `/approvals`, `/assets`, `/settings`.
- Real data: local project, approval, and artifact queries.
- Reference set: one screenshot and one exported HTML file per route; Project Detail has review, failure, and completed variants.
- Validation: lint, automated tests, production build, and a health command.
- Launch preference: manual local launch only.

## Initial page-state matrix

| Route | State | Primary action | Main mismatch | Planned treatment |
|---|---|---|---|---|
| `/` | no pending work | Open recent project | Current page is a generic empty dashboard | Rebuild hierarchy with real recent-project data |
| `/projects/new` | empty form | Create project | Too many technical fields | Keep topic and content primary; move options to secondary controls |
| `/projects/:id` | awaiting approval | Review current output | Preview is buried below logs | Put preview in the central workspace and the decision at right |
| `/projects/:id` | failed | Retry current step | Whole-project restart is emphasized | Expose local step retry; retain technical error details below |
| `/projects/:id` | completed | Play or download final | Final result is difficult to find | Place final player at the top |
| `/approvals` | mixed queue | Approve or revise | Cards do not distinguish media types | Add appropriate image/video preview and clear decision controls |
| `/assets` | populated | Preview or download | Files are shown as a technical table | Add visual library and inspector while keeping real artifact IDs |
| `/settings` | healthy | Inspect maintenance area | Technical pages dominate navigation | Group them under Maintenance and Settings |

## Decisions made

1. The reference screenshot defines visible composition; the exported HTML supplies token evidence.
2. Existing queries and mutation handlers stay unchanged.
3. Dashboard counts come from real data. Missing data creates an intentional empty state, never invented metrics.
4. Daily navigation contains Home, Projects, and Approvals. Assets and technical tools move under Maintenance and Settings.
5. Completed projects lead with the final player. Active projects lead with a node preview. Failed nodes offer only local retry.
6. Body text starts at 15px and meaningful compact labels at 11px, followed by overflow testing.
7. The local service starts only from a user-invoked launcher.

## Implementation passes

### Pass 1: shared shell

- Implement global navigation, width, color, typography, button, card, and breakpoint tokens.
- Verify the shell on every route before declaring it complete.

### Pass 2: primary journey

- Implement Home, New Project, Projects, Project Detail, Approvals, and completed-result states.
- Connect all visible values and actions to existing data and handlers.

### Pass 3: secondary surfaces and variants

- Implement Assets and Settings.
- Verify empty, running, approval, failed, completed, and unavailable states.

### Pass 4: visual and functional acceptance

- Capture each route at the reference viewport.
- Check hierarchy, card geometry, text wrapping, previews, sticky actions, and overflow.
- Run lint, tests, build, and health checks.

## Example acceptance summary

| Check | Result |
|---|---|
| Required routes reviewed individually | Pass |
| Real data preserved | Pass |
| Primary business action clear | Pass |
| Completed result prominent | Pass |
| Node or step preview visible | Pass |
| Meaningful text below 11px | None found |
| Unintended horizontal overflow | None found |
| Lint, tests, build, health | Pass |
| Automatic startup | Disabled as requested |

## Handoff

The user receives the exact local launch entry, the completed page-state matrix, the UI acceptance report, known differences, and the next recommended improvement. No database records, external APIs, or public deployment settings were changed as part of the UI redesign.
