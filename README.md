# Used Car Price Predictor

## Setup

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/used-car-price-predictor.git
    cd used-car-price-predictor
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

4. Create a `.env` file in the project root directory and add your database credentials:
    ```plaintext
    DB_USER=your_db_user
    DB_PASSWORD=your_db_password
    DB_HOST=your_db_host
    DB_NAME=your_db_name
    ```

5. Set up the database by running the setup script:
    ```bash
    python setup_database.py
    ```

6. Place your CSV file with used car data in the project directory and update the path in `load_data.py`:
    Use the following link to a Kaggle dataset:
    https://www.kaggle.com/datasets/shivanink8/used-cars-dataset
    Download the dataset as a csv file and copy its path. Update that path in `load_data.py`.
    
    ```plaintext
    path_to_your_csv_file.csv
    ```

7. Load the data into the database by running the load script:
    ```bash
    python load_data.py
    ```

8. Run the build script to generate the model and column files:
    ```bash
    python build_model.py
    ```
    This will create `used_car_price_model.pkl` and `model_columns.pkl` files.
    This will also return the model's Mean Squared Error, R-squared, and Variance of Price values.

## Usage

This project predicts used car prices based on various features. Ensure that your database is set up and accessible using the credentials provided in the `.env` file.

To predict the price of a car based on its characteristics, run the following script and follow the prompts:

```bash
python predict_price.py
```
Note that the model is still limited in its parameter types, it was built using a smaller dataset. In the future, a larger dataset will be used to make the model more accurate and broad in its scope.
