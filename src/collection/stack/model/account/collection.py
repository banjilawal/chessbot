# src/collection/stack//model/account/collection.py

"""
Module: collection.stack.model.account.collection
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from collection import ModelStack
from domain import Account


class AccountStack(ModelStack[Account]):
    """
    Role:
        -   Collection

    Responsibilities:
        1.  Stack of unique Accounts.

    Attributes:
        items: List[Account]
 
    Provides:

    Super Class:
        ModelStack
    """