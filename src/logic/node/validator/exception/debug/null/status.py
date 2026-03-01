# src/logic/node/context/validator/exception/debug/null/status.py

"""
Module: logic.node.context.validator.exception.debug.null.status
Author: Banji Lawal
Created: 2026-02-18
version: 1.0.0
"""

from logic.system import NullException

__all__ = [
    # ======================# DISCOVERY_STATUS_NULL EXCEPTION #======================#
    "DiscoveryStatusNullException",
]


# ======================# DISCOVERY_STATUS_NULL EXCEPTION #======================#
class DiscoveryStatusNullException(NullException):
    """
    # ROLE: Error Variable Identifier, Exception Chain Layer 2, Exception Messaging

    # RESPONSIBILITIES:
    A failing ValidationResult was returned because the candidate was null.

    # PARENT:
        *   NullException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "DISCOVERY_STATUS_NULL_EXCEPTION"
    MSG = "Node validation failed: Expected a DiscoveryStatus, received null instead."