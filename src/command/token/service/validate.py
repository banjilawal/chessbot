# src/command/token/service/deploy.py

"""
Module: command.token.service.deploy
Author: Banji Lawal
Created: 2026-03-31
"""

from __future__ import annotations

from typing import Any, Dict

from system import IdFactory
from command.token.root import TokenCommand


class ValidateTokenCommand(TokenCommand):
    NAME = "validate_token"
    
    def __init__(
            self,
            candidate: Any,
            name: str = NAME,
            parameters: Dict[str, Any] = None,
            id: int = IdFactory.next_id(class_name="ValidateTokenCommand"),
    ):
        super().__init__(id=id, name=name, server=server, parameters=parameters)
    
    @classmethod
    def cipher(cls,) -> Dict[str, Any]:
        return {"rank": Any}