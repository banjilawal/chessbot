# src/assurance/depend/service/model/account/depend.py

"""
Module: assurance.depend.service.model.account.depend
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""


from __future__ import annotations

from assurance import ServiceDependency
from domain import Account


class AccountServiceDependency(ServiceDependency[Account]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Satisfy AccountValidator's ValidationService dependencies.

    Attributes:

    Provides:

    Super Class:
        Dependency
    """
    
    def __init__(self,):
        super().__init__()
