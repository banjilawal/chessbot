# src/assurance/attrribute/model/token/table.py

"""
Module: assurance.attrribute.model.token.table
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""


from __future__ import annotations

from typing import Optional

from assurance import (
    AttributeHelperTable, BoardValidator, RankValidator, SquareValidator, TeamValidator,
    PrimingValidator
)
from authorization import BlueprintIdExtractor, HomeSquareExtractor
from domain import Token
from microservice import IdentityService


class TokenHelperTable(AttributeHelperTable[Token]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Bundles validators a Token needs for its primitive and upstream relational
            partners attributes.

    Attributes:
        team_validator: TeamValidator
        rank_validator: RankValidator
        board_validator: BoardValidator
        square_validator: SquareValidator

    Provides:

    Super Class:
        AttributeHelperTable
    """
    _team_validator: TeamValidator
    _rank_validator: RankValidator
    _board_validator: BoardValidator
    _square_validator: SquareValidator
    _home_extractor: HomeSquareExtractor

    
    def __init__(
            self,
            team_validator: Optional[TeamValidator] | None = None,
            rank_validator: Optional[RankValidator] | None = None,
            board_validator: Optional[BoardValidator] | None = None,
            square_validator: Optional[SquareValidator] | None = None,
            identity_service: Optional[IdentityService] | None = None,
            priming_validator: Optional[PrimingValidator] | None = None,
            home_extractor: Optional[HomeSquareExtractor] | None = None,
            blueprint_id_extractor: Optional[BlueprintIdExtractor] | None = None,
    ):
        """
        Args:
            team_validator: Optional[TeamValidator]
            rank_validator: Optional[RankValidator]
            board_validator: Optional[BoardValidator]
            square_validator: Optional[SquareValidator]
            identity_service: Optional[IdentityService]
            priming_validator: Optional[PrimingValidator]
            home_extractor: Optional[HomeSquareExtractor]
            blueprint_id_extractor: Optional[BlueprintIdExtractor]
        """
        super().__init__(
            identity_service=identity_service,
            priming_validator=priming_validator,
            blueprint_id_extractor=blueprint_id_extractor,
        )
        self._team_validator = team_validator or TeamValidator()
        self._rank_validator = rank_validator or RankValidator()
        self._board_validator = board_validator or BoardValidator()
        self._square_validator = square_validator or SquareValidator()
        self._home_extractor = home_extractor or HomeSquareExtractor()
    
    @property
    def team_validator(self) -> TeamValidator:
        return self._team_validator
    
    @property
    def rank_validator(self) -> RankValidator:
        return self._rank_validator
    
    @property
    def board_validator(self) -> BoardValidator:
        return self._board_validator
    
    @property
    def square_validator(self) -> SquareValidator:
        return self._square_validator
    
    @property
    def home_extractor(self) -> HomeSquareExtractor:
        return self._home_extractor