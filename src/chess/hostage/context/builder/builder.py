from typing import Optional, cast

from chess.hostage import (
    CaptivityContext, CaptivityContextBuildException,
    CaptivityContextBuildRouteException, ExcessiveCaptivityContextFlagsException, ZeroCaptivityContextFlagsException
)
from chess.square import Square, SquareService
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
            token_service: TokenService = TokenService(),
            square_service: SquareService = SquareService(),
            identity_service: IdentityService = IdentityService(),
    ) -> BuildResult[CaptivityContext]:
        """
        # ACTION:
        Verifies candidate is a CaptivityContext in two steps.
            1. Test the candidate is a valid SearchCaptivityContext with a single searcher option switched on.
            2. Test the value passed to CaptivityContext passes its validation contract.
        # PARAMETERS:
            * candidate (Any): Object to verify is a Square.
            * validator (type[SquareValidator]): Enforces safety requirements on row, column, square_name squares.
        # RETURNS:
            * BuildResult[CaptivityContext] containing either:
                    - On failure: Exception.
                    - On success: CaptivityContext in the payload.
        # RAISES:
            * TypeError
            * NullCaptivityContextException
            * ZeroCaptivityContextFlagsException
            * CaptivityContextBuildException
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
                CaptivityContextBuildException(
                    message=f"{method}: {CaptivityContextBuildException.DEFAULT_MESSAGE}",
                    ex=ZeroCaptivityContextFlagsException(
                        f"{method}: {ZeroCaptivityContextFlagsException.DEFAULT_MESSAGE}"
                    )
                )
            )
        # Handle the case that more than one optional param is not-null.
        if param_count > 1:
            # Return the exception chain on failure.
            return BuildResult.failure(
                CaptivityContextBuildException(
                    message=f"{method}: {CaptivityContextBuildException.DEFAULT_MESSAGE}",
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
                    CaptivityContextBuildException(
                        message=f"{method}: {CaptivityContextBuildException.DEFAULT_MESSAGE}",
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
                    CaptivityContextBuildException(
                        message=f"{method}: {CaptivityContextBuildException.DEFAULT_MESSAGE}",
                        ex=validation.exception
                    )
                )
            # On validation success return a victorCaptivityContext in the BuildResult.
    
            return BuildResult.success(CaptivityContext(victor=victor))
        
        # Certification for the search-by-prisoner target.
        if prisoner is not None:
            validation = token_service.validator.verify_token_is_combatant(candidate=prisoner)
            if validation.is_failure:
                # Return the exception chain on failure.
                return BuildResult.failure(
                    CaptivityContextBuildException(
                        message=f"{method}: {CaptivityContextBuildException.DEFAULT_MESSAGE}",
                        ex=validation.exception
                    )
                )
            # On validation success return a prisonerCaptivityContext in the BuildResult.
            return BuildResult.success(CaptivityContext(prisoner=prisoner))
        
        # Certification for the search-by-captured-item target.
        if captured_square is not None:
            validation = square_service.validator.validate(candidate=captured_square)
            if validation.is_failure:
                # Return the exception chain on failure.
                return BuildResult.failure(
                    CaptivityContextBuildException(
                        message=f"{method}: {CaptivityContextBuildException.DEFAULT_MESSAGE}",
                        ex=validation.exception
                    )
                )
            # On validation success return a captured_squareCaptivityContext in the BuildResult.
            return BuildResult.success(CaptivityContext(captured_square=captured_square))
        
        # Return the exception chain if there is no build route for the context.
        return BuildResult.failure(
            CaptivityContextBuildException(
                message=f"{method}: {CaptivityContextBuildException.DEFAULT_MESSAGE}",
                ex=CaptivityContextBuildRouteException(
                    f"{method}: {CaptivityContextBuildRouteException.DEFAULT_MESSAGE}"
                )
            )
        )