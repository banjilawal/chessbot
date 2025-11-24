from typing import Optional

from chess.coord import Coord, CoordDataService


class Stack:
    _size: int
    _is_empty: bool
    _current_position: Coord
    _data_service: CoordDataService
    
    def __init__(
            self,
            data_service: CoordDataService = CoordDataService()
    ):
        self._data_service = data_service
        self._is_empty = self._data_service.is_empty()
        self._current_position = self._data_service.item[-1] if self._teams else None
    
    @property
    def is_empty(self) -> bool:
        return self._data_service.is_empty()
    
    
    @property
    def current_position(self) -> Optional[Coord]:
        return self._data_service.current_item