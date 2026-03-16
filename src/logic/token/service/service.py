# src/logic/token/service/service.py

"""
Module: logic.token.service.service
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""

from __future__ import annotations

from copy import deepcopy
from typing import cast

from logic.coord import Coord, CoordService
from logic.rank import Rank, RankService
from logic.schema import SchemaService
from logic.system import DeletionResult, IdFactory, InsertionResult, IntegrityService, LoggingLevelRouter, UpdateResult
from logic.token import PawnToken, Token, TokenFactory, TokenHandler, TokenServiceException, TokenValidator


class TokenService(IntegrityService[Token]):
    """
    # ROLE: Service, Lifecycle Management, Encapsulation, API layer, Computation, Transformer,.

    # LOCAL RESPONSIBILITIES:
    
    # INHERITED RESPONSIBILITIES:
        *   See IntegrityService class for inherited responsibilities.

    # PARENT:
        *   IntegrityService

    # PROVIDES:
    None

    Attributes:
        handler: TokenHandler

    # INHERITED ATTRIBUTES:
        *   See IntegrityService class for inherited attributes.

    # CONSTRUCTOR:
        id: int
        name: str
        handler: TokenHandler
        builder: TokenFactory
        validator: TokenValidator

    Methods:
        push_coord_to_token(token: Token, position: Coord, coord_service: CoordService) -> InsertionResult:
        promote_pawn(
                    self,
                    pawn_token: PawnToken,
                    new_rank: Rank,
                    rank_service: RankService = RankService()
            ) -> UpdateResult[PawnToken]:
        deploy_on_board(self,token: Token) -> InsertionResult[bool]:
        pop_coord_from_token(self, token) -> DeletionResult[Coord]:

    # INHERITED METHODS:
        *   See IntegrityService class for inherited methods.
    """
    SERVICE_NAME = "TokenService"
    _handler: TokenHandler
    
    def __init__(
            self,
            name: str = SERVICE_NAME,
            handler: TokenHandler = TokenHandler(),
            builder: TokenFactory = TokenFactory(),
            validator: TokenValidator = TokenValidator(),
            id: int = IdFactory.next_id(class_name="TokenService"),
    ):
        """
        Args:
            id: int
            name: str
            handler: TokenHandler
            builder: TokenFactory
            validator: TokenValidator
        """
        super().__init__(id=id, name=name, builder=builder, validator=validator)
        self._handler = handler
    
    @property
    def builder(self) -> TokenFactory:
        """get TokenFactory"""
        return cast(TokenFactory, self.entity_builder)
    
    @property
    def validator(self) -> TokenValidator:
        """get TokenValidator"""
        return cast(TokenValidator, self.entity_validator)
    
    @property
    def handler(self) -> TokenHandler:
        return self._handler
    
    @LoggingLevelRouter.monitor
    def pop_coord_from_token(self, token) -> DeletionResult[Coord]:
        """
        Undo the token's last move.
        
        Action:
            If the deletion fails, send an exception chain. Otherwise, send the success result.
        Args:
            token: Token
        Returns:
            DeletionResult[Coord]
        Raises:
            TokenServiceException
        """
        method = f"{self.__class__.__name__}.pop_coord_from_token"
        
        #--- Forward the request to the handler. ---#
        popping_coord_result = self._handler.coord.undo_current_token_position(
            token=token,
            token_validator=self.validator,
        )
        # Handle the case that, the request was not completed.
        if popping_coord_result.is_failure:
            # Return the exception chain on failure.
            return DeletionResult.failure(
                TokenServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenServiceException.MSG,
                    err_code=TokenServiceException.ERR_CODE,
                    ex=popping_coord_result.exception,
                )
            )
        # --- Forward the work product to the caller. ---#
        return popping_coord_result
    
    @LoggingLevelRouter.monitor
    def push_coord_to_token(
            self,
            token: Token,
            coord: Coord,
            coord_service: CoordService = CoordService()
    ) -> InsertionResult:
        """
        Record the token's last move.

        Action:
            If the insert fails, send an exception chain. Otherwise, send the success result.
        Args:
            token: Token
            coord: Coord
            coord_service
        Returns:
            InsertionResult[bool]
        Raises:
            TokenServiceException
        """
        method = f"{self.__class__.__name__}.push_coord_to_token"
        
        # --- Forward the request to the handler. ---#
        insertion_result = self._handler.coord.push_coord(
            token=token,
            coord=coord,
            coord_service=coord_service,
            token_validator=self.validator,
        )
        # Handle the case that, the request was not completed.
        if insertion_result.is_failure:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                TokenServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenServiceException.MSG,
                    err_code=TokenServiceException.ERR_CODE,
                    ex=insertion_result.exception,
                )
            )
        # --- Forward the work product to the caller. ---#
        return insertion_result
    
    @LoggingLevelRouter.monitor
    def promote_pawn(
            self,
            rank: Rank,
            pawn_token: PawnToken,
            rank_service: RankService = RankService(),
            schema_service: SchemaService = SchemaService(),
    ) -> UpdateResult[PawnToken]:
        """
        Promote the PawnToken.

        Action:
            If the promotion fails, send unmodified token along with an exception chain in the UpdateResult.
            Otherwise, send the success result.
        Args:
            rank: Rank
            pawn_token: PawnToken
            rank_service: RankService
            schema_service: SchemaService
        Returns:
            UpdateResult[PawnToken]
        Raises:
            TokenServiceException
        """
        method = f"{self.__class__.__name__}.promote_pawn"
        
        # --- Forward the request to the handler. ---#
        pre_update_pawn_token = deepcopy(pawn_token)
        promotion_result = self._handler.pawn_promotion.execute(
            rank=rank,
            pawn_token=pawn_token,
            rank_service=rank_service,
            schema_service=schema_service,
            token_validator=self.validator,
        )
        # Handle the case that, the request was not completed.
        if promotion_result.is_failure:
            # Return the exception chain on failure.
            return UpdateResult.update_failure(
                original=pre_update_pawn_token,
                exception=(
                    TokenServiceException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=TokenServiceException.MSG,
                        err_code=TokenServiceException.ERR_CODE,
                        ex=promotion_result.exception
                    )
                )
            )
        # --- Forward the work product to the caller. ---#
        return promotion_result
    
    @LoggingLevelRouter.monitor
    def deploy_on_board(self,token: Token,) -> UpdateResult[Token]:
        """
        Deploy the token on its opening square.

        Action:
            If the deployment fails, send unmodified token along with an exception chain in the UpdateResult.
            Otherwise, send the success result.
        Args:
            token: Token
        Returns:
            UpdateResult[Token]
        Raises:
            TokenServiceException
        """
        method = f"{self.__class__.__name__}.deploy_on_board"
        
        # --- Forward the request to the handler. ---#
        pre_update_token = deepcopy(token)
        deployment_result = self._handler.deployment.execute(
            token=token,
            token_validator=self.validator,
        )
        # Handle the case that, the request was not completed.
        if deployment_result.is_failure:
            # Return the exception chain on failure.
            return UpdateResult.update_failure(
                original=pre_update_token,
                exception=(
                    TokenServiceException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=TokenServiceException.MSG,
                        err_code=TokenServiceException.ERR_CODE,
                        ex=deployment_result.exception
                    )
                )
            )
        # --- Forward the work product to the caller. ---#
        return deployment_result
        
        
   
