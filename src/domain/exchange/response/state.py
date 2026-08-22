# src/domain/exchange/response/state.py

"""
Module: domain.exchange.response.state
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from enum import Enum, auto


class ResponseState(Enum):
    SUCCESS = auto(),
    FAILURE = auto(),
    
