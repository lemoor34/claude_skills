# StoryScope Fiction Audit — smoke tests

These evals test whether the skill follows its editorial contract. They are not scientific validation of StoryScope and do not measure detector evasion.

## Eval 1 — Obvious structural convergence

### Input scenario
A ~3,000-word chapter repeatedly does all of the following:

- every emotional beat is rendered through chest/throat/hands/heartbeat;
- the narrator explains the lesson after the scene already demonstrates it;
- events follow an uninterrupted A→B→C→D causal chain;
- the protagonist solves the conflict with one decisive morally correct choice;
- the ending is a paragraph of internal realization and acceptance.

### Prompt

> Audit this chapter for structural machine-like patterns. Do not line-edit yet.

### Expected behavior

- Build a narrative skeleton first.
- Flag emotional-expression repetition, thematic commentary/explicitness, causal continuity, protagonist-choice resolution, and internal-understanding resolution.
- Use evidence from the text.
- Group them into 2–3 systemic clusters rather than reporting a fake numeric AI probability.
- Recommend at most 3–5 structural interventions.
- Do **not** solve embodied emotion by simply swapping one body cue for another.
- Do **not** add random flashbacks/subplots.

### Failure conditions

- “This is 87% AI.”
- Focus on em-dashes or words like “tapestry” instead of narrative construction.
- Add typos or awkwardness to look human.
- Recommend every one of the 30 features even when irrelevant.

---

## Eval 2 — Genre correction: cozy first-person fiction

### Input scenario
A first-person cozy chapter contains:

- extensive food smells and domestic sensory detail;
- clear spatial grounding at the opening;
- mostly linear chronology;
- warm thematic closure.

These are intentional genre/voice choices. The actual weakness is that the narrator repeats the same thematic conclusion three times in slightly different words.

### Prompt

> Run StoryScope audit but preserve the cozy voice and first-person intimacy.

### Expected behavior

- Mark sensory density/spatial grounding/linearity as plausible `INTENTIONAL — KEEP` unless evidence shows they are dysfunctional.
- Focus the edit on repeated thematic explanation.
- Explicitly state that StoryScope correlations are not universal writing rules.
- Preserve voice and genre comfort.

### Failure conditions

- Strip sensory writing simply because AI was elevated on sensory density.
- Force nonlinear chronology.
- Force moral ambiguity.
- Treat fourth-wall/reader address as mandatory.

---

## Eval 3 — False “human feature” trap

### Input scenario
A weak chapter contains many named brands, two flashbacks, direct reader address, moral ambiguity, and several locations, but they are decorative and do not improve causality, characterization, or revelation.

### Prompt

> Does this already look structurally human according to StoryScope?

### Expected behavior

- Refuse to equate human-elevated correlations with quality or authorship.
- Explain that feature presence without function is not a positive result.
- Audit whether the flashbacks recontextualize prior scenes, whether reader address belongs to the voice, and whether named references are organic.
- Flag decorative complexity if it produces no narrative effect.

### Failure conditions

- “Yes, it passes because it has flashbacks and brands.”
- Treat human-elevated features as points in a human score.

---

## Eval 4 — Before/after structural revision

### Version A
A reveal at chapter end simply states: the mentor was secretly the protagonist’s father.

### Version B
Earlier scenes contain unexplained avoidance, a strange reaction to a family object, and a lie about dates. The same reveal now forces the reader to reinterpret those scenes.

### Prompt

> Compare A and B with StoryScope before/after mode.

### Expected behavior

- Identify genuine improvement in `Depth of Recontextualization After Surprise`.
- Explain that the change is structural, not merely stylistic.
- Check for side effects in causality and character knowledge.
- Do not claim Version B is “human-written”.

---

# Manual test checklist

For each eval, verify:

- [ ] Narrative skeleton precedes line editing.
- [ ] Major findings include evidence.
- [ ] No AI probability/authorship claim.
- [ ] Genre and POV correction applied.
- [ ] No mechanical addition of human-elevated features.
- [ ] Maximum 3–5 priority interventions.
- [ ] Structural and stylistic issues are kept separate.
- [ ] Confidence is lowered for insufficient text.
- [ ] Re-audit target is included after revision.
