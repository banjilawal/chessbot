# src/chess/system/command/argument/validator/validator.py

"""
Module: chess.system.command.argument.validator.validator
Author: Banji Lawal
Created: 2026-02-24
"""

from __future__ import annotations

from typing import Any, Dict, cast

from chess.system import (
    ArgumentCountException, ArgumentNameException, ArgumentTypeException, ArgumentsValidationException,
    IdentityService, LoggingLevelRouter, NullArgumentsException, ValidationResult, Validator
)


class ArgumentsValidator(Validator[Dict]):
    """
    # ROLE: Validation, Data Integrity Guarantor, Security.
    
    # RESPONSIBILITIES:
    1.  Ensure a Argument has.
    *   The correct number of arguments.
    *   The arguments have the correct names.
    *   The correct types.
    
    # PARENT:
    *   Validator
    
    # PROVIDES:
    None
    
    # LOCAL ATTRIBUTES:
    None
    
    # INHERITED ATTRIBUTES:
    None
    
    # CONSTRUCTOR PARAMETERS:
    None
    
    # LOCAL METHODS:
        *   validate(
                    cipher: Command,
                    candidate: Any,
                    identity_service: IdentityService = IdentityService(),
            ) -> ValidationResult[Dict[Str, Any]
        
    # INHERITED METHODS:
    None
    """
    @classmethod
    @LoggingLevelRouter.monitor
    def validate(
            cls,
            cipher: Command,
            candidate: Any,
            identity_service: IdentityService = IdentityService(),
    ) -> ValidationResult[Dict[str, Any]]:
        """
         # ACTION:
             1. If the candidate fails either
                    *   existence
                    *   type.
                Send an exception chain the ValidationResult. Else cast to Dict, arguments.
            2.  If the arguments.length != cipher.parameters.length, send an exception chain the
                ValidationResult.
            3.  Iterate through the arguments and if a entry fails either tests
                    *   The is not a str inside cipher.keys().
                    *   arguments[name].type != cipher[name]
                Send an exception chain the ValidationResult.
            4.  The tests have been passed, return the success result.
         # PARAMETERS:
             *  cipher (Command)
             *  candidate (Any)
             *  identity_service (IdentityService)
         # RETURNS:
             *   ValidationResult[Dict[Str, Any]] containing either:
                     - On failure: Exception.
                     - On success: Dict[Str, Any] in the payload.
         # RAISES:
             *   ArgumentCountException
             *   ArgumentNameException
             *   ArgumentTypeException
             *   ArgumentValidationException
         """
        method = "ArgumentsValidator.validate"
        
        # Handle the nonexistence case.
        if candidate is None:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                ArgumentsValidationException(
                    mthd=method,
                    op=ArgumentsValidationException.OP,
                    msg=ArgumentsValidationException.MSG,
                    err_code=ArgumentsValidationException.ERR_CODE,
                    rslt_type=ArgumentsValidationException.RSLT_TYPE,
                    ex=NullArgumentsException(
                        err_code=NullArgumentsException.ERR_CODE,
                        msg=NullArgumentsException.MSG,
                    )
                )
            )
        # Handle the wrong class case.
        if not isinstance(candidate, Dict):
            # Return the exception chain on failure.
            return ValidationResult.failure(
                ArgumentsValidationException(
                    mthd=method,
                    op=ArgumentsValidationException.OP,
                    msg=ArgumentsValidationException.MSG,
                    err_code=ArgumentsValidationException.ERR_CODE,
                    rslt_type=ArgumentsValidationException.RSLT_TYPE,
                    ex=TypeError(
                            f"{method}: Expected Dict, got {type(candidate).__name__} instead."
                        )
                )
            )
        # --- Cast candidate to a Dict additional tests. ---#
        arguments = cast(Dict, candidate)

        # Handle the case that, arguments has the wrong number of arguments.
        if len(arguments) != len(cipher.parameters):
            # Return the exception chain on failure.
            return ValidationResult.failure(
                ArgumentsValidationException(
                    mthd=method,
                    op=ArgumentsValidationException.OP,
                    msg=ArgumentsValidationException.MSG,
                    err_code=ArgumentsValidationException.ERR_CODE,
                    rslt_type=ArgumentsValidationException.RSLT_TYPE,
                    ex=ArgumentCountException(
                        err_code=ArgumentCountException.ERR_CODE,
                        msg=ArgumentCountException.MSG,
                        val=len(arguments),
                    )
                )
            )
        # --- Iterated through the dictionary to verify the argument names. ---#
        
        for name in arguments.keys():
            # Handle the case that, the key is not a safe string.
            name_validation_result = identity_service.validate_name(name)
            if name_validation_result.is_failure:
                # Return the exception chain on failure.
                return ValidationResult.failure(
                    ArgumentsValidationException(
                        mthd=method,
                        op=ArgumentsValidationException.OP,
                        msg=ArgumentsValidationException.MSG,
                        err_code=ArgumentsValidationException.ERR_CODE,
                        rslt_type=ArgumentsValidationException.RSLT_TYPE,
                        ex=name_validation_result.exception,
                    )
            )
            # Handle the case that, the name isn't among the parameters.
            if name.upper() not in [param.upper() for param in cipher.parameters]:
                # Return the exception chain on failure.
                return ValidationResult.failure(
                    ArgumentsValidationException(
                        mthd=method,
                        op=ArgumentsValidationException.OP,
                        msg=ArgumentsValidationException.MSG,
                        err_code=ArgumentsValidationException.ERR_CODE,
                        rslt_type=ArgumentsValidationException.RSLT_TYPE,
                        ex=ArgumentNameException(
                            err_code=ArgumentNameException.ERR_CODE,
                            msg=f"Unknown argument:  {name}",
                            var=f"{name}",
                            val=name,
                        )
                    )
                )
            # --- Iterated through the dictionary to verify the argument names. ---#
        
            for name in arguments.keys():
                # Handle the case that an argument's type is wrong.
                if not isinstance(arguments[name], type(cipher.parameters[name])):
                    # Return the exception chain on failure.
                    correct_type = type(cipher.parameters[name]).__name__
                    wrong_type = type(arguments[name]).__name__
                    
                    return ValidationResult.failure(
                        ArgumentsValidationException(
                            op=ArgumentsValidationException.OP,
                            msg=ArgumentsValidationException.MSG,
                            err_code=ArgumentsValidationException.ERR_CODE,
                            rslt_type=ArgumentsValidationException.RSLT_TYPE,
                            ex=ArgumentTypeException(
                                err_code=ArgumentTypeException.ERR_CODE,
                                msg=f"Expected {correct_type} for {name}. Got {wrong_type} instead.",
                                var=f"{name}",
                                val=name,
                            )
                        )
                    )
        # --- The Arguments are correct, send the success result. ---#
        return ValidationResult.success(arguments)