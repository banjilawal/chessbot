# src/sync/turn/service/turn.py

"""
Module: sync.turn.service.turn
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional

from sync import TurnReferee



class TurnManagementService:
    _referee: TurnReferee
    
    def __init__(
            self,
            referee: Optional[TurnReferee] | None = None
    ):
        self._referee = referee or TurnReferee()
        
    @property
    def referee(self) -> TurnReferee:
        return self._referee
        
        
