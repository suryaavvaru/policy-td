# Metrics

Policy-TD evaluates runtime control with **paired** baseline/guided outcomes on the same prompt, student, seed, and condition.

- **Base accuracy**: correctness of the frozen student without behavior-changing runtime intervention.
- **Guided accuracy**: correctness after Policy-TD routing.
- **Helped**: baseline incorrect, guided correct.
- **Harmed**: baseline correct, guided incorrect.
- **Net**: helped minus harmed.
- **Intervention rate**: fraction of rows receiving behavior-changing actions.
- **Router-off**: evaluation path remains present, but behavior-changing interventions are disabled.

## Intervention targeting versus intervention success

The frozen CSV field `intervention_precision` is a historical name for **targeting precision**: the fraction of behavior-changing interventions applied to rows on which the baseline was incorrect. `false_intervention_rate` is the complementary fraction applied to baseline-correct rows.

These should not be confused with intervention success:

- **Help yield** = helped / interventions.
- **Harm yield** = harmed / interventions.

An intervention can be correctly targeted at a baseline failure yet fail to repair it, so targeting precision and help yield are different quantities. Paper notation should preserve this distinction.

## Locked condition names

`guided_v10_noharm` is a historical locked-condition identifier, **not a universal no-harm claim**. It has zero observed harms on the internal global heldout benchmark but nonzero harms on real public external evaluation. Public prose should call it the **conservative operating point** rather than infer safety from the identifier.

`guided_v12_hardened` is the second locked operating point used in the frozen tables; paper prose should describe its actual gate behavior rather than treat the name itself as evidence.
