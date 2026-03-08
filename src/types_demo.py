"""
// C#
int age = 30;
string name = "Ravi";
bool isActive = true;
List<string> skills = new List<string> { "C#", ".NET" };
Dictionary<string, int> scores = new Dictionary<string, int> {
  { "math", 90 }, { "code", 95 }
};
"""

age: int = 30
name: str = "Ravi"
is_active: bool = True
skills: list[str] = ["C#", ".NET", "A", "Python"]
scores: dict[str, int] = {
    "math": 90,
    "code": 95
}

# C#: skills.Where(s => s.Length > 2).Select(s => s.Upper()).ToList()

long_skills = [s.upper() for s in skills if len(s) > 2]