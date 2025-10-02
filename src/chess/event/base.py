from typing import Generic, TypeVar, Optional


A = TypeVar('A') # Actor Type
R = TypeVar('R') # Resource Type


class Event(Generic[A, R]):
    """
    A data-holding object representing an`actor`'s intent to perform a
    state changing transaction  on a `target`. An `Action` can change state of:

    The Directive is handled by an Executor who carry out the directive
    It is used for doing rollback

    * Its `actor` who initiates and performs the activity
    * The `target` which the transaction is performed upon.

    ## Possible State Changes:
    - If the actor wants to change its state then target is a resource `actor` needs.
    - If `actor` wants to change `target` state then the `actor' state might not be affected

    Attributes:
        _id (`int`): A unique identifier for an `transaction`.
        _actor (`T`): The entity performing the state-changing activity
        _target (`T`): The `target` can either
    """
    _id: int
    _actor: A
    _resource: Optional[R]
    _parent: Optional['Event']

    def __init__(self, event_id: int, actor: A, resource: Optional[R]=None, parent: Optional['Event']=None):
        self._id = event_id
        self._actor = actor
        self._parent = parent
        self._resource = resource

    @property
    def id(self) -> int:
        return self._id

    @property
    def actor(self) -> A:
        return self._actor

    @property
    def resource(self) -> Optional[R]:
        return self._resource

    @property
    def parent(self) -> Optional['Event']:
        return self._parent


    def __eq__(self, other):
        if other is self:
            return True
        if other is None:
            return False
        if not isinstance(other, Event):
            return False
        return self._id == other.id == other.id