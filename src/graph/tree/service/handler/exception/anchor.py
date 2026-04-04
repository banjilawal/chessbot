# src/logic/node/tree/service/exception/anchor.py

"""
Module: logic.node.tree.service.exception.anchor
Author: Banji Lawal
Created: 2026-03-12
version: 1.0.0
"""

from __future__ import annotations
from typing import Optional

__all__ = [
    # ======================# NODE_TREE_STACK_MIGRATOR_EXCEPTION #======================#
    "NodeTreeStackMigratorException",
]

from system import AnchorException

# ======================# NODE_TREE_STACK_MIGRATOR_EXCEPTION #======================#
class NodeTreeStackMigratorException(AnchorException):
    """
    Role:Coverage Target, Exception Chain Layer 0

    Responsibilities:
    1.  Anchors NodeTreeStackMigrator debug (layer-2) error state firing incident
        reports on
            *   the triggering variable
            *   The trigger's value.
    2.  Indicate which NodeTreeStackMigrator method received a worker's (layer-1) failure result.

    Super Class:
        *   AnchorException

    Provides:


    # INHERITED ATTRIBUTES:
        *   See AnchorException class for inherited attributes.

    Attributes:
        msg: Optional[str]
        ex: Optional[Exception]
        cls_name: Optional[str]
        cls_mthd: Optional[str]
        err_code: Optional[str]

    # LOCAL METHODS:
    None

    # INHERITED METHODS:
        *   See AnchorException class for inherited methods.
    """
    CLS_NAME = "NodeTreeStackMigrator"
    ERR_CODE = "NODE_TREE_STACK_MIGRATOR_EXCEPTION"
    MSG = "NodeTreeStackMigrator raised an exception."
    
    def __init__(
            self,
            msg: Optional[str] = None,
            ex: Optional[Exception] = None,
            cls_name: Optional[str] = None,
            cls_mthd: Optional[str] = None,
            err_code: Optional[str] = None,
    ):
        """
        Args:
            msg: Optional[str]
            ex: Optional[Exception]
            cls_name: Optional[str]
            cls_mthd: Optional[str]
            err_code: Optional[str]
        """
        msg = msg or self.MSG
        cls_name = cls_name or self.CLS_NAME
        err_code = err_code or self.ERR_CODE
        super().__init__(msg=msg, err_code=err_code, ex=ex, cls_name=cls_name, cls_mthd=cls_mthd)
