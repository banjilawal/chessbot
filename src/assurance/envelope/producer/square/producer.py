# src/assurance/envelope/producer/square/producer.py

"""
Module: assurance.envelope.producer.square.producer
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Optional, cast

from artifcat import ValidationResult
from assurance import RootEnvelopeProducer, SquareLoader, SquareValidatorToolkit
from domain import Coord, Square, SquareState, SquarePrimeExtract, Board, Token
from err import (
    RootSquareValidatorException, SquareCarrierEmptyException,
    SquareConsistencyException, SquareStateNullException
)
from exchange import CoordValidationRequest, BoardValidationRequest, TokenValidationRequest
from transit import RootSquareEnvelope, CoordCarrier, BoardCarrier, SquareCarrier, TokenCarrier
from util import IdFactory, LoggingLevelRouter


class SquareEnvelopeProducer(RootEnvelopeProducer[Square]):
    """
    Role
        -   Integrity, Consistency Maintenance

    Responsibilities:
        1.  Runs safety checks on Square super class, then send a RootSquareEnvelope
            for additional processing.

    Attributes:
        loader: SquareLoader

    Provides:
        -   def execute(candidate: Any) -> ValidationResult[RootSquareEnvelope]

    Super Class:
        RootValidator
    """
    
    def __init__(
            self,
            loader: Optional[SquareLoader] | None = None
    ):
        """
        Args:
            loader: Optional[SquareLoader]
        """
        super().__init__(loader=loader or SquareLoader())
        
    @property
    def loader(self) -> SquareLoader:
        return cast(SquareLoader, super().loader)
    
    @property
    def toolkit(self) -> SquareValidatorToolkit:
        return self.loader.toolkit
    
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ValidationResult[RootSquareEnvelope]:
        """
        Assure a candidate's properties are reference for a Square

        Action:
            1.  Send an exception chain in the ValidationResult if any of the following
                occur
                    -   The Loader fails.
                    -   Coord, Name, State, id, HomeSquare or Board are flagged.
            2.  Otherwise, send a SquareProductEnvelope in the success result.
        Args:
            candidate: Any
        Returns:
           ValidationResult[SquareProductEnvelope]
        Raises:
            RootSquareValidatorException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the blueprint cannot be extracted.
        loading = self.loader.execute(candidate)
        if loading.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                RootSquareValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=RootSquareValidatorException.MSG,
                    err_code=RootSquareValidatorException.ERR_CODE,
                    ex=loading.exception,
                )
            )
        # --- Get the PrimeExtract and Blueprint for additional processing. ---#
        prime_extract = cast(SquarePrimeExtract, loading.payload)
        carrier = prime_extract.reference
        blueprint = carrier.extract_blueprint()
        
        # Handle the case that the blueprint is null
        if blueprint is None:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                RootSquareValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=RootSquareValidatorException.MSG,
                    err_code=RootSquareValidatorException.ERR_CODE,
                    ex=SquareCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=SquareCarrierEmptyException.MSG,
                        err_code=SquareCarrierEmptyException.ERR_CODE,
                    ),
                )
            )
        # --- PROCESS_THE_ID_ATTRIBUTE. ---#
        
        # Handle the case that any id in the blueprint is flagged.
        id_validation = self.toolkit.blueprint_id_extractor.execute(
            candidate=blueprint,
            blueprint_owner_name=blueprint.domain_class_name,
            blueprint_type=self.toolkit.types.blueprint,
            blueprint_null_exception=self.toolkit.nulls.blueprint,
        )
        if id_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                RootSquareValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=RootSquareValidatorException.MSG,
                    err_code=RootSquareValidatorException.ERR_CODE,
                    ex=id_validation.exception,
                )
            )
        # --- PROCESS_THE_NAME_ATTRIBUTE. ---#
        name_validation = self.toolkit.identity_service.validate_name(
            candidate=blueprint.name
        )
        # Handle the case that the name is flagged.
        if name_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                RootSquareValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=RootSquareValidatorException.MSG,
                    err_code=RootSquareValidatorException.ERR_CODE,
                    ex=name_validation.exception,
                )
            )
        # --- PROCESS_THE_STATE_ATTRIBUTE. ---#
        state_validation = self.toolkit.priming_validator.execute(
            candidate=blueprint.state,
            target_model=SquareState,
            null_exception=SquareStateNullException(),
        )
        # Handle the case that the state is flagged.
        if state_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                RootSquareValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=RootSquareValidatorException.MSG,
                    err_code=RootSquareValidatorException.ERR_CODE,
                    ex=state_validation.exception,
                )
            )
        # --- PROCESS_THE_COORD_ATTRIBUTE. ---#
        coord_validation = self.toolkit.wrapper.coord.extract_model(
            request=CoordValidationRequest(
                item=CoordCarrier(model=blueprint.coord),
                id=IdFactory.next_id(class_name="CoordValidationRequest"),
            )
        )
        # Handle the case that the coord is flagged.
        if coord_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                RootSquareValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=RootSquareValidatorException.MSG,
                    err_code=RootSquareValidatorException.ERR_CODE,
                    ex=coord_validation.exception,
                )
            )
        # --- PROCESS_THE_BOARD_ATTRIBUTE. ---#
        board_validation = self.toolkit.wrapper.board.extract_model(
            request=BoardValidationRequest(
                item=BoardCarrier(model=blueprint.board),
                id=IdFactory.next_id(class_name="BoardValidationRequest"),
            )
        )
        # Handle the case that the board is unsafe.
        if board_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                RootSquareValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=RootSquareValidatorException.MSG,
                    err_code=RootSquareValidatorException.ERR_CODE,
                    ex=board_validation.exception,
                )
            )
        # --- PROCESS_THE_OCCUPANT_ATTRIBUTE. ---#
        occupant = blueprint.occupant
        
        # Handle the case that an inconsistency between occupant and state exists.
        if blueprint.is_not_consistent:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                RootSquareValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=RootSquareValidatorException.MSG,
                    err_code=RootSquareValidatorException.ERR_CODE,
                    ex=SquareConsistencyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=SquareConsistencyException.MSG,
                        err_code=SquareConsistencyException.ERR_CODE,
                    )
                )
            )
        if occupant is not None:
            occupant_validation = self.toolkit.wrapper.token.extract_model(
                request=TokenValidationRequest(
                    item=TokenCarrier(model=occupant),
                    id=IdFactory.next_id(class_name="TokenValidationRequest")
                )
            )
            # Handle the case that the existing occupant is not safe.
            if occupant_validation.is_failure:
                # Send the exception chain on failure.
                return ValidationResult.failure(
                    RootSquareValidatorException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=RootSquareValidatorException.MSG,
                        err_code=RootSquareValidatorException.ERR_CODE,
                        ex=occupant_validation.exception,
                    )
                )
            # Otherwise update the occupant temp variable.
            occupant = cast(Token, occupant_validation.payload)
        
        # --- EXTRACT_THE_VALIDATION_PAYLOADS. ---#
        id = cast(int, id_validation.payload)
        board = cast(Board, board_validation.payload)
        coord = cast(Coord, coord_validation.payload)
        name = cast(str, name_validation.payload)
        state = cast(SquareState, state_validation.payload)
        
        # --- SEND_THE_WORK_PRODUCT. ---#
        envelope = RootSquareEnvelope(
            id=id,
            coord=coord,
            board=board,
            name=name,
            state=state,
            occupant=occupant,
            prime_extract=prime_extract,
        )
        return ValidationResult.success(envelope)
    
    

    