# src/operand/state/query/stack/hostage/operand/state.py

"""
Module: operand.state.query.stack.hostage.operand
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import List

from operand import Hostage, HostageContext
from operand.query import StackQuery


@dataclass
class HostageQuery(StackQuery[Hostage]):
    """
    Role:
        -   Operand
        -   Search
        -   Stateless Data-Holder

    Responsibilities:
        1.  A list of hostages to search with context.


    Attributes:
        stack: HostageStackService
        context: HostageContext

    Provides:

    Super Class:
        StackQuery
    """
    stack: HostageStackService
    context: HostageContext

