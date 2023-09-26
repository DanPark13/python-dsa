# Similar behavior as `set()` in Python
# Hashset Implementation without using `set` function 
class HashSet:
    def __init__(self):
        self.hashSet = []

    # Add to hashset if not existing
    def add(self, key: int) -> None:
        if key not in self.hashSet:
            self.hashSet.append(key)

    # Remove from hashset if existing
    def remove(self, key: int) -> None:
        if key in self.hashSet:
            self.hashSet.remove(key)

    # Returns if value in hashset
    def contains(self, key: int) -> bool:
        return key in self.hashSet
    
    def __str__(self) -> str:
        return str(self.hashSet)

