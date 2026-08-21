# src/dossier/model/state/query/stack/hostage/dossier/model/state.py

"""
Module: domain.model.state.query.stack.hostage.model
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from dataclasses import dataclass

from domain.model import Hostage, HostageContext
from domain.model import StackQuery


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
        stack: HostageStackService
        context: HostageContext

    Provides:

    Super Class:
        StackQuery
    """
    stack: HostageStackService
    context: HostageContext

