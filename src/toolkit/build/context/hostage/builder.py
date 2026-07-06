# src/toolkit/context/hostage/toolkit.py

"""
Module: toolkit.context.hostage.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

class HostageContextToolkit(Toolkit[HostageContext]):
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

    @LoggingLevelRouter.monitor
    def __init__(
            self,
            victor: Optional[Token],
            captured_square: Optional[Square],
            prisoner: Optional[CombatantToken],
            id: Optional[int] = id_emitter.scout_report_id,
            token_service: TokenService = TokenService(),
            square_service: SquareService = SquareService(),
            identity_service: IdentityService = IdentityService(),
    ) -> ToolkitResult[HostageContext]:
        """
        # ACTION:
        Verifies rank is a HostageContext in two steps.
            1. Test the rank is a valid SearchHostageContext with a single searcher option switched on.
            2. Test the value passed to HostageContext passes its validation contract.
        # PARAMETERS:
            * rank (Any): Object to verify is a Square.
            * validation (type[SquareValidator]): Enforces safety requirements on row, column, square_name squares.
        # RETURNS:
            * ToolkitResult[HostageContext] containing either:
                    - On failure: Exception.
                    - On success: HostageContext in the payload.
        Raises:
            * TypeError
            * NullHostageContextException
            * ZeroHostageContextFlagsException
            * HostageContextToolkitException
            * HostageContextToolkitRouteException
        """
        method = "HostageContextToolkit.validate"
        
        # --- Count how many optional parameters are not-null. only one should be not null. ---#
        params = [id, prisoner, victor, captured_square]
        param_count = sum(bool(p) for p in params)
        
        # Handle the case that, all the optional params are null.
        if param_count == 0:
            # Send the exception chain on failure.
            return ToolkitResult.failure(
                HostageContextToolkitException(
                    msg=f"{method}: {HostageContextToolkitException.MSG}",
                    ex=ZeroHostageContextFlagsException(
                        f"{method}: {ZeroHostageContextFlagsException.MSG}"
                    )
                )
            )
        # Handle the case that, more than one optional param is not-null.
        if param_count > 1:
            # Send the exception chain on failure.
            return ToolkitResult.failure(
                HostageContextToolkitException(
                    msg=f"{method}: {HostageContextToolkitException.MSG}",
                    ex=ArenaHostageContextFlagsException(
                        f"{method}: {ArenaHostageContextFlagsException.MSG}"
                    )
                )
            )
        # --- Route to the appropriate validation/toolkit branch. ---#
        
        # Toolkit the id HostageContext if its flag is enabled.
        if id is not None:
            validation = identity_service.validate_id(candidate=id)
            if validation.is_failure:
                # Send the exception chain on failure.
                return ToolkitResult.failure(
                    HostageContextToolkitException(
                        msg=f"{method}: {HostageContextToolkitException.MSG}",
                        ex=validation.exception
                    )
                )
            # On validation success return an id_HostageContext in the ToolkitResult.
            return ToolkitResult.success(HostageContext(id=id))
        
        # Toolkit the victor HostageContext if its flag is enabled.
        if victor is not None:
            validation = token_service.execute.search_service(candidate=victor)
            if validation.is_failure:
                # Send the exception chain on failure.
                return ToolkitResult.failure(
                    HostageContextToolkitException(
                        msg=f"{method}: {HostageContextToolkitException.MSG}",
                        ex=validation.exception
                    )
                )
            # On validation success return a victorHostageContext in the ToolkitResult.
    
            return ToolkitResult.success(HostageContext(victor=victor))
        
        # Certification for the search-by-prisoner target.
        if prisoner is not None:
            validation = token_service.execute.verify_token_is_combatant(candidate=prisoner)
            if validation.is_failure:
                # Send the exception chain on failure.
                return ToolkitResult.failure(
                    HostageContextToolkitException(
                        msg=f"{method}: {HostageContextToolkitException.MSG}",
                        ex=validation.exception
                    )
                )
            # On validation success return a prisonerHostageContext in the ToolkitResult.
            return ToolkitResult.success(HostageContext(prisoner=prisoner))
        
        # Certification for the search-by-captured-item target.
        if captured_square is not None:
            validation = square_service.execute.build(candidate=captured_square)
            if validation.is_failure:
                # Send the exception chain on failure.
                return ToolkitResult.failure(
                    HostageContextToolkitException(
                        msg=f"{method}: {HostageContextToolkitException.MSG}",
                        ex=validation.exception
                    )
                )
            # On validation success return a captured_squareHostageContext in the ToolkitResult.
            return ToolkitResult.success(HostageContext(captured_square=captured_square))
        
        # Return the exception chain if there is no toolkit route for the context.
        return ToolkitResult.failure(
            HostageContextToolkitException(
                msg=f"{method}: {HostageContextToolkitException.MSG}",
                ex=HostageContextToolkitRouteException(
                    f"{method}: {HostageContextToolkitRouteException.MSG}"
                )
            )
        )