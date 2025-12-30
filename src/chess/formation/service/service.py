from typing import List, cast

from chess.formation import Formation, FormationValidator, FormationSuperKeyService
from chess.system import GameColor, HashService, id_emitter


class FormationService(HashService[Formation]):
    SERVICE_NAME = "FormationService"
    
    def __init__(
            self,
            name: str = SERVICE_NAME,
            id: int = id_emitter.service_id,
            validator: FormationValidator = FormationValidator(),
            super_key_service: FormationSuperKeyService = FormationSuperKeyService(),
    ):
        """
        # ACTION:
            Constructor
        # PARAMETERS:
            *   id (int)
            *   name (str)
            *   validator (FormationValidator)
            *   super_key_service (FormationSuperKeyService)
        # RETURNS:
            None
        # RAISES:
            None
        """
        super().__init__(id=id, name=name, validator=validator, super_key_service=super_key_service)
    
    @property
    def key_service(self) -> FormationSuperKeyService:
        """"""
        return cast(FormationSuperKeyService, self.hash_super_key_service)
    
    @property
    def formation_validator(self) -> FormationValidator:
        """"""
        return cast(FormationValidator, self.hash_validator)
    
    @classmethod
    def formation_colors(cls) -> List[GameColor]:
        """The values of the color attribute."""
        return [entry.color for entry in Formation]
    
    @classmethod
    def formation_designations(cls) -> List[str]:
        """A Formation name is the key to a metadata dictionary."""
        return [entry.name for entry in Formation]
    
    @classmethod
    def formation_square_names(cls) -> List[str]:
        """A Formation name is the key to a metadata dictionary."""
        return [entry.name for entry in Formation]
