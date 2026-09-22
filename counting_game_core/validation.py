def validate_rounds(rounds: int) -> int:
    rounds = int(rounds)
    if rounds < 1 or rounds > 1000:
        raise ValueError("rounds must be between 1 and 1000")
    return rounds

def validate_range(start: int, end: int) -> tuple[int, int]:
    start, end = int(start), int(end)
    if start >= end:
        raise ValueError("start must be less than end")
    return start, end

def validate_step(step: int) -> int:
    step = int(step)
    if step == 0:
        raise ValueError("step cannot be zero")
    return step
