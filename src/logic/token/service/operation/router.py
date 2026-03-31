# src/logic/system/route/router.py

"""
Module: logic.system.route.router
Author: Banji Lawal
Created: 2026-03-30
Version: 1.0.0
"""

from __future__ import annotations

from typing import Any

from command.token import DeployTokenCommand, PromotePawnCommand, TokenCommand, ValidateTokenCommand
from command.token.service.build import BuildTokenCommand
from logic.system import LoggingLevelRouter, Router
from logic.token import TokenOpsController, TokenService


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
        
