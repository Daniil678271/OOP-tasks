from abc import ABC, abstractmethod 
from typing import List

class Presents(ABC):
    def __init__(self, name: str, weight: float, sugar_content: int ):
        self._name = name
        self._weight = weight
        self._sugar_content = sugar_content

    @abstractmethod
    def description(self) -> str:
        pass
    def get_weight(self) -> float:
        return self._weight
    def get_sugar_content(self) -> int:
        return self._sugar_content
    def __str__(self):
        return f"{self._name}: Weight:{self._weight}, Sugar_content:{self._sugar_content}"
    
class Marmelad(Presents):
    def description(self) -> str:
        return f"Marmelad: {self._name}"
class Cakes(Presents):
    def description(self) -> str:
        return f"Cakes: {self._name}"
class Chocolate(Presents):
    def description(self) -> str:
        return f"Chocolate:{self._name}"
    
class PresentBox:
    def __init__(self):
        self.presents: List[Presents] = [ ]
    def add_presents(self, present: Presents):
        self.presents.append(present)
    def calculate_total_weight(self) -> float:
        total = sum(f.get_weight() for f in self.presents)
        return total
    def sort_by_sugar_content(self):
        self.presents.sort(key=lambda f: f.get_sugar_content(), reverse = True)
    def __str__(self):
        return "\n".join(str(present) for present in self.presents)
    
if __name__ == "__main__":
    present = PresentBox()
    present.add_presents(Marmelad("Marmelad", 100, 25))
    present.add_presents(Cakes("Cakes", 200, 30))
    present.add_presents(Chocolate("Chocolate", 80, 40))

    print("New Year Presentbox:")
    print(present)

    present.sort_by_sugar_content()
    print("\nSorted by Sugar_content:")
    print(present)

    print("\nPresents with sugar_content between 25 and 40 %:")
    print(present)