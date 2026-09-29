# src/sync/turn/service/turn.py

"""
Module: sync.turn.service.turn
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from sync import TurnReferee



class TurnManagementService:
    _referee: TurnReferee
    
    def __init__(self, referee: TurnReferee):
        self._referee = referee
        
    @property
    def referee(self) -> TurnReferee:
        return self._referee
        
        
