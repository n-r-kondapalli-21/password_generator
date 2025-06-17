# Password Generator Project

This is a simple password generator application built with Streamlit. It allows users to generate strong, random passwords by specifying the number of letters, digits, and symbols they want.

## Features

-   Generate passwords with a custom length.
-   Include a mix of letters (uppercase and lowercase), digits, and symbols.
-   Enforces minimum security requirements:
    -   At least 2 digits.
    -   At least 1 symbol.
    -   A minimum total password length of 8 characters.
-   Simple and easy-to-use web interface.
-   A visually appealing interface with a background image.

## How to Run

1.  **Prerequisites:**
    *   Python 3.x installed on your system.
    *   `pip` package manager.

2.  **Clone the repository or download the source code:**
    If you have git, you can clone it. Otherwise, just download the `passwordgen.py` file.

3.  **Install the required dependencies:**
    The only dependency is `streamlit`. You can install it using pip:
    ```bash
    pip install streamlit
    ```

4.  **Run the application:**
    Open your terminal or command prompt, navigate to the directory where `passwordgen.py` is located, and run the following command:
    ```bash
    streamlit run passwordgen.py
    ```

5.  Your web browser will open with the password generator application running.

## Code Overview

The main script `passwordgen.py` does the following:
- Imports necessary libraries (`random`, `streamlit`).
- Defines the character sets for letters, digits, and symbols.
- Sets up the Streamlit page with a title and a background image.
- Uses `st.number_input` to get user input for the number of letters, digits, and symbols.
- Validates the user input to ensure it meets the minimum security requirements.
- Generates the password by:
    - Randomly selecting characters of each type.
    - Shuffling the list of selected characters to ensure randomness.
    - Joining the characters to form the final password string.
- Displays the generated password to the user. 