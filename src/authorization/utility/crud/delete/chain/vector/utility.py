# src/authorization/utility/crud/delete/chain/vector/utility.py

"""
Module: authorization.utility.crud.delete.chain.vector.utility
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict

from assurance import StackDeleteContextValidator
from authorization import ChainDeletePermissionUtility
from domain import VectorNodeContext


@dataclass
class VectorChainDeletePermissionUtility(
    ChainDeletePermissionUtility[VectorNodeContext]
):
    """
    Role:
        - Utility

    Responsibilities:
        1.  Bundles resources the VectorNodeDeleteAuthorizer needs to evaluate a
            VectorNodeDeleteRequest.

    Attributes:
        validator: Dict[str, ContextValidator]
        vector_context_validator: VectorNodeContextValidator
        
    Provides:

    Super Class:
        ChainDeletePermissionUtility
    """
    validator: Dict[str, StackDeleteContextValidator] = field(
        default_factory=lambda: {
            "vector_node_context_validator": VectorNodeContextValidator(),
        }
    )
    
    @property
    def vector_node_context_validator(self) -> VectorNodeContextValidator:
        return self.resources["vector_node_context_validator"]

    