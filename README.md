# Counting Game

A command-line game for practicing **skip-counting**, with reusable Python domain logic and automated tests.

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

Supported domain functionality is exported from `counting_game_core`, including session analytics and metrics.

## Example

```text
Round 1: 3, 8, 13, 18, ...
What is the next number? 23
Correct!
```
