C: int = 299792458

def main():
    mass_kg = float(input("Enter mass (kg): "))
    energy_joule: float = mass_kg * (C ** 2)
    print("e = mc^2")
    print("m = " + str(mass_kg) + " kg")
    print("C = " + str(C) + " m/s")
    print(str(energy_joule) + " joules of energy!")

if __name__ == '__main__':
    main()