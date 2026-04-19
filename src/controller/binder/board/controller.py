from microservice import BoardTeamBinderService
from model import BoardTeamBinder


class BoardTeamBinderController:
     _binder: BoardTeamBinder
     _service: BoardTeamBinderService
     
     def __init__(self, binder: BoardTeamBinder, service: BoardTeamBinderService):
         self._binder = binder
         self._service = service
         
     @property
     def binder(self) -> BoardTeamBinder:
         return self._binder
     
     @property
     def service(self) -> BoardTeamBinderService:
         return self._service
    
    