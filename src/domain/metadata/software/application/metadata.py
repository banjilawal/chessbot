# src/domain/metadata/software/application/metadata.py

"""
Module: domain.metadata.software.application.metdata
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations




class Application(SoftwareMetadata):
    """
    Role:
        -   Softwareful Data Holder
        
    Responsibilities:
        1. Abstract representation of a chess piece.
        
    Attributes:
        id: int
        title: str
        version: int
        release_date: datetime
        license: SoftwareLicense
        subscriber: Subscriber
        
    Provides:

    Super Class:
        SoftwareModel
    """
    _id: int
    _title: str
    _version: int
    _release_date: datetime
    _license: SoftwareLicense
    _subscriber: Subscriber

    def __init__(
            self,
            id: int,
            title: str,
            version: int,
            release_date: datetime,
            license: SoftwareLicense,
            subscriber: Subscriber,
    ):
        """
        Args:
            id: int
            title: str
            version: int
            release_date: datetime
            license: SoftwareLicense
            subscriber: Subscriber
        """
        super().__init__()
        self._id = id
        self._title: str
        self._version = version
        self._release_date = release_date
        self._license: SoftwareLicense
        self._subscriber = subscriber
    
    @property
    def id(self) -> int:
        return self._id
    