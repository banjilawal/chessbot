from typing import Optional, TypeVar, cast

from chess.system import Dyad, RelationStatus, RelationReport, Result

P = TypeVar("P")
S = TypeVar("S")



class RelationReport(Result):
    _satellite: Optional[S]
    _relation_status: Optional[RelationStatus]
    
    def __init__(
            self,
            dyad: Optional[Dyad(P, S)],
            satellite: Optional[S],
            relation_status: Optional[RelationStatus],
            exception: Optional[Exception],
    ):
        super().__init__(payload=dyad, exception=exception)
        """INTERNAL: Use factory methods instead of direct constructor."""
        method = "RelationReport.__init__"
        self._satellite = satellite
        self._relation_status = relation_status
    
    @property
    def dyad(self) -> Optional[P]:
        return cast(Dyad, self.payload)
    
    @property
    def satellite(self) -> Optional[S]:
        return self._satellite
    
    @property
    def relation_status(self) -> Optional[RelationStatus]:
        return self._relation_status
    
    @property
    def are_not_related(self) -> bool:
        return self.exception is None and self.payload is None and self._satellite is None
    
    @property
    def registration_does_not_exist(self) -> bool:
        return self.exception is None and self.payload is None and self._satellite is not None
    
    @property
    def is_bidirectional(self) -> bool:
        return self.exception is None and self.payload is not None and self._satellite is not None
    
    @classmethod
    def no_relation(cls) -> RelationReport:
        return cast(RelationReport, cls.empty())
    
    @classmethod
    def registration_not_submitted(cls, satellite: S) -> RelationReport:
        return RelationReport(satellite=satellite,dyad=None, exception=None)
    
    @classmethod
    def bidirectional(cls, dyad: Dyad) -> RelationReport:
        return RelationReport(dyad=dyad, satellite=None, exception=None)
        
        
    
    