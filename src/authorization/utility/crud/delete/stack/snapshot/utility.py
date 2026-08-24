# src/authorization/utility/crud/delete/stack/snapshot/utility.py

"""
Module: authorization.utility.crud.delete.stack.snapshot.utility
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict

from assurance import StackDeleteContextValidator, SnapshotContextValidator
from authorization import StackDeletePermissionUtility
from domain import SnapshotDeleteContext


@dataclass
class SnapshotStackDeletePermissionUtility(StackDeletePermissionUtility[SnapshotDeleteContext]):
    """
    Role:
        -   Utility

    Responsibilities:
        1.  Bundles resources the SnapshotDeleteAuthorizer needs to evaluate a SnapshotDeleteRequest.

    Attributes:
        validator: Dict[str, ContextValidator]
        snapshot_context_validator: SnapshotContextValidator
        
    Provides:

    Super Class:
        StackDeletePermissionUtility
    """
    validator: Dict[str, StackDeleteContextValidator] = field(
        default_factory=lambda: {
            "snapshot_context_validator": SnapshotContextValidator(),
        }
    )
    
    @property
    def snapshot_context_validator(self) -> SnapshotContextValidator:
        return self.resources["snapshot_context_validator"]

    