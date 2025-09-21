def overworld_to_nether(x, y, z):
    return x // 8, y, z // 8

if __name__ == "__main__":
    x = int(input("Overworld X: "))
    y = int(input("Overworld Y: "))
    z = int(input("Overworld Z: "))
    nx, ny, nz = overworld_to_nether(x, y, z)
    print(f"Nether coordinates: ({nx}, {ny}, {nz})")

