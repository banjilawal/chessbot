# src/command/system/service/operation/validation/command/validator.py

"""
Module: command.system.service.operation.validation.command.validator
Author: Banji Lawal
Created: 2026-02-24
"""

from __future__ import annotations

from typing import Any, cast

from command import (
    Command, CommandArgsValidator, CommandNameNotFoundException, CommandTable, CommandTypeSupportException,
    CommandValidationException, NullCommandException
)
from logic.system import IdentityService, LoggingLevelRouter, ValidationResult, Validator


class CommandValidator(Validator[Command]):
    
    @classmethod
    @LoggingLevelRouter.monitor
    def validate(
            cls,
            candidate: Any,
            ciphers: CommandTable,
            identity_service: IdentityService = IdentityService(),
            args_validator: CommandArgsValidator = CommandArgsValidator(),
    ) -> ValidationResult[Command]:
        """
        Verifies a Command is safe to use.
        Action:
            1.  Send an exception chain in the ValidationResult if any
                of the following occur:
                    -   The rank is null or the wrong type.
                    -   Its rank's parameters fail a test.
            2.  Otherwise, send the success result.
        Args:
            candidate: Any
            ciphers: CommandTable
            identity_service: IdentityService
            args_validator: CommandArgsValidator
        Returns:
            ValidationResult[Command]
        Raises:
            TypeError
            CommandValidationException
            CommandTypeSupportException
            CommandNameNotFoundException
        """
        method = f"{cls.__name__}.validate"
        
        # Handle the nonexistence case.
        if candidate is None:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                CommandValidationException(
                    mthd=method,
                    title=cls.__name__,
                    op=CommandValidationException.OP,
                    msg=CommandValidationException.MSG,
                    err_code=CommandValidationException.ERR_CODE,
                    rslt_type=CommandValidationException.RSLT_TYPE,
                    ex=NullCommandException(
                        err_code=NullCommandException.ERR_CODE,
                        msg=NullCommandException.MSG,
                    )
                )
            )
        # Handle the wrong class case.
        if not isinstance(candidate, Command):
            # Return the exception chain on failure.
            return ValidationResult.failure(
                CommandValidationException(
                    mthd=method,
                    op=CommandValidationException.OP,
                    msg=CommandValidationException.MSG,
                    err_code=CommandValidationException.ERR_CODE,
                    rslt_type=CommandValidationException.RSLT_TYPE,
                    ex=TypeError(
                        f"Expected Command type, got "
                        f"{type(candidate).__name__} instead."
                    )
                )
            )
        # --- Cast rank to the key's type for additional tests. ---#
        command = cast(Command, candidate)
        
        # Handle the case that, the command's type is not in the cipher_table.
        if not isinstance(command, ciphers.command_types):
            # Return the exception chain on failure.
            return ValidationResult.failure(
                CommandValidationException(
                    mthd=method,
                    op=CommandValidationException.OP,
                    msg=CommandValidationException.MSG,
                    err_code=CommandValidationException.ERR_CODE,
                    rslt_type=CommandValidationException.RSLT_TYPE,
                    ex=CommandTypeSupportException(
                        var=command.name,
                        val=command,
                        msg=CommandTypeSupportException.MSG,
                        err_code=CommandTypeSupportException.ERR_CODE,
                    )
                )
            )
        # Handle the case that, the command identity is not safe.
        identity_validation_result = identity_service.validate_identity(
            id_candidate=command.id,
            name_candidate=command.name,
        )
        if identity_validation_result.is_failure:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                CommandValidationException(
                    mthd=method,
                    op=CommandValidationException.OP,
                    msg=CommandValidationException.MSG,
                    err_code=CommandValidationException.ERR_CODE,
                    rslt_type=CommandValidationException.RSLT_TYPE,
                    ex=identity_validation_result.exception
                )
            )
        # Handle the case that, command has an incorrect schema.
        if command.name not in ciphers.command_names:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                CommandValidationException(
                    mthd=method,
                    op=CommandValidationException.OP,
                    msg=CommandValidationException.MSG,
                    err_code=CommandValidationException.ERR_CODE,
                    rslt_type=CommandValidationException.RSLT_TYPE,
                    ex=CommandNameNotFoundException(
                        var=command.name,
                        val=command,
                        msg=CommandNameNotFoundException.MSG,
                        err_code=CommandNameNotFoundException.ERR_CODE,
                    )
                )
            )
        # Handle the case that, the command's arguments are not correct.
        arguments_validation_results = args_validator.validate(
            command=command,
            signature=ciphers.entries[command],
        )
        if arguments_validation_results.is_failure:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                CommandValidationException(
                    mthd=method,
                    op=CommandValidationException.OP,
                    msg=CommandValidationException.MSG,
                    err_code=CommandValidationException.ERR_CODE,
                    rslt_type=CommandValidationException.RSLT_TYPE,
                    ex=arguments_validation_results.exception
                )
            )
        # --- Forward the work product. ---#
        return ValidationResult.success(command)
 

    
    