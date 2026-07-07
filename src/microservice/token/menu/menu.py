# src/logic/system/route/router.py

"""
Module: logic.system.route.router
Author: Banji Lawal
Created: 2026-03-30
Version: 1.0.0
"""

from __future__ import annotations


from typing import Any, cast

from command import ArgumentCountException, ArgumentTypeException, NullArgumentsException, NullCommandException
from command.token import DeployTokenCommand, PromotePawnCommand, TokenCommand, ValidateTokenCommand
from command.token.service.build import BuildTokenCommand
from system import IdentityService, LoggingLevelRouter, Router, ValidationResult
from model.state.token import TokenCommandTable, TokenService, TokenServiceMenuException
from model.state.token import TokenCommandNotFoundException


class TokenServiceMenu(Router[TokenService]):
    """
    Role
        -   Transaction Worker
        -   Routing

    Responsibilities:
        1.  Ensure data-holders are safe before they are used or saved.

    Attributes:

    Provides:
        -   route(op_name: str) -> Result

    super Class:
    """
    

    _service: TokenService
    _commands: TokenCommandTable
    
    def __init__(
            self,
            service: TokenService = TokenService(),
            commands: TokenCommandTable = TokenCommandTable(),
    ):
        self._service = service
        self._commands = commands
        
    @property
    def commands(self) -> list[TokenCommand]:
        return self._commands.entry.keys
    
    @LoggingLevelRouter.monitor
    def route(
            self,
            command: TokenCommand,
            identity_service: IdentityService = IdentityService(),
    ) -> Any:
        method = f"{self.__class__.__name__}.route"
        
        # Handle the case that, the command does not exist
        if command is None:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenServiceMenuException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenServiceMenuException.MSG,
                    err_code=TokenServiceMenuException.ERR_CODE,
                    ex=NullCommandException(
                        msg=NullCommandException.MSG,
                        err_code=NullCommandException.ERR_CODE,
                    )
                )
            )
        # Handle the case that, the command is the wrong type.
        if not isinstance(command, TokenCommand):
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenServiceMenuException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenServiceMenuException.MSG,
                    err_code=TokenServiceMenuException.ERR_CODE,
                    ex=TypeError(
                        f"Expected TokenCommand but got {type(command).__name__} instead."
                    )
                )
            )
        # --- Cast the candidate into a TokenCommand for additional tests ---#
        token_command = cast(TokenCommand, command)
        
        # Handle the case that, the command's schema or id fail a safety ccheck.
        identity_validation_result = identity_service.validate_identity(
            id_candidate=token_command.id,
            name_candidate=token_command.name,
        )
        if identity_validation_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenServiceMenuException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenServiceMenuException.MSG,
                    err_code=TokenServiceMenuException.ERR_CODE,
                    ex=identity_validation_result.exception
                )
            )
        # Handle the case that the command is not supported.
        if command not in self._commands.entry.keys:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenServiceMenuException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenServiceMenuException.MSG,
                    err_code=TokenServiceMenuException.ERR_CODE,
                    ex=TokenCommandNotFoundException(
                        var=command.name,
                        val=command,
                        msg=TokenCommandNotFoundException.MSG,
                        err_code=TokenCommandNotFoundException.ERR_CODE,
                    )
                )
            )
        # Handle the case that, its params don't exist.
        if token_command.parameters is None:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenServiceMenuException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenServiceMenuException.MSG,
                    err_code=TokenServiceMenuException.ERR_CODE,
                    ex=NullArgumentsException(
                        var=command.name,
                        val=command,
                        msg=NullArgumentsException.MSG,
                        err_code=NullArgumentsException.ERR_CODE,
                    )
                )
            )
        # Handle the case that, the parameters are the wrong type.
        if not isinstance(token_command.parameters, self._commands.entry[token_command.name]):
            # Send the exception chain on failure.
            expected_type = type(self._commands.entry[token_command.name]).__name__
            actual_type = type(token_command.parameters).__name__
            return ValidationResult.failure(
                TokenServiceMenuException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenServiceMenuException.MSG,
                    err_code=TokenServiceMenuException.ERR_CODE,
                    ex=TypeError(
                        f"Expected {expected_type} but got {actual_type} instead."
                    )
                )
            )
        cipher = self._commands.entry[token_command.name]
        
        # Handle the case that, the number of params is wrong.
        if token_command.parameters.count != cipher.parameters.count:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenServiceMenuException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenServiceMenuException.MSG,
                    err_code=TokenServiceMenuException.ERR_CODE,
                    ex=ArgumentCountException(
                        msg=ArgumentCountException.MSG,
                        err_code=ArgumentCountException.ERR_CODE,
                    )
                )
            )
        # Handle the case that, a param is the wrong type
        for key in token_command.parameters.entries.keys():
            if not isinstance(token_command.parameters.entries[key], cipher.entries[key]):
                # Send the exception chain on failure.
                return ValidationResult.failure(
                    TokenServiceMenuException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=TokenServiceMenuException.MSG,
                        err_code=TokenServiceMenuException.ERR_CODE,
                        ex=ArgumentTypeException(
                            var=key,
                            val=token_command.parameters.entries[key],
                            msg=ArgumentCountException.MSG,
                            err_code=ArgumentCountException.ERR_CODE,
                        )
                    )
                )
        # --- Checks are passed the command. Route to the TokenService's worker. ---#
        
        # Select the TokenBuild worker
        if isinstance(command, BuildTokenCommand):
            return self._service.builder.build(
                owner=command.parameters["owner"],
                formation=command.parameters["formation"],
            )
        # Select the TokenValidation worker
        if isinstance(command, ValidateTokenCommand):
            return self._service.run.build(
                rank=command.parameters["rank"]
            )
        # Select the TokenDeployment worker.
        if isinstance(command, DeployTokenCommand):
            return self._service.deploy_on_board(
                token=command.parameters["token"]
            )
        # Select the PawnPromotion worker.
        if isinstance(command, PromotePawnCommand):
            return self._service.promote_pawn(
                pawn_token=command.parameters["pawn_token"],
                rank=command.parameters["rank"],
            )
        
