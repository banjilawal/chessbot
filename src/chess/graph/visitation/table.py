from typing import List

from chess.graph import Visitation


class VisitationTable:
    _entries: List[Visitation]
    
    def __init__(self, entries: List[Visitation]=List[Visitation]):
        self._entries = entries
        
    @property
    def entries(self) -> List[Visitation]:
        return self._entries