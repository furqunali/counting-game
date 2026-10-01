import json

from .session import CountingSession


def session_to_json(session: CountingSession) -> str:
    """Serialize a counting session snapshot to JSON."""
    if not isinstance(session, CountingSession):
        raise TypeError("session must be a CountingSession")
    return json.dumps(session.to_dict())


def session_from_json(payload: str) -> CountingSession:
    """Restore a counting session from a JSON snapshot."""
    if not isinstance(payload, str):
        raise TypeError("payload must be a string")
    data = json.loads(payload)
    if not isinstance(data, dict):
        raise ValueError("session payload must contain an object")
    return CountingSession.from_dict(data)
