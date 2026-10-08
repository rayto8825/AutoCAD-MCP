# Ray's Construction Drawing Style (Observed)

This reference records empirical conventions found in Ray's H: work files. It is a **style guide**, not a substitute for project requirements, GB/T, building/fire/electrical codes, or construction approval. Keep observations separate from assumptions; inspect the closest current source drawing before reusing a convention.

## Evidence inspected

AutoCAD 2022 opened these drawings read-only and their ModelSpace entities, layer names, units, scales, and layouts were inspected:

| Sample | ModelSpace entities | Key evidence |
| --- | ---: | --- |
| `Sample A` (integrated construction set) | 1,753 | Core layer set; millimetres; `DIMSCALE=50`; a construction-sheet layout |
| `Sample B` (container-shop construction set) | 1,932 | Same core layer set; 252 dimensions; millimetres; `DIMSCALE=40`; construction-sheet layout |
| `Sample C` (retail construction set) | 3,082 | Same core layer set; 419 dimensions; millimetres; `DIMSCALE=60`; construction-sheet layout |
| `Sample D` (separate elevation-system file) | 1,274 | 232 rotated dimensions and 2 aligned dimensions; contains imported/Xref layer and style names |

The first three are the strongest evidence for a repeated personal template: they share many identical base-layer names and fixed legend/frame-layer counts. The elevation file is useful evidence of project/system separation, but its imported names are not automatically personal defaults. A small older storefront-sign sample had only 17 layer-0 polylines and no dimensions; it is not a style exemplar. Source paths and client/project names are intentionally omitted from this public reference.

## Repeated drawing organization

- A project may be separated into system-specific DWGs, such as plan/system and elevation/system files, while also maintaining an integrated `施工图.dwg` with a construction-sheet layout. Follow the project's existing package structure; do not force every view into one oversized file or split files without preserving sheet identity and cross-references.
- AutoCAD model space contains dense, full-size editable geometry; drawing sheets/frames and legends are kept as reusable drawing content. The inspected drawing sets also expose a named `施工图` layout.
- Preserve editable polylines, blocks, hatches, MText, leaders, and associative/native dimensions where available. Do not flatten a layered drawing into an undifferentiated line export.

## Repeated layer vocabulary

The stable core observed across three 2026 project DWGs is:

| Layer | Observed role from its name/use | Working rule |
| --- | --- | --- |
| `墙体` | Wall geometry | Keep wall outlines distinct from furniture and annotation |
| `家具` | Furniture | Keep furniture/equipment editable and separately isolatable |
| `强电`, `电` | Electrical systems | Preserve the source's split between these two layers; inspect the sample before assigning new entities |
| `水图` | Water/plumbing plan | Keep it separate from electrical and architectural geometry |
| `地面布置图` | Floor/finish plan | Isolate floor-layout/finish information |
| `天花布置图`, `天花灯具图`, `天花尺寸` | Reflected-ceiling/lighting/dimensions | Split ceiling geometry, lighting, and ceiling dimensions when the source template does |
| `YQ_DIM` | Main dimension layer | Use for general dimensions unless the source convention assigns a dimension to its discipline layer |
| `TEXT`, `YQ_TEXT`, `A-TEXT-PLAN-文字` | Notes and labels | Separate annotation from geometry and preserve the project's chosen text layer |
| `LM-立面部分` | Elevation content | Keep elevation-system geometry independently controllable |
| `00.0-图框图例` | Sheet frames and legends | Reuse the project template's frame/legend content rather than redrawing it casually |
| `YQ_TITLE`, `YQ_IDEN` | Titles and identification | Retain when present in the selected template |
| `C-DETL-BOLD-粗`, `FURHATCH`, `CONCRETE` | Detail emphasis, furniture hatch, concrete | Use only where the matching template/material/detail convention exists |

Other observed legacy/source layers include `D`, `WINDOW`, `WALL`, `FURNITURE`, `LINE`, `GRATE`, `FF-FURN`, and imported names. They are not interchangeable aliases. Before drawing, inspect the actual project's layer table, color, linetype, lineweight, plot state, and existing geometry by layer. Do not invent a second spelling for an existing role.

### Layer assignment rules

1. Assign each new entity to its semantic drawing layer at creation time; avoid creating everything on layer `0` and sorting it out only at the end.
2. Keep primary categories separately switchable (walls, furniture/equipment, electrical, water, floor, ceiling/lighting, elevation, dimensions, notes, frame/legend).
3. `YQ_DIM` is a recurring general dimension layer, but samples also contain dimensions on `墙体`, `家具`, `电`, `天花灯具图`, and `天花尺寸`. Match the selected source's discipline-specific convention; do not blindly move every dimension to one layer.
4. Preserve block contents, attribute layers, Xrefs, and layer-0 inheritance semantics. Never explode reusable blocks solely to make the layer list look simpler.
5. Perform a layer-isolation check before handoff: hide/show each major discipline layer and verify that unrelated content does not disappear with it.

## Units, dimension and plotting scale

- The three repeated-template samples report `INSUNITS=4` (millimetres), `LTSCALE=10`, `DIMTXT=3`, and `DIMASZ=1`.
- `DIMSCALE` differs by project: 40, 50, and 60. **Never hardcode a single scale.** Read the selected template and intended plotted scale, then verify dimension text and arrow size in the actual layout/plot.
- Existing files may contain many dormant/imported dimension and text styles. Do not import an entire foreign style table merely to copy one annotation. Choose and verify the style actually used by the selected sample.
- Confirm paper size, orientation, viewport scale, plot style, lineweight visibility, font availability, and plotted PDF at sheet size. A visually correct model-space view alone does not prove a usable construction sheet.

## Workflow for a new drawing in this style

1. Inspect the closest current H: sample read-only. Identify whether it is a clean native/template drawing or an imported/customer/reference drawing.
2. Record the layer table and actual entity-to-layer use, dimension/text styles, `INSUNITS`, `LTSCALE`, `DIMSCALE`, layout names, sheet frames, and plot configuration. Treat differing scales as project-specific.
3. Start from a copy of the closest project template when possible; never edit the evidence/sample file. Reuse its title/frame/legend conventions only when appropriate to the new project.
4. Plan the drawing package by system/view, then create geometry on semantic layers with explicit dimensions, notes, and identifiers. Preserve cross-sheet references.
5. Inspect layers by toggling them, then open the output in the target AutoCAD version, zoom to extents, review the layout, and plot/open the PDF. Check text, dimensions, clipping, lineweights, missing fonts, and sheet organization.
6. Deliver editable DWG/DXF and a visual/PDF review artifact when requested. State assumptions and any construction-critical items not defined by the references.
