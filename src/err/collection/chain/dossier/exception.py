# src/err/collection/chain/dossier/exception.py

"""
Module: err.collection.chain.dossier.exception
Author: Banji Lawal
Created: 2026-04-04
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Optional

from err import ChainException
from artifcat import MethodResultType

__all__ = [
    # ======================# DOSSIER_CHAIN_ERROR #======================#
    "DossierChainException",
]

# ======================# DOSSIER_CHAIN_ERROR #======================#
class DossierChainException(ChainException):
    """
    Role:
        - Error Tracing

    Responsibilities:
        1.  Indicating a DossierChain encountered an error.

    Attributes:
        msg: Optional[str]
        var: Optional[str]
        val: Optional[Any]
        ex: Optional[Exception]
        cls_name: Optional[str]
        cls_mthd: Optional[str]
        err_code: Optional[str]
        mthd_rslt_type: Optional[MethodResultType]
            
    Provides:

    Super Class:
        ChainException
    """
    MSG = "DossierChain Error."
    ERR_CODE = "DOSSIER_CHAIN_ERROR"
    
    def __init__(
            self,
            msg: Optional[str] | None = None,
            var: Optional[str] | None = None,
            val: Optional[Any] | None = None,
            cls_mthd: Optional[str] | None = None,
            cls_name: Optional[str] | None = None,
            ex: Optional[Exception] | None = None,
            err_code: Optional[str] | None =None,
            mthd_rslt_type: Optional[MethodResultType] | None = None,
    ):
        """
        Args:
            msg: Optional[str]
            var: Optional[str]
            val: Optional[Any]
            ex: Optional[Exception]
            cls_name: Optional[str]
            cls_mthd: Optional[str]
            err_code: Optional[str]
            mthd_rslt_type: Optional[MethodResultType]
        """
        msg = msg or self.MSG
        err_code = err_code or self.ERR_CODE
        super().__init__(
            ex=ex,
            msg=msg,
            var=var,
            val=val,
            err_code=err_code,
            cls_name=cls_name,
            cls_mthd=cls_mthd,
           mthd_rslt_type=mthd_rslt_type,
        )