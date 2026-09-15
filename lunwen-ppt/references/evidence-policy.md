# Evidence policy

## Required ledger

Maintain `<project>/evidence/ledger.json` with one record per visible claim:

```json
{
  "slide": 5,
  "claim": "Virchow achieved 0.950 AUC across all tested cancers",
  "source_type": "paper",
  "locator": "page 2928, Fig. 2b",
  "verified": true
}
```

Use `source_type: external` only on the explicitly labeled extension slide.

## Allowed paper evidence

- Main text and methods
- Figure captions and table notes
- Supplementary material supplied with the paper
- Author-maintained official project or repository for implementation facts, clearly labeled

## Forbidden transformations

- Do not turn correlation into causation.
- Do not imply statistical significance without a reported test.
- Do not compare values from different cohorts as if they share an experimental setting.
- Do not translate “potential” or “may” into a confirmed clinical conclusion.
- Do not infer a missing model component from a schematic.
- Do not crop away legend, sample size, axes, uncertainty, or qualifiers that change interpretation.

## Extension boundary

Use a visible heading such as `前沿扩展（非原论文内容）`. Put the search cutoff and citations on the slide or in the standalone notes. Never use extension sources to rewrite what the original authors claimed.
