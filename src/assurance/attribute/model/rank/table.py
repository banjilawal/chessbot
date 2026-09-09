# src/assurance/attrribute/model/rank/table.py

"""
Module: assurance.attrribute.model.rank.table
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""


from __future__ import annotations

from typing import Optional

from assurance import AttributeHelperTable, PrimingValidator
from domain import Rank
from microservice import IdentityService


class RankHelperTable(AttributeHelperTable[Rank]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Bundles validators a Rank needs for its primitive and upstream relational
            partners attributes.

    Attributes:

    Provides:

    Super Class:
        AttributeHelperTable
    """
    
    def __init__(
            self,
            identity_service: Optional[IdentityService] | None = None,
            priming_validator: Optional[PrimingValidator] | None = None,
    ):
        """
        Args:
            identity_service: Optional[IdentityService]
            priming_validator: Optional[PrimingValidator]
        """
        super().__init__(
            identity_service=identity_service,
            priming_validator=priming_validator,
        )
        