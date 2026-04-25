# src/toolkit/team/toolkit.py

"""
Module: toolkit.team.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from model import Team
from operation import ValidationBootstrapper
from toolkit import Toolkit
from microvalidator import BoardValidator, IdentityValidator, PlayerValidator, SchemaValidator, BoardTeamBinderValidator


class TeamToolkit(Toolkit[Team]):
    """
    Role:
    -   Container
    
    Responsibilities:
        1.  Collection of workers and validators that are required for Board tasks.
        2.  Simplifies entry points.
        3.  No logic in the Toolkit.
    
    Attributes:
        board_validator: BoardValidator
        player_validator: PlayerValidator
        schema_validator: SchemaValidator
        identity_validator: IdentityValidator
    
    Provides:
    Super Class:
        Toolkit
    """
    _board_validator: BoardValidator
    _player_validator: PlayerValidator
    _schema_validator: SchemaValidator
    _team_binder_validator: BoardTeamBinderValidator

    def __init__(
            self,
            board_validator: BoardValidator | None = None,
            player_validator: PlayerValidator | None = None,
            schema_validator: SchemaValidator | None = None,
            team_binder_validator: BoardTeamBinderValidator | None = None,
    ):
        """
        Args:
            board_validator: BoardValidator
            player_validator: PlayerValidator
            schema_validator: SchemaValidator
        """
        super().__init__()
        self._board_validator = board_validator or BoardValidator()
        self._player_validator = player_validator or PlayerValidator()
        self._schema_validator = schema_validator or SchemaValidator()
        self._team_binder_validator = team_binder_validator or BoardTeamBinderValidator()
        
    @property
    def board_validator(self) -> BoardValidator:
        return self._board_validator
    
    @property
    def owner_validator(self) -> PlayerValidator:
        return self._player_validator
    
    @property
    def schema_validator(self) -> SchemaValidator:
        return self._schema_validator
    
    @property
    def team_binder_validator(self) -> BoardTeamBinderValidator:
        return self._team_binder_validator
