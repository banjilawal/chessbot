# src/bootstrap/assembly/coord/operation.py

"""
Module: operation.priming.assembly.coord.operation
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from typing import cast

from blueprint import ItineraryBlueprint
from controller import WorkerRegistryController
from err import (
    DisabledTokenManeuverException, InconsistentStateException, ItineraryAssemblyPrimerException,
    SquareNotFoundSearchException, StaleTokenLinkException, TokenAlreadyAtDestinationException
)
from model import Itinerary, SquareContext
from operation import AssemblyPrimer
from report import RelationReport, TokenReadinessReport
from result import MethodResultType, ValidationResult
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
        -   def execute(
                    blueprint: ItineraryBlueprint,
                    toolkit: ItineraryToolkit,
            ) -> ValidationResult[ItineraryBlueprint]:

    Super Class:
        AssemblyPrimer
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
            1.  Send an exception chain in the validation result if:
                    -   The blueprint.token is not free.
                    -   The token exists in more than one square.
                    -   The token is not found on the board.
                    -   There is a partial relationship between the token and its destination.
                    -   The token is already at its destination.
            2.  Otherwise, build a new ItineraryBlueprint containing the source square.
            3.  Send the success result.
        Args:
            blueprint: ItineraryBlueprint,
            toolkit: ItineraryToolkit
       Returns:
            ValidationResult[ItineraryBlueprint]
        Raises:
            DisabledTokenTravelerException
            ItineraryAssemblyPrimerException
            StaleTokenLinkException
            SquareNotFoundSearchException
            InconsistentStateException
            TokenAlreadyAtDestinationException
        """
        method = f"{cls.__class__.__name__}.execute"
        
        # --- Supply any missing dependencies. ---#
        if toolkit is None:
            toolkit = ItineraryToolkit()
        
        token_freedom_validation_result = toolkit.token_freedom_analyzer.analyze(blueprint.token)
        # Handle the case that, the freedom_analysis is not completed.
        if token_freedom_validation_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                ItineraryAssemblyPrimerException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=ItineraryAssemblyPrimerException.MSG,
                    err_code=ItineraryAssemblyPrimerException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.VALIDATION_RESULT,
                    ex=token_freedom_validation_result.exception,
                )
            )
        report = cast(TokenReadinessReport, token_freedom_validation_result.payload)
        # Handle the case that, the token is not free.
        if report.token_is_not_ready:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                ItineraryAssemblyPrimerException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=ItineraryAssemblyPrimerException.MSG,
                    err_code=ItineraryAssemblyPrimerException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.VALIDATION_RESULT,
                    ex=DisabledTokenManeuverException(
                        msg=DisabledTokenManeuverException.MSG,
                        err_code=DisabledTokenManeuverException.ERR_CODE,
                    ),
                )
            )
        source_square_search_result = blueprint.token.team.board.squares.search(
            context=SquareContext(occupant=blueprint.token)
        )
        # Handle the case that, the search is not completed.
        if source_square_search_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                ItineraryAssemblyPrimerException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=ItineraryAssemblyPrimerException.MSG,
                    err_code=ItineraryAssemblyPrimerException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.VALIDATION_RESULT,
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
                    mthd_rslt_type=MethodResultType.VALIDATION_RESULT,
                    ex=StaleTokenLinkException(
                        msg=f"The token is linked with more than one square. "
                            f"There are either inconsistencies or stale links.",
                        err_code=StaleTokenLinkException.ERR_CODE,
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
                    mthd_rslt_type=MethodResultType.VALIDATION_RESULT,
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
            candidate_satellite=blueprint.token,
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
                    mthd_rslt_type=MethodResultType.VALIDATION_RESULT,
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
                    mthd_rslt_type=MethodResultType.VALIDATION_RESULT,
                    ex=StaleTokenLinkException(
                        msg=f"Square has stale link to Token.",
                        err_code=StaleTokenLinkException.ERR_CODE,
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
                    mthd_rslt_type=MethodResultType.VALIDATION_RESULT,
                    ex=InconsistentStateException(
                        msg=f"The Token has an inconsistent occupation states between its "
                            f"source and its destination.",
                        err_code=InconsistentStateException.ERR_CODE,
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
                    mthd_rslt_type=MethodResultType.VALIDATION_RESULT,
                    ex=TokenAlreadyAtDestinationException(
                        msg=TokenAlreadyAtDestinationException.MSG,
                        err_code=TokenAlreadyAtDestinationException.ERR_CODE
                    ),
                )
            )
        
        # --- Send the work product. ---#
        return ValidationResult.success(
            ItineraryBlueprint(
                source=source_square,
                token=blueprint.token,
                destination=blueprint.destination
            )
        )
    
# Register the operation.
WorkerRegistryController.register_worker(worker=ItineraryAssemblyPrimer)
