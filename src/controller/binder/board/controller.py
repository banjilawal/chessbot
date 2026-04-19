from microservice import BoardTeamBinderService
from model import BoardBinder


class BoardTeamBinderController:
     _binder: BoardBinder
     _service: BoardTeamBinderService
     
     def __init__(self, binder: BoardBinder, service: BoardTeamBinderService):
         self._binder = binder
         self._service = service
         
     @property
     def binder(self) -> BoardBinder:
         return self._binder
     
     @property
     def service(self) -> BoardTeamBinderService:
         return self._service
    
    