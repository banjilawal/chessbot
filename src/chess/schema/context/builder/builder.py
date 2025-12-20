# src/chess/schema/context/builder/builder.py

"""
Module: chess.schema.context.builder.builder
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

from typing import Optional

from chess.system import (
    BuildResult, Builder, FailsafeBranchExitPointException, GameColor, GameColorValidator,
    IdentityService, LoggingLevelRouter
)
from chess.schema import (
    ZeroSchemaContextFlagsException, SchemaContext, ExcessiveSchemaContextFlagsException, SchemaContextBuildFailedException
)


class SchemaContextBuilder(Builder[SchemaContext]):
    """
    # ROLE: Builder, Data Integrity Guarantor, Data Integrity And Reliability Guarantor

    # RESPONSIBILITIES:
    1.  Produce SchemaContext instances whose integrity is always guaranteed.
    2.  Manage construction of SchemaContext instances that can be used safely by the client.
    3.  Ensure params for SchemaContext creation have met the application's safety contract.
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
            color: Optional[GameColor] = None,
            identity_service: IdentityService = IdentityService(),
            color_validator: GameColorValidator = GameColorValidator(),
    ) -> BuildResult[SchemaContext]:
        """
        # Action:
            1.  Confirm that only one in the (designation, color) tuple is not null.
            2.  Certify the not-null attribute is safe using the appropriate validating service.
            3.  If all checks pass build a SchemaContext and send in a BuildResult. Else, send an exception
                in the BuildResult.

        # Parameters:
            Only one these must be provided:
                *   designation (Optional[str])
                *   color (Optional[GameColor])
    
            These Parameters must be provided:
                *   color_validator (GameColorValidator)
                *   identity_service (IdentityService)

        # Returns:
        BuildResult[SchemaContext] containing either:
            - On success: SchemaContext in the payload.
            - On failure: Exception.

        # Raises:
            *   ZeroSchemaContextFlagsException
            *   SchemaContextBuildFailedException
            *   ExcessiveSchemaContextFlagsException
        """
        method = "SchemaContextBuilder.build"
        try:
            # Count how many optional parameters are not-null. One param needs to be not-null.
            params = [name, color,]
            param_count = sum(bool(p) for p in params)
            
            # Test if no params are set. Need an attribute-value pair to look up a team's schema.
            if param_count == 0:
                return BuildResult.failure(
                    ZeroSchemaContextFlagsException(f"{method}: {ZeroSchemaContextFlagsException.DEFAULT_MESSAGE}")
                )
            # Test if more than one param is set. Only one attribute-value tuple is allowed in a search.
            if param_count > 1:
                return BuildResult.failure(
                    ExcessiveSchemaContextFlagsException(f"{method}: {ExcessiveSchemaContextFlagsException}")
                )
            # After verifying only one Schema attribute-value-tuple is enabled, validate it.
            
            # Build the name SchemaContext if its flag is enabled.
            if name is not None:
                validation = identity_service.validate_name(candidate=name)
                if validation.is_failure:
                    return BuildResult.failure(validation.exception)
                # On validation success return a name_SchemaContext in the BuildResult.
                return BuildResult.success(SchemaContext(name=name))
            
            # Build the color SchemaContext if its flag is enabled.
            if color is not None:
                validation = color_validator.validate(candidate=color)
                if validation.is_failure:
                    return BuildResult.failure(validation.exception)
                # On validation success return a color_SchemaContext in the BuildResult.
                return BuildResult.success(SchemaContext(color=color))
            
            # As a failsafe send a buildResult failure if a context path was missed.
            BuildResult.failure(
                FailsafeBranchExitPointException(f"{method}: {FailsafeBranchExitPointException.DEFAULT_MESSAGE}")
            )
        # Finally, if there is an unhandled exception Wrap an SchemaContextBuildFailedException around it then
        # return the exception-chain inside the ValidationResult.
        except Exception as ex:
            return BuildResult.failure(
                SchemaContextBuildFailedException(
                    ex=ex, message=f"{method}: {SchemaContextBuildFailedException.DEFAULT_MESSAGE}"
                )
            )