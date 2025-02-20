# Restaurant Name Generator

This project is a simple Streamlit web application that generates a restaurant name and menu based on a selected nationality. It uses OpenAI's language model via LangChain to generate names and menu suggestions.

## Features
- Select a restaurant nationality from a dropdown menu.
- Generate a unique restaurant name.
- Get a list of suggested menu items for the restaurant.
- Handles OpenAI rate limits and authentication errors with retries.

## Installation

### Prerequisites
Ensure you have the following installed:
- Python 3.8+
- pip package manager

### Steps
1. Clone this repository:
   ```sh
   git clone https://github.com/your-repo/restaurant-name-generator.git
   cd restaurant-name-generator
   ```
2. Create and activate a virtual environment:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Set up OpenAI API Key:
   ```sh
   export OPENAI_API_KEY="your_api_key_here"  # On Windows use `set OPENAI_API_KEY=your_api_key_here`
   ```

## Usage
Run the Streamlit application with:
```sh
streamlit run main.py
```

## Project Structure
```
.
├── main.py  # Streamlit app entry point
├── restaurant_name_generator.py  # Core logic for name and menu generation
├── requirements.txt  # Dependencies list
├── README.md  # Project documentation
```

## How It Works
1. The user selects a restaurant nationality from the sidebar.
2. The system generates a restaurant name based on the selected nationality using LangChain and OpenAI.
3. The system then generates menu items based on the restaurant name.
4. The results are displayed in the Streamlit interface.

## Error Handling
- **Rate Limit Handling:** Implements exponential backoff to handle OpenAI rate limits.
- **Authentication Handling:** Catches OpenAI authentication errors and exits gracefully.

## Dependencies
- `langchain`
- `openai`
- `streamlit`
- `time`

