from typing import Generic, TypeVar, Optional


A = TypeVar('A') # Actor Type
R = TypeVar('R') # Resource Type


class Directive(Generic[A, R]):
    """
    A data-holding object representing an`actor`'s intent to perform a
    state changing operation  on a `target`. An `Action` can change state of:

    The Directive is handled by an Executor who carry out the directive
    It is used for doing rollback

    * Its `actor` who initiates and performs the activity
    * The `target` which the operation is performed upon.

    ## Possible State Changes:
    - If the actor wants to change its state then target is a resource `actor` needs.
    - If `actor` wants to change `target` state then the `actor' state might not be affected

    Attributes:
        _id (`int`): A unique identifier for an `operation`.
        _actor (`T`): The entity performing the state-changing activity
        _target (`T`): The `target` can either
    """
    _id: int
    _actor: A
    _resource: Optional[R]

    def __init__(self, directive_id: int, actor: A, resource: Optional[R]=None):
        self._id = directive_id
        self._actor = actor
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


    def __eq__(self, other):
        if other is self:
            return True
        if other is None:
            return False
        if not isinstance(other, Directive):
            return False
        return self._id == other.id == other.id