---
name: prototype-to-product-ui
description: Turn product requirements, Stitch/Figma exports, screenshots, or an existing web app into a functional, high-fidelity interface with real data, business-friendly flows, visual comparison, regression checks, and an appropriate local or hosted launch path. Use for webpage UI redesign, prototype implementation, page-by-page visual matching, frontend usability simplification, or production-readiness work; do not use for a visual mockup that is intentionally nonfunctional.
---

# Prototype to Product UI

Build a usable product interface, not a disconnected visual shell. Preserve existing business logic, data, workflows, permissions, and artifacts unless the user explicitly asks to change them.

## Start by establishing the truth

1. Identify the real application root, framework, routes, data source, start command, and validation commands. Read project recovery or product documents when present; do not scan unrelated folders.
2. Inventory the required pages and states. Distinguish product requirements, visual references, current implementation, and live data behavior.
3. If references include exported HTML/CSS and screenshots, treat both as evidence: screenshots define the visible target; exported code helps recover colors, spacing, typography, and component structure.
4. Record mismatches page by page before editing. Do not assume that matching the homepage proves the remaining routes match.

For detailed implementation guidance, read [references/prototype-implementation.md](references/prototype-implementation.md).
When the project has multiple routes or UI states, copy and fill [templates/page-state-matrix.md](templates/page-state-matrix.md) instead of keeping the audit only in conversation.

## Translate for the actual operator

Adapt information architecture and wording to the user's expertise. For a nontechnical operator:

- lead with current work, pending decisions, progress, previews, and deliverables;
- keep database, registry, logs, tests, backend state, and recovery controls outside the default workflow;
- expose one clear primary action per state;
- translate system status into business language while retaining technical details in a secondary or collapsible area;
- automate routine steps and stop only at subjective, expensive, irreversible, or risky decisions.

Do not hide required functionality merely to make a screen look clean. Move advanced functions to an intentional maintenance surface.

## Implement in controlled passes

Use this order unless the product demands otherwise:

1. Shared shell and design tokens: navigation, page width, colors, typography, buttons, cards, spacing, and responsive rules.
2. Primary journey: home, create/start, list, detail/workspace, approval/review, and final result.
3. Secondary surfaces: asset library, settings, audit, recovery, and capability management.
4. State variants: empty, running, awaiting approval, failed/retry, completed, and unavailable.
5. Real data and interactions: reuse existing queries and actions; never replace real records with invented prototype metrics.

Prefer reusable components and tokens, but allow page-specific composition when the reference genuinely differs. Visual fidelity does not require forcing unlike modules into one generic card.

## Verify visually and functionally

After each meaningful pass, render the actual routes at the intended viewport and compare them with the corresponding references. Check hierarchy, density, alignment, visible states, text wrapping, media previews, controls, and scroll behavior—not only colors.

Use a readable type system. For desktop business tools, treat 15px body text and an 11px minimum for meaningful labels as a practical default, then adjust for the design and language. Decorative marks may be smaller only when they carry no information.

Read [references/visual-qa.md](references/visual-qa.md) before final visual acceptance.
Use [templates/ui-acceptance-report.md](templates/ui-acceptance-report.md) when the user needs a durable review record or GitHub handoff.

Run the project's existing lint, tests, build, and health checks in proportion to the change. A visual pass is incomplete if core actions, routes, or real-data rendering regress.

## Launch and handoff

Choose a launch model that matches the user's needs: development server, manually launched local app, background service, or hosted site. Never enable login/startup persistence, public exposure, paid APIs, or external services without explicit authorization.

Read [references/local-launch-and-handoff.md](references/local-launch-and-handoff.md) when the user needs a local application, desktop launcher, deployment, recovery document, or operational handoff.

## Completion criteria

Finish only when:

- required routes and state variants have been checked individually;
- the UI uses real data or clearly labelled intentional empty states;
- primary business actions are understandable without technical knowledge;
- previews and final deliverables are easy to find;
- typography is readable and no tested viewport has unintended horizontal overflow;
- existing functional checks pass;
- the user has a clear way to open, stop, recover, and continue improving the product.

Report what changed, what was verified, any remaining mismatch, and the exact launch or review entry point.

For an end-to-end fictional example, read [examples/stitch-to-existing-app.md](examples/stitch-to-existing-app.md) only when a concrete demonstration would help interpret the workflow.
