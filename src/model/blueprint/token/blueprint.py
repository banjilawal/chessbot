# src/model/blueprint/token/blueprint.py

"""
Module: model.blueprint.token.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from dataclasses import dataclass

from catalog import Formation
from model import Blueprint, Team, Token


@dataclass
class TokenBlueprint(Blueprint[Token]):
    id: int
    team: Team
    formation: Formation
