# Counting Game

A command-line game for practicing **skip-counting**, with reusable Python domain logic, session analytics, persistence, and automated tests.

## Install

Requires Python 3.11+.

```bash
python -m pip install -e ".[dev]"
```

## Run

```bash
python counting_game.py
```

## Test

```bash
pytest
```

## Package API

Supported domain functionality is exported from `counting_game_core`:

- `CountingSession` — stateful round/session lifecycle
- `SessionStats` — accuracy and streak analytics
- `session_metrics` — session-level reporting
- `session_to_json` / `session_from_json` — validated JSON persistence
- `counting_sequence` / `sequence_until` — reusable sequence generation

## Persistence

Sessions can be serialized as JSON and restored later without losing the configured game parameters or recorded results.

```python
from counting_game_core import session_from_json, session_to_json

payload = session_to_json(session)
restored = session_from_json(payload)
```

The persistence layer validates payload structure and delegates state validation to the domain model.

## Example

```text
Round 1: 3, 8, 13, 18, ...
What is the next number? 23
Correct!
```

## Roadmap

- Richer CLI session summaries
- Exportable analytics reports
- Additional persistence formats
- Small interactive demo for the reusable domain API
