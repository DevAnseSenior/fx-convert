# FXConvert

FXConvert is a currency conversion API built using FastAPI. It provides real-time currency exchange rates and conversion features to integrate into your applications seamlessly.

## Features

- **Real-time exchange rates**: Fetch the latest exchange rates for a variety of currencies.
- **Currency conversion**: Convert amounts from one currency to another.
- **Fast and efficient**: Powered by FastAPI for high performance and minimal latency.
- **Scalable and secure**: Designed to handle high traffic and ensure secure data transactions.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/DevAnseSenior/fx-convert.git
   cd fx-convert
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv .venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Start the FastAPI server:
   ```bash
   uvicorn main:app --reload
   ```

5. Access the API documentation:
   - Interactive API docs (Swagger UI): `http://127.0.0.1:8000/docs`
   - Alternative API docs (ReDoc): `http://127.0.0.1:8000/redoc`

## Usage

### Endpoints

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE.txt) file for details.

---

