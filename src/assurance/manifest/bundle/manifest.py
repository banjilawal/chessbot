# src/assurance/manifest/bundle/manifest.py

"""
Module: assurance.manifest.bundle.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 1.0.1
"""

from __future__ import annotations

from abc import ABC
from dataclasses import dataclass
from typing import Generic, TypeVar

from assurance import NullExceptionManifest, TypesManifest
from model import Model

T = TypeVar("T", bound="Model")

@dataclass(frozen=True)
class Manifest(ABC, Generic[T]):
    types: TypesManifest[T]
    null_exceptions: NullExceptionManifest[T]