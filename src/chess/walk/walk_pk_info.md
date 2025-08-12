# `chess.walk` Package Documentation

## Table of Contents

### Purpose
Tests if `ChessPiece` instance can reach a destination with constraints on motion by its `Rank`.

## Design Principles
 - Strategy pattern for scalable maintainable independent movement validation.
 - Fast validation with simple boolean test.
 - Single objets in system with static methods.

## Class Relationship Diagram
```plantuml
    @startuml
    title Relationships Between Classes Implementing Walk Interface
    
    Interface Walk {
      + is_walkable(chess_piece: ChessPiece, destination: Coordinate): bool
    }
    
    Class KingWalk {}
    Class QueenWalk {}
    Class KnightWalk {}
    Class BishopWalk {}
    Class CastleWalk {}
    Class PawnWalk {
      - can_advance(chess_piece: ChessPiece, destination: Coordinate): bool
      - can_attack(chess_piece: ChessPiece, destination: Coordinate): bool
    }
    
    Walk <-left- KingWalk
    Walk <-right- QueenWalk
    
    Walk <-up- BishopWalk
    Walk <-up- CastleWalk
    
    Walk <-Down- KnightWalk
    Walk <-Down- PawnWalk
    
    @enduml
```
## Classes

## Class Relationship Diagram
```plantuml
@startuml
title Relationships Between Classes in Walk Package

Interface Walk {
  + is_walkable(chess_piece: ChessPiece, destination: Coordinate): bool
}

Class KingWalk {}
Class QueenWalk {}
Class KnightWalk {}
Class BishopWalk {}
Class CastleWalk {}
Class PawnWalk {
  - can_advance(chess_piece: ChessPiece, destination: Coordinate): bool
  - can_attack(chess_piece: ChessPiece, destination: Coordinate): bool
}

Walk <-left- KingWalk
Walk <-right- QueenWalk

Walk <-up- BishopWalk
Walk <-up- CastleWalk

Walk <-Down- KnightWalk
Walk <-Down- PawnWalk

@enduml
```

## 🧩 Classes

### `Walk Interface`

#### Methods:
Abstract, static class which must be implemented
```python
 # Returns true if the destination is reachable from the chess_piece location
is_walkable(chess_piece: ChessPiece, destination: Coordinate) -> bool:
```

#### Validation:
 - Rejects Null ChessPiece  (`NullChessPieceException`)
 - rejects Null Coordinate (`NullCoordinateException`)

### `Walk` Interface Implementors
- `KingWalk`
- `PawnWalk`
- `KnightWalk`
- `BishopWalk`
- `CastleWalk`
- `QueenWalk`
```python

## Usage Examples

### `ChessPiece` Validating `Coordinate` is Reachable Before Executing Walk
```python
destination = Coordinate(2,3)
origin = chess_piece.coordinate_stack.current_coordinate()

if not chess_piece.rank.is_walkable(chess_piece, destination):
    raise DestinationUnreachableException(
        f"ChessPiece {chess_piece.name} "
        f"cannot reach {destination} "
        f"from its current coordinate {origin}"
    )
chess_board.capture_square(chess_piece, destination)
```

