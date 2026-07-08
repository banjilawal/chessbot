# src/tester/extractor/home/extractor.py

"""
Module: tester.extractor.home.extractor
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import cast

from blueprint import TokenBlueprint
from err import BlueprintHomeSquareExtractorException
from model import Board, HomeSquare, Square
from result import ValidationResult
from toolkit import TokenToolkit
from util import LoggingLevelRouter


class BlueprintHomeSquareExtractor:
    """
    Role
        -   Transaction Worker
        -   Integrity Maintenance
        -   Consistency Assurance
        -   Process Runner

    Responsibilities:
        1.  Validate a TokenBlueprint's home_square if it exists. Otherwise, find it using
            the formation and board.


    Attributes:
        toolkit: TokenToolkit

    Provides:
        -   execute(self, blueprint: TokenBlueprint) -> ValidationResult
        -   _find_on_board(self, board: Board, square_name: str,) -> ValidationResult
        -   _validate_home_square(self, square: Square,) -> ValidationResult

    Super Class:
    """
    _toolkit: TokenToolkit
    
    def __init__(self, toolkit: TokenToolkit | None = TokenToolkit()):
        self._toolkit = toolkit
    
    @LoggingLevelRouter.monitor
    def execute(self, blueprint: TokenBlueprint) -> ValidationResult[HomeSquare]:
        """
        Process a TokenBlueprint's HomeSquare validator.

        Action:
            1.  If the blueprint's home_square is null:
                    -   Detect it using the blueprint's formation and board.
            2.  If the blueprint's home_square exists:
                    -   Validate it.
            3.  Send an exception chain in the ValidationResult if either route fails.
            4.  Send the success result from either route taken.
        Args:
            blueprint: TokenBlueprint
            toolkit: TokenToolkit
        Returns:
            ValidationResult[HomeSquare]
        Raises:
            BlueprintHomeSquareExtractorException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # --- If the TokenBlueprint does not have its home_square set find it. ---#
        if blueprint.home_square is None:
            detection_result = self._find_on_board(
                board=blueprint.team.board,
                square_name=blueprint.formation.home_square_name,
                home_square_detector=self._toolkit.home_square_detector,
            )
            # Handle the case that the _find_on_board raised an error.
            if detection_result.is_failure:
                return ValidationResult.failure(
                    BlueprintHomeSquareExtractorException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=BlueprintHomeSquareExtractorException.MSG,
                        err_code=BlueprintHomeSquareExtractorException.ERR_CODE,
                        ex=detection_result.exception,
                    )
                )
            # --- Forward the work product to the caller. ---#
            return ValidationResult.success(detection_result.payload)
        
        # --- For the default case, validate the home_square which already exists in the TokenBlueprint. ---#
        validation_result = self._validate_home_square(
            square=blueprint.home_square,
        )
        if validation_result.is_failure:
            # Handle the case that the _validate_home_square raised an error.
            return ValidationResult.failure(
                BlueprintHomeSquareExtractorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=BlueprintHomeSquareExtractorException.MSG,
                    err_code=BlueprintHomeSquareExtractorException.ERR_CODE,
                    ex=validation_result.exception,
                )
            )
        # --- Forward the work product to the caller. ---#
        return validation_result
        
    @LoggingLevelRouter.monitor
    def _find_on_board(self, board: Board, square_name: str,) -> ValidationResult:
        """
        Detect the HomeSquare from the Board when its not in the TokenBlueprint.

        Action:
            1.  Send an exception chain in the ValidationResult if the detector fails.
            2.  Otherwise, Send the success result.
        Args:
            board: Board
            square_name: str
        Returns:
            ValidationResult[HomeSquare]
        Raises:
            BlueprintHomeSquareExtractorException
        """
        method = f"{self.__class__.__name__}._find_on_board"
        
        # --- Run the home_square_detector. ---#
        detection_result = self._toolkit.home_square_detector.execute(
            board=board,
            square_name=square_name,
        )
        # Handle the case that, the detector aborts.
        if detection_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                BlueprintHomeSquareExtractorException(
                    msg=BlueprintHomeSquareExtractorException.MSG,
                    err_code=BlueprintHomeSquareExtractorException.ERR_CODE,
                    ex=detection_result.exception,
                )
            )
        # --- Forward the work product to the caller. ---#
        return ValidationResult.success(detection_result.payload)        
        
    @LoggingLevelRouter.monitor
    def _validate_home_square(self, square: Square,) -> ValidationResult:
        """
        Verify TokenBlueprint.home_square when its set.

        Action:
            1.  Send an exception chain in the ValidationResult if any following occurs:
                    -   square is not validated.
                    -   It's not a HomeSquare.
            2.  Otherwise, Send the success result.
        Args:
            square: Square,
        Returns:
            ValidationResult[Blueprint]
        Raises:
            BlueprintHomeSquareExtractorException
        """
        method = f"{self.__class__.__name__}._validate_home_square"
        
        # Handle the case that, the square is flagged.
        validation_result = self._toolkit.square_validator.execute(square)
        if validation_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                BlueprintHomeSquareExtractorException(
                    msg=BlueprintHomeSquareExtractorException.MSG,
                    err_code=BlueprintHomeSquareExtractorException.ERR_CODE,
                    ex=validation_result.exception,
                )
            )
        # Handle the case that, the square is the wrong type.
        if not isinstance(square, HomeSquare):
            # Send the exception chain on failure.
            return ValidationResult.failure(
                BlueprintHomeSquareExtractorException(
                    msg=BlueprintHomeSquareExtractorException.MSG,
                    err_code=BlueprintHomeSquareExtractorException.ERR_CODE,
                    ex=TypeError(f"Expected HomeSquare got Square instead."),
                )
            )
        # --- Forward the work product to the caller. ---#
        return ValidationResult.success(cast(HomeSquare, square))
