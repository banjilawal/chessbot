# src/command/token/service/deploy.py

"""
Module: command.token.service.deploy
Author: Banji Lawal
Created: 2026-03-31
"""

from __future__ import annotations

from typing import Dict

from system import IdFactory
from command.token.root import TokenCommand
from model.token import Token, TokenService


class DeployTokenCommand(TokenCommand):
    NAME = "deploy_token"
    
    def __init__(
            self,
            server: TokenService,
            name: str = NAME,
            parameters: Dict[str, Token] = None,
            id: int = IdFactory.next_id(class_name="DeployTokenCommand"),
    ):
        super().__init__(id=id, name=name, server=server, parameters=parameters)
    
    @classmethod
    def cipher(cls,) -> Dict[str, Token]:
        return {"token": Token}