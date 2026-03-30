from email.headerregistry import Address

from command import Command


class Request:
    _id: int
    _address: Address
    _command: Command
    
    def __init__(self, id: int, address: Address, command: Command):
        """
        Args:
            id: int
            address: Address
            command: Command
        """
        self._id = id
        self._address = address
        self._command = command
        
        
    @property
    def id(self) -> int:
        return self._id
    
    @property
    def address(self) -> Address:
        return self._address
    
    @property
    def command(self) -> Command:
        return self._command
    
    def __eq__(self, other: object) -> bool:
        if other is self: return True
        if other is None: return False
        if isinstance(other, Request):
            return self._id == other._id
        return False
        