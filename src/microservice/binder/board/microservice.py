# src/microservice/binder/team/microservice.py

"""
Module: microservice.binder.team.microsafe
Author: Banji Lawal
Created: 2025-02-08
version: 1.0.0
"""

from __future__ import annotations

from copy import deepcopy
from typing import Optional

from analyzer import BoardTeamBinderRelationAnalyzer, BoardTeamRelationAnalyzer
from integrity import SchemaValidator, TeamValidator
from microservice import BoardService, Microservice
from model import Board, BoardBinder, Schema, Team
from operation import BoardTeamBinderValidator
from result import AnalysisResult, SearchResult, UpdateResult
from system import IdFactory, LoggingLevelRouter


class BoardTeamBinderService(Microservice[BoardBinder]):
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
        *   build (Builder[BoarBoardTeamBinder])
        *   validation (Validator[BoardTeamBinder])

    # INHERITED ATTRIBUTES:
        *   See Microservice class for inherited attributes.

    Attributes:
        *   id (int)
        *   schema (schema)
        *   build (Builder[BoardTeamBinder])
        *   validation (Validator[BoardTeamBinder])

    # LOCAL METHODS:
    None

    # INHERITED METHODS:
    *   See Microservice class for inherited methods.
    """
    SERVICE_NAME = "BoardTeamBinderMicroservice"
    _builder: BoardTeamBinderBuilder
    _validator: BoardTeamBinderValidator
    _board_relation_analyst: BoardTeamBinderRelationAnalyzer
    
    def __init__(
            self,
            name: str = SERVICE_NAME,
            builder: BoardTeamBinderBuilder | None = None,
            validator: BoardTeamBinderValidator | None = None,
            id: int = IdFactory.next_id(class_name="BoardTeamBinderService"),
            board_relation_analyst: BoardTeamRelationAnalyzer | None = None,
    ):
        super().__init__(id=id, name=name)
        self._builder = builder or BoardTeamBinderBuilder()
        self._validator = validator or BoardTeamBinderValidator()
        self._board_relation_analyst = board_relation_analyst or BoardTeamBinderRelationAnalyzer()
    
    @property
    def builder(self) -> BoardTeamBinderBuilder:
        return self._builder
    
    @property
    def validator(self) -> BoardTeamBinderValidator:
        return self._validator
    
    def __eq__(self, other):
        if super().__eq__(other):
            if isinstance(other, BoardTeamBinderService):
                return True
        return False
    
    @LoggingLevelRouter.monitor
    def analyze_board_relation(
            self,
            board: Board,
            binder: BoardBinder,
            board_service: BoardService | None = None,
    ) -> AnalysisResult[RelationReport[Board, BoardBinder]]:
        method = f"{self.__class__.__name__}.analyze_board_relation"
        
        if board_service is None:
            board_service = BoardService()
        
        return self._board_relation_analyst.execute(
            candidate_primary=board,
            candidate_binder=binder,
            team_binder_validator=self._validator,
            board_validator=board_service.validator,
        )
    
    @LoggingLevelRouter.monitor
    def slot_occupant(
            self,
            schema: Schema,
            binder: BoardBinder,
            schema_validator: SchemaValidator | None = None,
    ) -> SearchResult[Optional[Team]]:
        method = f"{self.__class__.__name__}"
        
        if schema_validator is None:
            schema_validator = SchemaValidator()
    
        # Handle the case that, the binder is not certified as safe.
        binder_validation_result = self._validator.execute(binder)
        if binder_validation_result.is_failure:
            # Return the exception chain on failure
            return SearchResult.failure(
                BoardTeamBinderServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=BoardTeamBinderServiceException.MSG,
                    err_code=BoardTeamBinderServiceException.ERR_CODE,
                    ex=binder_validation_result.exception,
                )
            )
        # Handle the case that, the binder is not certified as safe.
        schema_validation_result = schema_validator.execute(schema)
        if schema_validation_result.is_failure:
            # Return the exception chain on failure
            return SearchResult.failure(
                BoardTeamBinderServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=BoardTeamBinderServiceException.MSG,
                    err_code=BoardTeamBinderServiceException.ERR_CODE,
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
            binder: BoardBinder,
            team_validator: TeamValidator | None = None,
    ) -> UpdateResult[BoardBinder]:
        method = f"{self.__class__.__name__}.add_team"
        
        if team_validator is None:
            team_validator = TeamValidator()
        
        # Handle the case that, the binder is not certified as safe.
        binder_validation_result = self._validator.execute(binder)
        if binder_validation_result.is_failure:
            # Return the exception chain on failure
            return UpdateResult.update_failure(
                original=binder,
                exception=BoardTeamBinderServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=BoardTeamBinderServiceException.MSG,
                    err_code=BoardTeamBinderServiceException.ERR_CODE,
                    ex=binder_validation_result.exception,
                )
            )
        # Handle the case that, the team is flagged.
        team_validation_result = team_validator.execute(team)
        if team_validation_result.is_failure:
            # Return the exception chain on failure
            return UpdateResult.update_failure(
                original=binder,
                exception=BoardTeamBinderServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=BoardTeamBinderServiceException.MSG,
                    err_code=BoardTeamBinderServiceException.ERR_CODE,
                    ex=team_validation_result.exception,
                )
            )
        # Handle the case that, the binder is already full.
        if binder.is_full:
            # Return the exception chain on failure
            return UpdateResult.update_failure(
                original=binder,
                exception=BoardTeamBinderServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=BoardTeamBinderServiceException.MSG,
                    err_code=BoardTeamBinderServiceException.ERR_CODE,
                    ex=FullBoardTeamBinderException(
                        msg=FullBoardTeamBinderException.MSG,
                        err_code=FullBoardTeamBinderException.ERR_CODE,
                    ),
                )
            )
        # Handle the case that, the team belongs to a different board.
        if binder.board != team.board:
            # Return the exception chain on failure
            return UpdateResult.update_failure(
                original=binder,
                exception=BoardTeamBinderServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=BoardTeamBinderServiceException.MSG,
                    err_code=BoardTeamBinderServiceException.ERR_CODE,
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
                exception=BoardTeamBinderServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=BoardTeamBinderServiceException.MSG,
                    err_code=BoardTeamBinderServiceException.ERR_CODE,
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
                exception=BoardTeamBinderServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=BoardTeamBinderServiceException.MSG,
                    err_code=BoardTeamBinderServiceException.ERR_CODE,
                    ex=BoardTeamBinderSlotAlreayOccupiedException(
                        msg=BoardTeamBinderSlotAlreayOccupiedException.MSG,
                        err_code=BoardTeamBinderSlotAlreayOccupiedException.ERR_CODE,
                    ),
                )
            )
        if occupant_check_result.payload is not None and occupant_check_result.payload == team:
            return UpdateResult.nothing_to_update()
        pre_update_binder = deepcopy(binder)
        binder.table[team.schema] = team
        
        return UpdateResult.update_success(original=pre_update_binder, updated=binder,)