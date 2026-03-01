# src/logic/battle_space/factory.py
"""
Module: logic.battle_space.validation
Author: Banji Lawal
Created: 2025-10-27
version: 1.0.0
"""


from typing import Any

from logic.system import ValidationResult, Validator
from logic.battle_space.service import ProjectionService



class ProjectionServiceValidator(Validator[ProjectionService]):
    
    @classmethod
    def validate(cls, candidate: Any) -> ValidationResult[ProjectionService]:
        pass