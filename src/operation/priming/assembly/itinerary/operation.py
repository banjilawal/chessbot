# src/operation/priming/assembly/coord/operation.py

"""
Module: operation.priming.assembly.coord.operation
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import cast

from blueprint import ItineraryBlueprint
from model import Itinerary
from operation import AssemblyPrimer
from report import RelationReport, TokenFreedomReport
from result import ValidationResult
from toolkit import ItineraryToolkit
from util import LoggingLevelRouter


class ItineraryAssemblyPrimer(AssemblyPrimer[Itinerary]):
    NAME = "itinerary_assembly_primer"
    """
    Role:
        - Transaction Worker
        - Consistency, Integrity Maintenance
        - Process Runner

    Responsibilities:
        1.  Square entry exception owner.
        2.  Preserve original and updated square data for rollbacks.
        3.  Ensure both the token and the squares are consistent throughout
            square entry lifecycle.

    Attributes:

    Provides:
        -   execute(
                    token: Token,
                    square: Square,
                    token_freedom_analyzer: TokenFreedomAnalyzer,
                    square_validator: SquareValidator,
            ) -> UpdateResult[Square]:

    Super Class:
    """
    
    @classmethod
    @LoggingLevelRouter.monitor()
    def execute(
            cls,
            blueprint: ItineraryBlueprint,
            toolkit: ItineraryToolkit | None = None,
    ) -> ValidationResult[ItineraryBlueprint]:
        """
        Action:
            1.  Send the original square along with an exception chain in the validation result if:
                    -   The square or token are insecure.
                    -   The token is disabled
                    -   The token belongs to a different board.
                    -   The new token is being deployed to the wrong square.
                    -   The square is already occupied.
                    -   The square accepts the token but the token cannot update its position.
            2.  Otherwise, each updates its state.
            3.  Send the success result.
        Args:
            token: Token
            destination_square: Square
            token_freedom_analyzer: TokenFreedomAnalyzer
            square_validator: SquareValidator
       Returns:
            UpdateResult[Square]
        Raises:
        """
        method = f"{cls.__class__.__name__}.execute"
        
        # --- Supply any missing dependencies. ---#
        if toolkit is None:
            toolkit = ItineraryToolkit()
        
        token_freedom_build_result = toolkit.token_freedom_analyzer.analyze(blueprint.traveler)
        # Handle the case that, the freedom_analysis is not completed.
        if token_freedom_build_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                ItineraryAssemblyPrimerException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=ItineraryAssemblyPrimerException.MSG,
                    err_code=ItineraryAssemblyPrimerException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.BUILD_RESULT,
                    ex=token_freedom_build_result.exception,
                )
            )
        report = cast(TokenFreedomReport, token_freedom_build_result.payload)
        # Handle the case that, the token is not free.
        if report.token_is_not_free:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                ItineraryAssemblyPrimerException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=ItineraryAssemblyPrimerException.MSG,
                    err_code=ItineraryAssemblyPrimerException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.BUILD_RESULT,
                    ex=DisabledTokenMoveException(
                        msg=DisabledTokenMoveException.MSG,
                        err_code=DisabledTokenMoveException.ERR_CODE,
                    ),
                )
            )
        source_square_search_result = blueprint.traveler.team.board.squares.search(context=SquareContext(occupant=token))
        # Handle the case that, the search is not completed.
        if source_square_search_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                ItineraryAssemblyPrimerException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=ItineraryAssemblyPrimerException.MSG,
                    err_code=ItineraryAssemblyPrimerException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.BUILD_RESULT,
                    ex=source_square_search_result.exception,
                )
            )
        # Handle the case that more than one hit is found.
        if len(source_square_search_result.payload) > 1:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                ItineraryAssemblyPrimerException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=ItineraryAssemblyPrimerException.MSG,
                    err_code=ItineraryAssemblyPrimerException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.BUILD_RESULT,
                    ex=StaleTokenSquareLinkException(
                        msg=StaleTokenSquareLinkException.MSG,
                        err_code=StaleTokenSquareLinkException.ERR_CODE,
                    )
                )
            )
        # Handle the case that, the token was not found on the board.
        if source_square_search_result.is_empty:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                ItineraryAssemblyPrimerException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=ItineraryAssemblyPrimerException.MSG,
                    err_code=ItineraryAssemblyPrimerException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.BUILD_RESULT,
                    ex=SquareNotFoundSearchException(
                        msg=SquareNotFoundSearchException.MSG,
                        err_code=SquareNotFoundSearchException.ERR_CODE,
                    )
                )
            )
        source_square = source_square_search_result.payload[0]
        
        # Handle the case, that the token and the destination are already related.
        token_destination_relation_result = toolkit.square_token_relation_analyzer.analyze(
            candidate_primary=blueprint.destination,
            candidate_satellite=blueprint.traveler,
        )
        # Handle the case that, the relation analysis fails.
        if token_destination_relation_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                ItineraryAssemblyPrimerException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=ItineraryAssemblyPrimerException.MSG,
                    err_code=ItineraryAssemblyPrimerException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.BUILD_RESULT,
                    ex=token_destination_relation_result.exception,
                )
            )
        relation = cast(RelationReport, token_destination_relation_result.payload)
        # Handle the case that, there is a stale link between the destination and the token.
        if relation.stale_link_exists:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                ItineraryAssemblyPrimerException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=ItineraryAssemblyPrimerException.MSG,
                    err_code=ItineraryAssemblyPrimerException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.BUILD_RESULT,
                    ex=StaleTokenSquareLinkException(
                        msg=StaleTokenSquareLinkException.MSG,
                        err_code=StaleTokenSquareLinkException.ERR_CODE,
                    ),
                )
            )
        # Handle the case that the token has an orphan link with the destination.
        if relation.registration_does_not_exist:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                ItineraryAssemblyPrimerException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=ItineraryAssemblyPrimerException.MSG,
                    err_code=ItineraryAssemblyPrimerException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.BUILD_RESULT,
                    ex=TokenSquareMissingRegistrationException(
                        msg=TokenSquareMissingRegistrationException.MSG,
                        err_code=TokenSquareMissingRegistrationException.ERR_CODE,
                    ),
                )
            )
        # Handle the case that, the square is already at the destination.
        if relation.fully_exists and source_square == blueprint.destination:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                ItineraryAssemblyPrimerException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=ItineraryAssemblyPrimerException.MSG,
                    err_code=ItineraryAssemblyPrimerException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.BUILD_RESULT,
                    ex=TokenAlreadyAtDestinationException(
                        msg=TokenAlreadyAtDestinationException.MSG,
                        err_code=TokenAlreadyAtDestinationException.ERR_CODE
                    ),
                )
            )
        # Handle 

        # Handle the case that, the token is already on the square.
        
        # --- Security tests are passed. Return the registration result to the caller. ---#
        return ValidationResult.success(ItineraryBlueprint(source=source_square, traveler=blueprint.traveler, destination=blueprint.destination))
    

    


# Register the operation.
WorkerRegistryController.register_worker(worker=CoordAssemblyPrimer)
