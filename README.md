# League Tiebreak Auditor

Recomputes a league table from match results and applies a fully specified tie-break chain.

## Tools

`compute_standings` calculates every row; `audit-league-standings` ranks teams by points, goal difference, goals for, then team id.

## Layout

`contract.py` declares matches and rows, `src/plugin/` computes the table, `verifier/` independently recounts it, and `tests/` cover results, tie-breaks, empty seasons, and invalid matches.

## Develop and run

Run `uv sync --extra dev`, `uv run pytest`, and `uv run ruff check .`.
