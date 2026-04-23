# src/model/query/stack/hostage/model.py

"""
Module: model.query.stack.hostage.model
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import List

from model import Hostage, HostageContext
from model.query import StackQuery


@dataclass
class HostageQuery(StackQuery[Hostage]):
    """
    Role:
        -   Model
        -   Search
        -   Stateless Data-Holder

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

