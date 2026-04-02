# src/logic/token/database/search/context/service/operation/validation/validator.py

"""
Module: logic.token.database.search.context.service.operation.validation.validator
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from __future__ import annotations
from typing import Any, cast


from logic.system import LoggingLevelRouter, Validator, ValidationResult
from logic.token import (
    ExcessTokenContextFlagsException, NullTokenContextException, TokenContext, TokenContextIntegrityWorkers,
    TokenContextValidationException, TokenContextValidationRouteException, ZeroTokenContextFlagsException
)

class TokenContextValidator(Validator[TokenContext]):
    """
    Role
        -   Transaction Worker
        -   Integrity Maintenance
        -   Consistency Assurance
        -   Process Runner

    Responsibilities:
        1.  Ensure a TokenContext instance is certified safe, reliable and consistent before use.

    Attributes:

    Provides:
        -   def validate(
                    candidate: Any,
                    workers: TokenContextIntegrityWorkers,
            ) -> BuildResult[TokenContext]:

    Super Class:
        Validator
    """
    @classmethod
    @LoggingLevelRouter.monitor
    def validate(
            cls,
            candidate: Any,
            workers: TokenContextIntegrityWorkers,
    ) -> ValidationResult[TokenContext]:
        """
        Certify a candidate is a TokenContext that is safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if any of the following
                occur
                    -   The candidate is null.
                    -   The candidate is not a TokenContext.
                    -   It has no attributes enabled.
                    -   It has more than one attribute enabled.
                    -   The enabled attribute fails a safety check.
                    -   There is no validation path for the attribute.
            2.  Otherwise, send the success result.
        Args:
            candidate: Any,
            workers: TokenContextIntegrityWorkers
        Returns:
            ValiationResult[TokenContext]
        Raises:
            TypeError
            NullTokenContextException
            ZeroTokenContextFlagsException
            TokenContextValidationException
            ExcessTokenContextFlagsException
            TeamContextValidationRouteException
        """
        method = f"{cls.__name__}.validate"
        
        # Handle the nonexistence case.
        if candidate is None:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                TokenContextValidationException(
                    mthd=method,
                    title=cls.__name__,
                    op=TokenContextValidationException.OP,
                    msg=TokenContextValidationException.MSG,
                    err_code=TokenContextValidationException.ERR_CODE,
                    rslt_type=TokenContextValidationException.RSLT_TYPE,
                    ex=NullTokenContextException(
                        msg=TokenContextValidationException.MSG,
                        err_code=TokenContextValidationException.ERR_CODE,
                    )
                )
            )
        # Handle the wrong class case.
        if not isinstance(candidate, TokenContext):
            # Return the exception chain on failure.
            return ValidationResult.failure(
                TokenContextValidationException(
                    mthd=method,
                    title=cls.__name__,
                    op=TokenContextValidationException.OP,
                    msg=TokenContextValidationException.MSG,
                    err_code=TokenContextValidationException.ERR_CODE,
                    rslt_type=TokenContextValidationException.RSLT_TYPE,
                    ex=TypeError(
                        f"Expected TokenContext, got {type(candidate).__name__} instead."
                    )
                )
            )
        # --- Cast the candidate to TokenContext for additional tests. ---#
        context = cast(TokenContext, candidate)
        
        # Handle the case of searching with no attribute-value provided.
        flag_count = len(context.to_dict())
        if flag_count == 0:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                TokenContextValidationException(
                    mthd=method,
                    title=cls.__name__,
                    op=TokenContextValidationException.OP,
                    msg=TokenContextValidationException.MSG,
                    err_code=TokenContextValidationException.ERR_CODE,
                    rslt_type=TokenContextValidationException.RSLT_TYPE,
                    ex=ZeroTokenContextFlagsException(
                        msg=ZeroTokenContextFlagsException.MSG,
                        err_code=ZeroTokenContextFlagsException.ERR_CODE,
                    )
                )
            )
        # Handle the case of too many attributes being used in a search.
        if flag_count > 1:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                TokenContextValidationException(
                    mthd=method,
                    title=cls.__name__,
                    op=TokenContextValidationException.OP,
                    msg=TokenContextValidationException.MSG,
                    err_code=TokenContextValidationException.ERR_CODE,
                    rslt_type=TokenContextValidationException.RSLT_TYPE,
                    ex=ExcessTokenContextFlagsException(
                        msg=ExcessTokenContextFlagsException.MSG,
                        err_code=ExcessTokenContextFlagsException.ERR_CODE,
                    )
                )
            )
        # --- Route to the appropriate validation branch. ---#
        
        # Certification for the search-by-id target.
        if context.id is not None:
            validation_result = workers.identity_service.validate_id(
                candidate=context.id
            )
            if validation_result.is_failure:
                # Return the exception chain on failure.
                return ValidationResult.failure(
                    TokenContextValidationException(
                        mthd=method,
                        title=cls.__name__,
                        op=TokenContextValidationException.OP,
                        msg=TokenContextValidationException.MSG,
                        err_code=TokenContextValidationException.ERR_CODE,
                        rslt_type=TokenContextValidationException.RSLT_TYPE,
                        ex=validation_result.exception
                    )
                )
            # On validation success forward the work product to the caller.
            return ValidationResult.success(context)
        
        # Certification for the search-by-designation target.
        if context.designation is not None:
            validation_result = workers.identity_service.validate_name(
                candidate=context.designation
            )
            if validation_result.is_failure:
                # Return the exception chain on failure.
                return ValidationResult.failure(
                    TokenContextValidationException(
                        mthd=method,
                        title=cls.__name__,
                        op=TokenContextValidationException.OP,
                        msg=TokenContextValidationException.MSG,
                        err_code=TokenContextValidationException.ERR_CODE,
                        rslt_type=TokenContextValidationException.RSLT_TYPE,
                        ex=validation_result.exception
                    )
                )
            # On validation success forward the work product to the caller.
            return ValidationResult.success(context)
        
        # Certification for the search-by-opening_square_name target.
        if context.opening_square_name is not None:
            validation_result = workers.identity_service.validate_name(
                candidate=context.opening_square_name
            )
            if validation_result.is_failure:
                # Return the exception chain on failure.
                return ValidationResult.failure(
                    TokenContextValidationException(
                        mthd=method,
                        title=cls.__name__,
                        op=TokenContextValidationException.OP,
                        msg=TokenContextValidationException.MSG,
                        err_code=TokenContextValidationException.ERR_CODE,
                        rslt_type=TokenContextValidationException.RSLT_TYPE,
                        ex=validation_result.exception
                    )
                )
            # On validation success forward the work product to the caller.
            return ValidationResult.success(context)
        
        # Certification for the search-by-coord target.
        if context.coord is not None:
            validation_result = workers.coord_service.validator.validate(
                candidate=context.coord
            )
            if validation_result.is_failure:
                # Return the exception chain on failure.
                return ValidationResult.failure(
                    TokenContextValidationException(
                        mthd=method,
                        title=cls.__name__,
                        op=TokenContextValidationException.OP,
                        msg=TokenContextValidationException.MSG,
                        err_code=TokenContextValidationException.ERR_CODE,
                        rslt_type=TokenContextValidationException.RSLT_TYPE,
                        ex=validation_result.exception
                    )
                )
            # On validation success forward the work product to the caller..
            return ValidationResult.success(context)
        
        # Certification for the search-by-team target.
        if context.team is not None:
            validation_result = workers.team_service.validator.validate(
                candidate=context.team
            )
            if validation_result.is_failure:
                # Return the exception chain on failure.
                return ValidationResult.failure(
                    TokenContextValidationException(
                        mthd=method,
                        title=cls.__name__,
                        op=TokenContextValidationException.OP,
                        msg=TokenContextValidationException.MSG,
                        err_code=TokenContextValidationException.ERR_CODE,
                        rslt_type=TokenContextValidationException.RSLT_TYPE,
                        ex=validation_result.exception
                    )
                )
            # On validation success forward the work product to the caller.
            return ValidationResult.success(context)
        
        # Certification for the search-by-rank target.
        if context.rank is not None:
            validation_result = workers.rank_service.validator.validate(
                candidate=context.rank
            )
            if validation_result.is_failure:
                # Return the exception chain on failure.
                return ValidationResult.failure(
                    TokenContextValidationException(
                        mthd=method,
                        title=cls.__name__,
                        op=TokenContextValidationException.OP,
                        msg=TokenContextValidationException.MSG,
                        err_code=TokenContextValidationException.ERR_CODE,
                        rslt_type=TokenContextValidationException.RSLT_TYPE,
                        ex=validation_result.exception
                    )
                )
            # On validation success forward the work product to the caller.
            return ValidationResult.success(context)
        
        # Certification for the search-by-color target.
        if context.color is not None:
            validation_result = workers.color_validator.validate(
                candidate=context.color
            )
            if validation_result.is_failure:
                # Return the exception chain on failure.
                return ValidationResult.failure(
                    TokenContextValidationException(
                        mthd=method,
                        title=cls.__name__,
                        op=TokenContextValidationException.OP,
                        msg=TokenContextValidationException.MSG,
                        err_code=TokenContextValidationException.ERR_CODE,
                        rslt_type=TokenContextValidationException.RSLT_TYPE,
                        ex=validation_result.exception
                    )
                )
            # On validation success forward the work product to the caller.
            return ValidationResult.success(context)
        
        # Certification for the search-by-ransom target.
        if context.ransom is not None:
            validation_result = workers.number_validator.validate(
                candidate=context.ransom,
                floor=workers.persona_service.min_ransom,
                ceiling=workers.persona_service.max_ransom,
            )
            # Return the exception chain on failure.
            if validation_result.is_failure:
                # Return the exception chain on failure.
                return ValidationResult.failure(
                    TokenContextValidationException(
                        mthd=method,
                        title=cls.__name__,
                        op=TokenContextValidationException.OP,
                        msg=TokenContextValidationException.MSG,
                        err_code=TokenContextValidationException.ERR_CODE,
                        rslt_type=TokenContextValidationException.RSLT_TYPE,
                        ex=validation_result.exception
                    )
                )
            # On validation success forward the work product to the caller.
            return ValidationResult.success(context)
        
        # Handle the case that, there is no validation logic for the attribute.
        return ValidationResult.failure(
            TokenContextValidationException(
                mthd=method,
                title=cls.__name__,
                op=TokenContextValidationException.OP,
                msg=TokenContextValidationException.MSG,
                err_code=TokenContextValidationException.ERR_CODE,
                rslt_type=TokenContextValidationException.RSLT_TYPE,
                ex=TokenContextValidationRouteException(
                    msg=TokenContextValidationRouteException.MSG,
                    err_code=TokenContextValidationRouteException.ERR_CODE,
                )
            )
        )
        
    
