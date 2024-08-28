# Ship Data CLI

## Overview

The Ship Data CLI is a command-line tool designed to analyze ship data. It allows users to perform various operations on a dataset of ships, such as printing the number of ships, listing ship names and countries, generating histograms of ship speeds, and visualizing ship locations on a map.

## Features

- **Print number of ships**: Displays the total count of ships in the dataset.
- **Print names of all ships**: Lists the names of all ships.
- **Print countries of all ships**: Lists the countries associated with each ship.
- **Print unique countries of all ships**: Displays unique countries from the dataset.
- **Print count of ships by type**: Shows the count of ships categorized by their types.
- **Search for ships by name**: Finds ships whose names contain a given query (case-insensitive).
- **Create a histogram of ship speeds**: Generates and saves a histogram of ship speeds.
- **Draw a map of ship locations**: Creates a map with markers for each ship's location and saves it as an HTML file.

## Requirements

- Python 3.x
- `matplotlib` library
- `folium` library
- `load_data` module (must define the `load_data` function that returns ship data)

You can install the required libraries using pip:

```bash
pip install matplotlib folium
```

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/Vrana710/Titanic.git
   ```

2. Navigate to the project directory:

   ```bash
   cd Titanic
   ```

3. Install the required libraries (if not already installed):

   ```bash
   pip3 install matplotlib folium
   ```

## Usage

1. Ensure that your dataset is available and correctly configured in the `load_data` module.
2. Run the CLI application:

   ```bash
   python titanic.py
   ```

3. Enter commands as prompted. Available commands are:

   - `1`: Print number of ships
   - `2`: Print names of all ships
   - `3`: Print countries of all ships
   - `4`: Print unique countries of all ships
   - `5`: Print count of ships by type
   - `6 <name>`: Search for ships by name (replace `<name>` with the query string)
   - `7`: Create a histogram of ship speeds
   - `8`: Draw a map of ship locations
   - `exit`: Exit the program

4. The program will generate output based on your commands. For example, the histogram of ship speeds will be saved as `speed_histogram.png`, and the map of ship locations will be saved as `ships_map.html`.

## Example

Here’s an example of running the application and using some commands:

```bash
python titanic.py
```

```
Enter command: 1
There are 150 ships in the file.

Enter command: 2
Names of all the ships:
- Ship A
- Ship B
...

Enter command: 7
Speed histogram saved as 'speed_histogram.png'

Enter command: 8
Ship map saved as 'ships_map.html'

Enter command: exit
Exiting the program.
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Feel free to open issues or submit pull requests. All contributions are welcome!

## Contact

For any questions or suggestions, please reach out to [ranavarsha710@gmail.com](mailto:ranavarsha710@gmail.com).
