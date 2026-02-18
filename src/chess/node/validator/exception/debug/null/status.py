# src/chess/node/validator/exception/debug/status.py

"""
Module: chess.node.validator.exception.debug.status
Author: Banji Lawal
Created: 2025-02-17
version: 1.0.0
"""


from chess.system import NullException

__all__ = [
    # ======================# NULL_DISCOVERY_STATUS EXCEPTION #======================#
    "NullDiscoveryStatusException",
]

class NullDiscoveryStatusException(NullException):
    pass