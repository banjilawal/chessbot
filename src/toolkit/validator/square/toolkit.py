# src/toolkit/validator/token/toolkit.py

"""
Module: toolkit.validator.token.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Any, Dict, Optional, Type

from err import TokenBlueprintNullException, TokenCarrierNullException, TokenNullException
from fabrication import TokenBlueprint
from model import Token
from toolkit import ModelManifest
from transit import TokenCarrier


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
    _defaults: Dict[str, Any]
    
    def __init__(
            self,
            model_type: Optional[Type[Token]] | None = None,
            blueprint_type: Optional[Type[TokenBlueprint]] | None = None,
            carrier_type: Optional[Type[TokenCarrier]] | None = None,
            model_null_exception: Optional[TokenNullException] | None = None,
            blueprint_null_exception: Optional[TokenBlueprintNullException] | None = None,
            carrier_null_exception: Optional[TokenCarrierNullException] | None = None,
    ):
        """
        Args:
            model_type: Optional[Type[Token]]
            blueprint_type: Optional[Type[TokenBlueprint]]
            carrier_type: Optional[Type[TokenCarrier]]
            
            model_null_exception: Optional[TokenNullException]
            blueprint_null_exception: Optional[TokenBlueprintNullException]
            carrier_null_exception: Optional[TokenCarrierNullException]
        """
        super().__init__()
        
        self._entry["model_type"] = model_type or Token
        self._entry["blueprint_type"] = blueprint_type or TokenBlueprint
        self._entry["carrier_type"] = carrier_type or TokenCarrier
        self._entry["model__null_exception"] = (
                model_null_exception or TokenNullException()
        )
        self._entry["blueprint_null_exception"] = (
                blueprint_null_exception or TokenBlueprintNullException()
        )
        self._entry["carrier_null_exception"] = (
                carrier_null_exception or TokenCarrierNullException()
        )

    @property
    def model_type(self) -> Type[Token]:
        return self._entry["model_type"]
    
    @property
    def blueprint_type(self) -> Type[TokenBlueprint]:
        return self._entry["blueprint_type"]
    
    @property
    def carrier_type(self) -> Type[TokenCarrier]:
        return self._entry["carrier_type"]
    
    @property
    def model__null_exception(self) -> TokenNullException:
        return self._entry["model__null_exception"]
    
    @property
    def blueprint_null_exception(self) -> TokenBlueprintNullException:
        return self._entry["blueprint_null_exception"]
    
    @property
    def carrier_null_exception(self) -> TokenCarrierNullException:
        return self._entry["carrier_null_exception"]
