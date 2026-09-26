# src/assurance/attrribute/model/coord/table.py

"""
Module: assurance.attrribute.model.coord.table
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""


from __future__ import annotations

from typing import Optional

from assurance import ModelHelperTable, NumberValidator, PrimingValidator
from client import BoardValidatorClient
from domain import Coord

class CoordHelperTable(ModelHelperTable[Coord]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Bundles validatorClients an Coord needs for its primitive and upstream relational
            partners attributes.

    Attributes:
        board_client: BoardValidatorClient

    Provides:

    Super Class:
        ModelHelperTable
    """
    _board_client: BoardValidatorClient
    
    def __init__(
            self,
            board_client: Optional[BoardValidatorClient] | None = None,
            number_validator: Optional[NumberValidator] | None = None,
            priming_validator: Optional[PrimingValidator] | None = None,
    ):
        """
        Args:
            board_client: Optional[BoardValidatorClient]
            number_validator: Optional[NumberValidator]
            priming_validator: Optional[PrimingValidator]
        """
        super().__init__(
            number_validator=number_validator,
            priming_validator=priming_validator,
        )
        self._board_client = board_client or BoardValidatorClient()
    
    @property
    def board_client(self) -> BoardValidatorClient:
        return self._board_client
    
