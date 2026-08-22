# src/domain/metadata/builder/pattern/builder.py

"""
Module: builder.pattern.builder
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, Type, TypeVar, cast

from domain.metadata.blueprint import Blueprint
from err import SignatureNullException

T = TypeVar("T", bound="Signature")

class SignatureBlueprint(Blueprint, ABC, Generic[T]):
    
    def __init__(self, model_class: Type[T], null_exception: SignatureNullException):
        super().__init__(model_class=model_class, null_exception=null_exception)
    
    @property
    def model_class(self) -> Type[T]:
        return cast(Type[T], super().model_class)
    
    @property
    def null_exception(self) -> SignatureNullException:
        return cast(SignatureNullException, super().null_exception)


