# src/controller/visit/controller.py

"""
Module: controller.visit.controller
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from controller import Controller


class VisitationController(Controller):
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
    
    def controller(
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