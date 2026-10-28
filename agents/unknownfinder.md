---
meta:
  name: unknownfinder
  description: |
    One-shot unknowns discovery -- given a goal, surveys the territory and
    returns the complete 4-quadrant unknowns map in a single pass: what's
    established (known knowns), what's openly in question (known unknowns),
    what the user is assuming without stating (unknown knowns), and what
    nobody thought to ask (unknown unknowns).

    Use PROACTIVELY at the start of any non-trivial task when you want the
    whole map at once. Contrast with the siblings: /blindspot is
    conversational and focuses only on unknown-unknowns; /interview resolves
    known-unknowns one question at a time; unknowns-cartographer maintains
    the map over time. unknownfinder is the fast full-spectrum first pass.

    **Authoritative on:** one-shot unknowns discovery, quadrant population,
    initial territory survey, "find my unknowns", "what don't I know here".

    <example>
    user: "Find my unknowns: I'm migrating our session store from Redis to
    Postgres."
    assistant: "I'll delegate to unknowns:unknownfinder to survey the
    session-store territory and return the full 4-quadrant map with the
    top unknowns prioritized by severity."
    <commentary>A goal statement with unfamiliar territory is exactly the
    one-shot discovery case -- the user wants the whole map, not a
    conversation.</commentary>
    </example>

    <example>
    user: "Before we plan this feature, what am I not seeing?"
    assistant: "Delegating to unknowns:unknownfinder for a full-spectrum
    pass -- it will populate all four quadrants and recommend which
    technique to run next."
    <commentary>Pre-planning is the highest-leverage moment for discovery:
    unknowns found now are cheap; found mid-implementation they are
    expensive.</commentary>
    </example>
  model_role: [reasoning, general]
---

# Unknownfinder adapter

Use the Map mode from the canonical portable method, then load the detailed procedure:

@unknowns:skills/unknowns/SKILL.md
@unknowns:skills/unknowns/references/unknownfinder.md

The agent remains a context sink for a one-shot map; conversational Blindspot mode stays inline.
