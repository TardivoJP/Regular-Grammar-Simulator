# Regular Grammar Simulator
## _A simple educational tool for visualizing a Regular Grammar_

![Arcane cosmic tree](https://i.imgur.com/MJeipuE.jpg)

This desktop application allows the user to customize and build their own Regular Grammar, by setting the variables, terminals and production rules and see if it builds whatever word they want while visualizing the path of production rules in whichever order they were utilized to achieve to the end result.

For the purpuses of the educational simulation, we'll assume that a production rule with double asterisks ** represents a null terminal.

The application features two possible input methods, manual and file:

![Application welcome screen](https://i.imgur.com/mW4jlVG.png)

The manual method allows for more granular inputs, perfect for someone who's trying to play with a smaller grammar:

![Application manual input screen](https://i.imgur.com/dg6dHmc.png)

After inputting the base settings of variables, terminals, and starting variable the application will then generate a line for each variable so that the production rules are added:

![Application production rule input screen](https://i.imgur.com/AIEcxbx.png)

Meanwhile the file method allows more flexibility and quicker iteration when testing:

![Application file input screen text field](https://i.imgur.com/oRacN93.png)

Ultimately the input method is up to the user, what really matters are the results!

![Application results screen](https://i.imgur.com/Pl6bVp7.png)

They show a detailed log of every production rule used in chronological order, perfect for learning how the grammar built the input word step by step!


## Usage

- Run the application and choose the desired input method in the welcome screen

**Manual**
  * Insert the variables split by commas (,).
      * Each variable must be a single symbol.
      * Each variable must be unique.
  * Click the "continue" button below.
  * Insert the terminals split by commas (,).
      * Each terminal must be a single symbol.
      * Each terminal must be unique.
      * Terminals can't use the same symbols as variables.
  * Click the "continue" button below.
  * Insert initial variable value.
  * Click the "continue" button below.
  * Insert the production rules for each variable.
      * Production rules must use the variable, terminal or null symbols (**).
      * Two different variables can have the same production rule, however the same variable can't have two of the same rule.
  * Click the "continue" button below.
  * Insert the word to be tested.
  * Click the "test" button below.
  * Enjoy the results!

**File**
  * Paste in a valid regular grammar in the text field.
  * Input formatting goes as follows:
    * [VARIABLE]>[PRODUCTION RULES]
    * Where variables and their production rules are separated by the > symbol.
    * Where production rules are separated by a comma , symbol.
    * Where each line represents a variable and its production rules
    * If there are two lines with the same variable, the input will be considered invalid.
    * If there's two or more exact same production rules in a single line, the input will be considered invalid.
  * Insert the word to be tested.
  * Click the "test" button below.
  * Enjoy the results!

**Miscellaneous**
  * The back button in either the manual or file screens will return to the welcome screen.
  * The reset button in either the manual or file screens will return that screen to its initial state.


## Packages used

This educational application was only made possible because of these amazing packages.

| Package | Link |
| ------ | ------ |
| PyQt6 | https://pypi.org/project/PyQt6/ |
| PyInstaller | https://pypi.org/project/pyinstaller/ |

## Building the application

If you want to build the application yourself from the source code:

**Windows**
1. Download Python from https://www.python.org/downloads/ and install it
2. Open a terminal and run this command to install the dependencies:
```sh
pip install PyQt6 PyInstaller
```
3. Navigate to the source code's directory and run this command to build the application:
```sh
pyInstaller main_window.py --onefile --noconsole --icon=logo.ico --add-data "resources;resources"
```
4. Run the newly created .exe in the "dist" folder

**Linux**
1. Download and install Python using the package manager from your distro:
* Ubuntu/Debian
```sh
sudo apt install python3
```
* Fedora
```sh
sudo dnf install python3
```
* CentOS/RHEL
```sh
sudo yum install centos-release-scl
sudo yum install rh-python36
scl enable rh-python36 bash
```
* Arch
```sh
sudo pacman -S python
```
2. Download and install the Package Installer for Python (pip):
```sh
python3 get-pip.py
```
3. Download and install the dependencies:
```sh
sudo pip3 install pyinstaller pyqt6
```
4. Navigate to the source code's directory and run this command to build the application:
```sh
python3 -m PyInstaller main_window.py --onefile --noconsole --icon=logo.ico --add-data "resources:resources"
```
5. Navigate to the newly created "dist" folder
6. Run this command on the main_window binary file to grant it permission to execute
```sh
chmod +x main_window
```
7. Run the application with this command:
```sh
./main_window
```

## Compatibility

This application currently runs on Windows 10 and Linux. I am looking into the possibility of adding a macOS release but I won't make any promises.

## Future development

This application does have a few possibilities for additional features which may include:

- More complex input parsing, i.e actually analysing if the user input a good grammar or not
- Showing the user whether they input a RLG, LLG, or other variations.
- Optimizations to performance on tougher grammars.
- Saving manual inputs as .txt files that can be loaded later.