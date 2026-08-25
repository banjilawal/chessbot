# src/domain/metadata/software/license/metadata.py

"""
Module: domain.metadata.software.license.metadata
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from datetime import datetime

from domain import Application, Subscriber


class SoftwareLicense:
    """
    Role:
        -   Softwareful Data Holder
        
    Responsibilities:
        1. Abstract representation of a chess piece.
        
    Attributes:
        id: int
        issue_date: datetime
        expiration_date: datetime
        application: Application
        subscriber: Subscriber
        
    Provides:

    Super Class:
    """
    _id: int
    _issue_date: datetime
    _expiration_date: datetime
    _application: Application
    _subscriber: Subscriber

    def __init__(
            self,
            id: int,
            issue_date: datetime,
            expiration_date: datetime,
            application: Application,
            subscriber: Subscriber,
    ):
        """
        Args:
            id: int
            issue_date: datetime
            expiration_date: datetime
            application: Application
            subscriber: Subscriber
        """
        self._id = id
        self._issue_date = issue_date
        self._expiration_date = expiration_date
        self._application = application
        self._subscriber = subscriber
    
    @property
    def id(self) -> int:
        return self._id
    
    @property
    def issue_date(self) -> datetime:
        return self._issue_date
    
    @property
    def expiration_date(self) -> datetime:
        return self._issue_date
    
    @property
    def application(self) -> Application:
        return self._application
    
    @property
    def subscriber(self) -> Subscriber:
        return self._subscriber
