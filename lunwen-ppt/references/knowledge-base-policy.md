# Paper knowledge-base policy

Use `论文库/` as durable memory across Codex windows. Treat PPTX files as presentation products, not the primary searchable record.

## Before creating a deck

1. Read `论文库/catalog.json` and the Markdown entries most similar in task, modality, method, validation design, or clinical endpoint.
2. Identify 2–5 genuinely related papers. Do not match only by title words or model names.
3. Decide whether the new paper extends an existing cluster or requires a new cluster.

## Required entry content

Create or update `论文库/条目/<id>.md` with metadata plus:

- one-sentence takeaway;
- publication identity and verified level;
- problem, data, preprocessing, method, results, visualization, strengths, limitations;
- terminology glossary with concept type;
- module-level `input → output → next destination` descriptions;
- open-source/self-developed status and verified official links;
- beginner reproduction guide, implementation gaps, and explicitly labeled experience-based assumptions;
- evidence locators and numbered sources;
- relationships to 2–5 library papers: shared point, difference, and why the connection matters.

## Update rules

- Update `论文库/catalog.json` as the machine-readable source and `论文库/README.md` as the human index.
- Add reciprocal related-paper links where appropriate; never overwrite unrelated existing analysis.
- Link by task, modality, method, validation, clinical endpoint, or research progression.
- Note a possible paper sequence, such as `general foundation model → disease-specific adaptation → clinical validation` or `single agent → pathology navigation agent → autonomous clinical workflow`.
- Do not regenerate old single-paper or summary PPTX files unless the user explicitly asks.
- If metadata or publication status changed, preserve the prior status in notes and record the verification date.
