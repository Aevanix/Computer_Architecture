memory = {100: 12, 104: 8}
registers = {"R1": 0, "R2": 0, "R3": 0}

instructions = [
    ("LOAD", "R1", 100),
    ("LOAD", "R2", 104),
    ("ADD", "R3", "R1", "R2"),
    ("STORE", "R3", 108)
]

for instruction in instructions:
    if instruction[0] == "LOAD":
        registers[instruction[1]] = memory[instruction[2]]
        print(f"Executing: LOAD {instruction[1]}, {instruction[2]}")

    elif instruction[0] == "ADD":
        registers[instruction[1]] = registers[instruction[2]] + registers[instruction[3]]
        print(f"Executing: ADD {instruction[1]}, {instruction[2]}, {instruction[3]}")

    elif instruction[0] == "STORE":
        memory[instruction[2]] = registers[instruction[1]]
        print(f"Executing: STORE {instruction[1]}, {instruction[2]}")

    print("R1 =", registers["R1"], "R2 =", registers["R2"], "R3 =", registers["R3"])
    print()

print("Final Register Contents:")
for register, value in registers.items():
    print(register, "=", value)

print("\nFinal Memory Contents:")
print("M[108] =", memory[108])
