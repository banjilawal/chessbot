from typing import Optional, List

from chess.exception.coordinate.NullCoordinatePushException import NullCoordinatePushException
from chess.exception.coordinate.PopEmptyCoordinateStackException import PopEmptyCoordinateStackException
from chess.exception.coordinate.duplicate_coordinate_push import DuplicateCoordinatePushException
from chess.exception.coordinate.internal__stack_data_structure import InternalStackDataStructureException

from chess.geometry.coordinate.coordinate import Coordinate


class CoordinateStack:
    _items: List[Coordinate]
    _current_coordinate: [Coordinate]

    def __init__(self):
        self._items = []
        self._current_coordinate = self._items[-1] if self._items else None
        

    @property
    def stack(self) -> List[Coordinate]:
        return self._items
    
    
    @property
    def current_coordinate(self) -> Optional[Coordinate]:
        return self._items[-1] if self._items else None


    def is_empty(self) -> bool:
        return len(self._items) == 0


    def size(self) -> int:
        return len(self._items)

    
    def top_coord(self) -> Optional[Coordinate]:
        return self._items[-1] if self._items else None

    
    def push_coordinate(self, coordinate):
        method_name = "CoordinateStack.push"
        
        if coordinate is None:
            raise NullCoordinatePushException(
                f"{method_name} - {NullCoordinatePushException.DEFAULT_MESSAGE}"
            )
        
        if self._items is None:
            raise InternalStackDataStructureException(
                f"{method_name} - {InternalStackDataStructureException.ERROR_CODE}"
            )
        
        if  self.current_coordinate == coordinate:
            raise DuplicateCoordinatePushException(
                f"{method_name} - Cannot push duplicate coordinate onto stack"
            )
        self._items.append(coordinate)


    def undo_push(self):
        method_name = "CoordinateStack.undo_push"

        if len(self._items) == 0:
            raise PopEmptyCoordinateStackException(
                f"{method_name} - {PopEmptyCoordinateStackException.DEFAULT_MESSAGE}"
            )
        self._items.pop()