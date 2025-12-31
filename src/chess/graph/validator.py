# src/chess/graph/coord_stack_validator.py

"""
Module: chess.graph.validation
Author: Banji Lawal
Created: 2025-10-28
version: 1.0.0
"""

from typing import Any

from chess.board import Board, BoardValidator
from chess.graph import Graph, NullGraphException
from chess.system import ChessException, LoggingLevelRouter, Validator, ValidationResult


class GraphValidator(Validator[Graph]):
    """
     # ROLE: Validation, Data Integrity Guarantor, Security.

    # RESPONSIBILITIES:
    1.  Ensure a Graph instance is certified safe, reliable and consistent before use.
    2.  If verification fails indicate the reason in an exception, returned to the caller.

    # PARENT:
        *   Validator

    # PROVIDES:
        * GraphValidator

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def validate(cls, candidate: Any) -> ValidationResult[Graph]:
        """"""
        method = "GraphValidator.validate"
        
        try:
            if candidate is None:
                return ValidationResult.failure(
                    NullGraphException(f"{method}: {NullGraphException.DEFAULT_MESSAGE}")
                )
                
                if not isinstance(candidate, Graph):
                    return ValidationResult.failure(
                        TypeError(f"{method} Expected Graph, got {type(candidate).__name__} instead.")
                    )
                
                graph = dast(Graph, candidate)
                id_validation = IdValidator.validate(graph.id)
                if id_validation.is_failure():
                    return ValidationResult.failure(id_validation)
                
                board_validation = BoardValidator.validate(graph.board)
                if board_validation.is_failure():
                    return ValidationResult.failure(board_validation)
                
                if graph.domains is None:
                    return ValidationResult.failure(
                        ChessException(f"{method}: Graph.domains cannot be null")
                    )
                
                if graph.neighbors is None:
                    return ValidationResult.failure(
                        ChessException(f"{method}: Graph.neighbors cannot be null")
                    )
                
                return ValidationResult.success(graph)
        
        except Exception as e:
            return ValidationResult.failure(e)
