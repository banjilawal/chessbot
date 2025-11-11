# src/chess/domain/origin/validator.py

"""
Module: chess.domain.origin.validator
Author: Banji Lawal
Created: 2025-11-11
version: 1.0.0
"""


from typing import Any, cast

from chess.domain import DomainOrigin
from chess.system import Validator, ValidationResult

class DomainOriginValidator(Validator[DomainOrigin]):