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

from analysis import BoardBinderRelationAnalyst, BoardTeamRelationAnalyst
from integrity import SchemaValidator, TeamValidator
from integrity.build.binder import TeamBinderBuilder
from microservice import BoardService, Microservice, TeamService
from model import Board, Schema, Team, BoardTeamBinder, TeamBinderValidator
from report import RelationReport
from result import AnalysisResult, SearchResult, UpdateResult
from system import IdFactory, LoggingLevelRouter


class TeamBinderService(Microservice[BoardTeamBinder]):
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
    _board_relation_analyst: BoardBinderRelationAnalyst
    
    def __init__(
            self,
            name: str = SERVICE_NAME,
            builder: TeamBinderBuilder | None = None,
            validator: TeamBinderValidator | None = None,
            id: int = IdFactory.next_id(class_name="TeamBinderService"),
            board_relation_analyst: BoardTeamRelationAnalyst | None = None,
    ):
        super().__init__(id=id, name=name)
        self._builder = builder or TeamBinderBuilder()
        self._validator = validator or TeamBinderValidator()
        self._board_relation_analyst = board_relation_analyst or BoardBinderRelationAnalyst()
    
    @property
    def builder(self) -> TeamBinderBuilder:
        return self._builder
    
    @property
    def validator(self) -> TeamBinderValidator:
        return self._validator
    
    def __eq__(self, other):
        if super().__eq__(other):
            if isinstance(other, TeamBinderService):
                return True
        return False
    
    @LoggingLevelRouter.monitor
    def analyze_board_relation(
            self,
            board: Board,
            binder: BoardTeamBinder,
            board_service: BoardService | None = None,
    ) -> AnalysisResult[RelationReport[Board, BoardTeamBinder]]:
        method = f"{self.__class__.__name__}.analyze_board_relation"
        
        if board_service is None:
            board_service = BoardService()
        
        return self._board_relation_analyst.analyze(
            candidate_primary=board,
            candidate_binder=binder,
            team_binder_validator=self._validator,
            board_validator=board_service.validator,
        )
    
    @LoggingLevelRouter.monitor
    def slot_occupant(
            self,
            schema: Schema,
            binder: BoardTeamBinder,
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
            binder: BoardTeamBinder,
            team_validator: TeamValidator | None = None,
    ) -> UpdateResult[BoardTeamBinder]:
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