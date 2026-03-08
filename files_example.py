"""
C# uses using for files while python uses with
"""

# simple code to read a file

with open("/Users/konpalgupta/PythonProjects/python-for-ai/python-claude-roadmap/Phase 1/data.txt", "r") as f:
    # content = f.read()
    lines = f.readlines()
    content = f.read()

    print(lines)
    print(content)

# Either or readLines or read runs since python reads the full file 
# in a single go. So need to be careful on how it processes

# how to write a file

with open("/Users/konpalgupta/PythonProjects/python-for-ai/python-claude-roadmap/Phase 1/data.txt", "w") as f:
    f.write("Konpal")

# The above example overwrites the existing file

with open("/Users/konpalgupta/PythonProjects/python-for-ai/python-claude-roadmap/Phase 1/data.txt", "a") as f:
    f.write("Konpal")

# open("file.txt", "r")   # read only (default)
# open("file.txt", "w")   # write — OVERWRITES entire file (like File.WriteAllText)
# open("file.txt", "a")   # append — adds to end (like File.AppendAllText)
# open("file.txt", "r+")  # read AND write — file must already exist

