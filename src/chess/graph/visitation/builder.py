# src/chess/graph/visitation/builder.py

"""
Module: chess.graph.visitation.builder
Author: Banji Lawal
Created: 2025-111-03
version: 1.0.0
"""


from chess.graph.domain import DomainValidator
from chess.piece import Piece, PieceValidator
from chess.graph import Visitation
from chess.system import BuildResult, Builder, ChessException, IdValidator, InvalidIdException, LoggingLevelRouter


class VisitationBuilder(Builder[Visitation]):
    """"""

    @classmethod
    @LoggingLevelRouter.monitor
    def build(cls, id: int, domain, domain_visitor: Piece) -> BuildResult[Visitation]:
        """"""
        method = "VisitationBuilder.build"
        
        try:
            id_validation = IdValidator.validate(id)
            if id_validation.is_failure():
                return BuildResult.failure(
                    InvalidIdException(f"{method}: {InvalidIdException.DEFAULT_MESSAGE}")
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
            
            BuildResult.success(payload=Visitation(domain=domain, visitor=domain_visitor))
            
        except Exception as e:
            return BuildResult.failure(e)
