# src/query/stack/hostage/query.py

"""
Module: query.stack.hostage.query
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import List

from model import Hostage, HostageContext
from query import StackQuery


@dataclass
class HostageStackQuery(StackQuery[Hostage]):
    """
    Role:
        -   Model
        -   Stateless Data-Holder
        -   Messaging

    Responsibilities:
        1.  A list of hostages to search with context.


    Attributes:
        stack: List[Hostage]
        context: HostageContext

    Provides:

    Super Class:
        StackQuery
    """
    stack: List[Hostage]
    context: HostageContext

