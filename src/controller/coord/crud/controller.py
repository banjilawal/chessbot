# src/logic/coord/database/kernel/operation/exception.py

"""
Module: logic.coord.database.kernel.operation.operation
Author: Banji Lawal
Created: 2025-11-22
version: 1.0.0
"""

from __future__ import annotations

from logic.coord import CoordQueryService, CoordStackPop, CoordStackPush


class CoordStackCrudController:
    """
    Role:
        -   CRUD controller
        -   Consistency provider
        -   Integrity lifecycle manager

    Responsibilities:
        1.  Manage insertion/deletion operations for CoordStackService.

    Attributes:
        pop: CoordStackPop
        push: CoordStackServicePush

    Provides:

    Super Class:
    """
    
    _pop: CoordStackPop
    _push: CoordStackPush
    _query: CoordQueryService
    
    def __init__(
            self,
            pop: CoordStackPop = CoordStackPop(),
            push: CoordStackPush = CoordStackPush(),
            query: CoordQueryService = CoordQueryService(),
    ):
        self._pop = pop
        self._push = push
        self._query = query
        
    @property
    def pop(self) -> CoordStackPop:
        return self._pop
    
    @property
    def push(self) -> CoordStackPush:
        return self._push
    
    @property
    def query(self) -> CoordQueryService:
        return self._query
    
    
    