# src/transit/dispatcher/fabrication/model/board/validator.py

"""
Module: transit.dispatcher.fabrication.model.board.validator
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, cast


from assurance import BoardValidator
from artifcat import BuildResult
from domain import Board
from err import BoardBuildDispatcherException
from transit import ModelBuildDispatcher, BoardCarrier
from util import LoggingLevelRouter


class BoardBuildDispatcher(ModelBuildDispatcher[Board]):
    """
    Role
        -   Integrity Assurance Manager

    Responsibilities:
        1.  Direct the BoardBuild workflow.

    Attributes:
        validator: BoardValidator

    Provides:
        -   def execute(self, candidate: Any) -> BuildResult[validatorCarrier]

    Super Class:
        ModelBuildDispatcher
    """

    def __init__(
            self,
            validator: BoardValidator | None = None,
    ):
        super().__init__(validator=validator or BoardValidator())
        
    @property
    def validator(self) -> BoardValidator:
        return cast(BoardValidator, super().validator)
    

    @LoggingLevelRouter.monitor
    def execute(self, job: Any) -> BuildResult[BoardCarrier]:
        """
        Forward a job to a BoardValidator then deliver the result.

        Action:
            1.  Send an exception chain in the BuildResult if the validator cannot
                certify the job's content.
            2.  Otherwise, cast the job payload into a BoardCarrier and send in
                the success result.
        Args:
            job: Any
        Returns:
            BuildResult[BoardCarrier]
        Raises:
             BoardBuildDispatcherException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the candidate is not safe.
        build = self.validator.execute(job)
        if build.is_failure:
            # Send the exception chain on failure.
            return BuildResult.failure(
                BoardBuildDispatcherException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=BoardBuildDispatcherException.MSG,
                    err_code=BoardBuildDispatcherException.ERR_CODE,
                    ex=build.exception,
                )
            )
        # --- Forward the work product to the caller. ---#
        carrier = cast(BoardCarrier, build.payload)
        return BuildResult.success(carrier)