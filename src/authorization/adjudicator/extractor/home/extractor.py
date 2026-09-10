# src/authorization/adjudicator/extractor/home/extractor.py

"""
Module: authorization.adjudicator.extractor.home.extractor
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from assurance import TokenValidatorToolkit
from domain import Board, Formation, HomeSquare, Square, SquareContext, TokenBlueprint
from err import BlueprintHomeSquareExtractorException, SquareSearchResultEmptyException
from artifcat import ValidationResult
from util import LoggingLevelRouter


class BlueprintHomeSquareExtractor:
    """
    Role
        - Transaction Worker
        - Integrity Maintenance
        - Consistency Assurance
        - Process Runner

    Responsibilities:
        1.  Validate a TokenBlueprint's home_square if it exists. Otherwise, find it using
            the formation and board.


    Attributes:
        bundle: TokenValidationToolkit

    Provides:
        - execute(self, blueprint: TokenBlueprint) -> ValidationResult
        - _find_on_board(self, board: Board, square_name: str,) -> ValidationResult
        - _validate_home_square(self, square: Square,) -> ValidationResult

    Super Class:
    """
    _toolkit: TokenValidatorToolkit
    
    def __init__(
            self,
            toolkit: Optional[TokenValidatorToolkit] | None = None,
    ):
        self._bundle = toolkit or TokenValidatorToolkit()
    
    @LoggingLevelRouter.monitor
    def execute(self, blueprint: TokenBlueprint) -> ValidationResult[HomeSquare]:
        """
        Process a TokenBlueprint's HomeSquare validator.

        Action:
            1.  If the blueprint's home_square is null:
                    - Detect it using the blueprint's formation and board.
            2.  If the blueprint's home_square exists:
                    - Validate it.
            3.  Send an exception chain in the ValidationResult if either route fails.
            4.  Send the success result from either route taken.
        Args:
            blueprint: TokenBlueprint
            bundle: TokenValidationToolkit
        Returns:
            ValidationResult[HomeSquare]
        Raises:
            BlueprintHomeSquareExtractorException
        """
        method = f"{self.__class__.__name__}.execute"
        
        home_square = blueprint.home_square
        # --- If the TokenBlueprint does not have its home_square set find it. ---#
        if home_square is None:
            detection = self._detect_home_square(
                board=blueprint.team.board,
                formation=blueprint.formation,
            )
            # Handle the case that the _find_on_board raised an error.
            if detection.is_failure:
                return ValidationResult.failure(
                    BlueprintHomeSquareExtractorException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=BlueprintHomeSquareExtractorException.MSG,
                        err_code=BlueprintHomeSquareExtractorException.ERR_CODE,
                        ex=detection.exception,
                    )
                )
            # --- Forward the work product to the caller. ---#
            return ValidationResult.success(cast(HomeSquare, detection.payload))
        
        # --- For the default case, validate the home_square which already exists in the TokenBlueprint. ---#
        validation = self._validate_home_square(square=home_square)
        if validation.is_failure:
            # Handle the case that the _validate_home_square raised an error.
            return ValidationResult.failure(
                BlueprintHomeSquareExtractorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=BlueprintHomeSquareExtractorException.MSG,
                    err_code=BlueprintHomeSquareExtractorException.ERR_CODE,
                    ex=validation.exception,
                )
            )
        # --- Forward the work product to the caller. ---#
        return ValidationResult.success(cast(HomeSquare, validation.payload))
        
    @LoggingLevelRouter.monitor
    def _detect_home_square(self, board: Board, formation: Formation) -> ValidationResult:
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
        search = board.squares.search.execute(context=SquareContext(formation=formation))
        
        # Handle the case that HomeSquare search aborts
        if search.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                BlueprintHomeSquareExtractorException(
                    msg=BlueprintHomeSquareExtractorException.MSG,
                    err_code=BlueprintHomeSquareExtractorException.ERR_CODE,
                    ex=search.exception,
                )
            )
        # Handle the case that the HomeSquare is not found.
        if search.is_empty:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                BlueprintHomeSquareExtractorException(
                    msg=BlueprintHomeSquareExtractorException.MSG,
                    err_code=BlueprintHomeSquareExtractorException.ERR_CODE,
                    ex=SquareSearchResultEmptyException(
                        msg=BlueprintHomeSquareExtractorException.MSG,
                        err_code=BlueprintHomeSquareExtractorException.ERR_CODE,
                    ),
                )
            )
        # --- Otherwise, forward the work product to the caller. ---#
        home_square = cast(HomeSquare, search.payload)
        return ValidationResult.success(home_square)
        
    @LoggingLevelRouter.monitor
    def _validate_home_square(self, square: Square,) -> ValidationResult:
        """
        Verify TokenBlueprint.home_square when its set.

        Action:
            1.  Send an exception chain in the ValidationResult if any following occurs:
                    - square is not validated.
                    - It's not a HomeSquare.
            2.  Otherwise, Send the success result.
        Args:
            square: Square,
        Returns:
            ValidationResult[Blueprint]
        Raises:
            BlueprintHomeSquareExtractorException
        """
        method = f"{self.__class__.__name__}._validate_home_square"
        
        # Handle the case that the square is flagged.
        validation_result = self._bundle.square_validator.execute(square)
        if validation_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                BlueprintHomeSquareExtractorException(
                    msg=BlueprintHomeSquareExtractorException.MSG,
                    err_code=BlueprintHomeSquareExtractorException.ERR_CODE,
                    ex=validation_result.exception,
                )
            )
        # Handle the case that the square is the wrong type.
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
