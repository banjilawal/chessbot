# src/logic/token/query/service/process.py

"""
Module: logic.token.query.service.service
Author: Banji Lawal
Created: 2025-11-24
version: 1.0.0
"""

from typing import List, cast

from logic.system import QueryService, IdFactory, LoggingLevelRouter, SearchResult
from logic.token import (
    Token, TokenContext, TokenContextService, TokenDatasetNullException, TokenQueryServiceException,
    TokenSearchRouter
)

class TokenQueryService(QueryService[Token]):
    """
    Role:
        -   API
        -   Search Micro Service,

    Responsibilities:
        1.  Public facing API for querying square collections.

    Args:
        id: int
        name: str
        router: SearchRouter[T]
        context_service: IntegrityService[Context[T]]

    Provides:
        -   execute(dataset: List[T], query: Context[T]) -> SearchResult[List[T]]

    Super Class:
        Service
    """
    """
    Role:
        Search Service, Lifecycle Management, Encapsulation, API layer.

    Responsibilities:
    1.  Public facingToken search microservice API.
    2.  Provides a map aware utility for searchingToken objects.
    3.  Encapsulate integrity assurance logic in one extendable module.
    4.  Create a single source of truth forToken search results by having single entry and exit points for the
       Token search flow.

    Super Class:
        *   QueryService

    # PROVIDES:
        *  TokenQueryService


    # INHERITED ATTRIBUTES:
        *   See QueryService for inherited attributes.
    """
    SERVICE_NAME = "TokenQueryService"
    _router: TokenSearchRouter
    _context_service: TokenContextService

    def __init__(
            self,
            name: str = SERVICE_NAME,
            router: TokenSearchRouter = TokenSearchRouter(),
            id: int = IdFactory.next_id(class_name="TokenQueryService"),
            context_service: TokenContextService =TokenContextService(),
    ):
        """
        Args:
            id: int
            name: str
            router: TokenSearchRouter
            context_service: TokenContextService
        """
        super().__init__(id=id, name=name)
        self._router = router
        self._context_service = context_service
    
    @property
    def router(self) ->TokenSearchRouter:
        return self._router
    
    @property
    def context_service(self) -> TokenContextService:
        return self._context_service
    
    @LoggingLevelRouter.monitor
    def execute(self, dataset: List[Token], context: TokenContext) -> SearchResult[List[Token]]:
        """
        Find tokens whose attribute value fits the query.

        Action:
            Send an exception chain if the operation gets interrupted. Otherwise, send
            the success result.
        Args:
            context: TokenContext
            dataset: List[Token]
        Returns:
            SearchResult[List[Token]]
        Raises:
            TokenQueryServiceException
        """
        method = f"{self.__class__.__name__}.query"
        
        param_validation_result = self._run_safety_checks(dataset=dataset, context=context)
        if param_validation_result.is_failure:
            return param_validation_result
        # --- Forward the request to the context_service. ---#
        query_result = self._router.route(dataset=dataset, context=context)
        
        # Handle the case that, the request was not completed.
        if query_result.is_failure:
            # Return the exception chain on failure.
            return SearchResult.failure(
                TokenQueryServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenQueryServiceException.MSG,
                    err_code=TokenQueryServiceException.ERR_CODE,
                    ex=query_result.exception,
                )
            )
        # --- Forward the work product to the caller. ---#
        return query_result
    
    @LoggingLevelRouter.monitor
    def _run_safety_checks(
            self,
            dataset: List[Token],
            context: TokenContext
    ) -> SearchResult[List[Token]]:
        method = f"{self.__class__.__name__}._run_safety_checks"
        
        # Handle the case that, the query is incorrect
        context_validation_result = self._context_service.validation.execute(context)
        if context_validation_result.is_failure:
            # Return the exception chain on failure.
            return SearchResult.failure(
                TokenQueryServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenQueryServiceException.MSG,
                    err_code=TokenQueryServiceException.ERR_CODE,
                    ex=context_validation_result.exception,
                )
            )
        # Handle the case that, the dataset does not exist
        if dataset is None:
            # Return the exception chain on failure.
            return SearchResult.failure(
                TokenQueryServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenQueryServiceException.MSG,
                    err_code=TokenQueryServiceException.ERR_CODE,
                    ex=TokenDatasetNullException(
                        msg=TokenDatasetNullException.MSG,
                        err_code=TokenDatasetNullException.ERR_CODE,
                    )
                )
            )
        # Handle the case that, the dataset is the wrong type.
        if not isinstance(dataset, List):
            # Return the exception chain on failure.
            return SearchResult.failure(
                TokenQueryServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenQueryServiceException.MSG,
                    err_code=TokenQueryServiceException.ERR_CODE,
                    ex=TypeError(f"Expected List, got {type(dataset).__name__} instead.")
                )
            )
        # Handle the case that, the does not contain tokens.
        if not isinstance(dataset[0], Token):
            # Return the exception chain on failure.
            return SearchResult.failure(
                TokenQueryServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenQueryServiceException.MSG,
                    err_code=TokenQueryServiceException.ERR_CODE,
                    ex=TypeError(f"List contains {type(dataset).__name__}  instead of squares.")
                )
            )
        return SearchResult.empty()
    
    