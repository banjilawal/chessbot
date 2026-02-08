# src/chess/system/relation/report.py

"""
Module: chess.system.relation.report
Created: 2025-10-01
version: 1.0.0
"""

from __future__ import annotations
from typing import Generic, Optional, TypeVar

from chess.system import RelationStatus

P = TypeVar("P")
S = TypeVar("S")

class RelationReport(Generic[P, S]):
    _primary: Optional[P]
    _satellite: Optional[S]
    _exception: Optional[Exception]
    
    def __init__(
            self,
            primary: Optional[P],
            satellite: Optional[S],
            relation_status: Optional[RelationStatus],
            exception: Optional[Exception],
    ):
        super().__init__(payload=primary, exception=exception)
        """INTERNAL: Use factory methods instead of direct constructor."""
        method = "RelationReport.__init__"
        self._primary = primary
        self._satellite = satellite
        self._relation_status = relation_status
        
    @property
    def primary(self) -> Optional[P]:
        return self._primary
    
    @property
    def satellite(self) -> Optional[S]:
        return self._satellite
    
    @property
    def exception(self) -> Optional[Exception]:
        return self._exception
    
    @property
    def relation_status(self) -> Optional[RelationStatus]:
        return self._relation_status
    
    @property
    def is_failure(self) -> bool:
        return (
                self._exception is not None and
                self._primary is None and
                self._satellite is None and
                self._relation_status is None
        )
    
    @property
    def does_not_exist(self) -> bool:
        return (
                self._exception is None and
                self._primary is None and
                self._satellite is None and
                self._relation_status == RelationStatus.NO_RELATION
        )
    
    @property
    def registration_does_not_exist(self) -> bool:
        return (
                self._exception is None and
                self._primary is None and
                self._satellite is not None and
                self._relation_status == RelationStatus.REGISTRATION_NOT_SUBMITTED
        )
    
    @property
    def stale_link_exists(self) -> bool:
        return (
                self._exception is None and
                self._primary is not None and
                self._satellite is None and
                self._relation_status == RelationStatus.STALE_LINK_NOT_PURGED
        )

    @property
    def fully_exists(self) -> bool:
        return (
                self._exception is None and
                self._primary is not None and
                self._satellite is not None and
                self._relation_status == RelationStatus.BIDIRECTIONAL
        )
    
    @classmethod
    def failure(cls, exception: Exception) -> RelationReport[P, S]:
        return RelationReport(
            primary=None,
            satellite=None,
            exception=exception,
            relation_status=None,
        )
    
    @classmethod
    def no_relation(cls) -> RelationReport[P, S]:
        return RelationReport(
            primary=None,
            satellite=None,
            exception=None,
            relation_status=RelationStatus.NO_RELATION,
        )
    
    @classmethod
    def registration_missing(cls, satellite: S) -> RelationReport[P, S]:
        return RelationReport(
            primary=None,
            exception=None,
            satellite=satellite,
            relation_status=RelationStatus.REGISTRATION_NOT_SUBMITTED
        )
    
    @classmethod
    def stale_link(cls, primary: P) -> RelationReport[P, S]:
        return RelationReport(
            satellite=None,
            exception=None,
            primary=primary,
            relation_status=RelationStatus.STALE_LINK_NOT_PURGED
        )
    
    @classmethod
    def bidirectional(cls, primary: P, satellite: S) -> RelationReport[P,S]:
        return RelationReport(
            exception=None,
            primary=primary,
            satellite=satellite,
            relation_status=RelationStatus.BIDIRECTIONAL,
        )
        