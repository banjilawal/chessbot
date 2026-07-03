# src/toolkit/context/persona/toolkit.py

"""
Module: toolkit.context.persona.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from model.catalog.persona import (
    ArenaPersonaKeysException, PersonaKey, PersonaKeyToolkitException,
    PersonaKeyToolkitRouteException, ZeroPersonaKeysException
)
from system import NumberValidator, ToolkitResult, Toolkit, IdentityService, LoggingLevelRouter


class PersonaContextToolkit(Toolkit[PersonaKey]):
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
            quota: Optional[int] = None,
            ransom: Optional[int] = None,
            designation: Optional[str] = None,
            identity_service: IdentityService = IdentityService(),
            number_validator: NumberValidator = NumberValidator(),
    ) -> ToolkitResult[PersonaKey]:
        """
        # ACTION:
            1.  If only one optional param is not-null return an exception in the ToolkitResult. Else
            2.  If the enabled param is not certified by the appropriate validating service return an exception in
                the ToolkitResult.
            3.  After the active param is validated create the PersonaContext object and return in the ToolkitResult.
        # PARAMETERS:
            *   Only one these must be provided:
                    *   schema (Optional[str])
                    *   quota (Optional[int])
                    *   ransom (Optional[int])
                    *   designation (Optional[str])
            *   These Parameters must be provided:
                    *   color_validator (GameColorValidator)
                    *   identity_service (IdentityService)
                    *   number_validation (NumberValidator)

        # RETURNS:
            *   ToolkitResult[PersonaContext] containing either:
                    - On failure: Exception.
                    - On success: PersonaContext in the payload.
        Raises:
            *   ZeroPersonaKeysException
            *   PersonaKeyToolkitException
            *   ArenaPersonaKeysException
            *   PersonaKeyToolkitRouteException
        """
        method = "PersonaContextToolkit.toolkit"
        
        # Count how many optional parameters are not-null. One param needs to be not-null.
        params = [name, designation, quota, ransom]
        param_count = sum(bool(p) for p in params)
        
        # Test if no params are set. Need an attribute-value pair to look up a rank's persona_entry.
        if param_count == 0:
            # Send the exception chain on failure.
            return ToolkitResult.failure(
                PersonaKeyToolkitException(
                    msg=f"{method}: {PersonaKeyToolkitException.ERR_CODE}",
                    ex=ZeroPersonaKeysException(f"{method}: {ZeroPersonaKeysException.MSG}")
                )
            )
        # Test if more than one param is set. Only one attribute-value tuple is allowed in a search.
        if param_count > 1:
            # Send the exception chain on failure.
            return ToolkitResult.failure(
                PersonaKeyToolkitException(
                    msg=f"{method}: {PersonaKeyToolkitException.ERR_CODE}",
                    ex=ArenaPersonaKeysException(f"{method}: {ArenaPersonaKeysException}")
                )
            )
        # After verifying only one Persona hash key-value is set, validate it.
        
        # Toolkit the schema PersonaContext if its flag is enabled.
        if name is not None:
            validation = identity_service.validate_name(candidate=name)
            if validation.is_failure:
                # Send the exception chain on failure.
                return ToolkitResult.failure(
                    PersonaKeyToolkitException(
                        msg=f"{method}: {PersonaKeyToolkitException.ERR_CODE}",
                        ex=validation.exception
                    )
                )
            # On validation success return a ransom_PersonaKey in the ToolkitResult.
            return ToolkitResult.success(PersonaKey(name=name))
        
        # Toolkit the designation PersonaContext if its flag is enabled.
        if designation is not None:
            validation = identity_service.validate_name(candidate=designation)
            if validation.is_failure:
                # Send the exception chain on failure.
                return ToolkitResult.failure(
                    PersonaKeyToolkitException(
                        msg=f"{method}: {PersonaKeyToolkitException.ERR_CODE}",
                        ex=validation.exception
                    )
                )
            # On validation success return a designation_PersonaKey in the ToolkitResult.
            return ToolkitResult.success(PersonaKey(designation=designation))
        
        # Toolkit the quota PersonaContext if its flag is enabled.
        if quota is not None:
            # Quotas have to be between king_count=1 and pawn_count=8
            validation = number_validator.build(floor=1, ceiling=9)
            if validation.is_failure:
                # Send the exception chain on failure.
                return ToolkitResult.failure(
                    PersonaKeyToolkitException(
                        msg=f"{method}: {PersonaKeyToolkitException.ERR_CODE}",
                        ex=validation.exception
                    )
                )
            # On validation success return a quota_PersonaKey in the ToolkitResult.
            return ToolkitResult.success(PersonaKey(quota=quota))
        
        # Toolkit the ransom PersonaContext if its flag is enabled.
        if ransom is not None:
            # Ransoms have to be between king_ransom=0 and 20
            validation = number_validator.build(floor=0, ceiling=20)
            if validation.is_failure:
                # Send the exception chain on failure.
                return ToolkitResult.failure(
                    PersonaKeyToolkitException(
                        msg=f"{method}: {PersonaKeyToolkitException.ERR_CODE}",
                        ex=validation.exception
                    )
                )
            # On validation success return a ransom_PersonaKey in the ToolkitResult.
            return ToolkitResult.success(PersonaKey(ransom=ransom))
        
        # The default path returns failure.
        ToolkitResult.failure(
            PersonaKeyToolkitException(
                msg=f"{method}: {PersonaKeyToolkitException.ERR_CODE}",
                ex=PersonaKeyToolkitRouteException(
                    f"{method}: {PersonaKeyToolkitRouteException.MSG}"
                )
            )
        )