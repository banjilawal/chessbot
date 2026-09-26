# src/assurance/attrribute/model/token/table.py

"""
Module: assurance.attrribute.model.token.table
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""


from __future__ import annotations

from typing import Optional

from assurance import ModelHelperTable
from authorization import BlueprintIdExtractor, HomeSquareExtractor
from client import (
    BoardValidationResponseService, RankValidationResponseService, SquareValidationResponseService,
    TeamValidationResponseService
)
from domain import Token
from microservice import IdentityService


class TokenHelperTable(ModelHelperTable[Token]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Bundles validatorClients a Token needs for its primitive and upstream relational
            partners attributes.

    Attributes:
        team_client: TeamValidatorClient
        rank_client: RankValidatorClient
        board_client: BoardValidatorClient
        square_client: SquareValidatorClient

    Provides:

    Super Class:
        ModelHelperTable
    """
    _team_client: TeamValidationResponseService
    _rank_client: RankValidationResponseService
    _board_client: BoardValidationResponseService
    _square_client: SquareValidationResponseService
    _home_extractor: HomeSquareExtractor

    
    def __init__(
            self,
            team_client: Optional[TeamValidationResponseService] | None = None,
            rank_client: Optional[RankValidationResponseService] | None = None,
            board_client: Optional[BoardValidationResponseService] | None = None,
            square_client: Optional[SquareValidationResponseService] | None = None,
            identity_service: Optional[IdentityService] | None = None,
            priming_validator: Optional[PrimingValidator] | None = None,
            home_extractor: Optional[HomeSquareExtractor] | None = None,
            blueprint_id_extractor: Optional[BlueprintIdExtractor] | None = None,
    ):
        """
        Args:
            team_client: Optional[TeamValidatorClient]
            rank_client: Optional[RankValidatorClient]
            board_client: Optional[BoardValidatorClient]
            square_client: Optional[SquareValidatorClient]
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
        self._team_client = team_client or TeamValidationResponseService()
        self._rank_client = rank_client or RankValidationResponseService()
        self._board_client = board_client or BoardValidationResponseService()
        self._square_client = square_client or SquareValidationResponseService()
        self._home_extractor = home_extractor or HomeSquareExtractor()
    
    @property
    def team_client(self) -> TeamValidationResponseService:
        return self._team_client
    
    @property
    def rank_client(self) -> RankValidationResponseService:
        return self._rank_client
    
    @property
    def board_client(self) -> BoardValidationResponseService:
        return self._board_client
    
    @property
    def square_client(self) -> SquareValidationResponseService:
        return self._square_client
    
    @property
    def home_extractor(self) -> HomeSquareExtractor:
        return self._home_extractor