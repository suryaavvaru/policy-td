# Metrics

Policy-TD uses paired runtime outcomes.

- **Base accuracy**: correctness of the frozen student without runtime intervention.
- **Guided accuracy**: correctness after Policy-TD routing.
- **Helped**: baseline incorrect, guided correct.
- **Harmed**: baseline correct, guided incorrect.
- **Net**: helped minus harmed.
- **Intervention rate**: fraction of examples receiving behavior-changing actions.
- **Router-off**: evaluation path present, behavior-changing interventions disabled.
