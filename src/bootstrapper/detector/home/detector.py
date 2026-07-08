# src/bootstrapper/detector/home/detector.py

"""
Module: bootstrapper.detector.home.detector
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Optional, cast

from bootstrapper import DetectorBootstrapper
from context import TokenHomeContext
from err import (
    ExcessContextFlagsException, HomeDetectorBootstrapperException, HomeSquareSearchResultEmptyException,
    ZeroContextFlagsException
)
from microservice import IdentityService
from model import Board, HomeSquare, SquareContext, Token
from result import Result
from util import LoggingLevelRouter
from validator import BoardValidator, TokenValidator


class HomeDetectorBootstrapper(DetectorBootstrapper):
    """
    Role:
        - Transaction Worker
        - Search
        
    Responsibilities:
        1.  Find a token's home square.
    
    Attributes:
    
    Provides:
        -   execute(
                    token: Token,
                    token_validator: TokenFreedomAnalyzer,
            ) -> Result[HomeSquareClaimReport]
            
    Super Class:
    """

    @classmethod
    @LoggingLevelRouter.monitor
    def execute(
            cls,
            context: TokenHomeContext,
            toolkit: Toke,
    ) -> Result[HomeSquare]:
        """
        Find the token's home square.
        
        Action:
            1.  Send an exception chain in the Result if any of the conditions occur.
                    -   The token is not safe.
                    -   The search for the home square is not completed.
                    -   The home square was not found.
            2.  Otherwise, send the success result.
        Args:
            token: Optional[Token]
            board: Optional[Board]
            square_name: Optional[str]
            board_validator: BoardValidator
            token_validator: TokenValidator
            identity_service: IdentityService
        Returns:
            Result[HomeSquare]
        Raises:
            HomeDetectorBootstrapperException
            DuplicateTokenDeploymentException
            HomeSquareSearchResultEmptyException
        """
        method = f"{cls.__class__.__name__}.validator"
        
        # --- Supply any missing dependencies. ---#
        if board_validator is None:
            board_validator = BoardValidator()
        if token_validator is None:
            token_validator = TokenValidator()
        if identity_service is None:
            identity_service = IdentityService()
        
        # --- Count how many optional parameters are not-null. only one should be not null. ---#
        params = [token, square_name]
        param_count = sum(bool(p) for p in params)
        
        # Handle the case that, all the optional params are null.
        if param_count == 0:
            # Send the exception chain on failure.
            return Result.failure(
                HomeDetectorBootstrapperException(
                    cls_mthd=method,
                    cls_name=cls.__class__.__name__,
                    msg=HomeDetectorBootstrapperException.MSG,
                    err_code=HomeDetectorBootstrapperException.ERR_CODE,
                    ex=ZeroContextFlagsException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        msg=ZeroContextFlagsException.MSG,
                        err_code=ZeroContextFlagsException.ERR_CODE,
                    ),
                )
            )
        # Handle the case that, the enabled param is not the token.
        if param_count > 1 and token is None:
            # Send the exception chain on failure.
            return Result.failure(
                HomeDetectorBootstrapperException(
                    cls_mthd=method,
                    cls_name=cls.__class__.__name__,
                    msg=HomeDetectorBootstrapperException.MSG,
                    err_code=HomeDetectorBootstrapperException.ERR_CODE,
                    ex=ExcessContextFlagsException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        msg=ExcessContextFlagsException.MSG,
                        err_code=ExcessContextFlagsException.ERR_CODE,
                    ),
                )
            )
        # Handle the case that, two params are enabled and one is the token.
        if param_count > 1 and square_name is None or board is None:
            # Send the exception chain on failure.
            return Result.failure(
                HomeDetectorBootstrapperException(
                    cls_mthd=method,
                    cls_name=cls.__class__.__name__,
                    msg=HomeDetectorBootstrapperException.MSG,
                    err_code=HomeDetectorBootstrapperException.ERR_CODE,
                    ex=ExcessContextFlagsException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        msg=ExcessContextFlagsException.MSG,
                        err_code=ExcessContextFlagsException.ERR_CODE,
                    ),
                )
            )
        # --- Route to the appropriate validation/ branch. ---#
        
        # Validating the name if its enabled.
        if square_name is not None and board is not None:
            name_validation_result = identity_service.validate_name(square_name)
            if name_validation_result.is_failure:
                # Send the exception chain on failure.
                return Result.failure(
                    HomeDetectorBootstrapperException(
                        cls_mthd=method,
                        cls_name=cls.__class__.__name__,
                        msg=HomeDetectorBootstrapperException.MSG,
                        err_code=HomeDetectorBootstrapperException.ERR_CODE,
                        ex=name_validation_result.exception,
                    )
                )
            board_validation_result = board_validator.execute(board)
            if board_validation_result.is_failure:
                # Send the exception chain on failure.
                return Result.failure(
                    HomeDetectorBootstrapperException(
                        cls_mthd=method,
                        cls_name=cls.__class__.__name__,
                        msg=HomeDetectorBootstrapperException.MSG,
                        err_code=HomeDetectorBootstrapperException.ERR_CODE,
                        ex=board_validation_result.exception,
                    )
                )
            
        # Validate the token if its enabled.
        if token is not None:
            # --- Perform analysis to see if the token is free. ---#
            token_validation_result = token_validator.execute(token)
            
            # Handle the case that, the analysis is not completed.
            if token_validation_result.is_failure:
                # Send the exception chain on failure.
                return Result.failure(
                    HomeDetectorBootstrapperException(
                        cls_mthd=method,
                        cls_name=cls.__class__.__name__,
                        msg=HomeDetectorBootstrapperException.MSG,
                        err_code=HomeDetectorBootstrapperException.ERR_CODE,
                        ex=token_validation_result.exception,
                    )
                )
            # Set the square_name to use in the search.
            square_name = token.formation.home_square_name
            board = token.team.board
            
            
        # --- Search for the token's opening square. ---#
        home_search_result = board.squares.search(context=SquareContext(name=square_name))
        # Handle the case that, searching for the opening square is not completed.
        if home_search_result.is_failure:
            # Send the exception chain on failure.
            return Result.failure(
                HomeDetectorBootstrapperException(
                    cls_mthd=method,
                    cls_name=cls.__class__.__name__,
                    msg=HomeDetectorBootstrapperException.MSG,
                    err_code=HomeDetectorBootstrapperException.ERR_CODE,
                    ex=home_search_result.exception,
                )
            )
        # Handle the case that, the opening square is not found.
        if home_search_result.is_empty:
            # Send the exception chain on failure.
            return Result.failure(
                HomeDetectorBootstrapperException(
                    cls_mthd=method,
                    cls_name=cls.__class__.__name__,
                    msg=HomeDetectorBootstrapperException.MSG,
                    err_code=HomeDetectorBootstrapperException.ERR_CODE,
                    ex=HomeSquareSearchResultEmptyException(
                        msg=HomeSquareSearchResultEmptyException.MSG,
                        err_code=HomeSquareSearchResultEmptyException.ERR_CODE,
                        var=f"home_square:{token.home_square.name}",
                        val=token.home_square,
                    ),
                )
            )
        # --- Send the work product ---#
        return Result.success(cast(HomeSquare, home_search_result.payload[0]))