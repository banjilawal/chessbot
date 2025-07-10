class HorizontalMovementStrategy(MovementStrategy):
    def move(self, mover: "Mover", grid: "Grid", direction: str, distance: int = 1):
        if mover.coordinate is None:
            print("[Warning] Mover has no coordinate.")
            return

        x, y = mover.coordinate.x, mover.coordinate.y
        new_x = x

        if direction == "left":
            new_x = x - distance
        elif direction == "right":
            new_x = x + distance
        else:
            print(f"[Warning] Invalid direction for horizontal mover: {direction}")
            return

        # Bounds check
        if not (0 <= new_x < grid.dimension.length):
            print(f"[Warning] Horizontal move out of bounds: {new_x}")
            return

        # Occupancy check
        target_cell = grid.cells[y][new_x]
        if target_cell.occupant is not None:
            print("[Info] Target cell is occupied.")
            return