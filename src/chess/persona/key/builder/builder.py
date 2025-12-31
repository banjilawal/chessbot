# src/chess/persona/builder/builder.py

"""
Module: chess.persona.builder.builder
Author: Banji Lawal
Created: 2025-09-08
version: 1.0.0
"""

from typing import Optional

from chess.persona import (
    ExcessivePersonaSuperKeysException, PersonaSuperKey, PersonaSuperKeyBuildFailedException,
    PersonaSuperKeyBuildRouteException, ZeroPersonaSuperKeysException
)
from chess.system import BoundNumberValidator, BuildResult, Builder, IdentityService, LoggingLevelRouter


class PersonaSuperKeyBuilder(Builder[PersonaSuperKey]):
    """
    # ROLE: Builder, Data Integrity And Reliability Guarantor

    # RESPONSIBILITIES:
        1.  Produce PersonaSuperKey instances whose integrity is guaranteed at creation.
        2.  Manage construction of PersonaSuperKey instances that can be used safely by the client.
        3.  Ensure params for PersonaSuperKey creation have met the application's safety contract.
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
            number_validator: BoundNumberValidator = BoundNumberValidator(),
    ) -> BuildResult[PersonaSuperKey]:
        """
        # ACTION:
            1.  If more than one optional param is not-null return an exception in the BuildResult.
            2.  If the enabled param is not certified by the appropriate validating service return an exception in
                the BuildResult.
            3.  After the active param is validated create the PersonaSuperKey object and return in the BuildResult.
        # PARAMETERS:
            *   Only one these must be provided:
                    *   name (Optional[str])
                    *   quota (Optional[int])
                    *   ransom (Optional[int])
                    *   designation (Optional[str])
            *   These Parameters must be provided:
                    *   color_validator (GameColorValidator)
                    *   identity_service (IdentityService)
                    *   number_validator (BoundNUmberValidator)

        # RETURNS:
            *   BuildResult[PersonaSuperKey] containing either:
                    - On failure: Exception.
                    - On success: PersonaSuperKey in the payload.
        # RAISES:
            *   ZeroPersonaSuperKeysException
            *   PersonaSuperKeyBuildFailedException
            *   ExcessivePersonaSuperKeysException
            *   PersonaSuperKeyBuildRouteException
        """
        method = "PersonaSuperKeyBuilder.build"
        
        # Count how many optional parameters are not-null. One param needs to be not-null.
        params = [name, designation, quota, ransom]
        param_count = sum(bool(p) for p in params)
        
        # Test if no params are set. Need an attribute-value pair to look up a rank's persona_entry.
        if param_count == 0:
            # Return the exception chain on failure.
            return BuildResult.failure(
                PersonaSuperKeyBuildFailedException(
                    message=f"{method}: {PersonaSuperKeyBuildFailedException.ERROR_CODE}",
                    ex=ZeroPersonaSuperKeysException(f"{method}: {ZeroPersonaSuperKeysException.DEFAULT_MESSAGE}")
                )
            )
        # Test if more than one param is set. Only one attribute-value tuple is allowed in a search.
        if param_count > 1:
            # Return the exception chain on failure.
            return BuildResult.failure(
                PersonaSuperKeyBuildFailedException(
                    message=f"{method}: {PersonaSuperKeyBuildFailedException.ERROR_CODE}",
                    ex=ExcessivePersonaSuperKeysException(f"{method}: {ExcessivePersonaSuperKeysException}")
                )
            )
        # After verifying only one Persona hash key-value is set, validate it.
        
        # Build the name PersonaSuperKey if its flag is enabled.
        if name is not None:
            validation = identity_service.validate_name(candidate=name)
            if validation.is_failure:
                # Return the exception chain on failure.
                return BuildResult.failure(
                    PersonaSuperKeyBuildFailedException(
                        message=f"{method}: {PersonaSuperKeyBuildFailedException.ERROR_CODE}",
                        ex=validation.exception
                    )
                )
            # On validation success return a ransom_PersonaSuperKey in the BuildResult.
            return BuildResult.success(PersonaSuperKey(name=name))
        
        # Build the designation PersonaSuperKey if its flag is enabled.
        if designation is not None:
            validation = identity_service.validate_name(candidate=designation)
            if validation.is_failure:
                # Return the exception chain on failure.
                return BuildResult.failure(
                    PersonaSuperKeyBuildFailedException(
                        message=f"{method}: {PersonaSuperKeyBuildFailedException.ERROR_CODE}",
                        ex=validation.exception
                    )
                )
            # On validation success return a designation_PersonaSuperKey in the BuildResult.
            return BuildResult.success(PersonaSuperKey(designation=designation))
        
        # Build the quota PersonaSuperKey if its flag is enabled.
        if quota is not None:
            # Quotas have to be between king_count=1 and pawn_count=8
            validation = number_validator.validate(floor=1, ceiling=9)
            if validation.is_failure:
                # Return the exception chain on failure.
                return BuildResult.failure(
                    PersonaSuperKeyBuildFailedException(
                        message=f"{method}: {PersonaSuperKeyBuildFailedException.ERROR_CODE}",
                        ex=validation.exception
                    )
                )
            # On validation success return a quota_PersonaSuperKey in the BuildResult.
            return BuildResult.success(PersonaSuperKey(quota=quota))
        
        # Build the ransom PersonaSuperKey if its flag is enabled.
        if ransom is not None:
            # Ransoms have to be between king_ransom=0 and 20
            validation = number_validator.validate(floor=0, ceiling=20)
            if validation.is_failure:
                # Return the exception chain on failure.
                return BuildResult.failure(
                    PersonaSuperKeyBuildFailedException(
                        message=f"{method}: {PersonaSuperKeyBuildFailedException.ERROR_CODE}",
                        ex=validation.exception
                    )
                )
            # On validation success return a ransom_PersonaSuperKey in the BuildResult.
            return BuildResult.success(PersonaSuperKey(ransom=ransom))
        
        # The default path returns failure
        BuildResult.failure(
            PersonaSuperKeyBuildFailedException(
                message=f"{method}: {PersonaSuperKeyBuildFailedException.ERROR_CODE}",
                ex=PersonaSuperKeyBuildRouteException(
                    f"{method}: {PersonaSuperKeyBuildRouteException.DEFAULT_MESSAGE}"
                )
            )
        )