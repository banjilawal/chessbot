# Responsibilities in Chess Game Architecture

## ChessPiece

Each `ChessPiece` instance is responsible for managing its own identity and movement history.

### Responsibilities:
- Holds a unique identifier (`id`), name (e.g., `"Pawn"`), color/team, and a reference to a `Rank`.
- Maintains a **stack** of positions to track its movement history (enabling undo).
- Does **not** validate moves — that’s the responsibility of the `Board`.
- Provides methods to:
  - Get current position.
  - Get previous position (top of the stack - 1).
  - Push a new position (when a legal move is made).
  - Pop a position (when a move is undone).
  - Check if it's making an opening move (based on position history length).
  - Report its current state: `FREE`, `CAPTURED`, or `PROMOTED`.

---

## Rank

Each `Rank` (e.g., `PawnRank`, `QueenRank`) defines a movement strategy.

### Responsibilities:
- Abstract class `Rank` provides:
  - `rank_name`: a string like `"Pawn"`, `"Knight"`, etc.
  - `movement_strategy`: a callable or object that encapsulates how the rank moves.
- Concrete subclasses (e.g., `PawnRank`, `KnightRank`) define specific behavior:
  - `PawnRank` includes logic for opening two-square move and diagonal captures.
  - Some ranks like `PawnRank` a
