# src/chess/board/square/service.py

"""
Module: chess.board.square.service
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""
from typing import cast

from chess.board import (


)
from chess.square import UniqueSquareDataService
from chess.system import COLUMN_SIZE,ROW_SIZE


class BoardSquareService:
    _capacity: int
    _member_service: UniqueSquareDataService
    _analyzer: BoardSquareRelationAnalyzer
    
    def __init__(
            self,
            capacity: int = ROW_SIZE * COLUMN_SIZE,
            member_service: UniqueSquareDataService = UniqueSquareDataService(),
            analyzer: BoardSquareRelationAnalyzer = BoardSquareRelationAnalyzer(),
    ):
        self._capacity = capacity
        self._analyzer = analyzer
        self._member_service = member_service

    
    @property
    def board_square_analyzer(self) -> BoardSquareRelationAnalyzer:
        return self._analyzer

    
    
