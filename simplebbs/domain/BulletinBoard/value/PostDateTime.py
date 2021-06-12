import copy
from datetime import datetime


class PostDateTime:
    """
    @DomainObject
    @ValueObject
    掲載日時
    """

    def __init__(self, dt: datetime):
        self.dt = dt

    def getValue(self) -> datetime:
        return copy.deepcopy(self.dt)
