# src/err/operation/registry/worker/search/domain/exception.py

"""
Module: err.operation.registry.worker.search.domain.exception
Author: Banji Lawal
Created: 2026-04-04
version: 1.0.1
"""

from __future__ import annotations
from typing import Any, Optional

from err import RegistryWorkerException


__all__ = [
    # ======================# WORKER_REGISTRY_DOMAIN_SEARCH_FAILURE #======================#
    "WorkerRegistryDomainSearchException",
]

# ======================# WORKER_REGISTRY_DOMAIN_SEARCH_FAILURE #======================#
class WorkerRegistryDomainSearchException(RegistryWorkerException):
    """
    Role:
        -   Error Tracing

    Responsibilities:
        1.  Indicate that an error occurred during a WorkerRegistryDomainSearch.

    Attributes:
        msg: Optional[str]
        var: Optional[str]
        val: Optional[Any]
        ex: Optional[Exception]
        cls_domain: Optional[str]
        cls_mthd: Optional[str]
        err_code: Optional[str]
        mthd_rslt_type: Optional[MethodResultType]
            
    Provides:

    Super Class:
        RegistryWorkerException
    """
    MSG = "Error during a WorkerRegistryDomainSearch."
    ERR_CODE = "WORKER_REGISTRY_DOMAIN_SEARCH_FAILURE"
    
    def __init__(
            self,
            msg: Optional[str] | None = None,
            var: Optional[str] | None = None,
            val: Optional[Any] | None = None,
            ex: Optional[Exception] | None = None,
            cls_domain: Optional[str] | None = None,
            cls_mthd: Optional[str] | None = None,
            err_code: Optional[str] | None = None,
    ):
        """
        Args:
            msg: Optional[str]
            var: Optional[str]
            val: Optional[Any]
            ex: Optional[Exception]
            cls_domain: Optional[str]
            cls_mthd: Optional[str]
            err_code: Optional[str]
        """
        msg = msg or self.MSG
        err_code = err_code or self.ERR_CODE
        super().__init__(
            ex=ex,
            msg=msg,
            var=var,
            val=val,
            err_code=err_code,
            cls_domain=cls_domain,
            cls_mthd=cls_mthd,
        )
