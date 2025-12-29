from typing import Optional, TypeVar, cast

from chess.system import Dyad, RelationStatus, RelationReport, Result

P = TypeVar("P")
S = TypeVar("S")



class RelationReport(Result):
    _satellite: Optional[S]
    _relation_status: Optional[RelationStatus]
    
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
        self._satellite = satellite
        self._relation_status = relation_status
    
    @property
    def primary(self) -> Optional[P]:
        return cast(P, self.payload)
    
    @property
    def satellite(self) -> Optional[S]:
        return self._satellite
    
    @property
    def relation_status(self) -> Optional[RelationStatus]:
        return self._relation_status
    
    @property
    def does_not_exist(self) -> bool:
        return (
                self.exception is None and
                self.payload is None and
                self._satellite is None and
                self._relation_status == RelationStatus.NO_RELATION
        )
    
    @property
    def partially_exists(self) -> bool:
        return (
                self.exception is None and
                self.payload is None and
                self._satellite is not None and
                self._relation_status == RelationStatus.REGISTRATION_NOT_SUBMITTED
        )
    
    @property
    def fully_exists(self) -> bool:
        return (
                self.exception is None and
                self.payload is not None and
                self._satellite is not None and
                self._relation_status == RelationStatus.BIDIRECTIONAL
        )
    
    @classmethod
    def not_related(cls) -> RelationReport:
        return RelationReport(relation_status=RelationStatus.NO_RELATION)
    
    @classmethod
    def partial(cls, satellite: S) -> RelationReport:
        return RelationReport(satellite=satellite, relation_status=RelationStatus.REGISTRATION_NOT_SUBMITTED)
    
    @classmethod
    def bidirectional(cls, primary: P, satellite: S) -> RelationReport:
        return RelationReport(primary=primary, satellite=None, relation_status=RelationStatus.BIDIRECTIONAL)
        