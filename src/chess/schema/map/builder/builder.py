# src/chess/schema/map/builder/builder.py

"""
Module: chess.schema.map.builder.builder
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
    ZeroSchemaMapKeysException, SchemaMap, ExcessiveSchemaMapKeysException, SchemaMapBuildFailedException
)


class SchemaMapBuilder(Builder[SchemaMap]):
    """
    # ROLE: Builder, Data Integrity Guarantor, Data Integrity And Reliability Guarantor

    # RESPONSIBILITIES:
    1.  Produce SchemaMap instances whose integrity is always guaranteed.
    2.  Manage construction of SchemaMap instances that can be used safely by the client.
    3.  Ensure params for SchemaMap creation have met the application's safety contract.
    4.  Return an exception to the client if a build resource does not satisfy integrity requirements.

    # PARENT:
        *   Builder

    # PROVIDES:
    None

    # LOCAL KEY-VALUES:
    None

    # INHERITED KEY-VALUES:
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
    ) -> BuildResult[SchemaMap]:
        """
        # Action:
            1.  Confirm that only one in the (designation, color) hash is not null.
            2.  Certify the not-null key-value is safe using the appropriate validating service.
            3.  If all checks pass build a SchemaMap and send in a BuildResult. Else, send an exception
                in the BuildResult.

        # Parameters:
            Only one these must be provided:
                *   designation (Optional[str])
                *   color (Optional[GameColor])
    
            These Parameters must be provided:
                *   color_validator (GameColorValidator)
                *   identity_service (IdentityService)

        # Returns:
        BuildResult[SchemaMap] containing either:
            - On success: SchemaMap in the payload.
            - On failure: Exception.

        # Raises:
            *   ZeroSchemaMapKeysException
            *   SchemaMapBuildFailedException
            *   ExcessiveSchemaMapKeysException
        """
        method = "SchemaMapBuilder.build"
        try:
            # Count how many optional parameters are not-null. One param needs to be not-null.
            params = [name, color,]
            param_count = sum(bool(p) for p in params)
            
            # Test if no params are set. Need a key-value to look up a team's schema.
            if param_count == 0:
                return BuildResult.failure(
                    ZeroSchemaMapKeysException(f"{method}: {ZeroSchemaMapKeysException.DEFAULT_MESSAGE}")
                )
            # Test if more than one param is set. Only one hash key-value is allowed in a lookup.
            if param_count > 1:
                return BuildResult.failure(
                    ExcessiveSchemaMapKeysException(f"{method}: {ExcessiveSchemaMapKeysException}")
                )
            # After verifying only one Schema hash key-value is set, validate it.
            
            # Build the name_key SchemaMap if its value is set.
            if name is not None:
                validation = identity_service.validate_name(candidate=name)
                if validation.is_failure:
                    return BuildResult.failure(validation.exception)
                # On validation success return a SchemaMap_name in the BuildResult.
                return BuildResult.success(SchemaMap(name=name))
            
            # Build the color_key SchemaMap if its value is set.
            if color is not None:
                validation = color_validator.validate(candidate=color)
                if validation.is_failure:
                    return BuildResult.failure(validation.exception)
                # On validation success return a SchemaMap_color in the BuildResult.
                return BuildResult.success(SchemaMap(color=color))
            
            # As a failsafe send a buildResult failure if a mapping path was missed.
            BuildResult.failure(
                FailsafeBranchExitPointException(f"{method}: {FailsafeBranchExitPointException.DEFAULT_MESSAGE}")
            )
        # Finally, if there is an unhandled exception Wrap an SchemaMapBuildFailedException around it then
        # return the exception-chain inside the ValidationResult.
        except Exception as ex:
            return BuildResult.failure(
                SchemaMapBuildFailedException(
                    ex=ex, message=f"{method}: {SchemaMapBuildFailedException.DEFAULT_MESSAGE}"
                )
            )