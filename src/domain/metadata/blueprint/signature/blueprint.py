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
    
    def __init__(self, domain_class: Type[T], domain_null_exception: SignatureNullException):
        super().__init__(domain_class=domain_class, domain_null_exception=domain_null_exception)
    
    @property
    def domain_class(self) -> Type[T]:
        return cast(Type[T], super().domain_class)
    
    @property
    def domain_null_exception(self) -> SignatureNullException:
        return cast(SignatureNullException, super().domain_null_exception)


