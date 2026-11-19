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
from repo import Repo
from transit import AccountPushDispatcher, AccountSearchDispatcher


class AccountRepo(Repo[AccountStack]):

    
    def __init__(
            self,
            data: AccountStack,
            searcher: Optional[AccountSearchDispatcher] | None = None,
            inserter: Optional[AccountPushDispatcher] | None = None,
    ):
        """
        Args:
            data: AccountStack,
            searcher: Optional[AccountSearchDispatcher]
            inserter: Optional[AccountPushDispatcher]
        """
        super().__init__(
            data=data,
            searcher=searcher or AccountSearchDispatcher(),
            inserter=inserter or AccountPushDispatcher(),
        )
        
    @property
    def data(self) -> AccountStack:
        return cast(AccountStack, super().data)
    
    @property
    def searcher(self) -> AccountSearchDispatcher:
        return cast(AccountSearchDispatcher, super().searcher)
    
    @property
    def inserter(self) -> AccountPushDispatcher:
        return cast(AccountPushDispatcher, super().inserter)
    