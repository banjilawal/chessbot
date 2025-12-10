from typing import Optional

from chess.system import BuildResult, Builder, GameColor, GameColorValidator, IdentityService, LoggingLevelRouter
from chess.team import (
    NoTeamSchemaContextFlagException, TeamSchemaContext, TooManyTeamSchemaContextFlagsException,
    TeamSchemaContextBuildFailedException
)


class TeamSchemaContextBuilder(Builder[TeamSchemaContext]):
    """
     # ROLE: Builder, Data Integrity Guarantor, Data Integrity And Reliability Guarantor

     # RESPONSIBILITIES:
     1.  Produce TeamSchemaContext instances whose integrity is always guaranteed.
     2.  Manage construction of TeamSchemaContext instances that can be used safely by the client.
     3.  Ensure params for TeamSchemaContext creation have met the application's safety contract.
     4.  Return an exception to the client if a build resource does not satisfy integrity requirements.

     # PARENT
         * Builder

     # PROVIDES:
         *   TeamSchemaContextBuilder

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
    ) -> BuildResult[TeamSchemaContext]:
        """
        # Action:
            1.  Confirm that only one in the (name, color) tuple is not null.
            2.  Certify the not-null attribute is safe using the appropriate entity_service or validator.
            3.  If any check fais return a BuildResult containing the exception raised by the failure.
            4.  On success Build an TeamSchemaContext and return in a BuildResult.

        # Parameters:
        Only one these must be provided:
            *   name (Optional[str])
            *   color (Optional[GameColor])

        These Parameters must be provided:
            *   color_validator (GameColorValidator)
            *   identity_service (IdentityService)

        # Returns:
        BuildResult[TeamSchemaContext] containing either:
            - On success: TeamSchemaContext in the payload.
            - On failure: Exception.

        # Raises:
            *   NoTeamSchemaContextFlagException
            *   TooManyTeamSchemaContextFlagsException
            *   TeamSchemaContextBuildFailedException
        """
        method = "TeamSchemaSearchContextBuilder.build"
        try:
            # Get how many optional parameters are not null. One param needs to be not-null
            params = [name, GameColor,]
            param_count = sum(bool(p) for p in params)
            
            # Cannot search for a TeamSchema object if no attribute value is provided for a hit.
            if param_count == 0:
                return BuildResult.failure(
                    NoTeamSchemaContextFlagException(f"{method}: {NoTeamSchemaContextFlagException.DEFAULT_MESSAGE}")
                )
            
            # Only one property-value pair is allowed in a search.
            if param_count > 1:
                return BuildResult.failure(
                    TooManyTeamSchemaContextFlagsException(f"{method}: {TooManyTeamSchemaContextFlagsException}")
                )
            
            # After verifying the correct number of flags has been enabled, follow the appropriate
            # TeamSchemaContext build flow.
            
            # name flag enabled, build flow.
            if name is not None:
                validation = identity_service.validate_name(candidate=name)
                if validation.is_failure:
                    return BuildResult.failure(validation.exception)
                # On validation success return an name_TeamSchema_context in the BuildResult.
                return BuildResult.success(TeamSchemaContext(name=name))
            
            # GameColor flag enabled, build flow.
            if color is not None:
                validation = color_validator.validate(candidate=GameColor)
                if validation.is_failure:
                    return BuildResult.failure(validation.exception)
                # On validation success return an GameColor_TeamSchema_context in the BuildResult.
                return BuildResult.success(TeamSchemaContext(color=color))
        
        # Finally, if none of the execution paths matches the state wrap the unhandled exception in a
        # TeamSchemaContextBuildFailedException then, send the exception chain a BuildResult.failure.
        except Exception as ex:
            return BuildResult.failure(
                TeamSchemaContextBuildFailedException(
                    ex=ex, message=f"{method}: {TeamSchemaContextBuildFailedException.DEFAULT_MESSAGE}"
                )
            )