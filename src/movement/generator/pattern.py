# src/space/generator/bishop/pattern.py

"""
Module: space.generator.bishop.pattern
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import  annotations

from abc import ABC
from typing import Generic, TypeVar

from sequence import VectorSequenceGenerator

T = TypeVar("T", bound="Rank")

class PatternGenerator(ABC, Generic[T]):
    _sequence_generator: VectorSequenceGenerator
    _ruleset:
