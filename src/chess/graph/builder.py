# src/chess/graph/factory.py

"""
Module: chess.graph.builder
Author: Banji Lawal
Created: 2025-11-08
version: 1.0.0
"""


from chess.graph import Graph
from chess.board import Board, BoardValidator
from chess.system import Builder, BuildResult, IdValidator, LoggingLevelRouter


class GraphBuilder(Builder[Graph]):
    """"""
    
    @classmethod
    @LoggingLevelRouter.monitor
    def build(cls, id: int, board: Board) -> BuildResult[Graph]:
        """"""
        method = "GraphBuilder.builder"
        
        try:
            id_validation = IdValidator.validate(id)
            if id_validation.is_failure():
                return BuildResult.failure(id_validation.exception)
            
            board_validation = BoardValidator.validate(board)
            if board_validation.is_failure():
                return BuildResult.failure(board_validation.exception)
            
            return BuildResult.success(Graph(id=id, board=board))
        except Exception as e:
            return BuildResult.failure(e)