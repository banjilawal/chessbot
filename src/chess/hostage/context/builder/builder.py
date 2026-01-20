from typing import Any, Optional, cast

from chess.coord import CoordService
from chess.hostage import (
    CaptivityContextBuildFailedExceptionBuild, CaptivityContextBuildRouteException, CaptivityContext,
    ExcessiveCaptivityContextFlagsException, NullCaptivityContextException, ZeroCaptivityContextFlagsException,
)
from chess.square import Square
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
            victor: Optional[Token],
            captured_square: Optional[Square],
            prisoner: Optional[CombatantToken],
            id: Optional[int] = id_emitter.scout_report_id,
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
        
        # --- Count how many optional parameters are not-null. only one should be not null. ---#
        params = [id, prisoner, victor, captured_square]
        param_count = sum(bool(p) for p in params)
        
        # Handle the case that all the optional params are null.
        if param_count == 0:
            # Return the exception chain on failure.
            return BuildResult.failure(
                CaptivityContextBuildFailedExceptionBuild(
                    message=f"{method}: {CaptivityContextBuildFailedExceptionBuild.DEFAULT_MESSAGE}",
                    ex=ZeroCaptivityContextFlagsException(
                        f"{method}: {ZeroCaptivityContextFlagsException.DEFAULT_MESSAGE}"
                    )
                )
            )
        # Handle the case that more than one optional param is not-null.
        if param_count > 1:
            # Return the exception chain on failure.
            return BuildResult.failure(
                CaptivityContextBuildFailedExceptionBuild(
                    message=f"{method}: {CaptivityContextBuildFailedExceptionBuild.DEFAULT_MESSAGE}",
                    ex=ExcessiveCaptivityContextFlagsException(
                        f"{method}: {ExcessiveCaptivityContextFlagsException.DEFAULT_MESSAGE}"
                    )
                )
            )
        # --- Route to the appropriate validation/build branch. ---#
        
        # Build the id CaptivityContext if its flag is enabled.
        if id is not None:
            validation = identity_service.validate_id(candidate=id)
            if validation.is_failure:
                # Return the exception chain on failure.
                return BuildResult.failure(
                    CaptivityContextBuildFailedExceptionBuild(
                        message=f"{method}: {CaptivityContextBuildFailedExceptionBuild.DEFAULT_MESSAGE}",
                        ex=validation.exception
                    )
                )
            # On validation success return an id_CaptivityContext in the BuildResult.
            return BuildResult.success(CaptivityContext(id=id))
        
        # Build the victor CaptivityContext if its flag is enabled.
        if victor is not None:
            validation = token_service.validator.validate(candidate=victor)
            if validation.is_failure:
                # Return the exception chain on failure.
                return BuildResult.failure(
                    CaptivityContextBuildFailedExceptionBuild(
                        message=f"{method}: {CaptivityContextBuildFailedExceptionBuild.DEFAULT_MESSAGE}",
                        ex=validation.exception
                    )
                )
            # On validation success return an victorCaptivityContext in the BuildResult.
            return BuildResult.success(CaptivityContext(victor=victor))
        
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