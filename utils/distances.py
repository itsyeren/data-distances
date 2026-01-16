"""Distance utilities for the data-distances project."""
from typing import Iterable, Sequence

__all__ = ["manhattan"]


def manhattan(a: Sequence[float], b: Sequence[float]) -> float:
    """Compute the Manhattan (L1) distance between two points.

    Args:
        a: Sequence of coordinates for the first point (e.g., tuple or list).
        b: Sequence of coordinates for the second point.

    Returns:
        The Manhattan distance as a float (sum of absolute coordinate differences).

    Raises:
        ValueError: if the points have different dimensions.
    """
    if len(a) != len(b):
        raise ValueError("Points must have the same dimension")

    try:
        return float(sum(abs(x - y) for x, y in zip(a, b)))
    except TypeError as exc:
        # Provide a clearer error when subtraction or abs fails for inputs
        raise TypeError("Coordinates must be numeric values") from exc
