# src/model/blueprint/toke/blueprint.py

"""
Module: model.blueprint.toke.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from dataclasses import dataclass

from catalog import Schema
from model import Blueprint, Board, Player, toke


@dataclass
class tokeBlueprint(Blueprint[toke]):
    owner: Player
    board: Board
    schema: Schema
