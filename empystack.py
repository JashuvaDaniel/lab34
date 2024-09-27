class SariesMember:
    def __init__(self, name, age):
        self.name = name
        self.age = age

names = ["Ava", "Liam", "Sophia", "Noah", "Mia"]
ages = [25, 30, 22, 28, 35]  # You can specify ages directly

saries_members = [SariesMember(name, age) for name, age in zip(names, ages)]

for member in saries_members:
    print(f"Name: {member.name}, Age: {member.age}")
