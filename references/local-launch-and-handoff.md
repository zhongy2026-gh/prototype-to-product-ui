# Local launch, deployment, and handoff

Use this reference when a webpage must behave like a locally installed product or when development needs a durable recovery path.

## Select the launch model

- Development server: appropriate during active implementation; it exists only while the process is running.
- Manual local application: suitable for a nontechnical owner who wants a desktop button and no startup/background behavior.
- Background service: suitable only when continuous availability is intentionally requested and resource use is acceptable.
- Hosted site: suitable when access from other devices or users is required; assess authentication, storage, privacy, and cost first.

Explain that `localhost` is an address served by a running local process, not a permanently available website.

## Manual local application pattern

A reliable desktop launcher should locate the application explicitly, run a health check, start the service only when needed, wait for the local URL, open the browser, and show a useful recovery message if startup fails.

Provide a separate repair or diagnostic entry only when the owner can benefit from it. Do not auto-start at login unless explicitly requested.

## Data and update safety

- Identify where the database and uploaded or generated assets live.
- Keep UI code changes separate from production data changes.
- Back up mutable local data before migrations or risky upgrades.
- Preserve existing data when replacing the UI.
- Verify that updated code can restart without silently switching databases.
- Avoid publishing local services to the network by default.

## Validation before handoff

Run the project's applicable lint, tests, build, health, database-integrity, and route smoke checks. Reopen the product through the same entry the user will use.

## Recovery document

Maintain one canonical recovery document for a long-running project. Include product purpose, user profile, current status, project path, launch entry, data and backup locations, completed pages and states, current issues, next action, actions not to repeat, and last validation results.

Update it from verified current state, not remembered counts or stale notes.
