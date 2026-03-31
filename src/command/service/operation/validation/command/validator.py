# src/command/root/service/operation/validation/command/validator.py

"""
Module: command.root.service.operation.validation.command.validator
Author: Banji Lawal
Created: 2026-02-24
"""

from __future__ import annotations

from typing import Any, cast

from command import (
    Command, CommandArgsValidator, CommandNotFoundException, CommandTable, CommandValidationException,
    NullCommandException
)
from command.service import CommandNameNotFoundException, CommandTypeSupportException
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
        # --- Cast candidate to the key's type for additional tests. ---#
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
        # Handle the case that, command has an incorrect name.
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
        # --- Command identity and type checks are passed. conduct param tests. ---#
        # Handle the case that, command's arguments are incorrect. does not match the cipher's\
        args_validation_result = args_validator.validate(command.name, cipher, identity_service)
        if args_validation_result.is_failure:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                CommandValidationException(
                    mthd=method,
                    op=CommandValidationException.OP,
                    msg=CommandValidationException.MSG,
                    err_code=CommandValidationException.ERR_CODE,
                    rslt_type=CommandValidationException.RSLT_TYPE,
                    ex=args_validation_result.exception
                )
            )
        # --- On certification successes send the square in the ValidationResult. ---#
        return ValidationResult.success(command)
        
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _validate_command_name(
            cls,
            name: str,
            cipher: Command,
            identity_service: IdentityService = IdentityService(),
    ) -> ValidationResult[str]:
        
        method = "CommandValidator._validate_command_name"
        
        # Handle the case that the command name is not a safe string.
        name_validation_result = identity_service.validate_name(command.name)
        if name_validation_result.is_failure:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                CommandValidationException(
                    mthd=method,
                    op=CommandValidationException.OP,
                    msg=CommandValidationException.MSG,
                    err_code=CommandValidationException.ERR_CODE,
                    rslt_type=CommandValidationException.RSLT_TYPE,
                    ex=name_validation_result.exception
                )
            )
        # Handle the case that, the command's name is wrong.
        if name.upper() != cipher.name.upper():
            # Return the exception chain on failure.
            return ValidationResult.failure(
                CommandValidationException(
                    mthd=method,
                    op=CommandValidationException.OP,
                    msg=CommandValidationException.MSG,
                    err_code=CommandValidationException.ERR_CODE,
                    rslt_type=CommandValidationException.RSLT_TYPE,
                    ex=CommandNameException(
                        err_code=CommandNameException.ERR_CODE,
                        msg=f"unknown command: {name}",
                        var=name,
                        val=f"{name}",
                    )
                )
            )
        # --- Return the verified command name to the caller. ---#
        return ValidationResult.success(name)
 

    
    