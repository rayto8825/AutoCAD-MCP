# Agent routing for this repository

Before handling a task, use this routing index to load the narrowest relevant instructions:

- **AutoCAD automation, generated DWG/DXF, geometry audits, layers, or plotting:** read the repository workflow and API guidance in [README.md](README.md) or [README.zh-CN.md](README.zh-CN.md), then inspect the applicable source/API documentation. Do not infer successful AutoCAD import or plotting from file creation alone.
- **Architectural, retail/interior, or other multi-system construction drawings:** read [`skills/industrial-product-design-gbt/SKILL.md`](skills/industrial-product-design-gbt/SKILL.md), then its [`Ray construction drawing style reference`](skills/industrial-product-design-gbt/references/ray-construction-drawing-style.md) when Ray's observed conventions are requested. Read [`CAD training preparation`](skills/industrial-product-design-gbt/references/cad-training-preparation.md) when inventorying examples or preparing local fine-tuning/LoRA data. This route covers plans, elevations, reflected ceilings, electrical, plumbing, furniture/equipment, details, schedules, and sheet/layout organization; do not narrow it to storefront signs.
- **Industrial product design and product-development work:** choose the suitable skill from [`skills/README.md`](skills/README.md). Use the comprehensive GBT skill only when its broader design and engineering workflow fits the task.
- **Manufacturing drawings for mechanical products:** use the mechanical-drafting skill referenced by the selected product-design workflow; architectural construction-drawing conventions are not a substitute for GB/T mechanical drafting requirements.

## Data handling for CAD learning

Treat workstation CAD libraries and derived per-project training examples as private. Keep raw drawings, manifests with identifying paths, extracted geometry, JSONL corpora, and checkpoints out of Git. Commit only generalized rules, schemas, and tools unless the user explicitly authorizes publication of specific data. See the CAD training preparation reference for the complete review and privacy workflow.

## Skills index

See [`skills/README.md`](skills/README.md) for purpose and routing of the repository's reusable agent skills.
