# src/domain/metadata/software/version/metadata.py

"""
Module: domain.metadata.software.version.metdata
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations



class VersionNumber:
    """
    Role:
        _   Metadata
        
    Responsibilities:
        1.  Identifier for a release.
    
    Attributes:
        major_number: int
        minor_number: int
        
    Provides:

    Super Class:
    """
    _major_number: int
    _minor_minor: int
    
    def __init__(self, major_number: int, minor_number: int):
        """
        Args:
            major_number: int
            minor_number: int
        """
        self._major_number = major_number
        self._major_number = minor_number
        
    @property
    def major_number(self) -> int:
        return self._major_number
    
    @property
    def minor_number(self) -> int:
        return self._minor_minor
