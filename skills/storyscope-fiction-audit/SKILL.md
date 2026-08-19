---
name: storyscope-fiction-audit
description: Structural audit for fiction using StoryScope-inspired narrative features. Use when reviewing a scene, chapter, short story, novel, or AI-assisted fiction for structural “machine-like” patterns, narrative naturalness, plot/revelation/character issues, or before line-edit/KDP finalization. Works in Russian, English, and German. Do not use as an authorship detector or to estimate AI probability.
---

# StoryScope Fiction Audit

Audit **narrative construction before prose style**. The goal is to detect repeated, overly tidy or over-explained narrative decisions and propose the smallest structural changes that improve the story without flattening genre, voice, or authorial intent.

This skill is an editorial adaptation of **StoryScope: Investigating idiosyncrasies in AI fiction**, COLM 2026, arXiv:2604.03136v6. The paper’s dataset contains 61,608 stories and 304 extracted features; its narrative-only classifier uses 257 narrative features, while a compact 30-feature core retains substantial signal. The study is on short fiction averaging roughly 4.7–5k words, so do **not** treat its correlations as universal rules for novels.

For the exact 30-feature reference and long-form interpretation, read [reference.md](reference.md).
For smoke-test scenarios and expected behavior, read [evals.md](evals.md).

## Non-negotiable rules

- Never output an “AI probability” or claim authorship from this audit.
- Never treat one feature as a diagnosis.
- Never “humanize” by adding random typos, grammar errors, flashbacks, subplots, brands, reader address, moral ambiguity, or contradictions.
- Never punish a genre convention merely because it correlates with an AI-elevated feature.
- Always cite textual evidence for major findings.
- Prefer **3–5 structural interventions maximum** per pass.
- If the issue is only stylistic, say so instead of inventing a structural problem.

## Phase 0 — Task lock

Before analysis, determine from the available context:

1. Scope: scene / chapter / several chapters / whole work.
2. Genre and subgenre.
3. POV and narratorial distance.
4. Known authorial constraints or intentional devices.
5. Whether the user wants audit only, revision plan, or before/after comparison.

Do not drift into grammar, punctuation, KDP formatting, marketing, or fact-checking unless they block the narrative task.

## Phase 1 — Build a narrative skeleton

For each scene, extract only what the text supports:

```text
SCENE ID:
POV:
TIME:
LOCATION:
CHARACTERS:
IMMEDIATE GOAL:
OBSTACLE:
KEY ACTION / CHOICE:
CONSEQUENCE:
NEW INFORMATION / REVEAL:
EMOTIONAL SHIFT:
THEME SIGNAL:
END STATE:
```

For a chapter or larger unit, also track:

```text
PRIMARY ARC:
SECONDARY ARC(S):
CAUSAL CHAIN:
TEMPORAL ORDER:
REVELATION ORDER:
RESOLUTION MODE:
OPEN QUESTIONS:
```

Do not line-edit yet.

## Phase 2 — Select the right audit depth

### Quick chapter mode
Use for ordinary chapter review. Evaluate the **5–10 features most relevant** to the actual text rather than mechanically filling all 30.

### Full 30-feature mode
Use when the user explicitly asks for a full audit, the chapter is structurally important, or several suspicious patterns overlap.

### Novel / multi-chapter mode
Prefer this for long-form work. Audit distributions across scenes/chapters and look for repeated defaults rather than forcing every individual chapter to contain “human-elevated” techniques.

### Before/after mode
Compare versions at the level of narrative decisions. Distinguish structural change from a merely different wording of the same pattern.

## Phase 3 — Score editorial risk, not authorship

For each selected feature, use:

```text
0 = absent / neutral
1 = local or plausibly intentional
2 = repeated pattern worth attention
3 = dominant pattern that narrows narrative variability
N/A = not applicable to genre, form, POV, or available scope
```

Every risk 2–3 must include evidence.

Do not sum scores into a single probability. Instead group findings into patterns:

- thematic over-determination
- sensory / embodied performativity
- structural streamlining
- temporal / revelation simplicity
- narrative homogeneity

## Phase 4 — Correct for genre and intent

Before recommending a change, ask:

**Could this feature be an intentional and effective genre/voice choice?**

If yes, mark it:

`INTENTIONAL — KEEP`

Examples:

- cozy fiction may intentionally have strong spatial grounding and sensory attention;
- literary fiction may intentionally sustain deep interior access;
- detective fiction may favor strong causal continuity while still using complex revelation structure;
- first-person memoir-like fiction may naturally address the reader;
- epic fantasy may require many locations without that being a quality signal by itself.

## Phase 5 — Detect systemic patterns in long-form

The following are **editorial heuristics, not thresholds from the paper**.

Treat a pattern as systemic when one or more are true:

- the same decision dominates at least 3 independent scenes/chapters;
- a risk-2/3 feature appears in roughly 30%+ of analyzed units;
- several different features point to the same underlying construction problem.

For fragments under ~1,500 words, lower confidence and do not generalize to the whole book.

## Phase 6 — Prioritize structural fixes

Choose no more than 3–5 interventions. Rank them by:

1. cross-chapter impact;
2. effect on reader experience;
3. compatibility with authorial intent;
4. low risk of breaking causality/continuity.

Use this format:

```text
PROBLEM:
EVIDENCE:
WHY IT MATTERS:
STRUCTURAL FIX:
WHAT NOT TO DO:
EXPECTED EFFECT:
CONFIDENCE: High / Medium / Low
```

Fix the **cause**, not the surface marker.

Example:

Bad fix: replace “his chest tightened” with another bodily reaction.

Better fix: if 8 of 10 emotional beats rely on bodily metaphors, diversify the narrative function of emotion: choice, silence, misdirection, speech, direct naming, behavior, delayed reaction, or no expected reaction.

Bad fix: “no flashbacks → add two flashbacks.”

Better fix: if all crucial information arrives in strict chronological order, identify one reveal that genuinely recontextualizes an earlier scene and restructure only around that reveal.

## Phase 7 — Re-audit

After revision, compare:

```text
BEFORE:
AFTER:
PATTERN REDUCED?
NEW SIDE EFFECTS?
CHARACTER / CAUSAL CONTINUITY PRESERVED?
```

Do not require all risk scores to go down. A strong novel may intentionally score high on several StoryScope-correlated features.

## Default output

```markdown
## StoryScope Audit — [work/chapter]

**Scope:**
**Confidence:** High / Medium / Low
**Verdict:** 2–3 sentences. Never claim “this is AI”.

### Narrative skeleton
- ...

### Main structural patterns
1. **[Pattern] — risk X**
   - Evidence:
   - Why it matters:

### Core-feature profile
| Feature | Risk | Evidence | Action |
|---|---:|---|---|

### Priority interventions
1. ...
2. ...
3. ...

### Keep unchanged
- strong intentional choices that should survive editing

### Re-audit target
- what to verify after revision
```

## Integration order for fiction

When multiple skills are available, use this order unless the task says otherwise:

```text
1. storyscope-fiction-audit
2. continuity / character logic audit
3. developmental edit
4. prose naturalness / line edit
5. KDP finalizer / production checks
```

If this audit finds major risk-2/3 structural problems, do not spend the main pass polishing sentences that are likely to be rewritten.

## Quality gate

Before finalizing the audit, verify:

- [ ] I analyzed narrative decisions, not just wording.
- [ ] Every major criticism has evidence.
- [ ] I did not turn correlation into a universal writing rule.
- [ ] I accounted for genre, POV, and authorial intent.
- [ ] I did not mechanically add “human-elevated” features.
- [ ] I limited the pass to 3–5 meaningful structural interventions.
- [ ] I separated structural editing from line editing.
- [ ] I did not output an AI probability or authorship claim.
- [ ] I lowered confidence when the sample is too short.
- [ ] I specified what to re-audit after changes.

## Sources

- Russell, Rajendhran, Pham, Iyyer, Wieting. *StoryScope: Investigating idiosyncrasies in AI fiction.* COLM 2026, arXiv:2604.03136v6.
- Official code/data: `jenna-russell/storyscope`.
- This skill’s scoring, long-form thresholds, workflow, and revision policy are editorial adaptations, not claims made by the paper.
