# src/chess/neighbor/factory.py

"""
Module: chess.graph.neighbor.builder
Author: Banji Lawal
Created: 2025-111-03
version: 1.0.0
"""


from chess.domain import DomainValidator
from chess.neighbor import VisitationEvent
from chess.piece import Piece, PieceValidator

from chess.system import BuildResult, Builder, ChessException, IdValidator, IdValidationException, LoggingLevelRouter



class VisitationEventBuilder(Builder[VisitationEvent]):
    """"""

    @classmethod
    @LoggingLevelRouter.monitor
    def build(cls, id: int, domain, domain_visitor: Piece) -> BuildResult[VisitationEvent]:
        """"""
        method = "VisitationBuilder.builder"
        
        try:
            id_validation = IdValidator.validate(id)
            if id_validation.is_failure():
                return BuildResult.failure(
                    IdValidationException(f"{method}: {IdValidationException.DEFAULT_MESSAGE}")
                )
            
            domain_validation = DomainValidator.validate(domain)
            if domain_validation.is_failure():
                return BuildResult.failure(domain_validation.exception)
            
            piece_validation = PieceValidator.validate(domain)
            if piece_validation.is_failure():
                return BuildResult.failure(piece_validation.exception)
            
            if domain_visitor == domain.owner:
                return BuildResult.failure(
                    ChessException(f"{method}: Domain Owner cannot be its own domain visitor")
                )
            
            if domain_visitor.current_position not in domain.tree:
                return BuildResult.failure(
                    ChessException(f"{method}: Visitor's current position is not in the domain tree.")
                )
            
            BuildResult.success(payload=VisitationEvent(domain=domain, visitor=domain_visitor))
            
        except Exception as e:
            return BuildResult.failure(e)
