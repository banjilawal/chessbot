# src/chess/formation/context/builder/__init__.py

"""
Module: chess.formation.context.builder.__init__
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

from typing import Optional

from chess.formation import (
    BattleOrderContext, BattleOrderContextBuildFailedException, NoBattleOrderContextFlagException,
    TooManyBattleOrderContextFlagsException
)
from chess.system import BuildResult, Builder, GameColor, GameColorValidator, IdentityService, LoggingLevelRouter


class BattleOrderContextBuilder(Builder[BattleOrderContext]):
    """
     # ROLE: Builder, Data Integrity Guarantor, Data Integrity And Reliability Guarantor

     # RESPONSIBILITIES:
     1.  Produce BattleOrderContext instances whose integrity is always guaranteed.
     2.  Manage construction of BattleOrderContext instances that can be used safely by the client.
     3.  Ensure params for BattleOrderContext creation have met the application's safety contract.
     4.  Return an exception to the client if a build resource does not satisfy integrity requirements.

     # PARENT:
         * Builder

     # PROVIDES:
     None

     # LOCAL ATTRIBUTES:
     None

     # INHERITED ATTRIBUTES:
     None
     """
    @classmethod
    @LoggingLevelRouter.monitor
    def build(
            cls,
            name: Optional[str] = None,
            square: Optional[str] = None,
            color: Optional[GameColor] = None,
            identity_service: IdentityService = IdentityService(),
            color_validator: GameColorValidator = GameColorValidator(),
    ) -> BuildResult[BattleOrderContext]:
        """
        # Action:
            1.  Confirm that only one in the (name, color) tuple is not null.
            2.  Certify the not-null attribute is safe using the appropriate entity_service or validator.
            3.  If any check fais return a BuildResult containing the exception raised by the failure.
            4.  On success Build an BattleOrderContext and return in a BuildResult.

        # Parameters:
        Only one these must be provided:
            *   name (Optional[str])
            *   square (Optional[str])
            *   color (Optional[GameColor])

        These Parameters must be provided:
            *   color_validator (GameColorValidator)
            *   identity_service (IdentityService)

        # Returns:
        BuildResult[BattleOrderContext] containing either:
            - On success: BattleOrderContext in the payload.
            - On failure: Exception.

        # Raises:
            *   NoBattleOrderContextFlagException
            *   TooManyBattleOrderContextFlagsException
            *   BattleOrderContextBuildFailedException
        """
        method = "BattleOrderSearchContextBuilder.build"
        try:
            # Get how many optional parameters are not null. One param needs to be not-null
            params = [name, square, color]
            param_count = sum(bool(p) for p in params)
            
            # Cannot search for a BattleOrder object if no attribute value is provided for a hit.
            if param_count == 0:
                return BuildResult.failure(
                    NoBattleOrderContextFlagException(f"{method}: {NoBattleOrderContextFlagException.DEFAULT_MESSAGE}")
                )
            # Only one property-value pair is allowed in a search.
            if param_count > 1:
                return BuildResult.failure(
                    TooManyBattleOrderContextFlagsException(f"{method}: {TooManyBattleOrderContextFlagsException}")
                )
            # After the verifying the correct number of flags are set follow the appropriate BattleOrder build flow.
            
            # name flag enabled, build flow.
            if name is not None:
                validation = identity_service.validate_name(candidate=name)
                if validation.is_failure:
                    return BuildResult.failure(validation.exception)
                # On validation success return an name_BattleOrder_context in the BuildResult.
                return BuildResult.success(BattleOrderContext(name=name))
            
            # square flag enabled, build flow.
            if square is not None:
                validation = identity_service.validate_name(candidate=square)
                if validation.is_failure:
                    return BuildResult.failure(validation.exception)
                # On validation success return an name_BattleOrder_context in the BuildResult.
                return BuildResult.success(BattleOrderContext(square_name=square))
            
            # GameColor flag enabled, build flow.
            if color is not None:
                validation = color_validator.validate(candidate=GameColor)
                if validation.is_failure:
                    return BuildResult.failure(validation.exception)
                # On validation success return an GameColor_BattleOrder_context in the BuildResult.
                return BuildResult.success(BattleOrderContext(color=color))
            
        # Finally, if none of the execution paths matches the state wrap the unhandled exception in a
        # BattleOrderContextBuildFailedException then, send the exception chain a BuildResult.failure.
        except Exception as ex:
            return BuildResult.failure(
                BattleOrderContextBuildFailedException(
                    ex=ex, message=f"{method}: {BattleOrderContextBuildFailedException.DEFAULT_MESSAGE}"
                )
            )