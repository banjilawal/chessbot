# src/chess/persona/builder/builder.py

"""
Module: chess.persona.builder.builder
Author: Banji Lawal
Created: 2025-09-08
version: 1.0.0
"""

from typing import Optional

from chess.persona import (
    ExcessivePersonaKeysException, PersonaKey, PersonaKeyBuildException,
    PersonaKeyBuildRouteException, ZeroPersonaKeysException
)
from chess.system import NumberValidator, BuildResult, Builder, IdentityService, LoggingLevelRouter


class PersonaKeyBuilder(Builder[PersonaKey]):
    """
    # ROLE: Builder, Data Integrity And Reliability Guarantor

    # RESPONSIBILITIES:
        1.  Produce PersonaKey instances whose integrity is guaranteed at creation.
        2.  Manage construction of PersonaKey instances that can be used safely by the client.
        3.  Ensure params for PersonaKey creation have met the application's safety contract.
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
            quota: Optional[int] = None,
            ransom: Optional[int] = None,
            designation: Optional[str] = None,
            identity_service: IdentityService = IdentityService(),
            number_validator: NumberValidator = NumberValidator(),
    ) -> BuildResult[PersonaKey]:
        """
        # ACTION:
            1.  If only one optional param is not-null return an exception in the BuildResult. Else
            2.  If the enabled param is not certified by the appropriate validating service return an exception in
                the BuildResult.
            3.  After the active param is validated create the PersonaKey object and return in the BuildResult.
        # PARAMETERS:
            *   Only one these must be provided:
                    *   name (Optional[str])
                    *   quota (Optional[int])
                    *   ransom (Optional[int])
                    *   designation (Optional[str])
            *   These Parameters must be provided:
                    *   color_validator (GameColorValidator)
                    *   identity_service (IdentityService)
                    *   number_validator (NumberValidator)

        # RETURNS:
            *   BuildResult[PersonaKey] containing either:
                    - On failure: Exception.
                    - On success: PersonaKey in the payload.
        # RAISES:
            *   ZeroPersonaKeysException
            *   PersonaKeyBuildException
            *   ExcessivePersonaKeysException
            *   PersonaKeyBuildRouteException
        """
        method = "PersonaKeyBuilder.build"
        
        # Count how many optional parameters are not-null. One param needs to be not-null.
        params = [name, designation, quota, ransom]
        param_count = sum(bool(p) for p in params)
        
        # Test if no params are set. Need an attribute-value pair to look up a rank's persona_entry.
        if param_count == 0:
            # Return the exception chain on failure.
            return BuildResult.failure(
                PersonaKeyBuildException(
                    message=f"{method}: {PersonaKeyBuildException.ERROR_CODE}",
                    ex=ZeroPersonaKeysException(f"{method}: {ZeroPersonaKeysException.DEFAULT_MESSAGE}")
                )
            )
        # Test if more than one param is set. Only one attribute-value tuple is allowed in a search.
        if param_count > 1:
            # Return the exception chain on failure.
            return BuildResult.failure(
                PersonaKeyBuildException(
                    message=f"{method}: {PersonaKeyBuildException.ERROR_CODE}",
                    ex=ExcessivePersonaKeysException(f"{method}: {ExcessivePersonaKeysException}")
                )
            )
        # After verifying only one Persona hash key-value is set, validate it.
        
        # Build the name PersonaKey if its flag is enabled.
        if name is not None:
            validation = identity_service.validate_name(candidate=name)
            if validation.is_failure:
                # Return the exception chain on failure.
                return BuildResult.failure(
                    PersonaKeyBuildException(
                        message=f"{method}: {PersonaKeyBuildException.ERROR_CODE}",
                        ex=validation.exception
                    )
                )
            # On validation success return a ransom_PersonaKey in the BuildResult.
            return BuildResult.success(PersonaKey(name=name))
        
        # Build the designation PersonaKey if its flag is enabled.
        if designation is not None:
            validation = identity_service.validate_name(candidate=designation)
            if validation.is_failure:
                # Return the exception chain on failure.
                return BuildResult.failure(
                    PersonaKeyBuildException(
                        message=f"{method}: {PersonaKeyBuildException.ERROR_CODE}",
                        ex=validation.exception
                    )
                )
            # On validation success return a designation_PersonaKey in the BuildResult.
            return BuildResult.success(PersonaKey(designation=designation))
        
        # Build the quota PersonaKey if its flag is enabled.
        if quota is not None:
            # Quotas have to be between king_count=1 and pawn_count=8
            validation = number_validator.validate(floor=1, ceiling=9)
            if validation.is_failure:
                # Return the exception chain on failure.
                return BuildResult.failure(
                    PersonaKeyBuildException(
                        message=f"{method}: {PersonaKeyBuildException.ERROR_CODE}",
                        ex=validation.exception
                    )
                )
            # On validation success return a quota_PersonaKey in the BuildResult.
            return BuildResult.success(PersonaKey(quota=quota))
        
        # Build the ransom PersonaKey if its flag is enabled.
        if ransom is not None:
            # Ransoms have to be between king_ransom=0 and 20
            validation = number_validator.validate(floor=0, ceiling=20)
            if validation.is_failure:
                # Return the exception chain on failure.
                return BuildResult.failure(
                    PersonaKeyBuildException(
                        message=f"{method}: {PersonaKeyBuildException.ERROR_CODE}",
                        ex=validation.exception
                    )
                )
            # On validation success return a ransom_PersonaKey in the BuildResult.
            return BuildResult.success(PersonaKey(ransom=ransom))
        
        # The default path returns failure.
        BuildResult.failure(
            PersonaKeyBuildException(
                message=f"{method}: {PersonaKeyBuildException.ERROR_CODE}",
                ex=PersonaKeyBuildRouteException(
                    f"{method}: {PersonaKeyBuildRouteException.DEFAULT_MESSAGE}"
                )
            )
        )