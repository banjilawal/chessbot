# Chess Game Design: Rank.md

## Purpose of the `Rank` Abstraction

The `Rank` class hierarchy encapsulates the behavior and movement strategy of each type of chess piece, separating movement logic from the piece's identity and state. Each `Rank` represents a distinct movement strategy (e.g., Pawn, Knight, Queen) and is immutable once assigned, except for special cases like promotion.

## Why Not Use Rank IDs

Unlike arrays or enums indexed by ID, each `Rank` is a concrete class with its own behavior and strategy methods. Using a `rankId` would not help because:
- Each `Rank` is already unique and not part of a uniform list.
- The key attribute is `rank_name`, which is human-readable and semantically meaningful.
- Behavior (like `canMove(from, to)`) is polymorphic and not switch-based.

## Typical Methods

Every `Rank` subclass (e.g., `PawnRank`, `KnightRank`) implements:

```ts
abstract class Rank {
  readonly rank_name: string;

  constructor(rank_name: string) {
    this.rank_name = rank_name;
  }

  abstract isValidMove(from: Coordinate, to: Coordinate, piece: ChessPiece, board: Board): boolean;
}
