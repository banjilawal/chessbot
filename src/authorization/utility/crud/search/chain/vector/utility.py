# src/authorization/utility/crud/search/chain/vector/utility.py

"""
Module: authorization.utility.crud.search.chain.vector.utility
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict

from assurance import StackSearchContextValidator
from authorization import ChainSearchPermissionUtility
from domain import VectorNodeContext


@dataclass
class VectorChainSearchPermissionUtility(
    ChainSearchPermissionUtility[VectorNodeContext]
):
    """
    Role:
        -   Toolkit

    Responsibilities:
        1.  Bundles resources the VectorNodeSearchAuthorizer needs to evaluate a
            VectorNodeSearchRequest.

    Attributes:
        validator: Dict[str, ContextValidator]
        vector_context_validator: VectorNodeContextValidator
        
    Provides:

    Super Class:
        ChainSearchPermissionUtility
    """
    validator: Dict[str, StackSearchContextValidator] = field(
        default_factory=lambda: {
            "vector_node_context_validator": VectorNodeContextValidator(),
        }
    )
    
    @property
    def vector_node_context_validator(self) -> VectorNodeContextValidator:
        return self.resources["vector_node_context_validator"]

    