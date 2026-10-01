"""Query data from the mock MySQL database."""

import os
import logging
import mysql.connector


# Configure logging
logging.basicConfig(level=logging.INFO)

# Read database credentials from environment variables
DBHOST = os.getenv("DBHOST")
DBUSER = os.getenv("DBUSER")
DBPASS = os.getenv("DBPASS")
DBNAME = os.getenv("DBNAME")


def get_data_by_group(value):
    """Return all rows where the `group` column equals value."""
    logging.info("Getting data for group: %s", value)

    try:
        connection = mysql.connector.connect(
            host=DBHOST,
            user=DBUSER,
            password=DBPASS,
            database=DBNAME,
        )

        cursor = connection.cursor()

        # Use a parameterized query to safely filter by group
        query = """
        SELECT *
        FROM mock
        WHERE `group` = %s
        """

        cursor.execute(query, (value,))
        results = cursor.fetchall()

        cursor.close()
        connection.close()

        return results

    except mysql.connector.Error as error:
        logging.error("Database error: %s", error)
        return []


def plot_counts(groupby):
    """Return counts of rows grouped by the specified column."""
    logging.info("Counting rows grouped by: %s", groupby)

    # Only allow columns that exist in our mock table
    allowed_columns = {
        "id",
        "group",
        "first_name",
        "last_name",
        "email",
        "age",
    }

    if groupby not in allowed_columns:
        raise ValueError("Invalid column name")

    try:
        connection = mysql.connector.connect(
            host=DBHOST,
            user=DBUSER,
            password=DBPASS,
            database=DBNAME,
        )

        cursor = connection.cursor()

        # Column names cannot use %s placeholders, so validate first
        query = f"""
        SELECT `{groupby}`, COUNT(*)
        FROM mock
        GROUP BY `{groupby}`
        """

        cursor.execute(query)
        results = cursor.fetchall()

        cursor.close()
        connection.close()

        return results

    except mysql.connector.Error as error:
        logging.error("Database error: %s", error)
        return []


def main():
    """Run example queries against the mock table."""

    # Demonstrate filtering by group
    group_data = get_data_by_group("Finance")
    print("Finance rows:")
    for row in group_data:
        print(row)

    # Demonstrate grouped counts
    counts = plot_counts("group")
    print("\nCounts by group:")
    for row in counts:
        print(row)


if __name__ == "__main__":
    main()