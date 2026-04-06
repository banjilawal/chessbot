# src/integrity/validation/context/coord/validator.py

"""
Module: integrity.validation.context.coord.validator
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations


class CoordContextValidator(Validator[CoordContext]):
    """
    Role
        -   Transaction Worker
        -   Integrity Maintenance
        -   Consistency Assurance
        -   Process Runner

    Responsibilities:
        1.  Ensure a CoordContext instance is certified safe, reliable and consistent before use.

    Attributes:

    Provides:
        -   execute(
                    rank: Any,
                    number_validator: NumberValidator = NumberValidator(),
            ) -> ValidationResult[CoordContext]
            
        -   _run_attribute_checks(
                    attributes: List[int],
                    number_validator: NumberValidator,
            ) -> ValidationResult[CoordContext]

    Super Class:
        Validator
    """

    @classmethod
    @LoggingLevelRouter.monitor
    def validate(
            cls,
            candidate: Any,
            number_validator: NumberValidator = NumberValidator(),
    ) -> ValidationResult[CoordContext]:
        """
        Action:
            1.  If the rank is either:
                    -   is null.
                    -   the type wrong
                    -   The attribute fails a validation check.
                send an exception chain in the ValidationResult.
            2.  Otherwise, send the success result.
        Args:
            candidate: Any
            number_validator: NumberValidator
        Returns:
            ValidationResult[CoordContext]
        Raises:
            TypeError
            CoordContextException
            NullCoordContextException
            ZeroCoordContextFlagsException
        """
        method = f"{cls.__name__}.validate"
        
        # Handle the nonexistence case.
        if candidate is None:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                CoordContextValidationException(
                    mthd=method,
                    title=cls.__name__,
                    op=CoordContextValidationException.OP,
                    msg=CoordContextValidationException.MSG,
                    err_code=CoordContextValidationException.ERR_CODE,
                    rslt_type=CoordContextValidationException.RSLT_TYPE,
                    ex=NullCoordContextException(
                        msg=CoordContextValidationException.MSG,
                        err_code=CoordContextValidationException.ERR_CODE,
                    )
                )
            )
        # Handle the case that, they type is wrong.
        if not isinstance(candidate, CoordContext):
            # Return the exception chain on failure.
            return ValidationResult.failure(
                CoordContextValidationException(
                    mthd=method,
                    title=cls.__name__,
                    op=CoordContextValidationException.OP,
                    msg=CoordContextValidationException.MSG,
                    err_code=CoordContextValidationException.ERR_CODE,
                    rslt_type=CoordContextValidationException.RSLT_TYPE,
                    ex=TypeError(f"Expected a CoordContext, got {type(candidate).__name__} instead.")
                )
            )
        # --- Cast rank to the CoordContext for additional tests. ---#
        context = cast(CoordContext, candidate)
        
        # Get how many context flags are set.
        switch_count = len(context.to_dict())
        
        # Handle the case that, no context flags are set.
        if switch_count == 0:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                CoordContextValidationException(
                    mthd=method,
                    title=cls.__name__,
                    op=CoordContextValidationException.OP,
                    msg=CoordContextValidationException.MSG,
                    err_code=CoordContextValidationException.ERR_CODE,
                    rslt_type=CoordContextValidationException.RSLT_TYPE,
                    ex=ZeroCoordContextFlagsException(
                        msg=CoordContextValidationException.MSG,
                        err_code=CoordContextValidationException.ERR_CODE,
                    )
                )
            )
        # --- Route to the appropriate validation branch. ---#
        
        # Certification for the search-by-column-and-row target.
        if switch_count == 2:
            # Handle the case that, the search-by-column-and-row target fails its integrity checks.
            validation_result = cls._run_attribute_checks(
                attributes=[context.row, context.column],
                number_validator=number_validator,
            )
            # On failure, forward the result
            if validation_result.is_failure:
                return validation_result
            # --- Otherwise forward the work product to the client. ---#
            return ValidationResult.success(context)
        
        # --- Validation route for row_CoordContext. ---#
        if context.row is not None:
            # Handle the case that, the context.row fails a check.
            validation_result = cls._run_attribute_checks(
                attributes=[context.row],
                number_validator=number_validator,
            )
            # On failure, forward the result
            if validation_result.is_failure:
                return validation_result
            # --- Otherwise forward the work product to the client. ---#
            return ValidationResult.success(context)
        
        # --- Validation route for column_CoordContext. ---#
        if context.column is not None:
            # Handle the case that, the context.column fails a check.
            validation_result = cls._run_attribute_checks(
                attributes=[context.column],
                number_validator=number_validator,
            )
            # On failure forward the result
            if validation_result.is_failure:
                return validation_result
            # --- Otherwise forward the work product to the client. ---#
            return ValidationResult.success(context)
        
        # Handle the case that, there is no validation route for the context.
        return ValidationResult.failure(
            CoordContextValidationException(
                mthd=method,
                title=cls.__name__,
                op=CoordContextValidationException.OP,
                msg=CoordContextValidationException.MSG,
                err_code=CoordContextValidationException.ERR_CODE,
                rslt_type=CoordContextValidationException.RSLT_TYPE,
                ex=CoordContextValidationRouteException(
                    msg=CoordContextValidationException.MSG,
                    err_code=CoordContextValidationException.ERR_CODE,
                )
            )
        )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _run_attribute_checks(
            cls,
            attributes: List[int],
            number_validator: NumberValidator,
    ) -> ValidationResult[CoordContext]:
        """
        Run checks on which ether attributes have been enabled.
        Action:
            Send an exception in the ValidationResult if list member fails a check.
            Otherwise, send the success result.
        Args:
            attributes: List[int]
            number_validator: NumberValidator
        Returns:
            ValidationResult[CoordContext]
        Raises:
            CoordContextValidationException
        """
        method = f"{cls.__name__}._run_validation_check"
        
        for attribute in attributes:
            # Handle the case that, the rowis not safe.
            validation_result = number_validator.validate(
                candidate=attribute,
                ceiling=BOARD_DIMENSION - 1,
                floor=0,
            )
            if validation_result.is_failure:
                # Return the exception chain on failure.
                return ValidationResult.failure(
                    CoordContextValidationException(
                        mthd=method,
                        title=cls.__name__,
                        op=CoordContextValidationException.OP,
                        msg=CoordContextValidationException.MSG,
                        err_code=CoordContextValidationException.ERR_CODE,
                        rslt_type=CoordContextValidationException.RSLT_TYPE,
                        ex=validation_result.exception
                    )
                )
        # --- Forward the work product to the caller. ---#
        return ValidationResult.success(CoordContext())
        



