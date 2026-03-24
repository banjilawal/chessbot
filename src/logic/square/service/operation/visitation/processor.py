# src/logic/square/service/visitation/processor.py

"""
Module: logic.square.service.visitation.processor
Author: Banji Lawal
Created: 2026-02-22
version: 1.0.0
"""

from __future__ import annotations

from logic.square import SquareDepartureProcess, SquareEntryProcess


class VisitationProcessor:
    """
    Role:
        -   Lifecycle Processor

    Responsibilities:
        1.  Owner of complete SquareVisitation lifecycle.
        2.  Provides single entry point to the processes for
                -   SquareEntry
                -   SquareDeparture
    Attributes:
        entry_processor: SquareEntryProcess
        departure_processor: SquareDepartureProcess
        
    Provides:
    Super Class:
    """
    
    _entry_processor: SquareEntryProcess
    _departure_processor: SquareDepartureProcess
    
    def __init__(
            self,
            entry_processor: SquareEntryProcess = SquareEntryProcess(),
            departure_processor: SquareDepartureProcess = SquareDepartureProcess(),
    ):
        self._entry_processor = entry_processor
        self._departure_processor = departure_processor
        
        
    @property
    def entry_processor(self) -> SquareEntryProcess:
        return self._entry_processor
    
    @property
    def departure_processor(self) -> SquareDepartureProcess:
        return self._departure_processor