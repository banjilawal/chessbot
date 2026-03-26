# src/logic/square/service/visitation/compute.py

"""
Module: logic.square.service.visitation.process
Author: Banji Lawal
Created: 2026-02-22
version: 1.0.0
"""

from __future__ import annotations

from logic.square import SquareDepartureProcess, SquareEntryProcess


class VisitationController:
    """
    Role:
        -   Lifecycle Management
        -   Controller

    Responsibilities:
        1.  Owner of complete SquareVisitation lifecycle.
        2.  Provides single entry point to the processes for
                -   SquareEntry
                -   SquareDeparture
    Attributes:
        entry_process: SquareEntryProcess
        departure_process: SquareDepartureProcess
        
    Provides:
    Super Class:
    """
    
    _entry_process: SquareEntryProcess
    _departure_process: SquareDepartureProcess
    
    def __init__(
            self,
            entry_process: SquareEntryProcess = SquareEntryProcess(),
            departure_process: SquareDepartureProcess = SquareDepartureProcess(),
    ):
        self._entry_process = entry_process
        self._departure_process = departure_process
        
        
    @property
    def entry(self) -> SquareEntryProcess:
        return self._entry_process
    
    @property
    def departure(self) -> SquareDepartureProcess:
        return self._departure_process