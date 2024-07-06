# Currency Converter

This project demonstrates a simple currency converter application using Python, Flask, HTML, and CSS. It utilizes an external API to fetch real-time exchange rates and allows users to convert between different currencies.

## Features

- Converts currency based on real-time exchange rates fetched from an API.
- Provides a user-friendly interface with HTML and CSS.
- Validates user input for amount and currency selection.
- Displays the converted amount dynamically on the webpage.

## Technologies Used

- **Python**: Backend logic and API integration.
- **Flask**: Web framework for routing and handling requests.
- **HTML**: Structure and content of the webpage.
- **CSS**: Styling and layout design.
- **API**: Utilizes the ExchangeRate-API for fetching exchange rates.

## Getting Started

1. **Prerequisites**:
   - Python 3.x installed on your system.
   - Flask framework (`pip install Flask`).

2. **Setup**:
   - Clone this repository: `git clone https://github.com/vishal-git21/CurrencyConverter`.
   - Navigate to the project directory.

3. **Run the Application**:
   - Open a terminal and run `python app.py`.
   - Access the application in your web browser at `http://localhost:6001`.

## Usage

1. Select the currency you want to convert from and to.
2. Enter the amount in the input field.
3. Click on the "Convert" button to see the converted amount.

## Example API Response

```json
{
    "converted_amount": 75.42
}
```

## Acknowledgments

- [ExchangeRate-API](https://www.exchangerate-api.com/): Provides real-time exchange rates.
