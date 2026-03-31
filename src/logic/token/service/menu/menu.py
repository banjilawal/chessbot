# src/logic/system/route/router.py

"""
Module: logic.system.route.router
Author: Banji Lawal
Created: 2026-03-30
Version: 1.0.0
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict

from command.token import DeployTokenCommand, PromotePawnCommand, TokenCommand, ValidateTokenCommand
from command.token.service.build import BuildTokenCommand
from logic.formation import Formation
from logic.system import LoggingLevelRouter, Router
from logic.team import Team
from logic.token import PawnToken, Token, TokenService


    

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
    
    COMMAND_TABLE: Dict[TokenCommand, CommandArgs]= {
        BuildTokenCommand: {"owner": Team, "formation": Formation},
        PromotePawnCommand: {"pawn_token": PawnToken},
        ValidateTokenCommand: {"candidate": Any},
        DeployTokenCommand: {"token": Token},
    }
    _service: TokenService
    _commands: list[TokenCommand]
    
    def __init__(
            self,
            service: TokenService = TokenService(),
            commands: list[TokenCommand] = SERVICE_COMMANDS,
    ):
        self._service = service
        self._commands = commands
        
    @property
    def commands(self) -> list[TokenCommand]:
        return self._commands
    
    @LoggingLevelRouter.monitor
    def route(
            self,
            command: TokenCommand,
            command_validator: TokenServiceCommandValidator = TokenServiceCommandValidator(),
    ) -> Any:
        
        if isinstance(command, BuildTokenCommand):
            return self._service.builder.build(
                owner=command.parameters["owner"],
                formation=command.parameters["formation"],
            )
        if isinstance(command, ValidateTokenCommand):
            return self._service.validator.validate(candidate=command.parameters["candidate"])
        if isinstance(command, DeployTokenCommand):
            return self._service.deploy_on_board(token=command.parameters["token"])
        if isinstance(command, PromotePawnCommand):
            return self._service.promote_pawn(
                pawn_token=command.parameters["pawn_token"],
                rank=command.parameters["rank"],
            )
        
