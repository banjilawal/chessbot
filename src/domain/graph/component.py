# src/domain/graph/component.py

"""
Module: domain.graph.component
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import TypeVar

from domain import Searchable

T = TypeVar("T", bound="StatefulModel")


class GraphComponent(ABC,  Searchable):
    pass