"""
C# code to convert into python code

// C# you already know
class Person {
  public string Name { get; set; }
  public int Age { get; set; }
  
  public string Greet() {
    return $"Hi, I'm {Name}, age {Age}";
  }
}
var p = new Person { Name = "Ravi", Age = 30 };
Console.WriteLine(p.Greet());
"""

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hi, I'm {self.name}, age {self.age}"

p = Person(name="Ravi", age=30)

print(p.greet())