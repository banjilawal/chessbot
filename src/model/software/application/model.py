# src/model/software/application/model/software.py

"""
Module: model.software.application.model
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from abc import abstractmethod
from typing import Optional

from database import CoordDatabase
from model import Coord, HomeSquare, KingApplication, Rank, SoftwareModel, Team, ApplicationActivitySoftware, DeploymentSoftware
from model.software.license import SoftwareLicense
from schema import Formation


class Application(SoftwareModel):
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
    