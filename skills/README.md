# Agent skills in this repository

Start here when an agent needs a reusable workflow rather than only the AutoCAD MCP API. Follow the closest task route and load only the references required by that skill.

| Skill | Use it for | Entry point |
| --- | --- | --- |
| Industrial product design | Product briefs, concept/design development, native 3D, review, and engineering handoff | [`industrial-product-design/SKILL.md`](industrial-product-design/SKILL.md) |
| Industrial product design with GB/T handoff | The comprehensive product-development workflow, 3D evidence, and mechanical manufacturing drawing handoff | [`industrial-product-design-gbt/SKILL.md`](industrial-product-design-gbt/SKILL.md) |
| Ray construction drawing conventions | Architectural/retail multi-system construction drawings using the user's observed conventions for plans, elevations, ceilings, MEP, furniture, details, and sheet organization | [`industrial-product-design-gbt/references/ray-construction-drawing-style.md`](industrial-product-design-gbt/references/ray-construction-drawing-style.md) |
| Local CAD fine-tuning preparation | Inventory and curate private CAD examples for future supervised fine-tuning or LoRA; JSONL contract, privacy, and review requirements | [`industrial-product-design-gbt/references/cad-training-preparation.md`](industrial-product-design-gbt/references/cad-training-preparation.md) |

The construction-drawing style reference is empirical and project-specific where noted. It does not replace project requirements, building/fire/electrical codes, applicable drawing standards, or construction approval. Keep raw source drawings and training corpora local; the repository contains only generalized guidance and data tooling.
