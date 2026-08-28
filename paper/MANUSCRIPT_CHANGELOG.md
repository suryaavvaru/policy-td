# Policy-TD final manuscript changes

This final pass turns the earlier draft into a publication-oriented manuscript without inventing new experiments.

- Rebuilt the title/author/contact block so all three names and emails are evenly spaced and readable.
- Reordered the scientific narrative to: motivation -> related work -> formalization -> controller design -> experimental design -> RQ-driven results -> discussion -> limitations -> reproducibility -> conclusion.
- Added a new architecture figure that separates offline teacher supervision from deployment-time control and shows all six actions.
- Corrected intervention terminology by separating post-hoc targeting precision from help yield and harm yield.
- Added an intervention-quality decomposition derived from the frozen public result tables.
- Elevated the recoverability boundary: public transfer can fail even when interventions still target baseline-incorrect states.
- Clarified that row-level intervals are descriptive because prompts repeat across student/seed combinations.
- Rewrote public-code language to match the curated GitHub artifact rather than imply release of the entire internal workbench.
- Preserved negative results and transfer failures rather than hiding them.
- Added a real conclusion and explicit author-contribution section.
- Rebuilt the supplement with metric definitions, intervention diagnostics, seed/student/family/domain tables, label-transfer caveat, traceability map, deployment criterion, and release boundary.
