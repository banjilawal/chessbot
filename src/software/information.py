# src/software/metdata.py

"""
Module: software.metdata
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from domain import Application, SoftwareLicense, Subscriber, VersionNumber


class SoftwareInformation:
    """
    Role:
        - Metdata

    Responsibilities:
        1. Provide information about the application.

    Attributes:

    Provides:

    Super Class:
    """
    _application: Application
    _version: VersionNumber
    _license: SoftwareLicense
    _subscriber: Subscriber
    
    def __init__(
            self,
            subscriber: Subscriber,
            application: Application,
            license: SoftwareLicense,
            version: VersionNumber,
    ):
        """
        Args:
            subscriber: Subscriber
            application: Application
            license: SoftwareLicense
            version: VersionNumber
        """
        self._subscriber = subscriber
        self._application = application
        self._license = license
        self._version = version
        
    @property
    def subscriber(self) -> Subscriber:
        return self._subscriber
    
    @property
    def application(self) -> Application:
        return self._application
    
    @property
    def license(self) -> SoftwareLicense:
        return self._license
    
    @property
    def application(self) -> VersionNumber:
        return self._version
    
    
    