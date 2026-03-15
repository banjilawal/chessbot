# src/logic/token/database/core/handler/handler.py

"""
Module: logic.token.database.core.handler.handler
Author: Banji Lawal
Created: 2025-11-22
version: 1.0.0
"""
from typing import List

from logic.token import (
    PoppingEmptyTokenStackException, RankQuotaAnalyzer, Token, TokenCollisionDetector, TokenContext,
    TokenCrudHandlerException,
    TokenStackCountsAnalyzer, TokenStackFullException, TokenStackPushException, TokenStackService, TokenStackState
)
from logic.system import DeletionResult, IdentityService, InsertionResult, LoggingLevelRouter, SearchResult


class TokenStackCrudHandler:
    """
    # ROLE: Handler
    # TASK: CRUD

    # RESPONSIBILITIES:
    1.  Separates the CRUD operations into a separate module to make the
        TokenStackService modular and easier to maintain.

    # PARENT:
    None

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None

    # CONSTRUCTOR PARAMETERS:
    None

    # LOCAL METHODS:
        *   add_occupant(token: Token, token: Token, token_list: list[Token]) -> UpdateResult[Token]
        *   remove_occupant_by_search(occupant: Token, token_list: List[Token]) -> DeletionResult[Token]

    # INHERITED METHODS:
    None
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def push(
            cls,
            token: Token,
            token_stack: TokenStackService,
            rank_quota_analyzer: RankQuotaAnalyzer = RankQuotaAnalyzer(),
            collision_detector: TokenCollisionDetector = TokenCollisionDetector(),
    ) -> InsertionResult:
        """
        Action:
            1.  Return a failure result containing an exception chain if
                    *   The token is not safe.
                    *   One of its properties already in use.
                    *   The TokenStackService cannot support another token.
            2.  If none of the failure conditions are met insert the token and send the success result.
            
        Args:
           token: Token
           token_stack: TokenStackService
           rank_quota_analyzer: RankQuotaAnalyzer
           collision_detector: TokenCollisionDetector

        Returns:
            InsertionResult
            
        Raises:
            TokenCrudHandlerException
        """
        method =  f"{cls.__name__}.push"
        
        # Handle the case that, the list is full.
        if token_stack.is_full:
            # Return the exception chain on failure
            return InsertionResult.failure(
                TokenCrudHandlerException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    err_code=TokenCrudHandlerException.ERR_CODE,
                    msg=TokenCrudHandlerException.MSG,
                    ex=TokenStackPushException(
                        op=TokenStackPushException.OP,
                        msg=TokenStackPushException.MSG,
                        mthd=TokenStackPushException.MTHD,
                        rslt_type=TokenStackPushException.RSLT_TYPE,
                        ex=TokenStackFullException(
                            msg=TokenStackFullException.MSG,
                            err_code=TokenStackFullException.ERR_CODE,
                        )
                    )
                )
            )
        # --- Handoff validation, id, designation or opening_square collision detection. ---#
        collision_detection_result = collision_detector.detect(
            target=token,
            dataset=token_stack.items,
        )
        # Handle the case that, the either a collision was detected or detector crashed.
        if not collision_detection_result.is_no_collision:
            # Return the exception chain on failure
            return InsertionResult.failure(
                TokenCrudHandlerException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    err_code=TokenCrudHandlerException.ERR_CODE,
                    msg=TokenCrudHandlerException.MSG,
                    ex=TokenStackPushException(
                        op=TokenStackPushException.OP,
                        msg=TokenStackPushException.MSG,
                        mthd=TokenStackPushException.MTHD,
                        rslt_type=TokenStackPushException.RSLT_TYPE,
                        ex=collision_detection_result.exception
                    )
                )
            )
        # --- Find out how many openings the rank has. ---#
        openings_count_result = rank_quota_analyzer.count_openings_for_rank(
            rank=token.rank,
            token_stack=token_stack
        )
        # Handle the case that, the analyzer doesn't give a count of open slots.
        if openings_count_result.is_failure:
            # Return the exception chain on failure
            return InsertionResult.failure(
                TokenCrudHandlerException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    err_code=TokenCrudHandlerException.ERR_CODE,
                    msg=TokenCrudHandlerException.MSG,
                    ex=TokenStackPushException(
                        op=TokenStackPushException.OP,
                        msg=TokenStackPushException.MSG,
                        mthd=TokenStackPushException.MTHD,
                        rslt_type=TokenStackPushException.RSLT_TYPE,
                        ex=openings_count_result.exception
                    )
                )
            )
        # --- Capacity, collision and opening check are completed. Push the token onto the stack ---#
        token_stack.items.append(token)
        
        # --- Perform cleanup and integrity maintenance tasks. ---#
        if token_stack.is_full:
            token_stack.state = TokenStackState.READY_FOR_DEPLOYMENT

        # --- The work is completed, send the success result. ---#
        return InsertionResult.success()
    
    @classmethod
    @LoggingLevelRouter.monitor
    def pop(cls, token_stack: TokenStackService) -> DeletionResult[Token]:
        """
        Action:
            1.  If the stack is empty send an exception in the DeletionResult. Else remove the
                token at the top of the stack and send in the DeletionResult
        Args:
            token_stack: TokenStackService
            
        Returns:
            DeletionResult[Token
            
        Raises:
            TokenCrudHandlerException
            PoppingEmptyTokenStackException
        """
        method = f"{cls.__name__}.pop"
        
        # Handle the case that, there are no tokens in the stack.
        if token_stack.is_empty:
            # Return the exception chain on failure.
            return DeletionResult.failure(
                TokenCrudHandlerException(
                    cls_mthd=method,
                    cls_name=cls.__class__.__name__,
                    err_code=TokenCrudHandlerException.ERR_CODE,
                    msg=TokenCrudHandlerException.MSG,
                    ex=TokenStackPushException(
                        op=TokenStackPushException.OP,
                        msg=TokenStackPushException.MSG,
                        mthd=TokenStackPushException.MTHD,
                        rslt_type=TokenStackPushException.RSLT_TYPE,
                        ex=PoppingEmptyTokenStackException(
                            msg=PoppingEmptyTokenStackException.MSG,
                            err_code=PoppingEmptyTokenStackException.ERR_CODE,
                        )
                    )
                )
            )
        # --- Pop the non-empty token stack. ---#
        token = token_stack.items.pop(-1)
        # --- Send the success result to the caller. ---#
        DeletionResult.success(token)
    
    @classmethod
    @LoggingLevelRouter.monitor
    def delete_by_id(
            cls,
            id: int,
            token_stack: TokenStackService,
            identity_service: IdentityService = IdentityService()
    ) -> DeletionResult[Token]:
        """
        Action:
            1.  If the id is not certified safe send an exception in the DeletionResult.
            2.  Create a temp variable for storing a token before it's deleted.
            3.  Iterate through the tokens.
                    *   If a token's id matches the target record the token in a temp variable before deleting
                        it from the list.
            4.  After the loop is finishes, if the temp variable is not None send it in the deletion success result.
                Else, send the nothing to delete result instead.
                
        Args:
            id: int
            token_stack: TokenStackService
            identity_service: IdentityService
            
        Returns:
            DeletionResult[Token]
            
        Raises:
            TokenCrudHandlerException
            TokenStackPopException
            PoppingEmptyTokenStackException
        """
        method = f"{cls.__name__}.delete_by_id"
        
        # Handle the case that, there are no items in the list.
        if token_stack.is_empty:
            # Return the exception chain on failure.
            return DeletionResult.failure(
                TokenCrudHandlerException(
                    cls_mthd=method,
                    cls_name=cls.__class__.__name__,
                    err_code=TokenCrudHandlerException.ERR_CODE,
                    msg=TokenCrudHandlerException.MSG,
                    ex=TokenStackPushException(
                        op=TokenStackPushException.OP,
                        msg=TokenStackPushException.MSG,
                        mthd=TokenStackPushException.MTHD,
                        rslt_type=TokenStackPushException.RSLT_TYPE,
                        ex=PoppingEmptyTokenStackException(
                            msg=PoppingEmptyTokenStackException.MSG,
                            err_code=PoppingEmptyTokenStackException.ERR_CODE,
                        )
                    )
                )
            )
        # Handle the case that, the id is not certified safe.
        validation = identity_service.validate_id(candidate=id)
        if validation.is_failure:
            # Return the exception chain on failure.
            return DeletionResult.failure(
                TokenCrudHandlerException(
                    cls_mthd=method,
                    cls_name=cls.__class__.__name__,
                    err_code=TokenCrudHandlerException.ERR_CODE,
                    msg=TokenCrudHandlerException.MSG,
                    ex=TokenStackPushException(
                        op=TokenStackPushException.OP,
                        msg=TokenStackPushException.MSG,
                        mthd=TokenStackPushException.MTHD,
                        rslt_type=TokenStackPushException.RSLT_TYPE,
                        ex=validation.exception
                    )
                )
            )
        # --- Loop through the collection to ensure all matches are removed. ---#
        target = None
        for token in token_stack.items:
            if token.id == id:
                # Record a hit before pulling it from the stack.
                target = token
                token_stack.items.remove(token)
        # --- After the purging loop finishes handle the possible return cases. ---#
        
        # At least one token was removed.
        if target is not None:
            return DeletionResult.success(payload=target)
        # Default case: no token were removed.
        return DeletionResult.nothing_to_delete()
    
    @classmethod
    @LoggingLevelRouter.monitor
    def query(cls, context: TokenContext, token_stack: TokenStackService) -> SearchResult[List[Token]]:
        """
        Action:
            1.  Pass the context param to context_service manages all error handling and operations in
                search lifecycle.
            2.  Any failures context_service will be encapsulated inside a TokenCrudHandlerException
                which is sent inside a SearchResult.
            3.  If the search completes successfully the result can be sent directly because it will contain the
                payload.
                
        Args:
            context: TokenContext
            token_stack: TokenStackService
            
        Returns:
            SearchResult[List[Token]

        Raises:
            TokenCrudHandlerException
        """
        method = f"{cls.__class__.__name__}.query"
        
        # --- Handoff the search responsibility to _stack_service. ---#
        query_result = token_stack.context_service.finder.find(dataset=token_stack.items, context=context)
        
        # Handle the case that, the search is not completed.
        if query_result.is_failure:
            # Return the exception chain on failure.
            return SearchResult.failure(
                TokenCrudHandlerException(
                    cls_mthd=method,
                    cls_name=cls.__class__.__name__,
                    err_code=TokenCrudHandlerException.ERR_CODE,
                    msg=TokenCrudHandlerException.MSG,
                    ex=TokenStackPushException(
                        op=TokenStackPushException.OP,
                        msg=TokenStackPushException.MSG,
                        mthd=TokenStackPushException.MTHD,
                        rslt_type=TokenStackPushException.RSLT_TYPE,
                        ex=query_result.exception
                    )
                )
            )
        # --- For either a successful or empty search result directly forward to the caller. ---#
        return query_result