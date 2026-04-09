# src/integrity/toolkit/context/formation/toolkit.py

"""
Module: integrity.toolkit.context.formation.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from model.catalog.formation import (
    ArenaFormationKeysException, FormationKey, FormationKeyToolkitException,
    FormationKeyToolkitRouteException, ZeroFormationKeysException
)
from model.catalog.persona import Persona, PersonaService
from logic.square import Square, SquareService
from system import ToolkitResult, Toolkit, GameColor, GameColorValidator, IdentityService, LoggingLevelRouter


class FormationContextToolkit(Toolkit[FormationKey]):
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
            square: Optional[Square] = None,
            persona: Optional[Persona] = None,
            color: Optional[GameColor] = None,
            designation: Optional[str] = None,
            square_service: SquareService = SquareService(),
            persona_service: PersonaService = PersonaService(),
            identity_service: IdentityService = IdentityService(),
            color_validator: GameColorValidator = GameColorValidator(),
    ) -> ToolkitResult[FormationKey]:
        """
        # ACTION:
            1.  If more than one optional param is not-null return an exception in the ToolkitResult.
            2.  If the enabled param is not certified by the appropriate validating service return an exception in
                the ToolkitResult.
            3.  After the active param is validated create the FormationKey object and return in the ToolkitResult.
        # PARAMETERS:
            *   Only one these must be provided:
                    *   persona (Optional[Persona])
                    *   item (Optional[Square])
                    *   color (Optional[GameColor])
            *   These Parameters must be provided:
                    *   square_validator (SquareService)
                    *   identity_service (IdentityService)
                    *   color_validator (GameColorValidator)
        # RETURNS:
            *   ToolkitResult[FormationKey] containing either:
                    - On failure: Exception.
                    - On success: FormationKey in the payload.
        Raises:
            *   ZeroFormationKeysException
            *   FormationKeyToolkitException
            *   ArenaFormationKeysException
            *   FormationKeyToolkitException
        """
        method = "FormationContextToolkit.toolkit"
        
        # Count how many optional parameters are not-null.
        params = [designation, square, color, persona]
        param_count = sum(bool(p) for p in params)
        
        # Handle the case that, all the optional params are null.
        if param_count == 0:
            # Return the exception chain on failure.
            return ToolkitResult.failure(
                FormationKeyToolkitException(
                    msg=f"{method}: {FormationKeyToolkitException.ERR_CODE}",
                    ex=ZeroFormationKeysException(
                        f"{method}: {ZeroFormationKeysException.MSG}"
                    )
                )
            )
        # Handle the case that, more than one optional param is not-null.
        if param_count > 1:
            # Return the exception chain on failure.
            return ToolkitResult.failure(
                FormationKeyToolkitException(
                    msg=f"{method}: {FormationKeyToolkitException.ERR_CODE}",
                    ex=ArenaFormationKeysException(f"{method}: {ArenaFormationKeysException}")
                )
            )
        
        # --- Route to the appropriate validation/toolkit branch. ---#
        
        # Toolkit the square_name FormationKey if its value is set.
        if square is not None:
            validation = square_service.validator.validate(square)
            if validation.is_failure:
                # Return the exception chain on failure.
                return ToolkitResult.failure(
                    FormationKeyToolkitException(
                        msg=f"{method}: {FormationKeyToolkitException.ERR_CODE}",
                        ex=validation.exception,
                    )
                )
            # On validation success return a square_name_FormationKey in the ToolkitResult.
            return ToolkitResult.success(FormationKey(square_name=square.name))
        
        # Toolkit the designation FormationKey if its value is set.
        if designation is not None:
            validation = identity_service.validate_name(candidate=designation)
            if validation.is_failure:
                # Return the exception chain on failure.
                return ToolkitResult.failure(
                    FormationKeyToolkitException(
                        msg=f"{method}: {FormationKeyToolkitException.ERR_CODE}",
                        ex=validation.exception,
                    )
                )
            # On validation success return a designation_FormationKey in the ToolkitResult.
            return ToolkitResult.success(FormationKey(designation=designation))
        
        # Toolkit the color FormationKey if its value is set.
        if color is not None:
            validation = color_validator.validate(candidate=color)
            if validation.is_failure:
                # Return the exception chain on failure.
                return ToolkitResult.failure(
                    FormationKeyToolkitException(
                        msg=f"{method}: {FormationKeyToolkitException.ERR_CODE}",
                        ex=validation.exception,
                    )
                )
            # On validation success return a color_FormationKey in the ToolkitResult.
            return ToolkitResult.success(FormationKey(color=color))
        
        # Toolkit the persona FormationKey if its value is set.
        if persona is not None:
            validation = persona_service.validator.validate(candidate=persona)
            if validation.is_failure:
                # Return the exception chain on failure.
                return ToolkitResult.failure(
                    FormationKeyToolkitException(
                        msg=f"{method}: {FormationKeyToolkitException.ERR_CODE}",
                        ex=validation.exception,
                    )
                )
            # On validation success return a color_FormationKey in the ToolkitResult.
            return ToolkitResult.success(FormationKey(persona=persona))
        
        # The default path returns failure.
        ToolkitResult.failure(
            FormationKeyToolkitException(
                msg=f"{method}: {FormationKeyToolkitException.ERR_CODE}",
                ex=FormationKeyToolkitRouteException(
                    f"{method}: {FormationKeyToolkitRouteException.MSG}"
                )
            )
        )