# src/bootstrap/fabrication/model/rank/loader.py

"""
Module: bootstrap.fabrication.model.rank.loader
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import BuildResult
from domain import Rank, RankBlueprint
from err import RankBuildLoaderException, RankBuildRequestNullException
from exchange import RankBuildRequest, RankValidationRequest, RankValidationService
from fabrication import ModelBuildLoader
from util import IdFactory, LoggingLevelRouter


class RankBuildLoader(ModelBuildLoader[Rank]):
    """
    Role
        -   Authorization
        -   Bootstrap
        
    Responsibilities:
        1.  Initialize the Rank build process by preparing a RankBlueprint
            if the BuildRequest is correct.

    Attributes:
        validator: RankValidationServer

    Provides:
        -   def execute(request: RankBuildRequest) -> BuildResult[RankBlueprint]

    Super Class:
        BuildLoader
    """
    
    def __init__(
            self,
            validator: Optional[RankValidationService] | None = None,
    ):
        """
        Args:
            validator: Optional[RankValidationServer]
        """
        super().__init__(validator=validator or RankValidationService())
    
    @property
    def validator(self) -> RankValidationService:
        return cast(RankValidationService, super().validator)
        
    @LoggingLevelRouter.monitor
    def execute(self, request: RankBuildRequest) -> BuildResult[RankBlueprint]:
        """
        Prepare a RankBlueprint which guarantees a safe Rank.
        
        Action:
            1.  Send an exception chain in the BuildResult if any of the following occur
                    -   The request is null or the wrong type.
                    -   The request does not contain a valid RankBlueprint.
            2.  Otherwise, forward the safe blueprint.
        Args:
            request: RankBuildRequest
        Returns:
            BuildResult[RankBlueprint]
        Raises:
            RankBuildLoaderException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # --- Verify the request is safe. ---#
        priming = self.priming_validator.execute(
            candidate=request,
            target_model=RankBuildRequest,
            null_exception=RankBuildRequestNullException(),
        )
        # Handle the case that the request is flagged.
        if priming.is_failure:
            # Send the exception chain on failure.
            return BuildResult.failure(
                RankBuildLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=RankBuildLoaderException.MSG,
                    err_code=RankBuildLoaderException.ERR_CODE,
                    ex=priming.exception,
                )
            )
        # --- Cast the priming result for additional processing. ---#
        build_request = cast(RankBuildRequest, priming.authorization_applicant)
        
        # Handle the case that the blueprint is faulty.
        blueprint_validation = self.validator.extract_blueprint(
            request=RankValidationRequest(
                item=build_request.item,
                id=IdFactory.next_id(class_name="RankValidationRequest")
            )
        )
        # Send the exception chain on failure.
        if blueprint_validation.is_failure:
            return BuildResult.failure(
                RankBuildLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=RankBuildLoaderException.MSG,
                    err_code=RankBuildLoaderException.ERR_CODE,
                    ex=blueprint_validation.exception
                )
            )
        # --- Forward the work product. ---#
        blueprint = cast(RankBlueprint, blueprint_validation.payload)
        return BuildResult.success(blueprint)