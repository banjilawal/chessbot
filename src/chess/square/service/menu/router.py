# src/chess/square/service/menu/operation/operation.py

"""
Module: chess.square.service.menu.operation.operation
Author: Banji Lawal
Created: 2026-02-24
"""

from __future__ import annotations



class SquareServiceMenu:
    _request: ServiceRequest
    _token_service: TokenService
    _square_service: SquareService
    _operations: List[ServiceOperation]
    
    def __init__(
            self,
            operations: List[ServiceOperation] = [],
            token_service: TokenService = TokenService(),
            square_service: SquareService = SquareService(),
    ):
        self._operations = operations
        self._token_service = token_service
        self._square_service = square_service
        self._request = None
    
    @property
    def operations(self) -> List[ServiceOperation]:
        return self._operations
    
    @property
    def request(self) -> Optional[ServiceRequest]:
        return self._request if not None else None
    
    @request.setter
    def request(self, request: ServiceRequest):
        self._request = request
    
    def verify(self):
        if self._verify_reqeust_op() is None:
            return False
        if not self.verify_arg_count():
            return False
        if not self._verify_identifiers(self._request, self._verify_reqeust_op()):
            return False
    
    def execute(self):
        if self._request.op_name.upper() == "begin_visit".upper():
            return self._square_service.begin_square_visit(
                square=self._request.arguments["square"],
                visitor=self._request.arguments["visitor"],
            )
        if self._request.op_name.upper() == "end_visit".upper():
            return self._square_service.end_square_visit(square=self._request.arguments["square"])
    
    def _verify_reqeust_op(self) -> Optional[ServiceOperation]:
        for operation in self._operations:
            if operation.name == self._request.op_name:
                return operation
        return None
    
    def _verify_arg_count(self, op: ServiceOperation) -> bool:
        return len(self._request.arguments) == len(op.params)
    
    def _verify_identifiers(self, request: ServiceRequest, service_op: ServiceOperation) -> bool:
        for arg_name in request.arguments.keys():
            if not self._identifier_found(arg_name, service_op):
                return False
        return True
    
    def verify_arg_type(self, request: ServiceRequest, service_op: ServiceOperation) -> bool:
        for arg_name in request.arguments.keys():
            if not isinstance(request.arguments[arg_name], service_op.params[arg_name]):
                return False
        return True
        
        for arg_name in request_args.keys():
            if not self._verify_identifier_match(arg_name):
                return False
    
    def _identifier_found(self, indentifier: str, service_op: ServiceOperation) -> bool:
        return indentifier in service_op.params.keys()
    
    def _verify_arg_types(self, request_args: Dict[str, Any], op: ServiceOperation) -> bool:
        matches = 0
        for arg_key in request_args.keys():
            if arg_key in op.params.keys():
                if isinstance(request_args[arg_key], op.params[arg_key]):
            
            for arg_name, arg_value in request_args.items():
                if not self._verify_type_match(arg_value, op.params[arg_name]):
                    return False
    
    def validate(self):
        for arg in self._request.arguments.values():
            if not self._verify_identifier_match(arg):
                return False
    
    def _verify_identifier_match(self, identifier: str) -> bool:
        if identifier in self._operations.keys():
            return True
        return False
    
    def _verify_type_match(self, arg_value: Any, op: ServiceOperation) -> bool:
        for param_type in op.params.values():
            if isinstance(arg_value, param_type):
                return True
        return False
    
    def verify_arg_count:
        def select_command(self, command: Command) -> Any:
            if command.name in self._menu.keys():
                self.verify_arguments(command)
    
    def verify_arguments(self, command: Command) -> ValidationResult[Command]:
        if command.name.startswith("begin"):
            if len(command.arguments) != 2:
                return ValidationResult.failure(ChessException())
    
    def verify_type(self):
        
        outcome = False
        for argument in command.arguments.values():
            if isinstance(argument, Square):
                return ValidationResult.failure(ChessException())
        
        for argument in command.arguments.values():
            if not isinstance(argument, Token):
    
    def found_type_match(self, argument: Any, param_types: List[Any]) -> bool:
        
        for param_type in param_types:
            if isinstance(argument, param_type):
                return True
        return False