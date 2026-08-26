# src/assurance/validator/domain/model/square/assurance/validator/domain/model.py

"""
Module: assurance.validator.domain.model.square.checker
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, cast

from assurance import ModelValidator
from domain import SquareBlueprint
from util import LoggingLevelRouter


class SquareValidator(ModelValidator[SquareBlueprint]):
    """
    Role
        -  Integrity, Consistency Maintenance

    Responsibilities:
        1.  Ensure a SquareBlueprint instance is certified safe, reliable and consistent before use.

    Attributes:
        bundle: SquareToolkit

    Provides:
        -  execute(self, candidate: Any) -> ValidationResult:

    Super Class:
        IntegrityChecker
    """
    
    def __init__(
            self,
            bundle: SquareToolkit | None = SquareToolkit()
    ):
        """
        Args:
            bundle: SquareToolkit
        """
        super().__init__(bundle=bundle)
    
    @property
    def toolkit(self) -> SquareBundle:
        return cast(SquareToolkit, super().bundle)
    
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ValidationResult:
        """
        Certify a candidate is a SquareBlueprint that is safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if any of the following
                occur
                    -  The validation_priming fails.
                    -  Either the board, owner or id get flagged unsafe.
            2.  Otherwise, send the success result.
        Args:
            candidate: Any,
        Returns:
            ValidationResult
        Raises:
            SquareCheckerException
        """
        method = f"{self.__class__.__name__}.execute"
        
        carrier_validation = self.toolkit.priming_validator.execute(
            candidate=candidate,
            target_model=SquareCarrier,
            null_exception=SquareCarrierNullException()
        )
        if carrier_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                SquareCheckerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=SquareCheckerException.MSG,
                    err_code=SquareCheckerException.ERR_CODE,
                    ex=carrier_validation.exception,
                )
            )
        carrier = cast(SquareCarrier, carrier_validation.payload)
        if carrier.is_not_carrying_anything:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                SquareCheckerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=SquareCheckerException.MSG,
                    err_code=SquareCheckerException.ERR_CODE,
                    ex=SquareCarrierNullException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=SquareCarrierNullException.MSG,
                        err_code=SquareCarrierNullException.ERR_CODE,
                    ),
                )
            )
        # --- Cast the candidate into a TokenBlueprint for additional tests. ---#
        blueprint = carrier.extract_blueprint()
        
        # Handle the case that, any id in the blueprint is flagged.
        id_test = self.toolkit.identity_service.validate_blueprint_id(
            owner_blueprint=blueprint,
            owner_name=blueprint.model_class_name,
        )
        if id_test.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                SquareCheckerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=SquareCheckerException.MSG,
                    err_code=SquareCheckerException.ERR_CODE,
                    ex=id_test.exception,
                )
            )
        name_test = self.toolkit.identity_service.validate_name.execute(
            candidate=blueprint.name,
        )
        if name_test.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                SquareCheckerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=SquareCheckerException.MSG,
                    err_code=SquareCheckerException.ERR_CODE,
                    ex=name_test.exception,
                )
            )
        # Handle the case that, square.coord is not safe.
        coord_test = self.toolkit.coord_checker.execute(blueprint.coord)
        if coord_test.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                SquareCheckerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=SquareCheckerException.MSG,
                    err_code=SquareCheckerException.ERR_CODE,
                    ex=coord_test.exception,
                )
            )
        # Handle the case that, square.board does not pass a validation check.
        board_test = self.toolkit.board_checker.execute(blueprint.board)
        if board_test.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                SquareCheckerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=SquareCheckerException.MSG,
                    err_code=SquareCheckerException.ERR_CODE,
                    ex=board_test.exception,
                )
            )

        formation = None
        if carrier.is_home_square_carrier:
            formation_test = self.toolkit.priming_validator.execute(
                candidate=blueprint.formation,
                target_model=Formation,
                null_exception=FormationNullException()
            )
            if formation_test.is_failure:
                # Send the exception chain on failure.
                return ValidationResult.failure(
                    SquareCheckerException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=SquareCheckerException.MSG,
                        err_code=SquareCheckerException.ERR_CODE,
                        ex=formation_test.exception,
                    )
                )
            formation = cast(Formation, formation_test.payload)
            
            
        # --- Extract and cast payloads of the validation results. ---#
        id = cast(int, id_test.payload)
        name = cast(str, name_test.payload)
        board = cast(Board, board_test.payload)
        coord = cast(Coord, coord_test.payload)
        
        
        if carrier.is_home_square_carrier:
            return ValidationResult.success(
                HomeSquare(
                    id=id,
                    name=name,
                    board=board,
                    coord=coord,
                    formation=formation,
                )
            )
        if carrier.is_carrying_model:
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