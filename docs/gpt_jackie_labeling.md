# GPT-Jackie labeling

The frozen release uses GPT-Jackie labels over frozen-student traces.

Legacy heuristic, local-teacher, and provider-switching label paths were used only during early prototyping and are not part of the curated release.

Malformed labels must fail validation or be excluded. They must not be silently replaced with heuristic fallback labels.
