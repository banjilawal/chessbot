from typing import Optional, List

from chess.exception.coordinate_stack.push_null import NullCoordinatePushException
from chess.exception.coordinate_stack.pop_empty import PopEmptyCoordinateStackException
from chess.exception.coordinate_stack.push_duplicate import DuplicateCoordinatePushException
from chess.exception.stack import CorruptedStackException, PopEmptyStackException

from chess.geometry.coordinate.coord import Coordinate


class CoordinateStack:
    _items: List[Coordinate]
    _current_coordinate: [Coordinate]

    def __init__(self):
        self._items = []
        self._current_coordinate = self._items[-1] if self._items else None
        

    @property
    def items(self) -> List[Coordinate]:
        return self._items
    
    
    @property
    def current_coordinate(self) -> Optional[Coordinate]:
        return self._items[-1] if self._items else None


    def is_empty(self) -> bool:
        return len(self._items) == 0


    def size(self) -> int:
        return len(self._items)

    
    def push_coordinate(self, coordinate):
        method_name = "CoordinateStack.push"
        
        if coordinate is None:
            raise NullCoordinatePushException(
                f"{method_name}: {NullCoordinatePushException.DEFAULT_MESSAGE}"
            )
        
        if self._items is None:
            raise CorruptedStackException(f"{method_name}: {CorruptedStackException.DEFAULT_MESSAGE}")
        
        if  self.current_coordinate == coordinate:
            raise DuplicateCoordinatePushException(
                f"{method_name}: {DuplicateCoordinatePushException.DEFAULT_MESSAGE}"
            )
        self._items.append(coordinate)


    def undo_push(self):
        method_name = "CoordinateStack.undo_push"

        if len(self._items) == 0:
            raise PopEmptyStackException(f"{method_name}: {PopEmptyStackException.DEFAULT_MESSAGE}")
        self._items.pop()
#
#
# def main():
#     coordinate_stack = CoordinateStack()
#     coordinate_stack.push_coordinate(Coordinate(1, 1))
#     coordinate_stack.push_coordinate(Coordinate(1, 1))
#     print(f"Current Coordinate: {coordinate_stack.current_coordinate}")
#     coordinate_stack.undo_push()
#     print(f"Current Coordinate after undo: {coordinate_stack.current_coordinate}")
#
#
# if __name__ == '__main__':
#     main()