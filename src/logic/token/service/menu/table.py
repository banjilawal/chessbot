# src/logic/system/route/router.py

"""
Module: logic.system.route.router
Author: Banji Lawal
Created: 2026-03-30
Version: 1.0.0
"""

from __future__ import annotations

from typing import Any, Dict

from logic.team import Team
from logic.token import PawnToken, Token
from logic.formation import Formation
from command.system.adt import CommandArgs, CommandTable
from command.token import (
    BuildTokenCommand, DeployTokenCommand, PromotePawnCommand, TokenCommand, ValidateTokenCommand
)


class TokenCommandTable(CommandTable):
    COMMAND_TABLE: Dict[TokenCommand, CommandArgs] = {
        BuildTokenCommand: CommandArgs({"owner": Team, "formation": Formation}),
        PromotePawnCommand: CommandArgs({"pawn_token": PawnToken}),
        ValidateTokenCommand: CommandArgs({"rank": Any}),
        DeployTokenCommand: CommandArgs({"token": Token}),
    }
    
    def __init__(self):
        super().__init__()
        super.table = self.COMMAND_TABLE
    