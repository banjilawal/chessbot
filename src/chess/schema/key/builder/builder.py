# src/chess/schema/key/builder/builder.py

"""
Module: chess.schema.key.builder.builder
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

from typing import Optional

from chess.system import (
    BuildResult, Builder, GameColor, GameColorValidator, IdentityService, LoggingLevelRouter
)
from chess.schema import (
    SchemaSuperKeyBuildRouteException, ZeroSchemaSuperKeysException, SchemaSuperKey, ExcessiveSchemaSuperKeysException,
    SchemaSuperKeyBuildFailedException
)


class SchemaSuperKeyBuilder(Builder[SchemaSuperKey]):
    """
    # ROLE: Builder, Data Integrity Guarantor, Data Integrity And Reliability Guarantor

    # RESPONSIBILITIES:
    1.  Produce SchemaSuperKey instances whose integrity is always guaranteed at creation.
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
    ) -> BuildResult[SchemaSuperKey]:
        """
        # Action:
            1.  If more than one optional param is not-null return an exception in the BuildResult.
            2.  If the enabled param is not certified by the appropriate validating service return an exception in
                the BuildResult.
            3.  After the active param is validated create the SchemaSuperKey object and return in the BuildResult.

        # Parameters:
            Only one these must be provided:
                *   name (Optional[str])
                *   color (Optional[GameColor])
    
            These Parameters must be provided:
                *   color_validator (GameColorValidator)
                *   identity_service (IdentityService)

        # Returns:
        BuildResult[SchemaSuperKey] containing either:
            - On failure: Exception.
            - On success: SchemaSuperKey in the payload.

        # Raises:
            *   ZeroSchemaSuperKeysException
            *   SchemaSuperKeyBuildFailedException
            *   ExcessiveSchemaSuperKeysException
        """
        method = "SchemaSuperKeyBuilder.build"
        try:
            # Count how many optional parameters are not-null.
            params = [name, color,]
            param_count = sum(bool(p) for p in params)
            
            # Handle the case that all the optional params are null.
            if param_count == 0:
                # Return the exception chain on failure.
                return BuildResult.failure(
                    SchemaSuperKeyBuildFailedException(
                        message=f"{method}: {SchemaSuperKeyBuildFailedException.ERROR_CODE} - ",
                        ex=ZeroSchemaSuperKeysException(f"{method}: {ZeroSchemaSuperKeysException.DEFAULT_MESSAGE}")
                    )
                )
            # Handle the case that more than one optional param is not-null.
            if param_count > 1:
                # Return the exception chain on failure.
                return BuildResult.failure(
                    SchemaSuperKeyBuildFailedException(
                        message=f"{method}: {SchemaSuperKeyBuildFailedException.ERROR_CODE} - ",
                        ex=ExcessiveSchemaSuperKeysException(f"{method}: {ExcessiveSchemaSuperKeysException}")
                    )
                )
            
            # Route to the appropriate validation branch.
            
            # Build the name SchemaSuperKey if its value is set.
            if name is not None:
                validation = identity_service.validate_name(candidate=name)
                if validation.is_failure:
                    # Return the exception chain on failure.
                    return BuildResult.failure(
                        SchemaSuperKeyBuildFailedException(
                            message=f"{method}: {SchemaSuperKeyBuildFailedException.ERROR_CODE} - ",
                            ex=validation.exception
                        )
                    )
                # On validation success return a SchemaKey_name in the BuildResult.
                return BuildResult.success(SchemaSuperKey(name=name))
            
            # Build the color_key SchemaSuperKey if its value is set.
            if color is not None:
                validation = color_validator.validate(candidate=color)
                if validation.is_failure:
                    # Return the exception chain on failure.
                    return BuildResult.failure(
                        SchemaSuperKeyBuildFailedException(
                            message=f"{method}: {SchemaSuperKeyBuildFailedException.ERROR_CODE} - ",
                            ex=validation.exception
                        )
                    )
                # On validation success return a SchemaKey_color in the BuildResult.
                return BuildResult.success(SchemaSuperKey(color=color))
            
            # Handle the default case where no exception is raised and SchemaSuperKey was not covered with an if-block
            return BuildResult.failure(
                SchemaSuperKeyBuildFailedException(
                    message=f"{method}: {SchemaSuperKeyBuildFailedException.ERROR_CODE} - ",
                    ex=SchemaSuperKeyBuildRouteException(
                        f"{method}: {SchemaSuperKeyBuildRouteException.DEFAULT_MESSAGE}"
                    )
                )
            )

        # Finally, wrap a SchemaSuperKeyBuildFailedException any missed exception then return the exception-chain
        # in the BuildResult.
        except Exception as ex:
            return BuildResult.failure(
                SchemaSuperKeyBuildFailedException(
                    ex=ex, message=f"{method}: {SchemaSuperKeyBuildFailedException.ERROR_CODE}"
                )
            )