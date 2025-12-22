# src/chess/formation/map/builder/builder.py

"""
Module: chess.formation.lookup/map.builder.builder
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

from typing import Optional

from chess.formation import (
    OrderContext, OrderContextBuildFailedException, NoOrderContextFlagException, ExcessiveOrderContextFlagsException
)
from chess.system import (
    BuildResult, Builder, FailsafeBranchExitPointException, GameColor, GameColorValidator,
    IdentityService, LoggingLevelRouter
)


class OrderContextBuilder(Builder[OrderContext]):
    """
    # ROLE: Builder, Data Integrity Guarantor, Data Integrity And Reliability Guarantor

    # RESPONSIBILITIES:
    1.  Produce OrderContext instances whose integrity is guaranteed at creation.
    2.  Manage construction of OrderContext instances that can be used safely by the client.
    3.  Ensure params for OrderContext creation have met the application's safety contract.
    4.  Return an exception to the client if a build resource does not satisfy integrity requirements.

    # PARENT:
        *   Builder

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
            designation: Optional[str] = None,
            identity_service: IdentityService = IdentityService(),
            color_validator: GameColorValidator = GameColorValidator(),
    ) -> BuildResult[OrderContext]:
        """
        # Action:
            1.  Confirm that only one in the (square, color, name, designation) tuple is not null.
            2.  Certify the not-null attribute is safe using the appropriate validating service.
            3.  If all checks pass build a OrderContext and send in a BuildResult. Else, return an exception
                in the BuildResult.

        # Parameters:
            Only one these must be provided:
                *   name (Optional[str])
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
            *   ZeroOrderContextFlagsException
            *   OrderContextBuildFailedException
            *   ExcessiveOrderContextFlagsException
        """
        method = "OrderContextBuilder.build"
        try:
            # Count how many optional parameters are not-null. One param needs to be not-null.
            params = [designation, square, color]
            param_count = sum(bool(p) for p in params)
            
            # Test if no params are set. Need an attribute-value pair to look up a piece's battle_order.
            if param_count == 0:
                return BuildResult.failure(
                    NoOrderContextFlagException(f"{method}: {NoOrderContextFlagException.DEFAULT_MESSAGE}")
                )
            # Test if more than one param is set. Only one attribute-value tuple is allowed in a search.
            if param_count > 1:
                return BuildResult.failure(
                    ExcessiveOrderContextFlagsException(f"{method}: {ExcessiveOrderContextFlagsException}")
                )
            # After verifying only one BattleOrder attribute-value-tuple is enabled, validate it.
            
            # Build the name OrderContext if its flag is enabled.
            if name is not None:
                validation = identity_service.validate_name(candidate=name)
                if validation.is_failure:
                    return BuildResult.failure(validation.exception)
                # On validation success return a designation_OrderContext in the BuildResult.
                return BuildResult.success(OrderContext(name=name))
            
            # Build the designation OrderContext if its flag is enabled.
            if designation is not None:
                validation = identity_service.validate_name(candidate=designation)
                if validation.is_failure:
                    return BuildResult.failure(validation.exception)
                # On validation success return a designation_OrderContext in the BuildResult.
                return BuildResult.success(OrderContext(designation=designation))
            
            # Build the square OrderContext if its flag is enabled.
            if square is not None:
                validation = identity_service.validate_name(candidate=square)
                if validation.is_failure:
                    return BuildResult.failure(validation.exception)
                # On validation success return a square_OrderContext in the BuildResult.
                return BuildResult.success(OrderContext(square=square))
            
            # Build the color OrderContext if its flag is enabled.
            if color is not None:
                validation = color_validator.validate(candidate=GameColor)
                if validation.is_failure:
                    return BuildResult.failure(validation.exception)
                # On validation success return a color_OrderContext in the BuildResult.
                return BuildResult.success(OrderContext(color=color))
            
            # As a failsafe, if the none of the none of the cases are handled by the if blocks return failsafeBranchExPointException in the buildResult failure if a map path was missed.
            BuildResult.failure(
                FailsafeBranchExitPointException(f"{method}: {FailsafeBranchExitPointException.DEFAULT_MESSAGE}")
            )
        # Finally, catch any missed exception, wrap an OrderContextBuildFailedException around it then
        # return the exception-chain inside the ValidationResult.
        except Exception as ex:
            return BuildResult.failure(
                OrderContextBuildFailedException(
                    ex=ex, message=f"{method}: {OrderContextBuildFailedException.DEFAULT_MESSAGE}"
                )
            )