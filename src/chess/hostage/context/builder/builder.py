from typing import Any, cast

from chess.coord import CoordService
from chess.hostage import (
    CaptivityContextBuildFailedExceptionBuild, CaptivityContextBuildRouteException, CaptivityContext,
    ExcessiveCaptivityContextFlagsException, NullCaptivityContextException, ZeroCaptivityContextFlagsException,
)
from chess.system import IdentityService, LoggingLevelRouter, BuildResult, Builder, id_emitter
from chess.token import CombatantToken, Token, TokenService


class CaptivityContextBuilder(Builder[CaptivityContext]):
    """
     # ROLE: Validation, Data Integrity Guarantor, Security.

    # RESPONSIBILITIES:
    1. Verify a candidate is a CaptivityContext that meets the application's safety contract before the client
        is allowed to use the CaptivityContext object.
    2. Provide pluggable factories for validating different options separately.

    # PARENT:
        * Validator

    3 PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    3 INHERITED ATTRIBUTES:
        *   See Validator class for inherited attributes.
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def build(
            cls,
            victor: Token,
            prisoner: CombatantToken,
            id: int = id_emitter.scout_report_id,
            coord_service: CoordService = CoordService(),
            token_service: TokenService = TokenService(),
            identity_service: IdentityService = IdentityService(),
    ) -> BuildResult[CaptivityContext]:
        """
        # ACTION:
        Verifies candidate is a CaptivityContext in two steps.
            1. Test the candidate is a valid SearchCaptivityContext with a single searcher option switched on.
            2. Test the value passed to CaptivityContext passes its validation contract.
        # PARAMETERS:
            * candidate (Any): Object to verify is a Coord.
            * validator (type[CoordValidator]): Enforces safety requirements on row, column, square_name coords.
        # RETURNS:
            * BuildResult[CaptivityContext] containing either:
                    - On failure: Exception.
                    - On success: CaptivityContext in the payload.
        # RAISES:
            * TypeError
            * NullCaptivityContextException
            * ZeroCaptivityContextFlagsException
            * CaptivityContextBuildFailedExceptionBuild
            * CaptivityContextBuildRouteException
        """
        method = "CaptivityContextBuilder.validate"
        
        # Handle the nonexistence case.
        if candidate is None:
            # Return the exception chain on failure.
            return BuildResult.failure(
                CaptivityContextBuildFailedExceptionBuild(
                    message=f"{method}: {CaptivityContextBuildFailedExceptionBuild.DEFAULT_MESSAGE}",
                    ex=NullCaptivityContextException(f"{method}: {NullCaptivityContextException.DEFAULT_MESSAGE}")
                )
            )
        # Handle the case that the type is wrong.
        if not isinstance(candidate, CaptivityContext):
            # Return the exception chain on failure.
            return BuildResult.failure(
                CaptivityContextBuildFailedExceptionBuild(
                    message=f"{method}: {CaptivityContextBuildFailedExceptionBuild.DEFAULT_MESSAGE}",
                    ex=TypeError(f"{method}: Expected a CaptivityContext, got {type(candidate).__name__} instead.")
                )
            )
        # --- Cast candidate to the CaptivityContext for additional tests. ---#
        context = cast(CaptivityContext, candidate)
        
        # Get how many context flags are set.
        switch_count = len(context.to_dict())
        
        # Handle the case that no context flags are set.
        if switch_count == 0:
            # Return the exception chain on failure.
            return BuildResult.failure(
                CaptivityContextBuildFailedExceptionBuild(
                    message=f"{method}: {CaptivityContextBuildFailedExceptionBuild.DEFAULT_MESSAGE}",
                    ex=ZeroCaptivityContextFlagsException(
                        f"{method}: {ZeroCaptivityContextFlagsException.DEFAULT_MESSAGE}"
                    )
                )
            )
        # Handle the case that more than one context flag is set.
        if switch_count > 1:
            # Return the exception chain on failure.
            return BuildResult.failure(
                CaptivityContextBuildFailedExceptionBuild(
                    message=f"{method}: {CaptivityContextBuildFailedExceptionBuild.DEFAULT_MESSAGE}",
                    ex=ExcessiveCaptivityContextFlagsException(
                        f"{method}: {ExcessiveCaptivityContextFlagsException.DEFAULT_MESSAGE}"
                    )
                )
            )
        # --- Route to the appropriate validation branch. ---#
        
        # Certification for the search-by-id target.
        if context.id is not None and context.id is not None:
            validation = identity_service.validate_id(context.id)
            if validation.is_failure:
                # Return the exception chain on failure.
                return BuildResult.failure(
                    CaptivityContextBuildFailedExceptionBuild(
                        message=f"{method}: {CaptivityContextBuildFailedExceptionBuild.DEFAULT_MESSAGE}",
                        ex=validation.exception
                    )
                )
            # On certification success return the id_CaptivityContext in the BuildResult.
            return BuildResult.success(payload=context)
        
        # Certification for the search-by-victor target.
        if context.victor is not None:
            validation = token_service.validator.validate(context.victor)
            if validation.is_failure:
                # Return the exception chain on failure.
                return BuildResult.failure(
                    CaptivityContextBuildFailedExceptionBuild(
                        message=f"{method}: {CaptivityContextBuildFailedExceptionBuild.DEFAULT_MESSAGE}",
                        ex=validation.exception
                    )
                )
            return BuildResult.success(payload=context)
        
        # Certification for the search-by-prisoner target.
        if context.prisoner is not None:
            validation = token_service.validator.validate(context.prisoner)
            if validation.is_failure:
                # Return the exception chain on failure.
                return BuildResult.failure(
                    CaptivityContextBuildFailedExceptionBuild(
                        message=f"{method}: {CaptivityContextBuildFailedExceptionBuild.DEFAULT_MESSAGE}",
                        ex=validation.exception
                    )
                )
            if not isinstance(validation.payload, CombatantToken):
                # Return the exception chain on failure.
                return BuildResult.failure(
                    CaptivityContextBuildFailedExceptionBuild(
                        message=f"{method}: {CaptivityContextBuildFailedExceptionBuild.DEFAULT_MESSAGE}",
                        ex=TypeError(f"{method}: Expected a CombatantToken, got {type(candidate).__name__} instead.")
                    )
                )
            return BuildResult.success(payload=context)
        
        # Return the exception chain if there was no validation route for the context.
        return BuildResult.failure(
            CaptivityContextBuildFailedExceptionBuild(
                message=f"{method}: {CaptivityContextBuildFailedExceptionBuild.DEFAULT_MESSAGE}",
                ex=CaptivityContextBuildRouteException(
                    f"{method}: {CaptivityContextBuildRouteException.DEFAULT_MESSAGE}"
                )
            )
        )