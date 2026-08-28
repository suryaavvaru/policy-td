# Public release scope

Policy-TD separates the **scientific public artifact** from the private research workbench.

This is deliberate. A useful public research repository should expose enough information to understand the method, audit the reported evidence, and reproduce released calculations without publishing credentials, provider logs, local process state, or every exploratory script created during development.

## Public

The public repository includes:

- stable runtime action definitions;
- the teacher-label contract and validation rules;
- paired evaluation metrics;
- curated frozen result tables;
- benchmark source/protocol reports;
- release manifests and checksums;
- tests and inspection utilities;
- method, limitations, and release documentation.

## Intentionally not public

The following remain outside the repository unless a later research release specifically requires them:

- API credentials and provider configuration;
- raw teacher/provider transcripts;
- local workbench orchestration and process files;
- exploratory or superseded prototype scripts;
- large generated trace directories;
- intermediate checkpoints and caches;
- local absolute paths and machine-specific state;
- artifacts whose redistribution terms do not permit publication.

## Reproducibility claim

The current repository supports **artifact inspection, result traceability, and verification of released summary calculations**. It should not be described as a complete turn-key reproduction of every training and inference step unless the corresponding frozen runtime data, checkpoints, and execution code are also released.

This boundary should be stated consistently in the README, paper, and release notes.
