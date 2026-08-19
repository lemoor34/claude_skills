# StoryScope Fiction Audit — 30-feature reference

## Purpose

Use this file when the main `SKILL.md` needs a full 30-feature audit or when a feature’s direction is unclear.

Source freeze: **StoryScope v6, 10 Aug 2026**, COLM 2026, arXiv:2604.03136. The paper reports 30 core narrative features selected for stable human-vs-AI separation. The values below are descriptive corpus statistics, **not quality targets**.

## Evidence context

- 10,272 prompts.
- Human story + five LLM versions per prompt.
- 61,608 stories total.
- Mean story length about 4,753 words.
- 304 extracted StoryScope features overall.
- Narrative-only experiment: 257 features, 93.2% macro-F1 human-vs-AI.
- Core-only experiment: 30 features, 84.8% macro-F1.
- The paper’s 30 core features are correlational discriminators, not a recipe for “human writing”.

## How to read the entries

`SOURCE DIRECTION` summarizes the v6 corpus difference.

`EDITORIAL USE` tells the audit what to inspect in a novel/chapter.

`DO NOT` blocks mechanical detector-gaming behavior.

---

# A. Thematic over-determination

## 1. Thematic Explicitness & Moralizing

**Source direction:** AI higher (human mean 3.28, AI mean 3.94 on 1–5 scale).

**Editorial use:** inspect whether the theme is dramatized and then restated by narrator or dialogue; check endings of scenes/chapters for explanatory summaries.

**Do not:** delete all explicit reflection. Keep it when voice, genre, or character genuinely requires it.

## 2. Moral / Philosophical Weighting

**Source direction:** AI higher (3.26 vs 3.68).

**Editorial use:** ask whether too many scenes are constructed to carry a moral/philosophical proposition rather than to pursue character goals.

## 3. Thematic Unity

**Source direction:** AI higher (4.41 vs 4.74).

**Editorial use:** look for over-perfect thematic alignment where nearly every object, subplot, conversation, and image reinforces one central idea.

**Do not:** introduce irrelevant material just to create noise.

## 4. Narratorial Thematic Commentary

**Source direction:** explicit narrator commentary was more common in AI stories (human 52%, AI 77%).

**Editorial use:** find places where the narrator explains a theme beyond what characters/actions already make legible.

## 5. Dialogue Function — Philosophical Debate

**Source direction:** more common in AI stories (34% vs 59%).

**Editorial use:** test whether dialogue exists because characters need something from one another or because the author wants two mouths to debate a thesis.

## 6. Reference Explicitness

**Source direction:** AI more often relied on implicit echoes (50% vs 72%); humans more often used a balanced explicit/implicit mix (37% vs 16%).

**Editorial use:** inspect whether references are vague and universal by default, or whether concrete named cultural/world-specific references appear naturally when appropriate.

**Do not:** insert brands, books, songs, or historical names purely to change the score.

---

# B. Sensory & embodied performativity

## 7. Dominant Emotional Expression

**Source direction:** embodied expression was much more common in AI stories (human 38%, AI 81%); explicit emotion labels were more common in human stories (29% vs 8%).

**Editorial use:** inspect the *distribution* of emotional representation: bodily reaction, action, speech, silence, direct naming, ambiguity, delayed response, misdirection.

**Do not:** convert every bodily cue into “he felt sad/angry”. The goal is variability, not one preferred mode.

## 8. Setting as Psychological Mirror

**Source direction:** AI higher (3.58 vs 4.07).

**Editorial use:** count how often weather, light, landscape, or room state mirrors a character’s inner state in an obvious way.

## 9. Environmental & Ecological Emphasis

**Source direction:** AI higher (2.83 vs 3.21).

**Editorial use:** ask whether natural/environmental detail carries story function or is repeatedly used as atmosphere filler.

## 10. Dominant Sensory Modalities — Olfactory

**Source direction:** olfactory detail more common in AI stories (57% vs 82%).

**Editorial use:** check whether smell is an automatic immersion device across many scenes.

## 11. Sensory Density

**Source direction:** AI higher (3.66 vs 3.93).

**Editorial use:** inspect whether every important scene gets a similar multi-sensory package independent of POV attention and scene purpose.

## 12. Depth of Interior Access

**Source direction:** AI higher (3.67 vs 3.93).

**Editorial use:** check whether the prose continuously explains inner states, leaving little room for external action or reader inference.

**Genre correction:** deep interiority may be a deliberate strength in literary, psychological, or first-person fiction.

---

# C. Structural streamlining

## 13. Causal Chain Continuity

**Source direction:** AI higher (3.92 vs 4.20).

**Editorial use:** map event causality. Look for a perfectly efficient A→B→C→D chain where every event visibly exists to trigger the next.

**Do not:** add random accidents or incoherence. Prefer meaningful side effects, delayed consequences, competing causes, or unresolved residue when the story supports them.

## 14. Spatial Granularity

**Source direction:** AI higher (2.27 vs 2.53 in the paper’s ordinal coding).

**Editorial use:** inspect whether physical space is described at the same granularity in every scene rather than according to what matters to the focal character.

## 15. Agency in Resolution

**Source direction:** protagonist-choice resolution was more common in AI stories (46% vs 69%).

**Editorial use:** ask whether conflicts repeatedly resolve because the protagonist makes the “right” choice at the decisive moment.

**Alternative structures:** mixed agency, other people’s actions, institutional forces, earlier decisions, chance with consequences, partial or costly control.

## 16. Character Introduction

**Source direction:** external-description introductions were more common in AI stories (30% vs 52%).

**Editorial use:** inspect whether key characters routinely arrive as mini portraits before doing anything.

**Alternatives:** action, dialogue, consequences of prior actions, reports by others, conflict, absence/trace before appearance.

## 17. Subplot Integration

**Source direction:** no-subplot stories were more common in AI writing (57% vs 79%); thematically parallel subplots were more common in human writing (42% vs 21%).

**Editorial use:** ask whether long-form fiction has secondary causal lines with their own stakes and effects on the main arc.

**Do not:** add subplots merely to satisfy this feature.

## 18. Resolution Mode

**Source direction:** internal-understanding resolutions were more common in AI stories (27% vs 47%).

**Editorial use:** inspect repeated endings built around realization, acceptance, closure, or “finally understanding”.

## 19. Opening Spatial Grounding

**Source direction:** AI slightly higher (human 2.12, AI 2.33 in ordinal coding).

**Editorial use:** compare openings across chapters. If many begin by establishing place/time/physical surroundings before conflict or voice, flag repetition rather than the device itself.

## 20. Pre-Threat Character Investment

**Source direction:** AI higher (2.76 vs 2.99).

**Editorial use:** inspect whether the book repeatedly uses the same order: establish likability/backstory → then introduce jeopardy.

---

# D. Intertextual richness

## 21. Intertextual Strategy — Explicit Named Reference

**Source direction:** explicit named references were more common in human stories (47% vs 24%).

**Editorial use:** for contemporary fiction, allow concrete real-world references when natural. For speculative fiction, the same principle can apply to specific internal-world texts, songs, myths, events, institutions, or artifacts.

**Do not:** use name-dropping as a detector trick.

---

# E. Reader engagement

## 22. Fourth-Wall Permeability

**Source direction:** higher in human stories (0.67 vs 0.39 in the paper’s ordinal coding).

**Editorial use:** relevant only when narrator form plausibly allows awareness of audience/storytelling frame.

**Default:** mark `N/A` for forms where fourth-wall permeability would damage POV or genre.

## 23. Direct Reader Address

**Source direction:** higher in human stories (0.28 vs 0.07 in ordinal coding).

**Editorial use:** observe it when already part of the voice.

**Do not:** recommend adding reader address solely because it is human-elevated in the corpus.

---

# F. Temporal complexity & revelation

## 24. Depth of Recontextualization After Surprise

**Source direction:** human higher (3.28 vs 2.95).

**Editorial use:** ask whether a reveal forces the reader to reinterpret earlier actions/scenes, or merely supplies a new fact.

## 25. Chronological Discontinuity

**Source direction:** human higher (2.40 vs 2.12).

**Editorial use:** audit whether the entire work defaults to strict chronology when delayed or displaced information would produce genuine meaning.

**Do not:** add time jumps without narrative purpose.

## 26. Nonlinear Framing for Delayed Disclosure

**Source direction:** human higher (1.96 vs 1.68).

**Editorial use:** inspect whether temporal ordering is ever used to control *how* a revelation lands, not just when it occurs chronologically.

## 27. Anachrony Intensity

**Source direction:** human higher (2.58 vs 2.31).

**Editorial use:** evaluate the function of flashback/flashforward and other anachronies. One meaningful reordering can matter more than many decorative flashbacks.

---

# G. Narrative diversity

## 28. Location Variety Scope

**Source direction:** human higher (1.34 vs 1.08 in ordinal coding).

**Editorial use:** inspect whether the physical world of the story is functionally varied or repeatedly collapses into the minimum set of generic locations.

**Do not:** expand geography without story value.

## 29. Dialogue-to-Narration Proportion

**Source direction:** human higher (2.95 vs 2.70 on the paper’s scale).

**Editorial use:** inspect the distribution of direct dialogue versus summarized conversation across scenes and chapters.

**Do not:** impose a universal dialogue percentage.

## 30. Moral Polarity Toward Protagonist

**Source direction:** ambivalent/mixed framing was more common in human stories (59% vs 38%).

**Editorial use:** ask whether the narrative itself tells the reader the protagonist is right/wrong, or whether consequences and competing viewpoints allow more than one defensible interpretation.

**Do not:** manufacture “gray morality” where the story’s ethical clarity is intentional and necessary.

---

# Feature clusters for editorial diagnosis

## Cluster 1 — Thematic over-determination
Likely members: 1–6.

Typical symptom: the story does not trust the reader to infer theme.

## Cluster 2 — Sensory / embodied performativity
Likely members: 7–12.

Typical symptom: “show, don’t tell” is applied as a mechanical style rule until every emotion and setting beat looks engineered.

## Cluster 3 — Structural streamlining
Likely members: 13–20.

Typical symptom: the story is clean, efficient, coherent, and therefore too visibly optimized.

## Cluster 4 — Temporal / revelation simplicity
Likely members: 24–27.

Typical symptom: information arrives in the same order as events and surprises add facts without changing interpretation.

## Cluster 5 — Narrative homogeneity
Likely members: 17, 21–23, 28–30 plus any repeated chapter-level defaults.

Typical symptom: every chapter uses the same mode of opening, emotional representation, location use, dialogue balance, and moral framing.

---

# Long-form interpretation rules

1. **Distribution beats presence.** A novel may legitimately contain any single AI-elevated feature. Repetition across many units matters more.
2. **Chapter roles differ.** Setup, reversal, aftermath, climax, and epilogue should not be judged against one identical feature profile.
3. **Genre is a prior.** Correct interpretation using genre conventions before recommending revision.
4. **POV constrains features.** Reader address, interiority, spatial detail, and explicit emotion behave differently in first-person, close third, omniscient, epistolary, etc.
5. **Series continuity matters.** Do not “humanize” a later book by breaking established narrative grammar.
6. **Revision should preserve load-bearing causality.** Structural variation is not an excuse for incoherence.
7. **One deep intervention is better than five cosmetic ones.** Prefer a reveal that recontextualizes three scenes over adding three decorative flashbacks.

# Source links

- Paper: https://arxiv.org/abs/2604.03136
- Official code/data: https://github.com/jenna-russell/storyscope

The feature names and source-direction statistics come from the paper’s v6 core-feature tables. The editorial risk scale, long-form heuristics, cluster workflow, and revision guidance are adaptations for practical book editing.
