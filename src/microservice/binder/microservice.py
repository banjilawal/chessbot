# src/microservice/binder/microservice.py

"""
Module: microservice.binder.microservice
Author: Banji Lawal
Created: 2025-02-08
version: 1.0.0
"""

from __future__ import annotations

from copy import deepcopy
from typing import Optional

from integrity import SchemaValidator, TeamValidator
from microservice import Microservice
from model import TeamBinder


class TeamBinderMicroservice(Microservice[TeamBinder]):
    """
    Role:Microservice API, Integrity Lifecycle Manager, APLifecycle Management.

    Responsibilities:
    1.  Integrity Lifecycle Management Microservice API.
    2.  Bundles primitives for assuring integrity and consistency in the two phases of
        the integrity lifecycle.
            *   At object creation.
            *   At object invocation.

    Super Class:
        *   Microservice

    Provides:

    # LOCAL ATTRIBUTES:
        *   build (Builder[TeamBinder])
        *   validation (Validator[TeamBinder])

    # INHERITED ATTRIBUTES:
        *   See Microservice class for inherited attributes.

    Attributes:
        *   id (int)
        *   schema (schema)
        *   build (Builder[TeamBinder])
        *   validation (Validator[TeamBinder])

    # LOCAL METHODS:
    None

    # INHERITED METHODS:
    *   See Microservice class for inherited methods.
    """
    SERVICE_NAME = "TeamBinderservice"
    _builder: Builder[TeamBinder]
    _validator: Validator[TeamBinder]
    
    def __init__(
            self,
            name: str = SERVICE_NAME,
            id: int = IdFactory.next_id(class_name="TeamBinderService"),
            builder: Builder[TeamBinder] = TeamBinderBuilder(),
            validator: Validator[TeamBinder] = Validator(),
    ):
        super().__init__(id=id, name=name)
        self._builder = builder
        self._validator = validator
    
    @property
    def builder(self) -> Builder[TeamBinder]:
        return self._builder
    
    @property
    def validator(self) -> Validator[TeamBinder]:
        return self.certifier
    
    def __eq__(self, other):
        if super().__eq__(other):
            if isinstance(other, TeamBinderMicroservice):
                return True
        return False
    
    @LoggingLevelRouter.monitor
    def slot_occupant(
            self,
            schema: Schema,
            team_table: TeamBinder,
            schema_validator: SchemaValidator | None = None,
    ) -> Optional[Team]:
        method = f"{self.__class__.__name__}"
        
        if schema_validator is None:
            schema_validator = SchemaValidator()
    
        # Handle the case that, the table is not certified as safe.
        table_validation_result = self._validator.validate(team_table)
        if table_validation_result.is_failure:
            # Return the exception chain on failure
            return UpdateResult.update_failure(
                original=team_table,
                exception=TeamBinderServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TeamBinderServiceException.MSG,
                    err_code=TeamBinderServiceException.ERR_CODE,
                    ex=table_validation_result.exception,
                )
            )
        # Handle the case that, the table is not certified as safe.
        schema_validation_result = schema_validator.validate(schema)
        if table_validation_result.is_failure:
            # Return the exception chain on failure
            return UpdateResult.update_failure(
                original=team_table,
                exception=TeamBinderServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TeamBinderServiceException.MSG,
                    err_code=TeamBinderServiceException.ERR_CODE,
                    ex=schema_validation_result.exception,
                )
            )
        if schema not in team_table.schemas:
            return None
        return team_table.table[schema]
        
    @LoggingLevelRouter.monitor
    def add_team(
            self,
            team: Team,
            team_table: TeamBinder,
            team_validator: TeamValidator | None = None,
    ) -> UpdateResult[TeamBinder]:
        method = f"{self.__class__.__name__}.add_team"
        
        if team_validator is None:
            team_validator = Validator()
        
        # Handle the case that, the table is not certified as safe.
        table_validation_result = self._validator.validate(team_table)
        if table_validation_result.is_failure:
            # Return the exception chain on failure
            return UpdateResult.update_failure(
                original=team_table,
                exception=TeamBinderServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TeamBinderServiceException.MSG,
                    err_code=TeamBinderServiceException.ERR_CODE,
                    ex=table_validation_result.exception,
                )
            )
        # Handle the case that, the team is flagged.
        team_validation_result = team_validator.validate(team)
        if team_validation_result.is_failure:
            # Return the exception chain on failure
            return UpdateResult.update_failure(
                original=team_table,
                exception=TeamBinderServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TeamBinderServiceException.MSG,
                    err_code=TeamBinderServiceException.ERR_CODE,
                    ex=team_validation_result.exception,
                )
            )
        # Handle the case that, the table is already full.
        if team_table.is_full:
            # Return the exception chain on failure
            return UpdateResult.update_failure(
                original=team_table,
                exception=TeamBinderServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TeamBinderServiceException.MSG,
                    err_code=TeamBinderServiceException.ERR_CODE,
                    ex=FullTeamBinderException(
                        msg=FullTeamBinderException.MSG,
                        err_code=FullTeamBinderException.ERR_CODE,
                    ),
                )
            )
        # Handle the case that, the team belongs to a different board.
        if team_table.board != team.board:
            # Return the exception chain on failure
            return UpdateResult.update_failure(
                original=team_table,
                exception=TeamBinderServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TeamBinderServiceException.MSG,
                    err_code=TeamBinderServiceException.ERR_CODE,
                    ex=TeamBelongsToDifferntBoardException(
                        msg=TeamBelongsToDifferntBoardException.MSG,
                        err_code=TeamBelongsToDifferntBoardException.ERR_CODE,
                    ),
                )
            )
        # Handle the case, that the team's slot is occupied by a different
        occupant_check_result = self._team_validator.validate(team_table, team.schema)
        if occupant_check_result.is_failure:
            # Return the exception chain on failure
            return UpdateResult.update_failure(
                original=team_table,
                exception=TeamBinderServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TeamBinderServiceException.MSG,
                    err_code=TeamBinderServiceException.ERR_CODE,
                    ex=TeamBelongsToDifferntBoardException(
                        msg=TeamBelongsToDifferntBoardException.MSG,
                        err_code=occupant_check_result.exception,
                    ),
                )
            )
        if occupant_check_result.payload is not None and occupant_check_result.payload != team:
            # Return the exception chain on failure
            return UpdateResult.update_failure(
                original=team_table,
                exception=TeamBinderServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TeamBinderServiceException.MSG,
                    err_code=TeamBinderServiceException.ERR_CODE,
                    ex=TeamBinderSlotAlreayOccupiedException(
                        msg=TeamBinderSlotAlreayOccupiedException.MSG,
                        err_code=TeamBinderSlotAlreayOccupiedException.ERR_CODE,
                    ),
                )
            )
        if occupant_check_result.payload is not None and occupant_check_result.payload == team:
            return UpdateResult.nothing_to_update()
        pre_update_table = deepcopy(team_table)
        team_table.table[team.schema] = team
        
        return UpdateResult.update_success(original=team_table, updated=team_table,)