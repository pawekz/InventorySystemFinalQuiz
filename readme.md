# A Very Simple Inventory System

This is a simple inventory management system built with Django.<br>
<strong>NOTE: pure HTML only</strong>

## Prerequisites

- Python 3.12.2
- pip

## Setup

1. Clone the repository:
    ```
    git clone https://github.com/pawekz/InventorySystem.git
    cd InventorySystem
    ```

2. Create a virtual environment and activate it:
    ```
    python -m venv .venv
    source .venv/bin/activate  # On Windows, use `.venv\Scripts\activate`
    ```

3. Install the required packages:
    ```
    pip install -r requirements.txt
    ```

4. Apply the migrations to create the database schema:
    ```
    python manage.py migrate
    ```

5. Run the development server:
    ```
    python manage.py runserver
    ```

Now, you can access the application at `http://localhost:8000`.

## Usage

The system allows you to manage products and suppliers. You can view a list of all products and suppliers, view the details of a specific product or supplier, and edit the details of a product.

## Contributing

If you want to contribute to this project, please fork the repository, make your changes, and open a pull request.

## License

This project is licensed under the MIT License.