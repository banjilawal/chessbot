# src/authorization/utility/crud/search/stack/snapshot/utility.py

"""
Module: authorization.utility.crud.search.stack.snapshot.utility
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict

from assurance import ContextValidator, SnapshotContextValidator
from authorization import SearchPermissionUtility
from domain import SnapshotSearchContext


@dataclass
class SnapshotSearchPermissionUtility(SearchPermissionUtility[SnapshotSearchContext]):
    """
    Role:
        -   Toolkit

    Responsibilities:
        1.  Bundles resources the SnapshotSearchAuthorizer needs to evaluate a SnapshotSearchRequest..

    Attributes:
        validator: Dict[str, ContextValidator]
        snapshot_context_validator: SnapshotContextValidator
        
    Provides:

    Super Class:
        SearchPermissionUtility
    """
    validator: Dict[str, ContextValidator] = field(
        default_factory=lambda: {
            "snapshot_context_validator": SnapshotContextValidator(),
        }
    )
    
    @property
    def snapshot_context_validator(self) -> SnapshotContextValidator:
        return self.resources["snapshot_context_validator"]

    