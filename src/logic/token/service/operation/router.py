# src/logic/system/route/router.py

"""
Module: logic.system.route.router
Author: Banji Lawal
Created: 2026-03-30
Version: 1.0.0
"""

from __future__ import annotations

from typing import Any, Dict

from command.token.deploy import DeployTokenCommand
from command.token.root import TokenCommand
from logic.system import LoggingLevelRouter, Router
from logic.token import Token, TokenOpsController, TokenService


class TokenOpsRouter(Router[str]):
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
    _controller: TokenOpsController
    
    def __init__(
            self,
            service: TokenService,
            controller: TokenOpsController = TokenOpsController(),
    ):
        self._service = service
        self._controller = controller
    
    @property
    def ops(self) -> TokenOpsController:
        return self._controller
    
    @LoggingLevelRouter.monitor
    def route(self, command: TokenCommand) -> Any:
        if command.name.upper() == "build".upper():
            return self._service.builder
        if command.name.upper() == "validate".upper():
            return self._service.validator
        if isinstance(command, DeployTokenCommand):
            cipher = Dict[str, Token]
            
            return self._service.deploy_on_board(token=command.parameters["token"])
        if command.name.upper() == "promote".upper():
            return self._controller.pawn_promoter
        
