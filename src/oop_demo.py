"""
// C# abstract class + interface
public abstract class Animal {
  public abstract string Sound();
  public string Name { get; private set; }
  public Animal(string name) { Name = name; }
}
public class Dog : Animal {
  public Dog(string name) : base(name) {}
  public override string Sound() => "Woof";
}
"""

from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name: str):
        self._name = name # adding _ before the variable makes it private
    
    @property
    def name(self):
        return self._name
    
    @abstractmethod
    def sound(self) -> str: ... # must be implemented

class Dog(Animal):
    def sound(self) -> str:
        return "Bark!!"
    
class Cat(Animal):
    def sound(self) -> str:
        return "Meow!!"
    
cat = Cat("Kitty")
print(f"{cat.name} says {cat.sound()}")

animals: list[Animal] = [Dog("Bruno"), Cat("Whiskers")]
for a in animals:
    print(f"{a.name}: {a.sound()}")