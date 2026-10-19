# src/fabrication/loader/model/board/loader.py

"""
Module: fabrication.loader.model.board.loader
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import BuildResult
from domain import Board, BoardBlueprint
from err import BoardBuildLoaderException, BoardBuildRequestNullException
from exchange import BoardBuildRequest, BoardValidationRequest, BoardValidationService
from fabrication import ModelBuildLoader
from util import IdFactory, LoggingLevelRouter


class BoardBuildLoader(ModelBuildLoader[Board]):
    """
    Role
        -   Authorization
        -   Bootstrapper
        
    Responsibilities:
        1.  Initialize the Board build process by preparing a BoardBlueprint
            if the BuildRequest is correct.

    Attributes:
        validator: BoardValidationServer

    Provides:
        -   def execute(request: BoardBuildRequest) -> BuildResult[BoardBlueprint]

    Super Class:
        BuildLoader
    """
    
    def __init__(
            self,
            validator: Optional[BoardValidationService] | None = None,
    ):
        """
        Args:
            validator: Optional[BoardValidationServer]
        """
        super().__init__(validator=validator or BoardValidationService())
    
    @property
    def validator(self) -> BoardValidationService:
        return cast(BoardValidationService, super().validator)
        
    @LoggingLevelRouter.monitor
    def execute(self, request: BoardBuildRequest) -> BuildResult[BoardBlueprint]:
        """
        Prepare a BoardBlueprint which guarantees a safe Board.
        
        Action:
            1.  Send an exception chain in the BuildResult if any of the following occur
                    -   The request is null or the wrong type.
                    -   The request does not contain a valid BoardBlueprint.
            2.  Otherwise, forward the safe blueprint.
        Args:
            request: BoardBuildRequest
        Returns:
            BuildResult[BoardBlueprint]
        Raises:
            BoardBuildLoaderException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # --- Verify the request is safe. ---#
        priming = self.priming_validator.execute(
            candidate=request,
            target_model=BoardBuildRequest,
            null_exception=BoardBuildRequestNullException(),
        )
        # Handle the case that the request is flagged.
        if priming.is_failure:
            # Send the exception chain on failure.
            return BuildResult.failure(
                BoardBuildLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=BoardBuildLoaderException.MSG,
                    err_code=BoardBuildLoaderException.ERR_CODE,
                    ex=priming.exception,
                )
            )
        # --- Cast the priming result for additional processing. ---#
        build_request = cast(BoardBuildRequest, priming.payload)
        
        # Handle the case that the blueprint is faulty.
        blueprint_validation = self.validator.extract_blueprint(
            request=BoardValidationRequest(
                item=build_request.item,
                id=IdFactory.next_id(class_name="BoardValidationRequest")
            )
        )
        # Send the exception chain on failure.
        if blueprint_validation.is_failure:
            return BuildResult.failure(
                BoardBuildLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=BoardBuildLoaderException.MSG,
                    err_code=BoardBuildLoaderException.ERR_CODE,
                    ex=blueprint_validation.exception
                )
            )
        # --- Forward the work product. ---#
        blueprint = cast(BoardBlueprint, blueprint_validation.payload)
        return BuildResult.success(blueprint)