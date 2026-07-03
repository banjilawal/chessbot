## src/toolkit/context/schema/toolkit.py

"""
Module: toolkit.context.schema.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations


class SchemaContextToolkit(Toolkit[SchemaKey]):
    """
    Role
        -   Transaction Worker
        -   Integrity Maintenance
        -   Consistency Assurance
        -   Toolkit Process Owner

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
            ) -> ToolkitResult[Token]

     Super Class:
         Toolkit
     """
    @classmethod
    @LoggingLevelRouter.monitor
    def __init__(
            self,
            name: Optional[str] = None,
            color: Optional[GameColor] = None,
            identity_service: IdentityService = IdentityService(),
            color_validator: GameColorValidator = GameColorValidator(),
    ) -> ToolkitResult[SchemaKey]:
        """
        # ACTION:
            1.  If more than one optional param is not-null return an exception in the ToolkitResult.
            2.  If the enabled param is not certified by the appropriate validating service return an exception in
                the ToolkitResult.
            3.  After the active param is validated create the SchemaKey object and return in the ToolkitResult.
        # PARAMETERS:
            *   Only one these must be provided:
                    *   schema (Optional[str])
                    *   color (Optional[GameColor])
            *   These Parameters must be provided:
                    *   color_validator (GameColorValidator)
                    *   identity_service (IdentityService)
        # RETURNS:
            *   ToolkitResult[SchemaKey] containing either:
                    - On failure: Exception.
                    - On success: SchemaKey in the payload.
        Raises:
            *   ZeroSchemaKeysException
            *   SchemaKeyToolkitException
            *   ArenaSchemaKeysException
        """
        method = "SchemaContextToolkit.toolkit"
        
        # Count how many optional parameters are not-null.
        params = [name, color,]
        param_count = sum(bool(p) for p in params)
        
        # Handle the case that, all the optional params are null.
        if param_count == 0:
            # Send the exception chain on failure.
            return ToolkitResult.failure(
                SchemaKeyToolkitException(
                    msg=f"{method}: {SchemaKeyToolkitException.ERR_CODE}",
                    ex=ZeroSchemaKeysException(f"{method}: {ZeroSchemaKeysException.MSG}")
                )
            )
        # Handle the case that, more than one optional param is not-null.
        if param_count > 1:
            # Send the exception chain on failure.
            return ToolkitResult.failure(
                SchemaKeyToolkitException(
                    msg=f"{method}: {SchemaKeyToolkitException.ERR_CODE}",
                    ex=ArenaSchemaKeysException(f"{method}: {ArenaSchemaKeysException}")
                )
            )
        # Route to the appropriate validation/toolkit branch.
        
        # Toolkit the schema SchemaKey if its value is set.
        if name is not None:
            validation = identity_service.validate_name(candidate=name)
            if validation.is_failure:
                # Send the exception chain on failure.
                return ToolkitResult.failure(
                    SchemaKeyToolkitException(
                        msg=f"{method}: {SchemaKeyToolkitException.ERR_CODE}",
                        ex=validation.exception
                    )
                )
            # On validation success return a name_SchemaKey in the ToolkitResult.
            return ToolkitResult.success(SchemaKey(name=name))
        
        # Toolkit the color_key SchemaKey if its value is set.
        if color is not None:
            validation = color_validator.build(candidate=color)
            if validation.is_failure:
                # Send the exception chain on failure.
                return ToolkitResult.failure(
                    SchemaKeyToolkitException(
                        msg=f"{method}: {SchemaKeyToolkitException.ERR_CODE}",
                        ex=validation.exception
                    )
                )
            # On validation success return a color_SchemaKey in the ToolkitResult.
            return ToolkitResult.success(SchemaKey(color=color))
        
        # The default path returns failure
        return ToolkitResult.failure(
            SchemaKeyToolkitException(
                msg=f"{method}: {SchemaKeyToolkitException.ERR_CODE}",
                ex=SchemaKeyToolkitRouteException(f"{method}: {SchemaKeyToolkitRouteException.MSG}")
            )
        )