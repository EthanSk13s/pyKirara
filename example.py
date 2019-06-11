import pyKirara

client = pyKirara.Kirara()
uzuki = client.get_idol(101)

print(f"HI! MY NAME IS {uzuki.conventional}")
print("I'll do my best!")
print(f"I'am {uzuki.age} years old!")

# Returns:
# HI! MY NAME IS Shimamura Uzuki
# I'll do my best!
# I'am 17 years old!