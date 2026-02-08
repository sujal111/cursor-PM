# backend/services/repository.py
from typing import Dict, List, TypeVar, Generic, Optional
from uuid import uuid4

T = TypeVar('T')

class InMemoryRepository(Generic[T]):
    def __init__(self):
        self._store: Dict[str, T] = {}
    
    def add(self, item: T, item_id: str = None) -> str:
        if item_id is None:
            item_id = str(uuid4())
        self._store[item_id] = item
        return item_id
    
    def get(self, item_id: str) -> Optional[T]:
        return self._store.get(item_id)
    
    def list_all(self) -> List[T]:
        return list(self._store.values())
    
    def update(self, item_id: str, item: T) -> bool:
        if item_id in self._store:
            self._store[item_id] = item
            return True
        return False
    
    def delete(self, item_id: str) -> bool:
        if item_id in self._store:
            del self._store[item_id]
            return True
        return False

# Initialize repositories
feedback_repo = InMemoryRepository()
features_repo = InMemoryRepository()
specs_repo = InMemoryRepository()
tasks_repo = InMemoryRepository()