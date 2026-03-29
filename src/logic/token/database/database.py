# src/logic/token/database/database.py

"""
Module: logic.token.database.database
Author: Banji Lawal
Created: 2025-11-24
version: 1.0.0
"""

from __future__ import annotations
from typing import List, Optional

from logic.rank import Rank, RankService
from logic.token import (
    RankQuotaReport, Token, TokenContext, TokenStackService, TokenService, TokenDatabaseException,
    TokenStackState
)
from logic.system import (
    ComputationResult, Database, DeletionResult, IdFactory, IdentityService, InsertionResult,
    LoggingLevelRouter, SearchResult,
)


class TokenDatabase(Database[Token]):
    """
    Role:
        -   Repo interface.
        -   Data Protection layer.

    Responsibilities:
        1.  Protects TokenStackService data from direct access.
        2.  Middle layer between clients and TokenStackService.
        3.  Platform for extending TokenStackService features.

    Attributes:
        SERVICE_NAME = "TokenDatabase"
        
        id: int
        name: str
        size: int
        is_empty: bool
        is_full: bool
        iterator: Iterator[Token]
        kernel: TokenStackService
        is_deployed_on_board: bool
        is_ready_for_deployment: bool
        current_item: Optional[Token]
        integrity_service: TokenService

    Provides:
        -   insert(token: Token) -> InsertionResult[bool]
        -   search(query: TokenContext) -> SearchResult[List[Token]]
        
        -   rank_quota_report(
                    rank: Rank,
                    rank_service: RankService = RankService(),
            ) -> ComputationResult[RankQuotaReport]
            
        -   delete_by_id(
                    id: int,
                    identity_service: IdentityService,
            ) -> DeletionResult
            
    Super:
        Database
    """
    SERVICE_NAME = "TokenDatabase"
    _kernel: TokenStackService
    
    def __init__(
            self,
            kernel: TokenStackService,
            name: str = SERVICE_NAME,
            id: int = IdFactory.next_id(class_name="TokenDatabase"),
    ):
        """
        Args:
            id: int
            name: str
            kernel: TokenStackService
        """
        super().__init__(id=id, name=name)
        self._kernel = kernel
    
    @property
    def integrity_service(self) -> TokenService:
        return self._kernel.integrity_service
    
    @property
    def iterator(self) -> iter:
        return self._kernel.iterator
    
    @property
    def size(self) -> int:
        return self._kernel.size
    
    @property
    def is_full(self) -> bool:
        return self._kernel.is_full
    
    @property
    def is_empty(self) -> bool:
        return self._kernel.is_empty
    
    @property
    def current_item(self) -> Optional[Token]:
        return self._kernel.current_item
    
    @property
    def is_ready_for_deployment(self) -> bool:
        return self._kernel.is_ready_for_deployment
    
    @property
    def is_deployed_on_board(self) -> bool:
        return self._kernel.is_deployed_on_board
    #
    # @property
    # def stack_state(self) -> TokenStackState:
    #     return self._kernel.stack_state
    #
    # @stack_state.setter
    # def stack_state(self, state: TokenStackState):
    #     self._kernel.deployment_state = state
    
    @LoggingLevelRouter.monitor
    def rank_quota_report(
            self,
            rank: Rank,
            rank_service: RankService = RankService(),
    ) -> ComputationResult[RankQuotaReport]:
        """
        Produce a quota report for the rank.
        
        Actions:
            1.  If the operation gets interrupted send an exception chain. Otherwise,
                send the success result.
        Args:
            rank: Rank
            rank_service: RankService
        Returns:
            ComputationResult[RankQoutaReport]
        Raises:
           TokenDatabaseException
        """
        method = f"T{self.__class__.name}.number_of_openings_for_rank"
        
        # --- Forward the request to the kernel. ---#
        rank_quota_analysis_result = self._kernel.request.rank_quota_analyzer.execute(
            rank=rank,
            token_stack=self._kernel,
            rank_service=rank_service,
        )
        # Handle the case that, the request is not completed.
        if rank_quota_analysis_result.is_failure:
            # Return the exception chain on failure
            return ComputationResult.failure(
                TokenDatabaseException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenDatabaseException.MSG,
                    err_code=TokenDatabaseException.ERR_CODE,
                    ex=rank_quota_analysis_result.exception
                )
            )
        # --- Forward the response to the client. ---#
        return rank_quota_analysis_result
    
    @LoggingLevelRouter.monitor
    def delete_by_id(
            self,
            id: int,
            identity_service: IdentityService = IdentityService(),
    ) -> DeletionResult[Token]:
        """
        Delete any token which has that id.

        Action:
            If the operation gets interrupted send an exception chain. Otherwise,
            send the success result.
        Args:
            id: int
            identity_service: IdentityService
        Returns:
            DeletionResult[Token]
        Raises:
            TokenStackServiceException
        """
        method = f"{self.__class__.__name__}.delete_by_id"
        
        # --- Forward the request to the kernel. ---#
        request_result = self._kernel.delete_by_id(
            id=id,
            identity_service=identity_service,
        )
        # Handle the case that, the request was not completed
        if request_result.is_failure:
            # Return the exception chain on failure
            return ComputationResult.failure(
                TokenDatabaseException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenDatabaseException.MSG,
                    err_code=TokenDatabaseException.ERR_CODE,
                    ex=request_result.exception
                )
            )
        # --- Forward the response to the client. ---#
        return request_result
   
    @LoggingLevelRouter.monitor
    def insert(self, token: Token) -> InsertionResult[bool]:
        """
        Insert a token into the database.

        Action:
            If the insertion fails, send an exception chain. Otherwise, send the success result.
        Args:
            token: Token
        Returns:
            InsertionResult[Token]
        Raises:
            TokenStackServiceException
        """
        method = f"{self.__class__.__name__}.insert"
        
        # --- Forward the request to the kernel. ---#
        insertion_result = self._kernel.push(item=token)
        
        # Handle the case that, the request was not completed.
        if insertion_result.is_failure:
            # Return the exception chain on failure
            return ComputationResult.failure(
                TokenDatabaseException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenDatabaseException.MSG,
                    err_code=TokenDatabaseException.ERR_CODE,
                    ex=insertion_result.exception
                )
            )
        # --- Forward the response to the client. ---#
        return insertion_result
    
    @LoggingLevelRouter.monitor
    def search(self, context: TokenContext) -> SearchResult[List[Token]]:
        """
        Find tokens whose attribute value fits the query.

        Action:
            Send an exception chain if the operation gets interrupted. Otherwise, send
            the success result.
        Args:
            context: TokenContext
        Returns:
            SearchResult[List[Token]]
        Raises:
            TokenDatabaseException
        """
        method = f"{self.__class__.__name__}.search_tokens"
        
        # --- Forward the request to the kernel. ---#
        query_result = self._kernel.query(context=context)
        
        # Handle the case that, the request was not completed.
        if query_result.is_failure:
            # Return the exception chain on failure
            return ComputationResult.failure(
                TokenDatabaseException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenDatabaseException.MSG,
                    err_code=TokenDatabaseException.ERR_CODE,
                    ex=query_result.exception
                )
            )
        # --- Forward the response to the client. ---#
        return query_result