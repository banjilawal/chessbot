# src/command/command/command/build/validator/validator.py

"""
Module: command.command.command.build.validator.validator
Author: Banji Lawal
Created: 2026-02-24
"""

from __future__ import annotations

from typing import Any, Dict, cast

from logic.system import (
    Command, IdentityService, Validator
)


class CommandValidator(Validator[Command]):
    
    @classmethod
    @LoggingLevelRouter.monitor
    def validate(
            cls,
            candidate: Any,
            cipher: Command = Command.cipher(),
            identity_service: IdentityService = IdentityService(),
            command_validator: CommandValidator = CommandValidator(),
            arguments_validator: ArgumentsValidator = ArgumentsValidator(),
    ) -> ValidationResult[Command]:
        method = "CommandValidator.validate"
        
        # Handle the nonexistence case.
        if candidate is None:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                CommandValidationException(
                    mthd=method,
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
        if not isinstance(candidate, type(key)):
            # Return the exception chain on failure.
            return ValidationResult.failure(
                CommandValidationException(
                    mthd=method,
                    op=CommandValidationException.OP,
                    msg=CommandValidationException.MSG,
                    err_code=CommandValidationException.ERR_CODE,
                    rslt_type=CommandValidationException.RSLT_TYPE,
                    ex=TypeError(
                        f"{method}: Expected {type(key).__name__}, got "
                        f"{type(candidate).__name__} instead."
                    )
                )
            )
        # --- Cast candidate to the key's type for additional tests. ---#
        command = cast(type(cipher), candidate)
        
        # Handle the case that, command's name does not match the cipher's\
        command_name_validation_result = cls._validate_command_name(command.name, cipher, identity_service)
        if command_name_validation_result.is_failure:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                CommandValidationException(
                    mthd=method,
                    op=CommandValidationException.OP,
                    msg=CommandValidationException.MSG,
                    err_code=CommandValidationException.ERR_CODE,
                    rslt_type=CommandValidationException.RSLT_TYPE,
                    ex=command_name_validation_result.exception
                )
            )
        # Handle the case that, command's arguments are incorrect. does not match the cipher's\
        arguments_validation_result = arguments_validator.validate(command.name, cipher, identity_service)
        if arguments_validation_result.is_failure:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                CommandValidationException(
                    mthd=method,
                    op=CommandValidationException.OP,
                    msg=CommandValidationException.MSG,
                    err_code=CommandValidationException.ERR_CODE,
                    rslt_type=CommandValidationException.RSLT_TYPE,
                    ex=arguments_validation_result.exception
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
 

    
    