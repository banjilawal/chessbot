# src/domain/context/model/account/category.py

"""
Module: domain.context.model.account.category
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from enum import Enum, auto


class AccountType(Enum):
    HUMAN_ACCOUNT = auto(),
    MACHINE_ACCOUNT = auto(),