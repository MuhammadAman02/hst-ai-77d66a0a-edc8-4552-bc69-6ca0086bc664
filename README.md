# ShopEase - E-commerce Landing Page

A simple yet elegant e-commerce landing page built with Python and NiceGUI.

## Features

- Responsive design that works on desktop and mobile
- Featured products section with discounts
- Category browsing
- Customer testimonials
- Newsletter signup
- Modern UI with smooth animations

## Installation

1. Clone this repository
2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Copy the example environment file:
   ```
   cp .env.example .env
   ```
5. Run the application:
   ```
   python main.py
   ```
6. Open your browser and navigate to `http://localhost:8000`

## Project Structure

```
project/
├── app/
│   ├── frontend/
│   │   └── nicegui_app.py  # Main NiceGUI application
│   ├── models/
│   │   └── product.py      # Product data models
│   └── static/
│       └── css/
│           └── styles.css  # Custom CSS styles
├── main.py                 # Application entry point
├── .env                    # Environment variables
└── README.md               # Documentation
```

## Customization

- Add your own product images to `app/static/images/`
- Modify product data in `app/models/product.py`
- Customize styles in `app/static/css/styles.css`

## Technologies Used

- Python 3.9+
- NiceGUI for the user interface
- Pydantic for data validation

## License

MIT