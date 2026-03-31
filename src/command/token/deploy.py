from typing import Dict

from logic.system import IdFactory
from command.token.root import TokenCommand
from logic.token import Token, TokenService


class DeployTokenCommand(TokenCommand):
    NAME = "deploy"
    
    def __init__(
            self,
            server: TokenService,
            name: str = NAME,
            parameters: Dict[str, Token] = Dict[str, Token],
            id: int = IdFactory.next_id(class_name="DeployTokenCommand"),
    ):
        super().__init__(id=id, name=name, server=server, parameters=parameters)
    
    @classmethod
    def cipher(cls,) -> Dict[str, Token]:
        return {}