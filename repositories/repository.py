from abc import ABC, abstractmethod
from typing import Generic, TypeVar, Optional, List

T = TypeVar('T')
ID = TypeVar('ID')

class Repository(ABC, Generic[T, ID]):
    @abstractmethod
    def save(self, entity: T) -> None: ...

    @abstractmethod
    def find_by_id(self, id: ID) -> Optional[T]: ...

    @abstractmethod
    def find_all(self) -> List[T]: ...

    @abstractmethod
    def delete(self, id: ID) -> None: ...
