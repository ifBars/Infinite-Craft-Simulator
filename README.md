# Infinite-Craft-Simulator

Welcome to the Infinite-Craft-Simulator! This script allows you to merge sets of words into new creations using the power of LLMs. 

## Installation

### Linux

1. Clone the repository:
    ```bash
    git clone https://github.com/ifBars/Infinite-Craft-Simulator
    ```

2. Navigate to the project directory:
    ```bash
    cd Infinite-Craft-Simulator
    ```

3. [Install Ollama](https://ollama.com/)

4. Install the required dependencies using pip:
    ```bash
    pip install -r requirements.txt
    ```

### Windows (using WSL)

1. Ensure you have Windows Subsystem for Linux (WSL) installed. You can follow the official documentation for installation: [WSL Installation Guide](https://docs.microsoft.com/en-us/windows/wsl/install)

2. Open WSL and clone the repository:
    ```bash
    wsl
    git clone https://github.com/ifBars/Infinite-Craft-Simulator
    ```

3. Navigate to the project directory:
    ```bash
    cd Infinite-Craft-Simulator
    ```

4. [Install Ollama](https://ollama.com/)

5. Install the required dependencies using pip:
    ```bash
    pip install -r requirements.txt
    ```

I did not test this with the windows preview version of ollama, as I already had the it installed on my WSL.

## Usage

1. Run the script:
    ```bash
    python app.py
    ```

2. Access the application in your web browser by visiting `http://localhost:5000`.

3. You can now generate new merged words by providing two sets of words separated by a dash (-) in the input field and clicking on the "Generate" button.

## Example

Suppose you want to merge the sets of words "magic" and "spell". You would input "magic-spell" into the prompt field, and the script will generate a new merged word for you.

Enjoy creating infinite combinations of words!
