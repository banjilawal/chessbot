# src/command/token/service/promote.py

"""
Module: command.token.service.promote
Author: Banji Lawal
Created: 2026-03-31
"""

from __future__ import annotations
from typing import Any, Dict

from logic.rank import Rank
from logic.system import IdFactory
from command.token.root import TokenCommand
from model.token import PawnToken, TokenService


class PromotePawnCommand(TokenCommand):
    COMMAND_NAME = "promote_pawn"
    
    def __init__(
            self,
            server: TokenService,
            parameters: Dict[str, Any],
            name: str = COMMAND_NAME,
            id: int = IdFactory.next_id(class_name="PromotePawnCommand"),
    ):
        super().__init__(id=id, name=name, server=server, parameters=parameters)
    
    @classmethod
    def cipher(cls,) -> Dict[str, Any]:
        return {
            "pawn_token": PawnToken,
            "rank": Rank
        }