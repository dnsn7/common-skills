---
name: lunwen-ppt
description: Convert a referenced academic paper PDF into an evidence-grounded Chinese research-group presentation and maintain a searchable paper knowledge base. Use when the user says “做个 PPT”, “做成组会 PPT”, “汇报这篇论文”, “论文 PPT”, or asks to read, explain, reproduce, compare, index, or connect medical-imaging, computational-pathology, computer-vision, or agent papers. Verify venue status and ranking, explain terminology for beginners in a separate personal-study Markdown when requested, assess reproducibility and open-source status, ground all non-extension content in the paper, connect related papers, create an editable PPTX, and run visual/openability QA.
---

# Lunwen PPT

Create a compact, evidence-grounded Chinese group-meeting deck and a durable paper record. Use the available PDF, presentation, document, and web capabilities for reading, authoring, rendering, and QA. Do not load the larger generic `CN_Spark_paper2ppt` instructions unless a required converter or checker is needed.

## Defaults

- Presenter: use the name supplied by the user; otherwise use a neutral placeholder
- Institution: use the institution supplied by the user; otherwise omit it
- Audience: 研究生课题组
- Domain: 计算机医学图像处理 / 计算病理
- Length: 8–10 slides, including cover and conclusion
- Canvas: 16:9
- Style: clean clinical/technical visual system; white or pale background, navy + cyan + restrained magenta accents
- Typography: Chinese title 32–38 pt, subheading 24–28 pt, body 22–26 pt, figure/table caption 16–18 pt, source footer 12–14 pt
- Deliverables: editable PPTX, updated paper-library entry/index, and QA summary. When the user explicitly asks to understand/read the paper or requests an MD, also create a separate detailed Chinese paper-study Markdown.

User instructions in the current request override these defaults.

### Projection readability contract

- Treat `22 pt` as the normal body-text baseline for a 16:9 group-meeting slide; important explanatory sentences should usually use `24–26 pt`.
- Do not use body text below `20 pt`. The only exceptions are compact figure/table labels already embedded in a paper image and short source/DOI footers, which must remain at least `12 pt`.
- Figure conclusions, chart interpretations, and method-node descriptions are audience-facing body content, not footnotes; keep them at least `20–22 pt`.
- If text does not fit at these sizes, shorten the copy, enlarge the visual, choose a less dense layout, or split/merge the narrative differently. Do not solve overflow by shrinking ordinary text.
- During visual QA, inspect the slide as a projected presentation: a normal paragraph, graph-node label, metric explanation, or figure takeaway that is technically present but difficult to read counts as a defect and must be revised.

## Fast workflow

1. Create `projects/<paper-short-name>_<date>/` with `ppt/` and, when requested, `md/`. Temporary source pages, crops, evidence, and renders may live under `tmp/` and should be removed after QA unless they are needed for durable indexing.
2. Run `scripts/inspect_paper.py <paper.pdf> --out <project>/evidence/paper.json --render-dir <project>/assets/pages`.
3. Read the extracted abstract, methods, results, discussion, figure captions, tables, supplement, and implementation details. Do not repeatedly re-read the complete PDF after the evidence file exists.
4. Read `references/paper-analysis-checklist.md` and complete the paper analysis before drafting. For a personal-study Markdown, follow its mandatory opening publication-identity report and all 9 question sections. Record “本文未提及” instead of guessing.
5. Verify publication status, venue, and level using authoritative sources. Read `references/venue-ranking.md` only for this step.
6. Build a page-level evidence ledger before drafting slide copy. Read `references/evidence-policy.md` and record each claim with a paper page, section, figure, or table.
7. Read `references/knowledge-base-policy.md`; inspect `论文库/catalog.json` and related entries before positioning the paper.
8. Select 3–5 source figures. Crop from high-resolution rendered PDF pages; preserve labels, legends, scale bars, and aspect ratio.
   Do not place full PDF pages or unreadable paper-page thumbnails on content slides. A full first page is allowed only as a compact cover citation anchor. Every other source visual must be a meaningful crop that supports the slide claim.
9. Use `assets/slide_blueprints.json` for the default narrative and `assets/theme.json` for design tokens. Merge pages when needed; do not exceed the requested count.
10. Search the web for official code/model pages and the clearly labeled final extension section. Prefer primary sources from the last 1–2 years. Do not mix web-derived claims into paper-summary slides.
11. Create the PPTX with the available presentation workflow. Reuse `scripts/deck_helpers.mjs` instead of rewriting common slide helpers.
12. Keep PowerPoint notes empty for compatibility. Put beginner explanations, reproducibility details, evidence locators, and sources in the separate personal-study Markdown when the user requests it; otherwise preserve them in the paper-library entry. Do not create a third speaker-notes file unless the user explicitly requests one.
13. Update the Markdown entry, `论文库/catalog.json`, `论文库/README.md`, and 2–5 meaningful related-paper links. Do not regenerate prior decks unless requested.
14. If the exporter adds empty notes parts, run `scripts/strip_pptx_notes.py <deck.pptx>`.
15. Render every slide, inspect every page, run overflow checks, and run the repository openability checker when available. Fix all defects before delivery.

## Audience split and dual deliverables

When the user asks for both a group-meeting PPT and a personal paper-study MD, treat them as separate products:

- Write the PPT for supervisors and lab members. Include only the research problem, motivation, core method, data/experiment design, decisive results, comparisons/ablations/error analysis, contribution, limitations, clearly separated recent-work extension, and research implications. Do not put beginner tutorials, installation commands, code-access steps, reproduction checklists, extraction uncertainty, or phrases such as “新手必须理解” on slides.
- Write the Markdown for the user’s private study. Use the role and structure in `references/paper-analysis-checklist.md`: first an independent publication-source and venue-level identity report, then the 9 required sections covering problem, data, preprocessing, model/method, results, visualization, contribution/limitations, beginner reproduction guide, and hidden implementation gaps. Include term tables, module input/output/next-destination statements, open-source versus author-created status, metric explanations, likely pitfalls, version risks, and “领域经验推测，非论文原文” labels where appropriate.
- Store them separately under `projects/<project>/ppt/` and `projects/<project>/md/` unless the user gives another destination.
- Use one evidence ledger for both. The PPT is a selective narrative; the MD is the complete learning record. Never transform the MD question list into the PPT outline.

## Content contract

- Show the verified venue and paper level on the cover, such as `AAAI 2026｜CCF A` or `Nature Medicine 2024｜Nature Portfolio 顶级医学期刊`.
- State whether the PDF is a preprint, accepted manuscript, proof, peer-review material, or final publication. If a preprint has no verified publication, say so explicitly and warn that the final version may differ.
- Keep the cover minimal: Chinese title, English title, venue/level/year, presenter, institution, date.
- Make every non-extension claim traceable to the source paper or its supplementary material.
- Never invent metrics, modules, datasets, experiments, clinical claims, causal explanations, or author opinions.
- Label reasonable interpretation as “本次解读” and keep it out of the paper-results wording.
- Mark the external section as `前沿扩展（非原论文内容）` and show the search cutoff date.
- Compare numeric results only under comparable datasets, splits, tasks, and metrics. Otherwise state that only a qualitative architecture comparison is made.
- Use paper figures as evidence, not decoration. Add one concise Chinese takeaway beside each figure.
- Redraw the core method as an editable data-flow diagram when the original figure is dense, low-resolution, or not presentation-friendly. Show `input → core module → intermediate representation/decision → output/next destination`, use consistent nodes and arrow semantics, and never invent a module or edge. Use `example_asset/example-transportation-partc.pptx` as the preferred visual reference for clean academic process diagrams in this project.
- Expand every acronym and specialist term on first use. Label it as a data concept or algorithm concept and explain the paper-specific implementation in plain Chinese.
- For each core module, state `input → output → next destination` in the notes and, when space permits, on the method slide.
- Identify whether each central method is author-created, reused open source, or unclear. Give verified official links and basic usage only when confirmed.
- Cover data source/accessibility, preprocessing, split, training setup, metrics, baselines, ablation, visualization, limitations, implementation gaps, and reproducibility. Personal-study Markdown must answer all 9 checklist questions; use “本文未提及” for absent facts.
- Explain each displayed metric in beginner-friendly language and do not report unsupported improvement values.
- End with 2–4 actionable research ideas: why, how, and expected value.

## Default slide sequence

1. Cover + verified venue level
2. Background, problem, and purpose
3. Data and method overview
4. Core architecture or research route
5. Main quantitative result
6. Comparison, ablation, or clinical/generalization result
7. Qualitative result, error analysis, or another key experiment
8. Strengths and limitations
9. Frontline extension and actionable research ideas
10. Conclusion and discussion

Adapt this sequence to the paper. Preserve one claim per slide and prioritize the paper’s strongest evidence.

## Completion gate

Deliver only when:

- slide count satisfies the request;
- every paper-summary slide has evidence ledger entries;
- cover venue level is verified and dated when ranking is time-sensitive;
- external material is visually and textually separated;
- no figure is distorted or cropped misleadingly;
- no text overlaps, clips, or falls below the readable minimum;
- PPTX opens and has no notes parts when the repository checker requires notes-free output;
- when a personal-study Markdown was requested, it is complete, separately stored, and does not substitute for PPT audience design.

