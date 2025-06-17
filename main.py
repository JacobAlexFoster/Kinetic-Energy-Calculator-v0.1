import math
print("Which two parts of the equation do you know?")
print("Kinetic Energy = Ek")
print("Mass = M")
print("Speed = V")

x = input("First known variable (Ek/M/V): ").strip().upper()
y = input("Second known variable (Ek/M/V): ").strip().upper()

if x == "M" and y == "V":
    M = float(input("Mass: "))
    V = float(input("Speed: "))
    Ek = 0.5 * M * V**2
    print(f"Kinetic Energy (Ek): {Ek}")

elif x == "Ek" and y == "M":
    Ek = float(input("Kinetic Energy: "))
    M = float(input("Mass: "))
    V = math.sqrt((2 * Ek) / M)
    print(f"Speed (V): {V}")

elif x == "Ek" and y == "V":
    Ek = float(input("Kinetic Energy: "))
    V = float(input("Speed: "))
    M = (2 * Ek) / V**2
    print(f"Mass (M): {M}")

else:
    print("Invalid input. Please enter Ek, M, or V.")