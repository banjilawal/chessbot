# src/operation/square/entry/operation.py

"""
Module: operation.maneuver.operation
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from copy import deepcopy

from logic.square import (
    Square, ManeuverException, SquareOccupiedException, SquareState, ItineraryValidator, SquareVisitorBoardException,
    SquareVisitorDisabledException, WrongOpeningSquareException
)
from setuptools.msvc import msvc14_get_vc_env

from err import ManeuverDestinationOccupiedException
from event import ManeuverEvent
from model import Itinerary
from result import ManeuverResult, MethodResultType
from util import IdFactory, LoggingLevelRouter, UpdateResult
from model.token import Token, DeploymentState, TokenFreedomAnalyzer


class Maneuver:
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
                    itinerary_validator: ItineraryValidator,
            ) -> ManeuverResult:

    Super Class:
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def execute(
            cls,
            itinerary: Itinerary,
            itinerary_validator: ItineraryValidator | None = None,
    ) -> ManeuverResult:
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
            itinerary: Itinerary
            itinerary_validator: ItineraryValidator
       Returns:
            ManeuverResult
        Raises:
        """
        method = f"{cls.__class__.__name__}.execute"
        
        if itinerary_validator is None:
            itinerary_validator = ItineraryValidator()
            
        # Handle the case that, the itinerary is not valid.
        validation_result = itinerary_validator.validate(itinerary)
        if validation_result.is_failure:
            # Send the exception chain on failure.
            return ManeuverResult.failure(
                ManeuverException(
                    cls_mthd=method,
                    op=ManeuverException.OP,
                    msg=ManeuverException.MSG,
                    err_code=ManeuverException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.MANEUVER_RESULT,
                    ex=validation_result.exception,
                )
            )
        # Handle the case that, the destination is not empty.
        if itinerary.destination.is_occupied:
            # Send the exception chain on failure.
            return ManeuverResult.failure(
                ManeuverException(
                    cls_mthd=method,
                    op=ManeuverException.OP,
                    msg=ManeuverException.MSG,
                    err_code=ManeuverException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.MANEUVER_RESULT,
                    ex=ManeuverDestinationOccupiedException(
                        msg=ManeuverDestinationOccupiedException.MSG,
                        err_code=ManeuverDestinationOccupiedException.ERR_CODE,
                    ),
                )
            )
        # --- Security tests are passed. Return the registration result to the caller. ---#
        arrival_result = cls._arrive(traveller=itinerary.token, destination=itinerary.destination,)
        if arrival_result.is_failure:
            # Send the exception chain on failure.
            return ManeuverResult.failure(
                ManeuverException(
                    cls_mthd=method,
                    op=ManeuverException.OP,
                    msg=ManeuverException.MSG,
                    err_code=ManeuverException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.MANEUVER_RESULT,
                    ex=arrival_result.exception,
                )
            )
        departure_result = cls._depart(source=itinerary.source,)
        
        return ManeuverResult.success(
            ManeuverEvent(
                traveller=arrival_result.updated.occupant,
                arrival_point=arrival_result.updated,
                departure_point=departure_result.updated,
            )
        )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _arrive(cls, traveller: Token, destination: Square, ) -> UpdateResult[Square]:
        """
        Puts the token into the square.

        Action:
            1.  Send the square and an exception chain in the UpdateResult if:
                    - Pushing the square's coord onto the token's schema fails.
            2.  Otherwise, after:
                    -   The square makes the token its occupant
                    -   The token updates its position
                    -   Each updates its state.
            3.  Send the success result.
        Args:
            traveller: Token
            destination: Square
        Returns:
            UpdateResult[Square]
        """
        method = f"{cls.__name__}._arrive"
        
        #  Make a deep copy of the square.
        pre_update_square = deepcopy(destination)
        # --- Set the square side of the relationship. ---#
        destination.occupant = traveller
        destination.state = SquareState.OCCUPIED
        
        # --- Push the square's coord onto the schema. ---#
        coord_insertion_result = traveller.positions.push(destination.coord)
        
        # Handle the case that, the push failed
        if coord_insertion_result.is_failure:
            # Rollback the square.
            destination.occupant = None
            destination.state = SquareState.EMPTY
            
            # Send the exception chain on failure.
            return UpdateResult.update_failure(
                original=pre_update_square,
                exception=ManeuverException(
                    cls_mthd=method,
                    op=ManeuverException.OP,
                    msg=ManeuverException.MSG,
                    err_code=ManeuverException.ERR_CODE,
                    mthd_rslt_type=ManeuverException.MTHD_RSLT,
                    ex=coord_insertion_result.exception,
                )
            )
        # --- Forward the work product to the caller. ---#
        return UpdateResult.update_success(original=pre_update_square, updated=destination)
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _depart(cls, source: Square, ) -> UpdateResult[Square]:
        """
        Remove the token from its source square.

        Action:
            1.  Set the square occupant to None then update its state.
            2.  Send the success result.
        Args:
            source: Square
        Returns:
            UpdateResult[Square]
        """
        method = f"{cls.__name__}._depart"
        
        #  Make a deep copy of the square.
        pre_update_square = deepcopy(source)
        # --- Remove the occupant. ---#
        source.occupant = None
        source.state = SquareState.EMPTY
        
        # --- Forward the work product to the caller. ---#
        return UpdateResult.update_success(original=pre_update_square, updated=source)
