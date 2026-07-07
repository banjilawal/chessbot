# src/builder/context/hostage/builder.py

"""
Module: builder.context.hostage.builder
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

class HostageContextBuilder(Builder[HostageContext]):
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
            victor: Optional[Token],
            captured_square: Optional[Square],
            prisoner: Optional[CombatantToken],
            id: Optional[int] = id_emitter.scout_report_id,
            token_service: TokenService = TokenService(),
            square_service: SquareService = SquareService(),
            identity_service: IdentityService = IdentityService(),
    ) -> BuildResult[HostageContext]:
        """
        # ACTION:
        Verifies rank is a HostageContext in two steps.
            1. Test the rank is a valid SearchHostageContext with a single searcher option switched on.
            2. Test the value passed to HostageContext passes its validation contract.
        # PARAMETERS:
            * rank (Any): Object to verify is a Square.
            * validation (type[SquareValidator]): Enforces safety requirements on row, column, square_name squares.
        # RETURNS:
            * BuildResult[HostageContext] containing either:
                    - On failure: Exception.
                    - On success: HostageContext in the payload.
        Raises:
            * TypeError
            * NullHostageContextException
            * ZeroHostageContextFlagsException
            * HostageContextBuilderException
            * HostageContextBuildRouteException
        """
        method = "HostageContextBuilder.validate"
        
        # --- Count how many optional parameters are not-null. only one should be not null. ---#
        params = [id, prisoner, victor, captured_square]
        param_count = sum(bool(p) for p in params)
        
        # Handle the case that, all the optional params are null.
        if param_count == 0:
            # Send the exception chain on failure.
            return BuildResult.failure(
                HostageContextBuilderException(
                    msg=f"{method}: {HostageContextBuilderException.MSG}",
                    ex=ZeroHostageContextFlagsException(
                        f"{method}: {ZeroHostageContextFlagsException.MSG}"
                    )
                )
            )
        # Handle the case that, more than one optional param is not-null.
        if param_count > 1:
            # Send the exception chain on failure.
            return BuildResult.failure(
                HostageContextBuilderException(
                    msg=f"{method}: {HostageContextBuilderException.MSG}",
                    ex=ArenaHostageContextFlagsException(
                        f"{method}: {ArenaHostageContextFlagsException.MSG}"
                    )
                )
            )
        # --- Route to the appropriate validation/build branch. ---#
        
        # Build the id HostageContext if its flag is enabled.
        if id is not None:
            validation = identity_service.validate_id(candidate=id)
            if validation.is_failure:
                # Send the exception chain on failure.
                return BuildResult.failure(
                    HostageContextBuilderException(
                        msg=f"{method}: {HostageContextBuilderException.MSG}",
                        ex=validation.exception
                    )
                )
            # On validation success return an id_HostageContext in the BuildResult.
            return BuildResult.success(HostageContext(id=id))
        
        # Build the victor HostageContext if its flag is enabled.
        if victor is not None:
            validation = token_service.run.search_service(candidate=victor)
            if validation.is_failure:
                # Send the exception chain on failure.
                return BuildResult.failure(
                    HostageContextBuilderException(
                        msg=f"{method}: {HostageContextBuilderException.MSG}",
                        ex=validation.exception
                    )
                )
            # On validation success return a victorHostageContext in the BuildResult.
    
            return BuildResult.success(HostageContext(victor=victor))
        
        # Certification for the search-by-prisoner target.
        if prisoner is not None:
            validation = token_service.run.verify_token_is_combatant(candidate=prisoner)
            if validation.is_failure:
                # Send the exception chain on failure.
                return BuildResult.failure(
                    HostageContextBuilderException(
                        msg=f"{method}: {HostageContextBuilderException.MSG}",
                        ex=validation.exception
                    )
                )
            # On validation success return a prisonerHostageContext in the BuildResult.
            return BuildResult.success(HostageContext(prisoner=prisoner))
        
        # Certification for the search-by-captured-item target.
        if captured_square is not None:
            validation = square_service.run.build(candidate=captured_square)
            if validation.is_failure:
                # Send the exception chain on failure.
                return BuildResult.failure(
                    HostageContextBuilderException(
                        msg=f"{method}: {HostageContextBuilderException.MSG}",
                        ex=validation.exception
                    )
                )
            # On validation success return a captured_squareHostageContext in the BuildResult.
            return BuildResult.success(HostageContext(captured_square=captured_square))
        
        # Return the exception chain if there is no build route for the context.
        return BuildResult.failure(
            HostageContextBuilderException(
                msg=f"{method}: {HostageContextBuilderException.MSG}",
                ex=HostageContextBuildRouteException(
                    f"{method}: {HostageContextBuildRouteException.MSG}"
                )
            )
        )