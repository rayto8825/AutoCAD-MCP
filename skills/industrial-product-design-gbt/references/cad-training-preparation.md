# CAD Construction Drawing Training Preparation

This workflow prepares a private, local corpus for possible later supervised fine-tuning or LoRA. It does not train a model by itself and does not treat a DWG as a ready-made instruction/answer pair. The existing [`ray-construction-drawing-style.md`](ray-construction-drawing-style.md) is a generalized, inspectable style reference; keep it alongside any future adapter because exact layer names, project rules, and current standards should remain editable and retrievable.

## Privacy and repository boundary

- Treat H: work files and all derived per-project examples as private by default. Never copy source DWG/DXF, title blocks, client names, addresses, phone numbers, logos, quoted text, proprietary geometry, or unlicensed reference images into this repository.
- Keep manifests, extracted entity/layer inventories, JSONL corpora, rendered previews, and model checkpoints in a user-controlled local directory excluded from Git. A file hash or controlled local path may be used for provenance; do not publish a path that identifies a customer or private directory tree.
- Work from read-only source access or a local copy. Do not save changes back into source drawings during corpus preparation.
- Generalize a convention only after checking more than one relevant project where possible. Mark each rule as observed, inferred, or project-specific; preserve exceptions and uncertainty.
- Remove personal/client text and inspect block attributes, Xrefs, embedded images, PDF underlays, and drawing metadata before sharing a derivative outside the workstation.

## Build useful examples from complete drawing sets

1. Inventory candidate files locally by project and drawing system. Include more than storefront elevations: floor plans, elevations, reflected ceiling plans, electrical, plumbing, furniture/equipment, details, schedules, and sheet/layout examples where present.
2. Select representative, legible, complete projects and retain the relationship among sheets from one project. Do not let many revisions of one job masquerade as independent examples.
3. Extract only the facts needed for drafting decisions: units, layouts, plot settings, text/dimension styles, layer names and properties, entity type counts by layer, block/attribute summaries, and bounded geometry descriptors. Keep raw geometry local; use rendered crops or simplified geometry only when necessary and approved for local training.
4. Pair evidence with an explicit task and reviewed answer. Good examples explain which drawing system/view is being produced, which layers own which entities, dimension/text/plot conventions, references to related sheets, assumptions, and unresolved decisions. A raw DWG, file name, or layer list alone is not an instruction-tuning example.
5. Capture corrections as before/after decisions with the user's disposition when available. Exclude guesses as ground truth. Keep safety, code, structural, electrical, fire, and accessibility requirements sourced from verified authoritative inputs, not inferred from personal drafting habits.
6. Normalize examples into JSON Lines using [`../assets/cad-training-example.schema.json`](../assets/cad-training-example.schema.json). Keep one self-contained example per line and store only generalized/private-safe content in any corpus intended to leave the local machine.

For a later local corpus, use the schema and template as the row contract and run the structural validator before training:

```powershell
New-Item -ItemType Directory -Force local-learning/cad-training
# Build corpus.jsonl locally; do not commit it.
uv run python skills/industrial-product-design-gbt/scripts/validate_cad_training_corpus.py local-learning/cad-training/corpus.jsonl
uv run python skills/industrial-product-design-gbt/scripts/validate_cad_training_corpus.py local-learning/cad-training/corpus.jsonl --training-ready
```

The first command checks row structure; the second also requires reviewed answers and rights review. These checks do not judge drafting correctness, anonymization completeness, or license rights. Have a qualified reviewer inspect those separately.

## Coverage and quality review

Track coverage by project and system, not just total sample count. Before tuning, check:

- all systems actually represented in the reference library are classified; missing disciplines are marked `not_available`, not invented;
- multiple independent projects contribute to reusable rules, with revisions grouped under their parent project;
- every answer has a provenance pointer or says it is a proposed convention, and project-specific exceptions remain explicit;
- layer assignments are semantic and consistent with the referenced example; preserve legacy layer names rather than silently merging them;
- units, dimension scales, text sizes, plot settings, layouts, Xrefs, and block behavior are captured when relevant;
- duplicated, contradictory, low-quality, incomplete, and confidential examples are flagged or excluded;
- split train/validation examples by project, not by individual rows, to reduce leakage between sheets from the same job.

## Later local training handoff

When the user asks to organize the training set, first confirm the intended local corpus root and inspect the available GPU/software versions. Produce a private data manifest, normalized JSONL, data-quality report, and a small held-out project set before any training run. Use a supported local instruction-tuning stack and a base model whose license, language capability, context length, and VRAM fit are checked at that time. LoRA can teach recurring response/drafting patterns; it cannot by itself guarantee valid CAD geometry or replace CAD-native validation. Keep the style guide as retrieval/reference memory and validate generated drawings with CAD parsing, layer audits, dimension checks, and visual review.

This preparation guide is a workflow, not a license grant. Local possession of a drawing does not establish permission to train on it or distribute derived data. If rights or confidentiality are unclear, keep that item out of the corpus until resolved.
