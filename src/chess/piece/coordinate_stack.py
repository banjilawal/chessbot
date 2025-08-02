# from assurance.transaction_report import StatusCode

#
    #
    #
    # # === Stack operations ===
    # def push_new_coordinate(self, coordinate: Coordinate) -> TransactionReport:
    #     method = "ChessPiece.push_new_coordinate"
    #     old_size = len(self._coordinate_stack)
    #
    #     if coordinate is None:
    #         return TransactionReport(method, Failure("Cannot push a null coordinate on to te stack"))
    #     if coordinate in self._coordinate_stack:
    #         print(f"{coordinate} is already on {self._label}'s stack. No need for a push.")
    #         return TransactionReport(method, StatusCode.SUCCESS)
    #
    #     self._coordinate_stack.append(coordinate)
    #
    #     if coordinate == self.current_coordinate() and old_size + 1 == len(self._coordinate_stack):
    #         return TransactionReport(method, StatusCode.SUCCESS)
    #     return TransactionReport(method, Failure("Failed to push coordinate on to stack"))
    #
    #
    # def undo_last_coordinate_push(self) -> Optional[Coordinate]:
    #
    #     if len(self._coordinate_stack) == 0:
    #         print(f"{self._label} has no coordinates to undo")
    #         return None
    #
    #     if self._coordinate_stack:
    #         return self._coordinate_stack.pop()
    #     return None
    #
    #
    # def current_coordinate(self) -> Optional[Coordinate]:
    #     return self._coordinate_stack[-1] if self._coordinate_stack else None