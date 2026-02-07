<!-- Purpose: concise, actionable guidance for AI coding agents working in this repo -->
# Copilot / AI agent instructions

This repository is a collection of standalone programming-challenge solutions organized by topic. The instructions below focus on concrete, discoverable facts about the codebase so an AI agent can be immediately productive.

## Big picture
- Repo type: ad-hoc collection of Python scripts (no package, no CI, no requirements file).
- Structure: topic folders (e.g. `arrays/`, `linkedlist/`, `trees/`, `graphs/`, `dp/`, `recursion/`, `sorting/`) contain small, mostly self-contained solutions.
- Interaction model: scripts are generally runnable directly with `python3 <path>`; there is minimal cross-module packaging.

## How to run / debug locally
- Run a single script: `python3 arrays/twosum.py` (replace with any path under the topic folders).
- When a script imports another module in the repo, run with the repository root on `PYTHONPATH`: `PYTHONPATH=. python3 trees/TreeDS.py`.
- There is no test runner or build step in the repo; execute scripts directly and inspect stdout/return values.

## Detectable conventions & patterns
- File naming: snake_case and short descriptive filenames (e.g. `twosum.py`, `single_list.py`).
- Directory organization: each top-level folder groups related problems (see `arrays/`, `trees/`, `graphs/`).
- Implementation style: single-file solutions, often one main function or class per file; many files are intended to be executed as scripts.
- Imports: assume local imports are relative to repo root; do not assume an installed package.

## Helpful examples to reference
- Example array problem: `arrays/twosum.py` (run to see input/output pattern).
- Example tree helpers: `trees/TreeDS.py` and `trees/inorderRecursive.py` show simple data-structure helpers and traversal usage.
- Example linked list: `linkedlist/single_list.py` demonstrates node/list operations and standalone execution.

## What AI agents should do first (concrete steps)
1. Open `README.md` to confirm repo scope.
2. Inspect the target folder (e.g., `arrays/`) and run one representative script to observe its I/O pattern.
3. If adding or modifying code, keep changes local to the topic folder and run the modified script with `PYTHONPATH=.` when cross-file imports are added.

## Merge/update guidance (if this file already exists)
- Preserve these sections: **Big picture**, **How to run**, **Conventions**, and **Examples**.
- Only add project-discoverable facts — do not add high-level team policies or speculative workflows.

## Where to look for common change targets
- Add algorithm improvements or refactors inside the appropriate topic folder (e.g., optimize `arrays/maxSubArray.py`).
- When introducing shared helpers, prefer adding a new module under `DataStructures/` or `utils/` (create `utils/` if needed) and update callers to use `PYTHONPATH=.` when running.

## Known gaps (what I could not detect)
- No automated tests or dependency manifest detected; assume standard library only unless a script imports external packages.
- No CI configs found; do not rely on repository-level automated checks.

If anything in this file is unclear or you want different emphasis (tests, packaging, CI, or specific coding style), tell me which areas to expand or examples to include.
