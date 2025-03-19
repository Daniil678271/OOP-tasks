from abc import ABC, abstractmethod 
from typing import List

class Vegetable(ABC):
    def __init__(self, name: str, weight: float, calories: float):
        self._name = name
        self._weight = weight
        self._calories = calories

    @abstractmethod
    def description(self) -> str:
        pass
    def get_weight(self) -> float:
        return self._weight
    def get_calories(self) -> float:
        return self._calories
    def __str__(self):
        return f"{self._name}: Weight:{self._weight}, Calories:{self._calories}"
    
class Tomato(Vegetable):
    def description(self) -> str:
        return f"Tomato: {self._name}"
class Cucumber(Vegetable):
    def description(self) -> str:
        return f"Cucumber: {self._name}"
class Onion(Vegetable):
    def description(self) -> str:
        return f"Onion: {self._name}"
class Cabbage(Vegetable):
    def description(self) -> str:
        return f"Cabbage: {self._name}"
    
class Salad:
    def __init__(self):
        self.vegetables: List[Vegetable] = [ ]
    def add_vegetable(self, vegetable: Vegetable):
        self.vegetables.append(vegetable)
    def calculate_total_calories(self) -> float:
        total = sum(f.get_calories() for f in self.vegetables)
        return total
    def sort_by_calories(self):
        self.vegetables.sort(key=lambda f: f.get_calories(), reverse = True)
    def __str__(self):
        return "\n".join(str(vegetable) for vegetable in self.vegetables)
    
if __name__ == "__main__":
    salad = Salad()
    salad.add_vegetable(Tomato("Tomato", 100, 22))
    salad.add_vegetable(Cucumber("Cucumber", 100, 15))
    salad.add_vegetable(Onion("Onion", 100, 40))
    salad.add_vegetable(Cabbage("Cabbage", 100, 25))

    print("Healthy Salad")
    print(salad)

    salad.sort_by_calories()
    print("\nSorted by calories:")
    print(salad)

    print("\nVegetables with stem length between 15 and 40 calories:")