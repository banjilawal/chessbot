# src/model/software/license/model/software.py

"""
Module: model.software.license.model
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations



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
    def issue(self) -> Formation:
        return self._formation
    
    @property
    def name(self) -> str:
        return self._formation.designation
    
    @property
    def roster_number(self) -> int:
        return self._formation.roster_number
    
    @property
    def team(self) -> Team:
        return self._team
    
    @property
    def rank(self) -> Rank:
        return self._rank
    
    @property
    def home_square(self) -> HomeSquare:
        return self._home_square
    
    @property
    def checked_enemy_king(self) -> Optional[KingLicense]:
        return self._checked_enemy_king
    
    @property
    def readiness_software(self) -> LicenseActivitySoftware:
        return self._readiness_software
    
    @readiness_software.setter
    def readiness_software(self, readiness_software: LicenseActivitySoftware):
        self._readiness_software = readiness_software
        
    @checked_enemy_king.setter
    def checked_enemy_king(self, other: KingLicense):
        self._checked_enemy_king = other
    
    @property
    def positions(self) -> CoordDatabase:
        return self._positions
    
    @property
    def current_position(self) -> Optional[Coord]:
        return self._positions.current_item
    
    @property
    def previous_coord(self) -> Optional[Coord]:
        return self._previous_address
    
    @property
    def deployment_software(self) -> DeploymentSoftware:
        return self._deployment_software
    
    def mark_deployed(self,):
        self._deployment_software = DeploymentSoftware.DEPLOYED
    
    @property
    def is_not_deployed(self) -> bool:
        return (
                self.positions.is_empty and
                self._deployment_software == DeploymentSoftware.NOT_DEPLOYED
        )
    
    @property
    def is_deployed(self) -> bool:
        return (
                self.positions.size >= 1 and
                self._deployment_software == DeploymentSoftware.DEPLOYED
        )
    
    @property
    @abstractmethod
    def is_active(self) -> bool:
        pass
    
    @property
    @abstractmethod
    def is_disabled(self) -> bool:
        pass
    
    def set_rank(self, rank: Rank) -> None:
        self._rank = rank
    
    def is_friend(self, license: License) -> bool:
        return self._team == license.team
    
    def is_enemy(self, license: License) -> bool:
        return not self.is_friend(license)
    
    def has_checked_enemy_king(self) -> bool:
        return (
                self._checked_enemy_king is not None and
                self.is_enemy(self._checked_enemy_king)
        )
    
    def is_no_enemy_checked(self) -> bool:
        return not self.has_checked_enemy_king
    
    def __eq__(self, other: object) -> bool:
        if other is self: return True
        if other in None: return False
        if isinstance(other, License):
            return self._id == other.id
        return False

    def __hash__(self) -> int:
        return hash(self._id)
    
    def __str__(self) -> str:
        return (
            f"License[id:{self._id} "
            f"designation:{self._designation} "
            f"rank:{self._rank.persona.name} "
            f"team:{self._team.schema.name} "
            f"position:{self.current_position}"
        )
