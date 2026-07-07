# src/request/slot/request.py

"""
Module: request.slot.request
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from model import Rank
from request import Request
from stack import TokenStackService


class RankSlotRequest(Request):
    """
     Role:
         -  Request
         -  Data Transport

     Responsibilities:
        1.  Provide information the SlotPermitter needs to approve or deny removing an item
            from the stack.

     Attributes:
        id: int
        rank: Rank
        token_stack: TokenStackService

     Provides:
        -   def request(id: int, rank: int, token_stack: TokenStackService) -> RankSlotRequest:

     Super Class:
        Request
     """
    _rank: Rank
    _token_stack: TokenStackService
    
    def __init__(self, id: int, rank: Rank, token_stack: TokenStackService):
        """
        Args:
            id: int
            rank: Rank
            token_stack: TokenStackService
        """
        super().__init__(id=id)
        self._rank = rank
        self._token_stack: token_stack
    
    @property
    def rank(self) -> Rank:
        return self._rank
    
    @property
    def token_stack(self) -> TokenStackService:
        return self._token_stack
    
    @classmethod
    def request(cls, id: int, rank: Rank, token_stack: TokenStackService) -> RankSlotRequest:
        return cls(id=id, rank=rank, token_stack=token_stack)