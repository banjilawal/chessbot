# src/chess/persona/builder/builder.py

"""
Module: chess.persona.builder.builder
Author: Banji Lawal
Created: 2025-09-08
version: 1.0.0
"""

from typing import Optional

from chess.persona import (
    PersonaSuperKey, PersonaSuperKeyBuildFailedException,
    ExcessivePersonaSuperKeyFlagsException, ZeroPersonaSuperKeyFlagsException
)
from chess.system import (
    BuildResult, Builder, UnhandledRouteException, IdentityService, LoggingLevelRouter,
    NotNegativeNumberValidator,
)


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
            not_negative_validator: NotNegativeNumberValidator = NotNegativeNumberValidator(),
    ) -> BuildResult[PersonaSuperKey]:
        """
        # Action:
            1.  Confirm that only one in the (name, designation, quota, ransom) tuple is not null.
            2.  Certify the not-null attribute is safe using the appropriate validating service.
            3.  If all checks pass build a PersonaSuperKey and send in a BuildResult. Else, return an exception
                in the BuildResult.

        # Parameters:
            Only one these must be provided:
                *   name (Optional[str])
                *   quota (Optional[str])
                *   designation (Optional[str])
                *   ransom (Optional[GameRansom])
    
            These Parameters must be provided:
                *   not_negative_validator (NumberValidator)
                *   identity_service (IdentityService)

        # Returns:
        BuildResult[PersonaSuperKey] containing either:
            - On success: PersonaSuperKey in the payload.
            - On failure: Exception.

        # Raises:
            *   ZeroPersonaSuperKeyFlagsException
            *   PersonaSuperKeyBuildFailedException
            *   ExcessivePersonaSuperKeyFlagsException
        """
        method = "PersonaSuperKeyBuilder.build"
        try:
            # Count how many optional parameters are not-null. One param needs to be not-null.
            params = [name, designation, quota, ransom]
            param_count = sum(bool(p) for p in params)
            
            # Test if no params are set. Need an attribute-value pair to look up a rank's persona_entry.
            if param_count == 0:
                return BuildResult.failure(
                    ZeroPersonaSuperKeyFlagsException(f"{method}: {ZeroPersonaSuperKeyFlagsException.DEFAULT_MESSAGE}")
                )
            # Test if more than one param is set. Only one attribute-value tuple is allowed in a search.
            if param_count > 1:
                return BuildResult.failure(
                    ExcessivePersonaSuperKeyFlagsException(f"{method}: {ExcessivePersonaSuperKeyFlagsException}")
                )
            # After verifying only one Schema hash key-value is set, validate it.
            
            # Build the name PersonaSuperKey if its flag is enabled.
            if name is not None:
                validation = identity_service.validate_name(candidate=name)
                if validation.is_failure:
                    return BuildResult.failure(validation.exception)
                # On validation success return a ransom_PersonaSuperKey in the BuildResult.
                return BuildResult.success(PersonaSuperKey(name=name))
            
            # Build the designation PersonaSuperKey if its flag is enabled.
            if designation is not None:
                validation = identity_service.validate_name(candidate=designation)
                if validation.is_failure:
                    return BuildResult.failure(validation.exception)
                # On validation success return a designation_PersonaSuperKey in the BuildResult.
                return BuildResult.success(PersonaSuperKey(designation=designation))
            
            # Build the quota PersonaSuperKey if its flag is enabled.
            if quota is not None:
                validation = not_negative_validator.validate(candidate=quota)
                if validation.is_failure:
                    return BuildResult.failure(validation.exception)
                # On validation success return a quota_PersonaSuperKey in the BuildResult.
                return BuildResult.success(PersonaSuperKey(quota=quota))
            
            # Build the ransom PersonaSuperKey if its flag is enabled.
            if ransom is not None:
                validation = not_negative_validator.validate(candidate=ransom)
                if validation.is_failure:
                    return BuildResult.failure(validation.exception)
                # On validation success return a ransom_PersonaSuperKey in the BuildResult.
                return BuildResult.success(PersonaSuperKey(ransom=ransom))
            
            # As a failsafe, if the none of the none of the cases are handled by the if blocks return failsafeBranchExPointException in the buildResult failure if a map path was missed.
            BuildResult.failure(
                UnhandledRouteException(f"{method}: {UnhandledRouteException.DEFAULT_MESSAGE}")
            )
        # Finally, catch any missed exception and wrap A PersonaSuperKeyBuildFailedException around it then
        # return the exception-chain inside the ValidationResult.
        except Exception as ex:
            return BuildResult.failure(
                PersonaSuperKeyBuildFailedException(
                    ex=ex, message=f"{method}: {PersonaSuperKeyBuildFailedException.DEFAULT_MESSAGE}"
                )
            )