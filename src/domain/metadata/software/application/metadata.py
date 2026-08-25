# src/domain/metadata/software/application/metadata.py

"""
Module: domain.metadata.software.application.metdata
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from datetime import datetime

from domain import SoftwareMetadata, VersionNumber


class Application(SoftwareMetadata):
    """
    Role:
        -   Metadata
        
    Responsibilities:
        1. Information about the application.
        
    Attributes:
        id: int
        title: str
        version: VersionNumber
        
    Provides:

    Super Class:
        SoftwareMetadata
    """
    _id: int
    _title: str
    _version: VersionNumber
    _release_date: datetime

    def __init__(
            self,
            id: int,
            title: str,
            version: VersionNumber,
            release_date: datetime,
    ):
        """
        Args:
            id: int
            title: str
            version: VersionNumber
        """
        super().__init__()
        self._id = id
        self._title = title
        self._version = version
        self._release_date = release_date
    
    @property
    def id(self) -> int:
        return self._id
    
    @property
    def title(self) -> str:
        return self._title
    
    @property
    def version(self) -> VersionNumber:
        return self._version
    
    @property
    def release_date(self) -> datetime:
        return self._release_date
    
    