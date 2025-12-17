# src/chess/team/schema/context/builder/builder.py

"""
Module: chess.team.schema.builder.builder
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

from typing import Optional

from chess.system import BuildResult, Builder, GameColor, GameColorValidator, IdentityService, LoggingLevelRouter
from chess.team import (
    NoSchemaContextFlagException, SchemaContext, TooManySchemaContextFlagsException, SchemaContextBuildFailedException
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
            color: Optional[GameColor] = None,
            identity_service: IdentityService = IdentityService(),
            color_validator: GameColorValidator = GameColorValidator(),
    ) -> BuildResult[SchemaContext]:
        """
        # Action:
            1.  Confirm that only one in the (designation, color) tuple is not null.
            2.  Certify the not-null attribute is safe using the appropriate entity_service or validator.
            3.  If any check fais return a BuildResult containing the exception raised by the failure.
            4.  On success Build an SchemaContext and return in a BuildResult.

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
            *   NoSchemaContextFlagException
            *   TooManySchemaContextFlagsException
            *   SchemaContextBuildFailedException
        """
        method = "TeamSchemaSearchContextBuilder.build"
        try:
            # Get how many optional parameters are not null. One param needs to be not-null
            params = [name, GameColor,]
            param_count = sum(bool(p) for p in params)
            
            # Cannot search for a TeamSchema object if no attribute value is provided for a hit.
            if param_count == 0:
                return BuildResult.failure(
                    NoSchemaContextFlagException(f"{method}: {NoSchemaContextFlagException.DEFAULT_MESSAGE}")
                )
            # Only one property-value pair is allowed in a search.
            if param_count > 1:
                return BuildResult.failure(
                    TooManySchemaContextFlagsException(f"{method}: {TooManySchemaContextFlagsException}")
                )
            # After the verifying the correct number of flags are set follow the appropriate TeamSchema build flow.
            
            # designation flag enabled, build flow.
            if name is not None:
                validation = identity_service.validate_name(candidate=name)
                if validation.is_failure:
                    return BuildResult.failure(validation.exception)
                # On validation success return an name_TeamSchema_context in the BuildResult.
                return BuildResult.success(SchemaContext(name=name))
            
            # GameColor flag enabled, build flow.
            if color is not None:
                validation = color_validator.validate(candidate=GameColor)
                if validation.is_failure:
                    return BuildResult.failure(validation.exception)
                # On validation success return an GameColor_TeamSchema_context in the BuildResult.
                return BuildResult.success(SchemaContext(color=color))
            
        # Finally, if none of the execution paths matches the state wrap the unhandled exception in a
        # SchemaContextBuildFailedException then, send the exception chain a BuildResult.failure.
        except Exception as ex:
            return BuildResult.failure(
                SchemaContextBuildFailedException(
                    ex=ex, message=f"{method}: {SchemaContextBuildFailedException.DEFAULT_MESSAGE}"
                )
            )