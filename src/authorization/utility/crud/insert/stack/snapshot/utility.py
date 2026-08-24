# src/authorization/utility/crud/insert/stack/snapshot/utility.py

"""
Module: authorization.utility.crud.insert.stack.snapshot.utility
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict

from assurance import StackInsertContextValidator, SnapshotContextValidator
from authorization import StackInsertPermissionUtility
from domain import SnapshotInsertContext


@dataclass
class SnapshotStackInsertPermissionUtility(StackInsertPermissionUtility[SnapshotInsertContext]):
    """
    Role:
        -   Utility

    Responsibilities:
        1.  Bundles resources the SnapshotInsertAuthorizer needs to evaluate a SnapshotInsertRequest.

    Attributes:
        validator: Dict[str, ContextValidator]
        snapshot_context_validator: SnapshotContextValidator
        
    Provides:

    Super Class:
        StackInsertPermissionUtility
    """
    validator: Dict[str, StackInsertContextValidator] = field(
        default_factory=lambda: {
            "snapshot_context_validator": SnapshotContextValidator(),
        }
    )
    
    @property
    def snapshot_context_validator(self) -> SnapshotContextValidator:
        return self.resources["snapshot_context_validator"]

    