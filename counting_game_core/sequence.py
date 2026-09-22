from collections.abc import Iterator

def counting_sequence(start: int, step: int, length: int) -> tuple[int, ...]:
    """Return a validated arithmetic counting sequence."""
    for name, value in (("start", start), ("step", step), ("length", length)):
        if isinstance(value, bool) or not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
    if step == 0:
        raise ValueError("step must not be zero")
    if length < 1:
        raise ValueError("length must be positive")
    return tuple(start + index * step for index in range(length))

def sequence_until(start: int, step: int, end: int) -> Iterator[int]:
    """Yield an arithmetic sequence without crossing its inclusive bound."""
    for name, value in (("start", start), ("step", step), ("end", end)):
        if isinstance(value, bool) or not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
    if step == 0:
        raise ValueError("step must not be zero")
    if (step > 0 and start > end) or (step < 0 and start < end):
        return
    current = start
    while (step > 0 and current <= end) or (step < 0 and current >= end):
        yield current
        current += step
