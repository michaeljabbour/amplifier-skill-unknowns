---
bundle:
  name: unknowns
  version: 0.1.0
  description: >
    Find and resolve unknowns -- the gap between your prompt (the map) and
    the codebase/reality (the territory). Implements the 4-quadrant unknowns
    matrix (known knowns, known unknowns, unknown knowns, unknown unknowns)
    from Thariq's "A Field Guide to Fable: Finding Your Unknowns" as a living
    DOT artifact (.ai/unknowns-map.dot) that every technique reads and writes.

    Entry points:
      /unknownfinder -- one-shot full-spectrum discovery: the complete
                       4-quadrant map from a goal (also delegable as the
                       unknowns:unknownfinder agent)
      /blindspot    -- surface unknown-unknowns before starting unfamiliar work
      /interview    -- resolve known-unknowns one question at a time
      unknowns:pipelines/unknowns-lifecycle.dot -- full pre/during/post lifecycle,
                       run via the attractor run_pipeline tool

includes:
  - bundle: git+https://github.com/microsoft/amplifier-foundation@main
  # Keep Attractor awareness and load its interactive entry by explicit source.
  # A fresh registry resolves concurrent includes independently; it must not
  # require an attractor alias registered by another include first.
  # The same existing dependency supplies run_pipeline and the interactive loop.
  - bundle: git+https://github.com/microsoft/amplifier-bundle-attractor@main
  - bundle: git+https://github.com/microsoft/amplifier-bundle-attractor@main#subdirectory=bundles/attractor-interactive.yaml
  - bundle: unknowns:behaviors/unknowns
---

# Unknowns Explorer

Find and resolve unknowns before they get expensive to fix -- the gap between
your prompt (the map) and the codebase/reality (the territory). Quick start
and composition notes: unknowns:README.md (read on demand -- not eagerly
loaded). The always-on framing this session carries is provided by the
unknowns:behaviors/unknowns behavior via context.include
(context/unknowns-awareness.md) -- not duplicated here.

---

@foundation:context/shared/common-system-base.md
