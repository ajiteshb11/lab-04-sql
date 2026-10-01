import pandas as pd

df = pd.read_csv("MOCK_DATA.csv")

print("First 5 rows:")
print(df.head())

print("\nData types:")
print(df.dtypes)

print("\nMissing values:")
print(df.isna().sum())

print("\nRows:", len(df))
import os
import logging
import pandas as pd
import mysql.connector

# Configure logging
logging.basicConfig(level=logging.INFO)

# Read database credentials from environment variables
DBHOST = os.getenv("DBHOST")
DBUSER = os.getenv("DBUSER")
DBPASS = os.getenv("DBPASS")
DBNAME = os.getenv("DBNAME")


def read_data(filename):
    """Read a CSV file and return it as a pandas DataFrame."""
    logging.info("Reading data from %s", filename)
    data = pd.read_csv(filename)
    return data


def clean_data(data):
    """Remove rows containing missing values and return cleaned data."""
    logging.info("Cleaning data")

    # Remove rows with any missing values
    cleaned_data = data.dropna()

    logging.info("Rows remaining after cleaning: %s", len(cleaned_data))
    return cleaned_data

def load_data(data, table):
    """Create the destination table and upload cleaned data to MySQL."""
    logging.info("Connecting to database")

    try:
        connection = mysql.connector.connect(
            host=DBHOST,
            user=DBUSER,
            password=DBPASS,
            database=DBNAME
        )

        cursor = connection.cursor()

        # Create the mock table if it does not already exist
        create_table_query = """
        CREATE TABLE IF NOT EXISTS mock (
            id BIGINT PRIMARY KEY,
            `group` VARCHAR(255),
            first_name VARCHAR(255),
            last_name VARCHAR(255),
            email VARCHAR(255),
            age DOUBLE
        )
        """
        cursor.execute(create_table_query)

        # Insert each row using a parameterized query
        insert_query = """
        INSERT INTO mock
        (id, `group`, first_name, last_name, email, age)
        VALUES (%s, %s, %s, %s, %s, %s)
        """

        for _, row in data.iterrows():
            values = (
                int(row["id"]),
                row["group"],
                row["first_name"],
                row["last_name"],
                row["email"],
                float(row["age"])
            )
            cursor.execute(insert_query, values)

        connection.commit()
        logging.info("Data uploaded successfully")

        cursor.close()
        connection.close()

    except mysql.connector.Error as error:
        logging.error("Database error: %s", error)
def main():
    """Run the complete ETL pipeline."""
    data = read_data("MOCK_DATA.csv")
    cleaned_data = clean_data(data)
    load_data(cleaned_data, "mock")


if __name__ == "__main__":
    main()