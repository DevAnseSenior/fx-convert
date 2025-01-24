# FXConvert

## 📋 Project Description
FXConvert is a currency conversion API built using **FastAPI**. It provides real-time currency exchange rates and powerful conversion features to support various applications, including e-commerce platforms, financial dashboards, and budgeting tools.

## Features

- 💱 Real-time currency conversion.
- 🌐 Support for multiple currencies.
- 🛠️ Lightweight and easy to integrate.

## 🛠️ Project Structure

```
/src
  ├── /api
  │     └── currency_routes.py  # Endpoints for currency conversion
  ├── /models
  │     └── currency_model.py   # Pydantic models for request validation
  ├── /services
  │     └── exchange_service.py # Core logic for currency conversions
  ├── /utils
  │     └── helpers.py          # Utility functions
  ├── main.py                   # FastAPI app initialization
  └── requirements.txt          # Project dependencies
```


## 🔧 Installation and Run

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

3. Get a personal [Alpha Vantage](https://www.alphavantage.co/) API key. In the website, follow the tutorial to obtain the personal key;


4. Create a **.env** file in the project root with the same template as **.env.example** and add your Alpha Vantage personal key in the indicated variable;


5. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

6. Start the FastAPI server:
   ```bash
   uvicorn main:app --reload
   ```

7. Access the API documentation:
   - Interactive API docs (Swagger UI): `http://127.0.0.1:8000/docs`
   - Alternative API docs (ReDoc): `http://127.0.0.1:8000/redoc`

## 📄 Usage

### Endpoints

| Method | Endpoint          | Description                                                |
|--------|-------------------|------------------------------------------------------------|
| GET    | `/converter/{from_currency}`        | Convert currency amount synchronously                      |
| GET    | `/converter/async/{from_currency}`          | Convert currency amount asynchronously w/ query parameters |
| GET    | `/converter/async/v2/{from_currency}`     | Convert currency amount asynchronously w/ body parameters  |

### Request Example (GET `/converter/{from_currency}`)
```bash
http://127.0.0.1:8000/converter/BRL?to_currencies=USD,GBP,EUR,JPY&value=5.61
```

### Response Example
```json
[
   0.952017, 
   0.7607160000000001, 
   0.9043320000000001, 
   148.13205000000002
]

```

### Request Example (GET `/converter/async/{from_currency}`)
```bash
http://127.0.0.1:8000/converter/async/BRL?to_currencies=USD,GBP,EUR,JPY&value=5.91
```

### Response Example
```json
[
    {
        "USD": 1.0023360000000001
    },
    {
        "GBP": 0.8008050000000001
    },
    {
        "EUR": 0.952101
    },
    {
        "JPY": 155.95899
    }
]
```
### Request Example (GET `/converter/async/v2/{from_currency}`)
```bash
http://127.0.0.1:8000/converter/async/v2/BRL
```
#### Request Body
```json
{
  "value": 5.90,
  "to_currencies": [
     "USD", 
     "GBP", 
     "EUR", 
     "JPY"
  ]
}
```

### Response Example
```json
{
    "message": "success",
    "data": [
        {
            "USD": 1.00005
        },
        {
            "GBP": 0.7994500000000001
        },
        {
            "EUR": 0.9504900000000001
        },
        {
            "JPY": 155.64790000000002
        }
    ]
}
```

## 📚 Use Cases

- **E-commerce platforms**: Display real-time prices in different currencies.
- **Finance apps**: Offer currency tracking and conversion tools for users.
- **Data analysis**: Integrate exchange rate data for market research.

## 📝 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE.txt) file for details.

## 📞 Contact

Feel free to reach out with questions or suggestions:

- **GitHub**: [DevAnseSenior](https://github.com/DevAnseSenior)

---

