# src/blueprint/model/token/blueprint.py

"""
Module: blueprint.model.token.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from dataclasses import dataclass
from tabnanny import process_tokens
from typing import Optional, Type, cast

from blueprint import ModelBlueprint
from model import HomeSquare, Rank, Team, Token
from schema import Formation


class TokenBlueprint(ModelBlueprint[Token]):
    """
    Role:
        -   Container
        -   DTO
        
    Responsibilities:
        1.  Provides values for instantiating a Token object.
        2.  DTO
        
    Attributes:
        team: Team,
        formation: Formation
        rank: Optional[Rank]
        home_square: Optional[HomeSquare]
        model_class: Type[Token]
        
    Provides:

     Super Class:
        ModelBlueprint
     """
    
    def __init__(
            self,
            team: Team,
            formation: Formation,
            id: Optional[int] | None = None,
            rank: Optional[Rank] | None = None,
            home_square: Optional[HomeSquare] | None = None,
            model_class: Type[Token] = Token,
    ):
        """
        Args:
            team: Team,
            formation: Formation
            id: Optional[int]
            rank: Optional[Rank]
            home_square: Optional[HomeSquare]
            model_class: Type[Token] = Type[Token]
        """
        super().__init__(model_class=model_class, id=id)
        self._team = team
        self._rank = rank
        self._formation = formation
        self._home_square = home_square
        
    @property
    def model_class(self) -> Type[Token]:
        return cast(Type[Token], self.model_class)
    
    @property
    def team(self) -> Team:
        return self._team
    
    @property
    def formation(self) -> Formation:
        return self._formation
    
    @property
    def rank(self) -> Optional[Rank]:
        return self._rank
    
    @property
    def home_square(self) -> Optional[HomeSquare]:
        return self._home_square
    
    

        
        