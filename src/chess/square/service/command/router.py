# src/chess/square/service/route/route.py

"""
Module: chess.square.service.route.route
Author: Banji Lawal
Created: 2026-02-24
"""

from __future__ import annotations

from typing import List

from chess.square import SquareService
from chess.system import CommandRouter


class SquareServiceRouter(CommandRouter):
    OPERATIONS: List[SquareServiceOperation] = [
        SquareBuildOperation
    ]
    operations: List[SquareServiceOperation]
    
    def __init__(self,
            service: SquareService = SquareService(),
            par: List[ServiceOperation],
    ):
        
    @property
    def operations(self) -> List[ServiceOperation]:
        return self._operations
    
    
    def route(self, service_request: ServiceRequest) -> Any:
    