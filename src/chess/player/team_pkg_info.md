# Team Design Summary

## Overview

The `Team` class represents one side in the chess game, responsible for tracking the pieces that belong to it, its color, starting positions, and strategy. Each `Team` instance is immutable in core identity (e.g., color, starting row), but maintains a mutable dictionary of its active pieces.

---

## Data Structure

```python
@dataclass(frozen=True)
class Team:
    color: GameColor
    starting_row: int
    advancement_direction: int  # +1 or -1
    goal_row: int
    # piece_registry is mutable but not None
    # Maps rank_name + number → ChessPiece or None if captured
    piece_registry: dict[str, Optional[ChessPiece]]
