# src/repo/account/repo.py

"""
Module: repo.account.repo
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from collection import AccountStack
from microservice import AccountInsertionMicroservice, AccountSearchMicroservice
from repo import Repo


class AccountRepo(Repo[AccountStack]):

    
    def __init__(
            self,
            data: AccountStack,
            searcher: Optional[AccountSearchMicroservice] | None = None,
            inserter: Optional[AccountInsertionMicroservice] | None = None,
    ):
        """
        Args:
            data: AccountStack,
            searcher: Optional[AccountSearchMicroservice]
            inserter: Optional[AccountInsertionMicroservice]
        """
        super().__init__(
            data=data,
            searcher=searcher or AccountSearchMicroservice(),
            inserter=inserter or AccountInsertionMicroservice(),
        )
        
    @property
    def data(self) -> AccountStack:
        return cast(AccountStack, super().data)
    
    @property
    def searcher(self) -> AccountSearchMicroservice:
        return cast(AccountSearchMicroservice, super().searcher)
    
    @property
    def inserter(self) -> AccountInsertionMicroservice:
        return cast(AccountInsertionMicroservice, super().inserter)
    