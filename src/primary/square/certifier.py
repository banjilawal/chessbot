# src/certifier/square/cerifier.py

"""
Module: certifier.square.certifier
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Any, cast

from blueprint import SquareBlueprint
from err import FormationNullException, SquareCertifierException, SquareEntityOperandNullException
from model import Board, Coord, HomeSquare, Square
from operand import SquareEntityOperand
from primary import RootCertifier
from result import ValidationResult
from schema import Formation
from toolkit import SquareToolkit
from util import LoggingLevelRouter


class SquareRootCertifier(RootCertifier[SquareBlueprint]):
    """
    Role
        -   Transaction Worker
        -   Integrity Maintenance
        -   Consistency Assurance
        -   Process Runner

    Responsibilities:
        1.  Ensure a SquareBlueprint instance is certified safe, reliable and consistent before use.

    Attributes:
        toolkit: SquareToolkit

    Provides:
        -   execute(self, candidate: Any) -> ValidationResult:

    Super Class:
        Certifier
    """
    
    def __init__(
            self,
            toolkit: SquareToolkit | None = SquareToolkit()
    ):
        """
        Args:
            toolkit: SquareToolkit
        """
        super().__init__(toolkit=toolkit)
    
    @property
    def toolkit(self) -> SquareToolkit:
        return cast(SquareToolkit, super().toolkit)
    
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ValidationResult:
        """
        Certify a candidate is a SquareBlueprint that is safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if any of the following
                occur
                    -   The validation_priming fails.
                    -   Either the board, owner or id get flagged unsafe.
            2.  Otherwise, send the success result.
        Args:
            candidate: Any,
        Returns:
            ValidationResult
        Raises:
            SquareCertifierException
        """
        method = f"{self.__class__.__name__}.execute"
        
        operand_validation = self.toolkit.priming_validator.execute(
            candidate=candidate,
            target_model=SquareEntityOperand,
            null_exception=SquareEntityOperandNullException()
        )
        if operand_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                SquareCertifierException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=SquareCertifierException.MSG,
                    err_code=SquareCertifierException.ERR_CODE,
                    ex=operand_validation.exception,
                )
            )
        operand = cast(SquareEntityOperand, operand_validation.payload)
        if operand.is_empty:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                SquareCertifierException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=SquareCertifierException.MSG,
                    err_code=SquareCertifierException.ERR_CODE,
                    ex=SquareEntityOperandNullException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=SquareEntityOperandNullException.MSG,
                        err_code=SquareEntityOperandNullException.ERR_CODE,
                    ),
                )
            )
        # --- Cast the candidate into a TokenBlueprint for additional tests. ---#
        blueprint = operand.extract_blueprint()
        
        # Handle the case that, any id in the blueprint is flagged.
        id_test = self.toolkit.identity_service.validate_blueprint_id(
            owner_blueprint=blueprint,
            owner_name=blueprint.owner_name,
        )
        if id_test.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                SquareCertifierException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=SquareCertifierException.MSG,
                    err_code=SquareCertifierException.ERR_CODE,
                    ex=id_test.exception,
                )
            )
        name_test = self.toolkit.identity_service.validate_name.execute(
            candidate=blueprint.name,
        )
        if name_test.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                SquareCertifierException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=SquareCertifierException.MSG,
                    err_code=SquareCertifierException.ERR_CODE,
                    ex=name_test.exception,
                )
            )
        # Handle the case that, square.coord is not safe.
        coord_test = self.toolkit.coord_validator.execute(blueprint.coord)
        if coord_test.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                SquareCertifierException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=SquareCertifierException.MSG,
                    err_code=SquareCertifierException.ERR_CODE,
                    ex=coord_test.exception,
                )
            )
        # Handle the case that, square.board does not pass a validation check.
        board_test = self.toolkit.board_validator.execute(blueprint.board)
        if board_test.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                SquareCertifierException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=SquareCertifierException.MSG,
                    err_code=SquareCertifierException.ERR_CODE,
                    ex=board_test.exception,
                )
            )

        formation = None
        if operand.is_home_square_operand:
            formation_test = self.toolkit.priming_validator.execute(
                candidate=blueprint.formation,
                target_model=Formation,
                null_exception=FormationNullException()
            )
            if formation_test.is_failure:
                # Send the exception chain on failure.
                return ValidationResult.failure(
                    SquareCertifierException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=SquareCertifierException.MSG,
                        err_code=SquareCertifierException.ERR_CODE,
                        ex=formation_test.exception,
                    )
                )
            formation = cast(Formation, formation_test.payload)
            
            
        # --- Extract and cast payloads of the validation results. ---#
        id = cast(int, id_test.payload)
        name = cast(str, name_test.payload)
        board = cast(Board, board_test.payload)
        coord = cast(Coord, coord_test.payload)
        
        
        if operand.is_home_square_operand:
            return ValidationResult.success(
                HomeSquare(
                    id=id,
                    name=name,
                    board=board,
                    coord=coord,
                    formation=formation,
                )
            )
        if operand.is_model_operand:
            return ValidationResult.success(
                Square(
                    id=id,
                    name=name,
                    board=board,
                    coord=coord,
                )
            )
        # --- Forward the work product to the caller. ---#
        return ValidationResult.success(
            SquareBlueprint(
                id=id,
                name=name,
                board=board,
                coord=coord,
                formation=formation,
            )
        )