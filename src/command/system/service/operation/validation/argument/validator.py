# src/command/system/service/operation/validation/argument/validator.py

"""
Module: command.system.service.operation.validation.argument.validator
Author: Banji Lawal
Created: 2026-02-24
"""

from __future__ import annotations

from typing import Dict, cast

from command import (
    ArgumentCountException, ArgumentNameException, ArgumentTypeException, ArgumentsValidationException,
    Command, CommandArgs, NullArgumentsException
)
from command.system.service import ArgumentNameTypeBindingException
from system import IdentityService, LoggingLevelRouter, ValidationResult, Validator

class CommandArgsValidator(Validator[Dict]):
    """
    Role:Validation, Data Integrity Guarantor, Security.
    
    Responsibilities:
    1.  Ensure a Argument has.
    *   The correct number of arguments.
    *   The arguments have the correct names.
    *   The correct types.
    
    Super Class:
    *   Validator
    
    Provides:
    
    
    # INHERITED ATTRIBUTES:
    None
    
    Attributes:
    None
    
    # LOCAL METHODS:
        *   validate(
                    cipher: Command,
                    rank: Any,
                    identity_service: IdentityService = IdentityService(),
            ) -> ValidationResult[Dict[Str, Any]
        
    # INHERITED METHODS:
    None
    """
    @classmethod
    @LoggingLevelRouter.monitor
    def validate(
            cls,
            command: Command,
            signature: CommandArgs,
            identity_service: IdentityService = IdentityService(),
    ) -> ValidationResult[CommandArgs]:
        """
        Verifies a command's arguments match the method's parameter list
        
        Action:
            1.  Send an exception chain in the ValidationResult if either of
                the following occur,
                    -   The command's parameters fail a type check.
                    -   The ccommand's identifier fails a schema check.
            2.  Otherwise, send the success result.
        Args:
            command: Command
            signature: CommandArgs
            identity_service: IdentityService
        Returns:
            ValidationResult[CommandArgs]
        Raises:
            ArgumentsValidationException
        """
        method = f"{cls.__name__}.validate"
        

        # Handle the case that, the rank does not pass type of count checks
        type_validation_results = cls._run_type_checks(
            signature=signature,
            candidate=command.parameters,
        )
        if type_validation_results.is_failure:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                ArgumentsValidationException(
                    cls_mthd=method,
                    op=ArgumentsValidationException.OP,
                    msg=ArgumentsValidationException.MSG,
                    err_code=ArgumentsValidationException.ERR_CODE,
                    mthd_rslt=ArgumentsValidationException.MTHD_RSLT,
                    ex=type_validation_results.exception
                )
            )
        # Handle the case that, an identifier, or the identifier-type binding checks fail.
        identifier_validation_results = cls._run_identifier_checks(
            signature=signature,
            candidate=type_validation_results.payload,
            identity_service=identity_service,
        )
        if not identifier_validation_results.is_failure:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                ArgumentsValidationException(
                    cls_mthd=method,
                    op=ArgumentsValidationException.OP,
                    msg=ArgumentsValidationException.MSG,
                    err_code=ArgumentsValidationException.ERR_CODE,
                    mthd_rslt=ArgumentsValidationException.MTHD_RSLT,
                    ex=identifier_validation_results.exception
                )
            )
        # --- Return the work product. ---#
        return ValidationResult.success(
            payload=identifier_validation_results.payload
        )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _run_type_checks(
            cls,
            candidate: CommandArgs,
            signature: CommandArgs,
    ) -> ValidationResult[CommandArgs]:
        """
        Verifies a command's arguments types match the types in the signature.

        Action:
            1.  Send an exception chain in the ValidationResult if any of t
                the following occurs:
                    -   The rank is null.
                    -   The rank's type is not the signature's.
                    -   The rank has the wrong number of arguments.
                    -   One of the rank's types is not in the signature
            2.  Otherwise, send the success result.
        Args:
            candidate: CommandArgs
            signature: CommandArgs
        Returns:
            ValidationResult[CommandArgs]
        Raises:
            TypeError
            ArgumentTypeException
            NullArgumentsException
            ArgumentCountException
            ArgumentsValidationException
        """
        method = f"{cls.__name__}._run_type_checks"
        
        # Handle the nonexistence case.
        if candidate is None:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                ArgumentsValidationException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    op=ArgumentsValidationException.OP,
                    msg=ArgumentsValidationException.MSG,
                    err_code=ArgumentsValidationException.ERR_CODE,
                    mthd_rslt=ArgumentsValidationException.MTHD_RSLT,
                    ex=NullArgumentsException(
                        msg=ArgumentsValidationException.MSG,
                        err_code=NullArgumentsException.ERR_CODE,
                    )
                )
            )
        # Handle the wrong class case.
        if not isinstance(candidate, type(signature)):
            # Return the exception chain on failure.
            signature_type = type(signature).__name__
            actual_type = type(candidate).__name__
            return ValidationResult.failure(
                ArgumentsValidationException(
                    cls_mthd=method,
                    op=ArgumentsValidationException.OP,
                    msg=ArgumentsValidationException.MSG,
                    err_code=ArgumentsValidationException.ERR_CODE,
                    mthd_rslt=ArgumentsValidationException.MTHD_RSLT,
                    ex=TypeError(
                        f"Expected {signature_type}, got {actual_type}."
                    )
                )
            )
        # --- Cast rank to the signature's type for additional tests. ---#
        args = cast(type(signature), candidate)
        
        # Handle the case that, the number of arguments is wrong.
        if args.count != signature.count:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                ArgumentsValidationException(
                    cls_mthd=method,
                    op=ArgumentsValidationException.OP,
                    msg=ArgumentsValidationException.MSG,
                    err_code=ArgumentsValidationException.ERR_CODE,
                    mthd_rslt=ArgumentsValidationException.MTHD_RSLT,
                    ex=ArgumentCountException(
                        msg=ArgumentCountException.MSG,
                        err_code=ArgumentCountException.ERR_CODE,
                    )
                )
            )
        # Handle the case that, an argument is the wrong type.
        for genus in args.types:
            if not isinstance(genus, signature.types):
                # Return the exception chain on failure.
                return ValidationResult.failure(
                    ArgumentsValidationException(
                        cls_mthd=method,
                        op=ArgumentsValidationException.OP,
                        msg=ArgumentsValidationException.MSG,
                        err_code=ArgumentsValidationException.ERR_CODE,
                        mthd_rslt=ArgumentsValidationException.MTHD_RSLT,
                        ex=ArgumentTypeException(
                            var=genus.__name__,
                            msg=ArgumentTypeException.MSG,
                            err_code=ArgumentTypeException.ERR_CODE,
                        )
                    )
                )
        # --- Argument type tests passed. Return the work product. ---#
        return ValidationResult.success(args)
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _run_identifier_checks(
            cls,
            candidate: CommandArgs,
            signature: CommandArgs,
            identity_service: IdentityService,
    ) -> ValidationResult[CommandArgs]:
        """
        Verifies a command's arguments match the method's parameter list

        Action:
            1.  Send an exception chain in the ValidationResult if any of
                the following occurs:
                    -   An identifier fails a safety check.
                    -   A identifier's type does not match what's in the
                        signature.
            2.  Otherwise, send the success result.
        Args:
            rank CommandArgs
            signature: CommandArgs
            identity_service: IdentityService
        Returns:
            ValidationResult[CommandArgs]
        Raises:
            ArgumentNameException
            ArgumentsValidationException
            ArgumentNameTypeBindingException
        """
        method = f"{cls.__name__}._run_identifier_checks"
        
        # Handle the case that identifier is not a valid string,
        for key in candidate.entries.keys():
            str_validation_result = identity_service.validate_name(
                candidate=key,
            )
            if str_validation_result.is_failure:
                # Return the exception chain on failure.
                return ValidationResult.failure(
                    ArgumentsValidationException(
                        cls_mthd=method,
                        op=ArgumentsValidationException.OP,
                        msg=ArgumentsValidationException.MSG,
                        err_code=ArgumentsValidationException.ERR_CODE,
                        mthd_rslt=ArgumentsValidationException.MTHD_RSLT,
                        ex=str_validation_result.exception,
                    )
                )
        # Handle the case that, an identifier is not in the signature.
        for identifier in candidate.identifiers:
            if identifier.upper() not in signature.identifiers:
                # Return the exception chain on failure.
                return ValidationResult.failure(
                    ArgumentsValidationException(
                        cls_mthd=method,
                        op=ArgumentsValidationException.OP,
                        msg=ArgumentsValidationException.MSG,
                        err_code=ArgumentsValidationException.ERR_CODE,
                        mthd_rslt=ArgumentsValidationException.MTHD_RSLT,
                        ex=ArgumentNameException(
                            var=identifier,
                            msg=ArgumentNameException.MSG,
                            err_code=ArgumentNameException.ERR_CODE,
                        )
                    )
                )
            # Handle the case that, of an incorrect identifier-type binding.
            for key in candidate.entries.keys():
                if not isinstance(candidate.entries[key], signature.entries[key]):
                    # Return the exception chain on failure.
                    return ValidationResult.failure(
                        ArgumentsValidationException(
                            cls_mthd=method,
                            op=ArgumentsValidationException.OP,
                            msg=ArgumentsValidationException.MSG,
                            err_code=ArgumentsValidationException.ERR_CODE,
                            mthd_rslt=ArgumentsValidationException.MTHD_RSLT,
                            ex=ArgumentNameTypeBindingException(
                                var=key,
                                val=f"expected type: {type(signature.entries[key]).__name__}",
                                msg=ArgumentNameTypeBindingException.MSG,
                                err_code=ArgumentNameTypeBindingException.ERR_CODE,
                            )
                        )
                    )
        # --- Argument identifier tests passed. Return the work product. ---#
        return ValidationResult.success(candidate)