# src/command/token/service/promote.py

"""
Module: command.token.service.promote
Author: Banji Lawal
Created: 2026-03-31
"""

from __future__ import annotations
from typing import Any, Dict

from command import CommandArgs
from logic.formation import Formation

from logic.system import IdFactory
from command.token.root import TokenCommand
from logic.team import Team
from logic.token import TokenService


class BuildTokenCommandArgs(CommandArgs):
    
    def __init__(self):
        super().__init__()
        self.args["owner"] = Team
        self.args["formation"] = Formation

class BuildTokenCommand(TokenCommand):
    COMMAND_NAME = "build_token"
    
    def __init__(
            self,
            server: TokenService,
            name: str = COMMAND_NAME,
            parameters: Dict[str, Any] = None,
            id: int = IdFactory.next_id(class_name="BuildTokenCommand"),
    ):
        super().__init__(id=id, name=name, server=server, parameters=parameters)
    
    @classmethod
    def cipher(cls,) -> Dict[str, Any]:
        return {
            "owner": Team,
            "formation": Formation
        }