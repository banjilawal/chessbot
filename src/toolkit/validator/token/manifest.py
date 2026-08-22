# src/toolkit/validator/token/toolkit.py

"""
Module: toolkit.validator.token.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Dict, Type

from assurance import TeamValidator
from authorization import BlueprintHomeSquareExtractor, BlueprintRankExtractor
from err import TokenBlueprintNullException, TokenCarrierNullException, TokenNullException
from fabrication import TokenBlueprint
from domain.model import Token
from sensor import TokenHomeReporter
from toolkit import ModelManifest
from domain.transit import TokenCarrier


class TokenValidatorToolkit(ModelManifest[Token]):
    """
    Role:
        -   Dependency Manager

    Responsibilities:
        1.  Bundles Token validation dependencies.
        2.  Unify Token assurance method signatures.

    Attributes:
        model_type: Optional[Type[Token]]
        blueprint_type: Optional[Type[TokenBlueprint]]
        carrier_type: Optional[Type[TokenCarrier]]
        
        model_null_exception: Optional[TokenNullException]
        blueprint_null_exception: Optional[TokenBlueprintNullException]
        carrier_null_exception: Optional[TokenCarrierNullException]

    Provides:

    Super
        ModelValidatorToolkit
    """
    _types: Dict[str, Dict[Type[Any], Any]] = {}
    _nulls: Dict[str, Any] = {}
    
    def __init__(
            self,
            types: Dict[str, Dict[Type[Any], Any]] | None = None,
            nulls: Dict[str, Any] | None = None,
            resources: Dict[str, Any] | None = None,
    ):
        """
        Args:
            types: Dict[str, Dict[Type[Any], Any]]
            nulls: Dict[str, Any] | None = None
            resources: Dict[str, Any]
        """
        super().__init__(
            resources=resources or {
                "team_validator": TeamValidator(),
                "home_detector": TokenHomeReporter(),
                "rank_extractor": BlueprintRankExtractor(),
                "home_square_extractor": BlueprintHomeSquareExtractor(),
            }
        )
        self._types = types or {
            "model_type": {Type[Token]: Token},
            "carrier_type": {Type[TokenCarrier]: TokenCarrier},
            "blueprint_type": {Type[TokenBlueprint]: TokenBlueprint},
        }
        self._nulls = nulls or {
            "model__null_exception": TokenNullException(),
            "blueprint_null_exception": TokenBlueprintNullException(),
            "carrier_null_exception": TokenCarrierNullException(),
        }


    @property
    def model_type(self) -> Type[Token]:
        return self._types["model_type"]
    
    @property
    def blueprint_type(self) -> Type[TokenBlueprint]:
        return self._types["blueprint_type"]
    
    @property
    def carrier_type(self) -> Type[TokenCarrier]:
        return self._types["carrier_type"]
    
    @property
    def model__null_exception(self) -> TokenNullException:
        return self._nulls["model__null_exception"]
    
    @property
    def blueprint_null_exception(self) -> TokenBlueprintNullException:
        return self._nulls["blueprint_null_exception"]
    
    @property
    def carrier_null_exception(self) -> TokenCarrierNullException:
        return self._nulls["carrier_null_exception"]
