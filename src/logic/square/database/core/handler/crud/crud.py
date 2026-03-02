# src/logic/square/database/core/handler/handler.py

"""
Module: logic.square.database.core.handler.handler
Author: Banji Lawal
Created: 2025-11-22
version: 1.0.0
"""
from typing import List

from logic.square import (
    PoppingEmptySquareStackException, Square, SquareContext, SquareCrudHandlerException,
    SquareStackPushException, SquareStackService
)
from logic.system import DeletionResult, IdentityService, InsertionResult, LoggingLevelRouter, SearchResult


class SquareCrudHandler:
    """
    # ROLE: Handler
    # TASK: CRUD

    # RESPONSIBILITIES:
    1.  Separates the CRUD operations into a separate module to make the
        SquareStackService modular and easier to maintain.

    # PARENT:
    None

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
        *   id (int)
        *   SERVICE_NAME (str)
        *   roster_deployer (RosterDeployer)

    # INHERITED ATTRIBUTES:
    None

    # CONSTRUCTOR PARAMETERS:
        Local:
            *   id (int)
            *   name (str)
            *   roster_deployer (RosterDeployer)

        Inherited:
        None

    # LOCAL METHODS:
        *   add_occupant(token: Token, square: Square, square_list: list[Square]) -> UpdateResult[Square]
        *   remove_occupant_by_search(occupant: Token, square_list: List[Square]) -> DeletionResult[Token]

    # INHERITED METHODS:
    None
    """
    
    @LoggingLevelRouter.monitor
    def push(self, stack: SquareStackService, item: Square) -> InsertionResult[bool]:
        """
        # ACTION:
            1.  If the item is not validated send the exception in the InsertionResult. Else, call the super class
                push method.
            2.  If super().push_item fails send the exception in the InsertionResult. Else extract the payload to cast
                and return to the caller in the BuildResult.
        Args:
            item: Square
        Returns:
            InsertionResult[Square]
        Raises:
            SquareCrudHandlerException
        """
        method = "SquareStackService.add_square"
        
        # Handle the case that, there is no capacity for adding another square.
        available_capacity_computation_result = stack.util.stats_analyzer.available_capacity(stack=stack)
        if available_capacity_computation_result.is_failure:
            # Return the exception chain on failure
            return InsertionResult.failure(
                SquareCrudHandlerException(
                    cls_mthd=method,
                    cls_name=SquareCrudHandler.__name__,
                    err_code=SquareCrudHandlerException.ERR_CODE,
                    msg=SquareCrudHandlerException.MSG,
                    ex=SquareStackPushException(
                        op=SquareStackPushException.OP,
                        msg=SquareStackPushException.MSG,
                        mthd=SquareStackPushException.MTHD,
                        rslt_type=SquareStackPushException.RSLT_TYPE,
                        ex=available_capacity_computation_result.exception
                    )
                )
            )
        # Handle the case that, the square is not safe, or its id, name, or coord are in use.
        collision_report = stack.integrity_service.collision_detector.detect(
            target=item,
            dataset=stack.items,
        )
        if collision_report.is_failure:
            # Return the exception chain on failure
            return InsertionResult.failure(
                SquareCrudHandlerException(
                    cls_mthd=method,
                    cls_name=SquareCrudHandler.__name__,
                    err_code=SquareCrudHandlerException.ERR_CODE,
                    msg=SquareCrudHandlerException.MSG,
                    ex=SquareStackPushException(
                        op=SquareStackPushException.OP,
                        msg=SquareStackPushException.MSG,
                        mthd=SquareStackPushException.MTHD,
                        rslt_type=SquareStackPushException.RSLT_TYPE,
                        ex=collision_report.exception
                    )
                )
            )
        # --- Append the square and send the successful InsertionResult. ---#
        stack.items.append(item)
        return InsertionResult.success()
    
    @LoggingLevelRouter.monitor
    def pop(self, stack: SquareStackService) -> DeletionResult[Square]:
        """
        # ACTION:
            1.  If the stack is empty send an exception in the DeletionResult. Else remove the
                square at the top of the stack and send in the DeletionResult
        # PARAMETERS:
                    *   None
        # RETURNS:
            *   DeletionResult[Square] containing either:
                    - On failure: Exception.
                    - On success: Token in the payload.
        # RAISES:
            *   SquareCrudHandlerException
            *   PoppingEmptySquareStackException
        """
        method = "SquareStackService.pop"
        
        # Handle the case that, there are no tokens in the stack.
        if stack.is_empty:
            # Return the exception chain on failure.
            return DeletionResult.failure(
                SquareCrudHandlerException(
                    cls_mthd=method,
                    cls_name=SquareCrudHandler.__name__,
                    err_code=SquareCrudHandlerException.ERR_CODE,
                    msg=SquareCrudHandlerException.MSG,
                    ex=SquareStackPushException(
                        op=SquareStackPushException.OP,
                        msg=SquareStackPushException.MSG,
                        mthd=SquareStackPushException.MTHD,
                        rslt_type=SquareStackPushException.RSLT_TYPE,
                        ex=PoppingEmptySquareStackException(
                            msg=PoppingEmptySquareStackException.MSG,
                            err_code=PoppingEmptySquareStackException.ERR_CODE,
                        )
                    )
                )
            )
        # --- Pop the non-empty token stack. ---#
        square = stack.items.pop(-1)
        # --- Send the success result to the caller. ---#
        DeletionResult.success(square)
    
    @LoggingLevelRouter.monitor
    def delete_by_id(
            self,
            id: int,
            stack: SquareStackService,
            identity_service: IdentityService = IdentityService()
    ) -> DeletionResult[Square]:
        """
        # ACTION:
            1.  If the id is not certified safe send an exception in the DeletionResult.
            2.  Create a temp variable for storing a square before it's deleted.
            3.  Iterate through the squares.
                    *   If a square's id matches the target record the square in a temp variable before deleting
                        it from the list.
            4.  After the loop is finishes, if the temp variable is not None send it in the deletion success result.
                Else, send the nothing to delete result instead.
        # PARAMETERS:
                    *   id (int)
                    *   identity_service (IdentityService)
        # RETURNS:
            *   DeletionResult[Square]
        # RAISES:
            *   SquareCrudHandlerException
            *   SquareStackPopException
            *   PoppingEmptySquareStackException
        """
        method = "SquareStackService.delete_by_id"
        
        # Handle the case that, there are no items in the list.
        if stack.is_empty:
            # Return the exception chain on failure.
            return DeletionResult.failure(
                SquareCrudHandlerException(
                    cls_mthd=method,
                    cls_name=SquareCrudHandler.__name__,
                    err_code=SquareCrudHandlerException.ERR_CODE,
                    msg=SquareCrudHandlerException.MSG,
                    ex=SquareStackPushException(
                        op=SquareStackPushException.OP,
                        msg=SquareStackPushException.MSG,
                        mthd=SquareStackPushException.MTHD,
                        rslt_type=SquareStackPushException.RSLT_TYPE,
                        ex=PoppingEmptySquareStackException(
                            msg=PoppingEmptySquareStackException.MSG,
                            err_code=PoppingEmptySquareStackException.ERR_CODE,
                        )
                    )
                )
            )
        # Handle the case that, the id is not certified safe.
        validation = identity_service.validate_id(candidate=id)
        if validation.is_failure:
            # Return the exception chain on failure.
            return DeletionResult.failure(
                SquareCrudHandlerException(
                    cls_mthd=method,
                    cls_name=SquareCrudHandler.__name__,
                    err_code=SquareCrudHandlerException.ERR_CODE,
                    msg=SquareCrudHandlerException.MSG,
                    ex=SquareStackPushException(
                        op=SquareStackPushException.OP,
                        msg=SquareStackPushException.MSG,
                        mthd=SquareStackPushException.MTHD,
                        rslt_type=SquareStackPushException.RSLT_TYPE,
                        ex=validation.exception
                    )
                )
            )
        # --- Loop through the collection to ensure all matches are removed. ---#
        target = None
        for square in stack.items:
            if square.id == id:
                # Record a hit before pulling it from the stack.
                target = square
                stack.items.remove(square)
        # --- After the purging loop finishes handle the possible return cases. ---#
        
        # At least one square was removed.
        if target is not None:
            return DeletionResult.success(payload=target)
        # Default case: no square were removed.
        return DeletionResult.nothing_to_delete()
    
    @LoggingLevelRouter.monitor
    def query(self, context: SquareContext, stack: SquareStackService) -> SearchResult[List[Square]]:
        """
        # ACTION:
            1.  Pass the context param to context_service manages all error handling and operations in
                search lifecycle.
            2.  Any failures context_service will be encapsulated inside a SquareCrudHandlerException
                which is sent inside a SearchResult.
            3.  If the search completes successfully the result can be sent directly because it will contain the
                payload.
        # PARAMETERS:
            *   context (SquareContext)
        # RETURN:
            *   SearchResult[List[Square] containing either:
                    - On failure: An exception.
                    - On success: List[Square] in payload.
                    - On Empty: No payload nor exception.
        # RAISES:
            *   SquareCrudHandlerException
        """
        method = "SquareStackService.query"
        
        # --- Handoff the search responsibility to _stack_service. ---#
        query_result = stack.context_service.finder.find(dataset=stack.items, context=context)
        
        # Handle the case that, the search is not completed.
        if query_result.is_failure:
            # Return the exception chain on failure.
            return SearchResult.failure(
                SquareCrudHandlerException(
                    cls_mthd=method,
                    cls_name=SquareCrudHandler.__name__,
                    err_code=SquareCrudHandlerException.ERR_CODE,
                    msg=SquareCrudHandlerException.MSG,
                    ex=SquareStackPushException(
                        op=SquareStackPushException.OP,
                        msg=SquareStackPushException.MSG,
                        mthd=SquareStackPushException.MTHD,
                        rslt_type=SquareStackPushException.RSLT_TYPE,
                        ex=query_result.exception
                    )
                )
            )
        # --- For either a successful or empty search result directly forward to the caller. ---#
        return query_result