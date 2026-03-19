# src/logic/neighbor/factory.py

"""
Module: logic.graph.neighbor.builder
Author: Banji Lawal
Created: 2025-111-03
version: 1.0.0
"""


from logic.domain import DomainValidationProcess
from logic.neighbor import VisitationEvent
from logic.piece import Piece, PieceValidator

from logic.system import BuildResult, BuildProcess, ChessException, IdValidationProcess, IdValidationException, LoggingLevelRouter



class VisitationEventBuildProcess(BuildProcess[VisitationEvent]):
    """"""

    @classmethod
    @LoggingLevelRouter.monitor
    def execute(cls, id: int, domain, domain_visitor: Piece) -> BuildResult[VisitationEvent]:
        """"""
        method = "VisitationBuilder.builder"
        
        try:
            id_validation = IdValidationProcess.execute(id)
            if id_validation.is_failure():
                return BuildResult.failure(
                    IdValidationException(f"{method}: {IdValidationException.MSG}")
                )
            
            domain_validation = DomainValidationProcess.execute(domain)
            if domain_validation.is_failure():
                return BuildResult.failure(domain_validation.exception)
            
            piece_validation = PieceValidator.execute(domain)
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
