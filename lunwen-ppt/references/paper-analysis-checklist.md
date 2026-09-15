# Paper analysis checklist

Complete this checklist before drafting slides or a personal-study Markdown. Put only the presentation-critical conclusions on slides; preserve the fuller analysis in the paper-library Markdown entry and, when requested, `projects/<project>/md/<paper>_论文精读.md`.

## 0. Reading role and style

For personal-study Markdown, write as a senior top-conference reviewer and a 10-year full-stack algorithm engineer helping a beginner researcher. Keep the answer structured, plain-language, evidence-grounded, data-driven, and honest about uncertainty. Do not turn this detailed checklist into PPT slide titles.

## 1. Mandatory opening: publication identity report

Place this independent report at the very beginning before answering any paper-specific question.

- Determine whether the PDF is an arXiv/preprint, submitted manuscript, accepted paper, author manuscript, proof, review material, or final version of record.
- Verify conference/journal, year, DOI, official proceedings/publisher page, CCF class when applicable, Nature/Science/Cell family status, top-conference/top-journal status, or time-stamped CAS/JCR quartile only when it is relevant and verified.
- For ordinary SCI journals, report the CAS quartile only with a version/year or state that it was not verified.
- If no formal publication is verified, write exactly: `本文目前为 arXiv 预印本，尚未查到正式发表信息` or `本文目前为预印本，尚未查到正式发表信息`, then explain the evidence.
- For an unaccepted preprint, warn that the final version may differ in experiments, appendix, references, and implementation details; reproduce against the final version or official code when available.
- Never infer acceptance, CCF class, impact factor, CAS quartile, or official code from filenames, search snippets, or memory.

## 2. Mandatory body: answer all 9 questions

For personal-study Markdown, use these 9 sections unless the user requests another structure. If the paper does not mention an item, write `本文未提及`.

1. `论文要解决什么问题？`
   - Task type: classification, detection, segmentation, generation, clustering, retrieval, prediction, survival analysis, etc.
   - Application setting: medicine, computational pathology, radiology, autonomous driving, NLP, etc.
   - Intended input, output, and decision supported.
2. `数据是什么？`
   - Data type: image, WSI, CT/MRI, text, video, table, signal, multimodal, etc.
   - Sample size, class count, cohorts/centers, label source, inclusion/exclusion, public/private status, and access route.
3. `数据怎么处理？`
   - Raw form, preprocessing, normalization, augmentation, tiling/cropping, tokenization, denoising, feature or embedding extraction, and train/validation/test split.
4. `用了什么模型或方法？`
   - For every core module, write one sentence in the form: `input -> output -> where the output goes next`.
   - Identify architecture, backbone, feature extractor, fusion/aggregation, loss, optimizer, learning rate, batch size, epochs, hardware, supervision type, parameter count, and initialization when reported.
   - Classify every central component as author-created, reused open source, closed third-party, or unclear.
   - For open-source components, verify official GitHub/Hugging Face/project links, installation/use route, weights, license if relevant, GPU need, and version constraints. Never invent a URL.
   - For author-created components, judge whether the paper/supplement/code provides enough detail to reproduce it.
5. `模型效果怎么样？`
   - Record metrics, confidence intervals/statistical tests, baselines, absolute/relative improvements, ablations, sensitivity analysis, external validation, subgroup results, and failure cases.
   - Explain every metric in beginner-friendly language, including directionality and practical meaning.
   - Compare values only under comparable tasks, cohorts, splits, and metrics. Otherwise state that values are not directly comparable.
6. `模型的可解释性或可视化分析`
   - Explain t-SNE/UMAP, attention or weight heatmaps, activation/feature maps, clustering, highlighted regions, and whether the paper provides medical/semantic validation.
   - State explicitly when a visualization is only suggestive and not causal evidence.
7. `论文解决了问题没有？能发表的核心原因是什么？`
   - Judge whether the stated goal is met using reported evidence.
   - Separate novelty into model, framework, application, performance, theory, dataset, validation, and engineering value.
   - Record author-stated limitations/future work separately from the reader's interpretation.
8. `复现指南：作为新手如何复现？`
   - State whether official code/weights are public and whether README/tutorials exist.
   - Explain what can use existing libraries, what needs custom code, recommended starting repository, data/approval barriers, compute requirements, likely failure points, random-seed or hyperparameter sensitivity, and multi-project version compatibility risks.
   - Recommend a practical minimum viable reproduction path instead of blindly reproducing the full paper when the full setup is unrealistic.
9. `论文没写但我需要知道的隐含信息`
   - List every implementation detail gap needed for reproduction.
   - If offering a typical default/range, label it exactly as `领域经验推测，非论文原文` and never place it on a paper-results slide as fact.
   - If official code exists, state whether the missing detail can likely be found there.

## 3. Beginner terminology requirements

- At first occurrence of every acronym or specialist term, provide the full Chinese/English name and a plain-language explanation.
- Mark each term as a data concept, algorithm concept, evaluation concept, clinical concept, or engineering concept.
- When a term has multiple implementations, identify the exact form used in this paper. For example, do not describe MoE generically if the paper uses model ensembling rather than layer-internal routed experts.
- Explain whether each method/model is open source, author-created, closed third-party, or unclear.

## 4. Evidence and citation

- Cite paper claims with numbered references such as `[1]` in entries and personal-study Markdown; retain precise page, section, figure, or table locators in the evidence ledger when available.
- Use prior knowledge only to fill a genuine context gap, label it as external interpretation, and provide a source when it affects the output.
- Keep paper evidence, official implementation evidence, and recent-work extension evidence as distinct source types.
- For web-based recent-work extension, include a search cutoff date and clearly mark it as non-paper content.
