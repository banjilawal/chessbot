## src/integrity/build/context/schema/builder.py

"""
Module: integrity.build.context.schema.builder
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations


class SchemaContextBuilder(Builder[SchemaKey]):
    """
    Role
        -   Transaction Worker
        -   Integrity Maintenance
        -   Consistency Assurance
        -   Build Process Owner

   Responsibilities:
        1.  Ensure a new Token instance is born safe and reliable.

     Attributes:

    Provides:
        -   def execute(
                    owner: Team,
                    id: int = IdFactory,
                    formation: Formation,
                    rank_service: RankService,
                    identity_service: IdentityService,
                    formation_service: FormationService,
                    team_validator: TeamValidator,
            ) -> BuildResult[Token]

     Super Class:
         Builder
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
                    *   schema (Optional[str])
                    *   color (Optional[GameColor])
            *   These Parameters must be provided:
                    *   color_validator (GameColorValidator)
                    *   identity_service (IdentityService)
        # RETURNS:
            *   BuildResult[SchemaKey] containing either:
                    - On failure: Exception.
                    - On success: SchemaKey in the payload.
        Raises:
            *   ZeroSchemaKeysException
            *   SchemaKeyBuildException
            *   ArenaSchemaKeysException
        """
        method = "SchemaContextBuilder.build"
        
        # Count how many optional parameters are not-null.
        params = [name, color,]
        param_count = sum(bool(p) for p in params)
        
        # Handle the case that, all the optional params are null.
        if param_count == 0:
            # Return the exception chain on failure.
            return BuildResult.failure(
                SchemaKeyBuildException(
                    msg=f"{method}: {SchemaKeyBuildException.ERR_CODE}",
                    ex=ZeroSchemaKeysException(f"{method}: {ZeroSchemaKeysException.MSG}")
                )
            )
        # Handle the case that, more than one optional param is not-null.
        if param_count > 1:
            # Return the exception chain on failure.
            return BuildResult.failure(
                SchemaKeyBuildException(
                    msg=f"{method}: {SchemaKeyBuildException.ERR_CODE}",
                    ex=ArenaSchemaKeysException(f"{method}: {ArenaSchemaKeysException}")
                )
            )
        # Route to the appropriate validation/build branch.
        
        # Build the schema SchemaKey if its value is set.
        if name is not None:
            validation = identity_service.validate_name(candidate=name)
            if validation.is_failure:
                # Return the exception chain on failure.
                return BuildResult.failure(
                    SchemaKeyBuildException(
                        msg=f"{method}: {SchemaKeyBuildException.ERR_CODE}",
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
                    SchemaKeyBuildException(
                        msg=f"{method}: {SchemaKeyBuildException.ERR_CODE}",
                        ex=validation.exception
                    )
                )
            # On validation success return a color_SchemaKey in the BuildResult.
            return BuildResult.success(SchemaKey(color=color))
        
        # The default path returns failure
        return BuildResult.failure(
            SchemaKeyBuildException(
                msg=f"{method}: {SchemaKeyBuildException.ERR_CODE}",
                ex=SchemaKeyBuildRouteException(f"{method}: {SchemaKeyBuildRouteException.MSG}")
            )
        )