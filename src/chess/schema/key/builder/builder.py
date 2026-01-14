# src/chess/schema/key/builder/builder.py

"""
Module: chess.schema.key.builder.builder
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

from typing import Optional

from chess.schema.key.builder.exception import SchemaKeyBuildFailedException, SchemaKeyBuildRouteException
from chess.system import (
    BuildResult, Builder, GameColor, GameColorValidator, IdentityService, LoggingLevelRouter
)
from chess.schema import (
    ZeroSchemaKeysException, SchemaKey, ExcessiveSchemaKeysException,
)


class SchemaKeyBuilder(Builder[SchemaKey]):
    """
    # ROLE: Builder, Data Integrity And Reliability Guarantor

    # RESPONSIBILITIES:
    1.  Produce SchemaKey instances whose integrity is always guaranteed at creation.
    2.  If the build fails indicate the reason in an exception returned to the caller.

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
    ) -> BuildResult[SchemaKey]:
        """
        # ACTION:
            1.  If more than one optional param is not-null return an exception in the BuildResult.
            2.  If the enabled param is not certified by the appropriate validating service return an exception in
                the BuildResult.
            3.  After the active param is validated create the SchemaKey object and return in the BuildResult.
        # PARAMETERS:
            *   Only one these must be provided:
                    *   name (Optional[str])
                    *   color (Optional[GameColor])
            *   These Parameters must be provided:
                    *   color_validator (GameColorValidator)
                    *   identity_service (IdentityService)
        # RETURNS:
            *   BuildResult[SchemaKey] containing either:
                    - On failure: Exception.
                    - On success: SchemaKey in the payload.
        # RAISES:
            *   ZeroSchemaKeysException
            *   SchemaKeyBuildFailedException
            *   ExcessiveSchemaKeysException
        """
        method = "SchemaKeyBuilder.build"
        
        # Count how many optional parameters are not-null.
        params = [name, color,]
        param_count = sum(bool(p) for p in params)
        
        # Handle the case that all the optional params are null.
        if param_count == 0:
            # Return the exception chain on failure.
            return BuildResult.failure(
                SchemaKeyBuildFailedException(
                    message=f"{method}: {SchemaKeyBuildFailedException.ERROR_CODE}",
                    ex=ZeroSchemaKeysException(f"{method}: {ZeroSchemaKeysException.DEFAULT_MESSAGE}")
                )
            )
        # Handle the case that more than one optional param is not-null.
        if param_count > 1:
            # Return the exception chain on failure.
            return BuildResult.failure(
                SchemaKeyBuildFailedException(
                    message=f"{method}: {SchemaKeyBuildFailedException.ERROR_CODE}",
                    ex=ExcessiveSchemaKeysException(f"{method}: {ExcessiveSchemaKeysException}")
                )
            )
        # Route to the appropriate validation/build branch.
        
        # Build the name SchemaKey if its value is set.
        if name is not None:
            validation = identity_service.validate_name(candidate=name)
            if validation.is_failure:
                # Return the exception chain on failure.
                return BuildResult.failure(
                    SchemaKeyBuildFailedException(
                        message=f"{method}: {SchemaKeyBuildFailedException.ERROR_CODE}",
                        ex=validation.exception
                    )
                )
            # On validation success return a name_SchemaKey in the BuildResult.
            return BuildResult.success(SchemaKey(name=name))
        
        # Build the color_key SchemaKey if its value is set.
        if color is not None:
            validation = color_validator.validate(candidate=color)
            if validation.is_failure:
                # Return the exception chain on failure.
                return BuildResult.failure(
                    SchemaKeyBuildFailedException(
                        message=f"{method}: {SchemaKeyBuildFailedException.ERROR_CODE}",
                        ex=validation.exception
                    )
                )
            # On validation success return a color_SchemaKey in the BuildResult.
            return BuildResult.success(SchemaKey(color=color))
        
        # The default path returns failure
        return BuildResult.failure(
            SchemaKeyBuildFailedException(
                message=f"{method}: {SchemaKeyBuildFailedException.ERROR_CODE}",
                ex=SchemaKeyBuildRouteException(f"{method}: {SchemaKeyBuildRouteException.DEFAULT_MESSAGE}")
            )
        )