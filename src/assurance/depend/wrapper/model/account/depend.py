# src/assurance/depend/wrapper/model/account/depend.py

"""
Module: assurance.depend.wrapper.model.account.depend
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""


from __future__ import annotations

from assurance import ModelWrapperDependency
from domain import Account


class AccountWrapperDependency(ModelWrapperDependency[Account]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Satisfy AccountValidator's ResponseWrapper dependencies.

    Attributes:

    Provides:

    Super Class:
        ModelWrapperDependency
    """
    
    def __init__(self,):
        super().__init__()
