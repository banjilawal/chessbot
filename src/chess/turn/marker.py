from typing import Optional

from chess.agent import PlayerAgent


class Marker:
    _current_holder: Optional[PlayerAgent]
    _previous_holder: Optional[PlayerAgent]
    
    def __init__(self):
        self._current_holder = None
        self._previous_holder = None
        
    @property
    def current_holder(self) -> Optional[PlayerAgent]:
        return self._current_holder
    
    @property
    def previous_holder(self) -> Optional[PlayerAgent]:
        return self._previous_holder
    
    @current_holder.setter
    def set_current_holder(self, player: PlayerAgent):
        self._previous_holder = self._current_holder
        self._current_holder = player