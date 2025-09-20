def normalize_direction(cmd):
    cmd = cmd.strip().lower()
    if cmd in ['n', 'north']:
        return 'N'
    elif cmd in ['s', 'south']:
        return 'S'
    elif cmd in ['e', 'east']:
        return 'E'
    elif cmd in ['w', 'west']:
        return 'W'
    elif cmd == 'stop':
        return 'STOP'
    else:
        return None

def main():
    x, y = 0, 0
    print("Welcome to the GPS tracker! Start at (0, 0).")
    while True:
        cmd = input("Enter direction (N/S/E/W) or STOP to end: ")
        direction = normalize_direction(cmd)
        if direction == 'STOP':
            break
        elif direction == 'N':
            y += 1
        elif direction == 'S':
            y -= 1
        elif direction == 'E':
            x += 1
        elif direction == 'W':
            x -= 1
        else:
            print("Invalid input. Please enter N, S, E, W or STOP.")
            continue
        print(f"Current position: ({x}, {y})")
    print(f"Session ended. Final position: ({x}, {y})")
    if x == 0 and y == 0:
        print("You returned to the origin (0, 0).")
    else:
        print("You did NOT return to the origin (0, 0).")

if __name__ == "__main__":
    main()