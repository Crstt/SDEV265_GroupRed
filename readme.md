# Oregon Trail with Python(s)

Welcome to the Oregon Trail game implemented in Python! This game puts you in the shoes of a pioneer traveling along the Oregon Trail, trying to make it to the next checkpoint before running out of food. Your decisions will determine the outcome of your journey.

## How to Play

1. **Choose Your Character**: At the beginning of the game, you have the option to pick one of three characters: Banker, Merchant, or Farmer. Each character has different starting money and skills. The character selection affects your odds of success in special events that may occur during the game.

2. **Manage Your Resources**: Money and food are your main resources in this game. Money is used to purchase food or special services such as ferry rides. Food is consumed each day, and if you run out of food, your journey will end. You can buy food at certain checkpoints using your money.

3. **Travel and Hunt**: Each day, you have the choice to either travel or hunt for food. Traveling progresses your journey but consumes food. Hunting allows you to gather additional food but does not present any other scenarios. The distance to the next checkpoint decreases randomly with each traveled day.

4. **Encounter Scenarios**: As you travel, you will encounter various scenarios randomly. Some scenarios require you to make decisions that affect the time it takes to reach the next checkpoint or your food rations. Special events may also occur based on your character selection and skills. Success in these scenarios depends on randomized outcomes and your character's abilities.

5. **Reach Checkpoints**: Your ultimate goal is to reach the next checkpoint before running out of food. There are three checkpoints between the start and finish, with a predetermined number of rivers to cross. Manage your resources wisely and overcome the challenges to complete the journey.

## Game Mechanics

- Each decision or scenario represents one day in the game.
- Randomization is used throughout the game to determine outcomes.
- Characters have different starting money, skills, and odds of success in special events.
- Money is used for purchasing food or special services.
- Time is tracked by a distance counter, which decreases randomly each day.
- Food is consumed daily, and you can buy additional food at certain checkpoints.
- Scenarios are randomly selected and can add or subtract time, food, or directly affect your survival.
- Hunting allows you to gather food but doesn't present additional scenarios.
- Success in scenarios depends on randomized outcomes and character abilities.

## Getting Started

**Installation**
To play the game, you'll first need to install Python on your system. Here are the steps to install Python and download the source code:

**Install Python:**
Visit the official Python website at https://www.python.org/.
Click on the "Downloads" tab and select the appropriate installer for your operating system (e.g., Windows, macOS, or Linux).
Download the latest version of Python 3.x.x (where x represents the specific version).
Run the installer and follow the instructions provided. Make sure to check the box that says "Add Python to PATH" during the installation process.

**Clone the repository:**
Open your preferred command-line interface (e.g., Command Prompt on Windows or Terminal on macOS/Linux).
Navigate to the directory where you want to store the game's source code.
Execute the following command to clone the repository:
git clone https://github.com/Crstt/SDEV265_GroupRed.git

**Access the game directory:**
Change your current directory to the "oregon-trail-python" folder within the cloned repository:
cd SDEV265_GroupRed/oregon-trail-python
Install the dependency with the following command “pip install -r .\requirements.txt.”

**Run the game script:**
Launch the game by executing the following command:
python oregon_trail.py
If you don't have Git installed or prefer not to use it, you can still download the source code for the Oregon Trail game directly from the GitHub repository. Here's an alternative method to download the source code:
Visit the Oregon Trail GitHub repository:
Go to the following URL in your web browser: https://github.com/Crstt/SDEV265_GroupRed.
Download the source code as a ZIP file:
On the repository page, click on the green "Code" button.
In the dropdown menu, click on "Download ZIP".
This will download the entire repository as a ZIP file to your computer.

**Extract the ZIP file:**
Once the ZIP file is downloaded, locate it on your computer and extract its contents to a desired location.
You can use a built-in ZIP extraction tool or a third-party software like 7-Zip or WinRAR.

**Access the game directory:**
Open the extracted folder that corresponds to the downloaded ZIP file.
Within that folder, navigate to the "oregon-trail-python" directory.
Install the dependency with the following command “pip install -r .\requirements.txt.”

**Run the game script:**
Open your preferred command-line interface (e.g., Command Prompt on Windows or Terminal on macOS/Linux).
Change your current directory to the "oregon-trail-python" folder you located in the previous step.
Execute the following command to start the game:
'python oregon_trail.py'


## Requirements

- Python 3.0 or above

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

## Acknowledgements

This game was inspired by the original Oregon Trail game and created as a Python implementation. Special thanks to the developers and contributors of the original game for their creativity and inspiration.

Enjoy your journey along the Oregon Trail!
