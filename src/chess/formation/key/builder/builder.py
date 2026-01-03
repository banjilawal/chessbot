# src/chess/formation/key/builder/builder.py

"""
Module: chess.formation.key.builder.builder
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

from typing import Optional

from chess.formation import (
    ExcessiveFormationSuperKeysException, FormationSuperKey, FormationSuperKeyBuildFailedException,
    FormationSuperKeyBuildRouteException, ZeroFormationSuperKeysException
)
from chess.persona import Persona, PersonaService
from chess.square import Square, SquareService
from chess.system import BuildResult, Builder, GameColor, GameColorValidator, IdentityService, LoggingLevelRouter


class FormationSuperKeyBuilder(Builder[FormationSuperKey]):
    """
    # ROLE: Builder, Data Integrity And Reliability Guarantor

    # RESPONSIBILITIES:
    1.  Produce FormationSuperKey instances whose integrity is guaranteed at creation.
    2.  Manage construction of FormationSuperKey instances that can be used safely by the client.
    3.  Ensure params for FormationSuperKey creation have met the application's safety contract.
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
            square: Optional[Square] = None,
            persona: Optional[Persona] = None,
            color: Optional[GameColor] = None,
            designation: Optional[str] = None,
            square_service: SquareService = SquareService(),
            persona_service: PersonaService = PersonaService(),
            identity_service: IdentityService = IdentityService(),
            color_validator: GameColorValidator = GameColorValidator(),
    ) -> BuildResult[FormationSuperKey]:
        """
        # ACTION:
            1.  If more than one optional param is not-null return an exception in the BuildResult.
            2.  If the enabled param is not certified by the appropriate validating service return an exception in
                the BuildResult.
            3.  After the active param is validated create the FormationSuperKey object and return in the BuildResult.
        # PARAMETERS:
            *   Only one these must be provided:
                    *   persona (Optional[Persona])
                    *   square (Optional[Square])
                    *   color (Optional[GameColor])
            *   These Parameters must be provided:
                    *   square_service (SquareService)
                    *   identity_service (IdentityService)
                    *   color_validator (GameColorValidator)
        # RETURNS:
            *   BuildResult[FormationSuperKey] containing either:
                    - On failure: Exception.
                    - On success: FormationSuperKey in the payload.
        # RAISES:
            *   ZeroFormationSuperKeysException
            *   FormationSuperKeyBuildFailedException
            *   ExcessiveFormationSuperKeysException
            *   FormationSuperKeyBuildFailedException
        """
        method = "FormationSuperKeyBuilder.build"
        
        # Count how many optional parameters are not-null.
        params = [designation, square, color, persona]
        param_count = sum(bool(p) for p in params)
        
        # Handle the case that all the optional params are null.
        if param_count == 0:
            # Return the exception chain on failure.
            return BuildResult.failure(
                FormationSuperKeyBuildFailedException(
                    message=f"{method}: {FormationSuperKeyBuildFailedException.ERROR_CODE}",
                    ex=ZeroFormationSuperKeysException(
                        f"{method}: {ZeroFormationSuperKeysException.DEFAULT_MESSAGE}"
                    )
                )
            )
        # Handle the case that more than one optional param is not-null.
        if param_count > 1:
            # Return the exception chain on failure.
            return BuildResult.failure(
                FormationSuperKeyBuildFailedException(
                    message=f"{method}: {FormationSuperKeyBuildFailedException.ERROR_CODE}",
                    ex=ExcessiveFormationSuperKeysException(f"{method}: {ExcessiveFormationSuperKeysException}")
                )
            )
        
        # --- Route to the appropriate validation/build branch. ---#
        
        # Build the square_name FormationSuperKey if its value is set.
        if square is not None:
            validation = square_service.validator.validate(square)
            if validation.is_failure:
                # Return the exception chain on failure.
                return BuildResult.failure(
                    FormationSuperKeyBuildFailedException(
                        message=f"{method}: {FormationSuperKeyBuildFailedException.ERROR_CODE}",
                        ex=validation.exception,
                    )
                )
            # On validation success return a square_name_FormationSuperKey in the BuildResult.
            return BuildResult.success(FormationSuperKey(square_name=square.name))
        
        # Build the designation FormationSuperKey if its value is set.
        if designation is not None:
            validation = identity_service.validate_name(candidate=designation)
            if validation.is_failure:
                # Return the exception chain on failure.
                return BuildResult.failure(
                    FormationSuperKeyBuildFailedException(
                        message=f"{method}: {FormationSuperKeyBuildFailedException.ERROR_CODE}",
                        ex=validation.exception,
                    )
                )
            # On validation success return a designation_FormationSuperKey in the BuildResult.
            return BuildResult.success(FormationSuperKey(designation=designation))
        
        # Build the color FormationSuperKey if its value is set.
        if color is not None:
            validation = color_validator.validate(candidate=color)
            if validation.is_failure:
                # Return the exception chain on failure.
                return BuildResult.failure(
                    FormationSuperKeyBuildFailedException(
                        message=f"{method}: {FormationSuperKeyBuildFailedException.ERROR_CODE}",
                        ex=validation.exception,
                    )
                )
            # On validation success return a color_FormationSuperKey in the BuildResult.
            return BuildResult.success(FormationSuperKey(color=color))
        
        # Build the persona FormationSuperKey if its value is set.
        if persona is not None:
            validation = persona_service.validator.validate(candidate=persona)
            if validation.is_failure:
                # Return the exception chain on failure.
                return BuildResult.failure(
                    FormationSuperKeyBuildFailedException(
                        message=f"{method}: {FormationSuperKeyBuildFailedException.ERROR_CODE}",
                        ex=validation.exception,
                    )
                )
            # On validation success return a color_FormationSuperKey in the BuildResult.
            return BuildResult.success(FormationSuperKey(persona=persona))
        
        # The default path returns failure.
        BuildResult.failure(
            FormationSuperKeyBuildFailedException(
                message=f"{method}: {FormationSuperKeyBuildFailedException.ERROR_CODE}",
                ex=FormationSuperKeyBuildRouteException(
                    f"{method}: {FormationSuperKeyBuildRouteException.DEFAULT_MESSAGE}"
                )
            )
        )