# src/chess/formation/lookup/context/builder/builder.py

"""
Module: chess.formation.lookup/context.builder.builder
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

from typing import Optional

from chess.formation import (
    OrderContext, OrderContextBuildFailedException, NoOrderContextFlagException, TooManyOrderContextFlagsException
)
from chess.system import BuildResult, Builder, GameColor, GameColorValidator, IdentityService, LoggingLevelRouter


class OrderContextBuilder(Builder[OrderContext]):
    """
     # ROLE: Builder, Data Integrity Guarantor, Data Integrity And Reliability Guarantor

     # RESPONSIBILITIES:
     1.  Produce OrderContext instances whose integrity is always guaranteed.
     2.  Manage construction of OrderContext instances that can be used safely by the client.
     3.  Ensure params for OrderContext creation have met the application's safety contract.
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
            square: Optional[str] = None,
            color: Optional[GameColor] = None,
            designation: Optional[str] = None,
            identity_service: IdentityService = IdentityService(),
            color_validator: GameColorValidator = GameColorValidator(),
    ) -> BuildResult[OrderContext]:
        """
        # Action:
            1.  Confirm that only one in the (designation, color) tuple is not null.
            2.  Certify the not-null attribute is safe using the appropriate entity_service or validator.
            3.  If any check fais return a BuildResult containing the exception raised by the failure.
            4.  On success Build an OrderContext and return in a BuildResult.

        # Parameters:
        Only one these must be provided:
            *   square (Optional[str])
            *   designation (Optional[str])
            *   color (Optional[GameColor])

        These Parameters must be provided:
            *   color_validator (GameColorValidator)
            *   identity_service (IdentityService)

        # Returns:
        BuildResult[OrderContext] containing either:
            - On success: OrderContext in the payload.
            - On failure: Exception.

        # Raises:
            *   NoOrderContextFlagException
            *   TooManyOrderContextFlagsException
            *   OrderContextBuildFailedException
        """
        method = "OrderContextBuilder.build"
        try:
            # Get how many optional parameters are not null. One param needs to be not-null
            params = [designation, square, color]
            param_count = sum(bool(p) for p in params)
            
            # Cannot search for a BattleOrder object if no attribute value is provided for a hit.
            if param_count == 0:
                return BuildResult.failure(
                    NoOrderContextFlagException(f"{method}: {NoOrderContextFlagException.DEFAULT_MESSAGE}")
                )
            # Only one property-value pair is allowed in a search.
            if param_count > 1:
                return BuildResult.failure(
                    TooManyOrderContextFlagsException(f"{method}: {TooManyOrderContextFlagsException}")
                )
            # After the verifying the correct number of flags are set follow the appropriate BattleOrder build flow.
            
            # designation flag enabled, build flow.
            if designation is not None:
                validation = identity_service.validate_name(candidate=designation)
                if validation.is_failure:
                    return BuildResult.failure(validation.exception)
                # On validation success return an name_BattleOrder_context in the BuildResult.
                return BuildResult.success(OrderContext(designation=designation))
            
            # square flag enabled, build flow.
            if square is not None:
                validation = identity_service.validate_name(candidate=square)
                if validation.is_failure:
                    return BuildResult.failure(validation.exception)
                # On validation success return an name_BattleOrder_context in the BuildResult.
                return BuildResult.success(OrderContext(square=square))
            
            # GameColor flag enabled, build flow.
            if color is not None:
                validation = color_validator.validate(candidate=GameColor)
                if validation.is_failure:
                    return BuildResult.failure(validation.exception)
                # On validation success return an GameColor_BattleOrder_context in the BuildResult.
                return BuildResult.success(OrderContext(color=color))
        
        # Finally, if none of the execution paths matches the state wrap the unhandled exception in a
        # OrderContextBuildFailedException then, send the exception chain a BuildResult.failure.
        except Exception as ex:
            return BuildResult.failure(
                OrderContextBuildFailedException(
                    ex=ex, message=f"{method}: {OrderContextBuildFailedException.DEFAULT_MESSAGE}"
                )
            )