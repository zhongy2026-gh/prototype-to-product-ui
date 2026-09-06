# Prototype to Product UI

`prototype-to-product-ui` is a Codex Skill for turning product requirements, Stitch/Figma exports, screenshots, or an existing web interface into a functional, visually verified product UI.

It is designed for work where visual fidelity and real behavior both matter. The Skill keeps existing data and business logic intact, adapts the interface to the operator's level of technical expertise, checks every required route and state, and finishes with a practical launch and handoff path.

## What it helps with

- Implement a Stitch or Figma prototype in an existing application.
- Compare reference screenshots with rendered pages route by route.
- Redesign a technical dashboard for nontechnical operators.
- Connect high-fidelity UI to real data instead of prototype placeholders.
- Make previews, decisions, progress, and final deliverables easy to find.
- Check typography, wrapping, overflow, responsive behavior, and state variants.
- Prepare a local launch flow or deployment handoff without changing data unintentionally.

## When not to use it

Do not use this Skill for a deliberately nonfunctional visual mockup, standalone graphic design, backend-only debugging, native mobile development, or infrastructure-only deployment.

## Installation

Clone or download this repository, then copy the `prototype-to-product-ui` folder into your Codex skills directory:

```text
~/.codex/skills/prototype-to-product-ui/
```

The installed folder must contain `SKILL.md` at its root. Restart or refresh Codex if the Skill does not appear immediately.

## Usage

Invoke it explicitly:

```text
Use $prototype-to-product-ui to compare these Stitch screens with my existing app, implement every required page and state, preserve real data, and complete visual and functional acceptance.
```

For a nontechnical product owner:

```text
Use $prototype-to-product-ui to redesign this dashboard so I only handle business decisions. Keep technical controls available under maintenance, and guide me through the final UI review.
```

## Workflow

1. Establish the real project, routes, data, commands, and constraints.
2. Build a page-state matrix connecting references to implementation.
3. Extract design tokens and shared layout rules.
4. Implement the primary journey, secondary pages, and state variants.
5. Preserve real data, mutations, approvals, retries, and rollback behavior.
6. Compare rendered pages with references at matching viewports.
7. Run functional checks and prepare the appropriate launch path.
8. Deliver an acceptance report with remaining mismatches and next actions.

## Repository contents

```text
prototype-to-product-ui/
├── README.md
├── LICENSE
├── SKILL.md
├── VALIDATION.md
├── .gitignore
├── agents/openai.yaml
├── references/
│   ├── prototype-implementation.md
│   ├── visual-qa.md
│   └── local-launch-and-handoff.md
├── templates/
│   ├── page-state-matrix.md
│   └── ui-acceptance-report.md
├── scripts/
│   └── validate_package.py
└── examples/
    └── stitch-to-existing-app.md
```

## Safety and privacy

- Do not commit API keys, credentials, databases, private screenshots, customer data, generated media, or local backups.
- Replace machine-specific absolute paths with project-relative paths in public examples.
- UI redesign does not authorize changing production records, enabling paid APIs, exposing a local service publicly, or adding startup persistence.
- Back up mutable data before migrations or risky deployment changes.

## Validation

Run the dependency-free package check:

```text
python3 scripts/validate_package.py .
```

Also validate the Skill structure with the Codex `skill-creator` validator when available:

```text
python quick_validate.py /path/to/prototype-to-product-ui
```

Structural validation is only the first layer. A release should also pass an isolated behavior test using a fictional project and the acceptance criteria in `templates/ui-acceptance-report.md`.

The current release evidence is recorded in [VALIDATION.md](VALIDATION.md).

## License

MIT. See [LICENSE](LICENSE).
