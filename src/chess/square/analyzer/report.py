# src/chess/square/analyzer/report.py

"""
Module: chess.square.analyzer.report
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from typing import Optional, cast

from chess.token import Token
from chess.square import Square
from chess.system import NotImplementedException, RelationStatus, RelationReport



class SquareTokenRelationReport(RelationReport[Square, Token]):
    
    def __init__(
            self,
            primary: Optional[Square],
            satellite: Optional[Token],
            relation_status: Optional[RelationStatus],
            exception: Optional[Exception],
    ):
        super().__init__(
            primary=primary, 
            satellite=satellite, 
            exception=exception, 
            relation_status=RelationStatus.NO_RELATION
        )
        """INTERNAL: Use factory methods instead of direct constructor."""
        method = "RelationReport.__init__"
    
    @property
    def primary(self) -> Optional[Square]:
        return cast(Square, self.primary)
    
    @property
    def satellite(self) -> Optional[Token]:
        return cast(Token, self._satellite)
    
    @property
    def relation_status(self) -> Optional[RelationStatus]:
        return self._relation_status
    
    @property
    def does_not_exist(self) -> bool:
        return (
                self.exception is None and
                self.primary is None and
                self.satellite is None and
                self.relation_status == RelationStatus.NO_RELATION
        )
    
    @property
    def partially_exists(self) -> bool:
        return (
                self.exception is None and
                self.primary is None and
                self._satellite is not None and
                self._relation_status == RelationStatus.REGISTRATION_NOT_SUBMITTED
        )
    
    @property
    def fully_exists(self) -> bool:
        return (
                self.exception is None and
                self.primary is not None and
                self._satellite is not None and
                self._relation_status == RelationStatus.BIDIRECTIONAL
        )
    
    @classmethod
    def not_related(cls) -> RelationReport[Square, Token]:
        return cls(
            primary=None,
            satellite=None,
            exception=None,
            relation_status=RelationStatus.NO_RELATION,
        )
    
    @classmethod
    def square_not_submitted_lease_termination(cls, primary: Square) -> RelationReport[Square, Token]:
        return cls(
            primary=primary,
            exception=None,
            satellite=None,
            relation_status=RelationStatus.REGISTRATION_NOT_SUBMITTED
        )
    
    @classmethod
    def token_not_registered_with_square(cls, satellite: Token) -> RelationReport[Square, Token]:
        return cls(
            primary=None,
            exception=None,
            satellite=satellite,
            relation_status=RelationStatus.REGISTRATION_NOT_SUBMITTED
        )
    
    @classmethod
    def partial(cls, satellite: Token) -> RelationReport[Square, Token]:
        return cls(
            primary=None,
            exception=NotImplementedException("SquareTokenRelation does not unidrecitonalimplement partial relation reporting."),
            satellite=None,
            relation_status=RelationStatus.REGISTRATION_NOT_SUBMITTED
        )
    
    @classmethod
    def bidirectional(cls, primary: Square, satellite: Token) -> RelationReport[Square, Token]:
        return cls(
            exception=None,
            primary=primary,
            satellite=satellite,
            relation_status=RelationStatus.BIDIRECTIONAL,
        )