# src/repo/repo.py

"""
Module: repo.repo
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar

from collection import DataStruct

T = TypeVar("T")

class Repo(ABC, Generic[T]):
    _data: DataStruct[T]
    _inserter: Inser
    
    def __init__(
            self,
            data: DataStruct[T]
            
    ):
    