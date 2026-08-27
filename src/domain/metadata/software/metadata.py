# src/domain/metadata/software/metdata.py

"""
Module: domain.metadata.software.metdata
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC

from domain import DomainMetadata


class SoftwareMetadata(DomainMetadata, ABC):
    """
    Role:
        - Metdata

    Responsibilities:
        1. Provide information about the application.

    Attributes:

    Provides:

    Super Class:
        DomainMetadata
    """
    pass