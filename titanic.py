import matplotlib.pyplot as plt
import folium

from load_data import load_data


def load_and_print_keys():
    """
    Load data using the load_data function and print the keys of the loaded data.

    Returns:
        dict: The loaded data containing 'data' and 'totalCount' keys.
    """
    all_data = load_data()
    print(all_data.keys())  # Expecting keys: 'data' and 'totalCount'
    return all_data


def print_number_of_ships(all_data):
    """
    Print the number of ships in the loaded data.

    Args:
        all_data (dict): The loaded data containing ship information.
    """
    ships = all_data['data']
    num_ships = len(ships)
    print(f"There are {num_ships} ships in the file.")


def print_ship_names(all_data):
    """
    Print the names of all the ships in the loaded data.

    Args:
        all_data (dict): The loaded data containing ship information.
    """
    ships = all_data['data']
    if ships and "SHIPNAME" in ships[0]:
        ship_names = [ship["SHIPNAME"] for ship in ships]
        print("Names of all the ships:")
        for name in ship_names:
            print(name)
    else:
        print("No 'SHIPNAME' key found in the ship entries.")


def print_ship_countries(all_data):
    """
    Print the countries of all the ships in the loaded data.

    Args:
        all_data (dict): The loaded data containing ship information.
    """
    ships = all_data['data']
    if ships and "COUNTRY" in ships[0]:
        ship_countries = [ship["COUNTRY"] for ship in ships]
        print("Countries of all the ships:")
        for country in ship_countries:
            print(country)
    else:
        print("No 'COUNTRY' key found in the ship entries.")


def print_unique_countries(all_data):
    """
    Print unique countries of all the ships in the loaded data.

    Args:
        all_data (dict): The loaded data containing ship information.
    """
    ships = all_data['data']
    if ships and "COUNTRY" in ships[0]:
        ship_countries = [ship["COUNTRY"] for ship in ships]
        unique_countries = sorted(set(ship_countries))
        print("Countries of all the ships without duplicates:")
        for country in unique_countries:
            print(country)
    else:
        print("No 'COUNTRY' key found in the ship entries.")


def ships_by_types(all_data):
    """
    Print the count of ships by their types in the loaded data.

    Args:
        all_data (dict): The loaded data containing ship information.
    """
    ships = all_data['data']
    ship_types = {}
    for ship in ships:
        ship_type = ship.get("TYPE_SUMMARY", "Unknown")
        ship_types[ship_type] = ship_types.get(ship_type, 0) + 1
    print("Ships by types:")
    for ship_type, count in ship_types.items():
        print(f"{ship_type}: {count}")


def search_ship(all_data, name_query):
    """
    Search for ships by name in the loaded data (case-insensitive and partial match).

    Args:
        all_data (dict): The loaded data containing ship information.
        name_query (str): The name query to search for in ship names.
    """
    ships = all_data['data']
    name_query = name_query.lower()
    matching_ships = [
        ship for ship in ships
        if name_query in ship.get("SHIPNAME", "").lower()
    ]
    print(f"Ships matching '{name_query}':")
    for ship in matching_ships:
        print(ship.get("SHIPNAME"))


def speed_histogram(all_data):
    """
    Create and save a histogram of ship speeds from the loaded data.

    Args:
        all_data (dict): The loaded data containing ship information.
    """
    ships = all_data['data']
    speeds = [ship.get("SPEED") for ship in ships if "SPEED" in ship]
    plt.hist(speeds, bins=10)
    plt.xlabel('Speed')
    plt.ylabel('Number of Ships')
    plt.title('Histogram of Ship Speeds')
    plt.savefig('speed_histogram.png')
    print("Speed histogram saved as 'speed_histogram.png'")


def draw_map(all_data):
    """
    Draw a map with markers for each ship's location from the loaded data and save it as HTML.

    Args:
        all_data (dict): The loaded data containing ship information.
    """
    ships = all_data['data']
    ship_map = folium.Map(location=[0, 0], zoom_start=2)
    for ship in ships:
        name = ship.get("SHIPNAME", "Unknown")
        lat = ship.get("LAT")
        lon = ship.get("LON")
        if lat is not None and lon is not None:
            folium.Marker(
                location=[lat, lon],
                popup=name,
                icon=folium.Icon(icon="ship", prefix="fa")
            ).add_to(ship_map)
    ship_map.save("ships_map.html")
    print("Ship map saved as 'ships_map.html'")


def display_help():
    """
    Display a help message listing all available commands.
    """
    print("\nWelcome to the Ship Data CLI!")
    print("Available commands:")
    print("1 - Print number of ships")
    print("2 - Print names of all ships")
    print("3 - Print countries of all ships")
    print("4 - Print unique countries of all ships")
    print("5 - Print count of ships by type")
    print("6 <name> - Search for ships by name")
    print("7 - Create a histogram of ship speeds")
    print("8 - Draw a map of ship locations")
    print("exit - Exit the program")


def dispatcher(command, all_data, *args):
    """
    Dispatcher function to execute various commands based on input.

    Args:
        command (str): The command to execute.
        all_data (dict): The loaded data containing ship information.
        *args: Additional arguments for specific commands.
    """
    commands = {
        "1": lambda: print_number_of_ships(all_data),
        "2": lambda: print_ship_names(all_data),
        "3": lambda: print_ship_countries(all_data),
        "4": lambda: print_unique_countries(all_data),
        "5": lambda: ships_by_types(all_data),
        "6": lambda name_query: search_ship(all_data, name_query),
        "7": lambda: speed_histogram(all_data),
        "8": lambda: draw_map(all_data),
    }

    func = commands.get(command)
    if func:
        try:
            if command == "6":  # Command 6 requires an argument
                func(*args)
            else:
                func()
        except TypeError as e:
            print(f"Error executing command: {e}")
    else:
        print(
            f"Unknown command: {command}. Type 'help' to see the available commands."
        )


def main():
    """
    Main function to handle user commands interactively.
    """
    try:
        all_data = load_and_print_keys()
    except Exception as e:
        print(f"Error loading data: {e}")
        return

    display_help()

    while True:
        try:
            command = input("\nEnter command: ").strip().lower()

            if command == "help":
                display_help()
            elif command == "exit":
                print("Exiting the program.")
                break
            else:
                parts = command.split(maxsplit=1)
                cmd = parts[0]
                arg = parts[1] if len(parts) > 1 else ""
                dispatcher(cmd, all_data, arg)
        except KeyboardInterrupt:
            print("\nProgram interrupted. Exiting...")
            break
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
