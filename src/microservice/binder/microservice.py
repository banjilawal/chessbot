# src/microservice/binder/microservice.py

"""
Module: microservice.binder.microservice
Author: Banji Lawal
Created: 2025-02-08
version: 1.0.0
"""

from __future__ import annotations

from copy import deepcopy
from typing import List, Optional

from integrity import SchemaValidator, TeamValidator
from integrity.build.binder import TeamBinderBuilder
from microservice import Microservice
from model import Schema, Team, TeamBinder, TeamBinderValidator
from result import SearchResult, UpdateResult
from system import IdFactory, LoggingLevelRouter


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
    SERVICE_NAME = "TeamBinderMicroservice"
    _builder: TeamBinderBuilder
    _validator: TeamBinderValidator
    
    def __init__(
            self,
            name: str = SERVICE_NAME,
            builder: TeamBinderBuilder | None = None,
            validator: TeamBinderValidator | None = None,
            id: int = IdFactory.next_id(class_name="TeamBinderService"),
    ):
        super().__init__(id=id, name=name)
        if builder is None:
            builder = TeamBinderBuilder()
        
        if validator is None:
            validator = TeamBinderValidator()
        self._builder = builder
        self._validator = validator
    
    @property
    def builder(self) -> TeamBinderBuilder:
        return self._builder
    
    @property
    def validator(self) -> TeamBinderValidator:
        return self._validator
    
    def __eq__(self, other):
        if super().__eq__(other):
            if isinstance(other, TeamBinderMicroservice):
                return True
        return False
    
    @LoggingLevelRouter.monitor
    def slot_occupant(
            self,
            schema: Schema,
            binder: TeamBinder,
            schema_validator: SchemaValidator | None = None,
    ) -> SearchResult[Optional[Team]]:
        method = f"{self.__class__.__name__}"
        
        if schema_validator is None:
            schema_validator = SchemaValidator()
    
        # Handle the case that, the binder is not certified as safe.
        binder_validation_result = self._validator.validate(binder)
        if binder_validation_result.is_failure:
            # Return the exception chain on failure
            return SearchResult.failure(
                TeamBinderServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TeamBinderServiceException.MSG,
                    err_code=TeamBinderServiceException.ERR_CODE,
                    ex=binder_validation_result.exception,
                )
            )
        # Handle the case that, the binder is not certified as safe.
        schema_validation_result = schema_validator.validate(schema)
        if schema_validation_result.is_failure:
            # Return the exception chain on failure
            return SearchResult.failure(
                TeamBinderServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TeamBinderServiceException.MSG,
                    err_code=TeamBinderServiceException.ERR_CODE,
                    ex=schema_validation_result.exception,
                )
            )
        if schema not in binder.schemas:
            return SearchResult.empty()
        return SearchResult.success([binder.table[schema]])
        
    @LoggingLevelRouter.monitor
    def add_team(
            self,
            team: Team,
            binder: TeamBinder,
            team_validator: TeamValidator | None = None,
    ) -> UpdateResult[TeamBinder]:
        method = f"{self.__class__.__name__}.add_team"
        
        if team_validator is None:
            team_validator = TeamValidator()
        
        # Handle the case that, the binder is not certified as safe.
        binder_validation_result = self._validator.validate(binder)
        if binder_validation_result.is_failure:
            # Return the exception chain on failure
            return UpdateResult.update_failure(
                original=binder,
                exception=TeamBinderServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TeamBinderServiceException.MSG,
                    err_code=TeamBinderServiceException.ERR_CODE,
                    ex=binder_validation_result.exception,
                )
            )
        # Handle the case that, the team is flagged.
        team_validation_result = team_validator.validate(team)
        if team_validation_result.is_failure:
            # Return the exception chain on failure
            return UpdateResult.update_failure(
                original=binder,
                exception=TeamBinderServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TeamBinderServiceException.MSG,
                    err_code=TeamBinderServiceException.ERR_CODE,
                    ex=team_validation_result.exception,
                )
            )
        # Handle the case that, the binder is already full.
        if binder.is_full:
            # Return the exception chain on failure
            return UpdateResult.update_failure(
                original=binder,
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
        if binder.board != team.board:
            # Return the exception chain on failure
            return UpdateResult.update_failure(
                original=binder,
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
        occupant_check_result = self.slot_occupant(binder=binder, schema=team.schema)
        if occupant_check_result.is_failure:
            # Return the exception chain on failure
            return UpdateResult.update_failure(
                original=binder,
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
                original=binder,
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
        pre_update_binder = deepcopy(binder)
        binder.table[team.schema] = team
        
        return UpdateResult.update_success(original=pre_update_binder, updated=binder,)