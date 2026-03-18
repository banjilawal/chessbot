# src/logic/square/service/visitation/processor.py

"""
Module: logic.square.service.visitation.processor
Author: Banji Lawal
Created: 2026-02-22
version: 1.0.0
"""

from __future__ import annotations

from logic.square import SquareDepartureProcessor, SquareEntryProcessor


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
        entry_processor: SquareEntryProcessor
        departure_processor: SquareDepartureProcessor
        
    Provides:
    Super Class:
    """
    
    _entry_processor: SquareEntryProcessor
    _departure_processor: SquareDepartureProcessor
    
    def __init__(
            self,
            entry_processor: SquareEntryProcessor = SquareEntryProcessor(),
            departure_processor: SquareDepartureProcessor = SquareDepartureProcessor(),
    ):
        self._entry_processor = entry_processor
        self._departure_processor = departure_processor
        
        
    @property
    def entry_processor(self) -> SquareEntryProcessor:
        return self._entry_processor
    
    @property
    def departure_processor(self) -> SquareDepartureProcessor:
        return self._departure_processor