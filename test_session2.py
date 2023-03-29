import sqlite3
import os
import pytest

DB_PATH = '/Users/gopinath.h03/Library/CloudStorage/OneDrive-IMC/1st Year/Databases/exercise-and-homework-Gopinathh22/Session2/test-db.db'


@pytest.fixture(scope='module')
def db_connection():
    # Remove the database file if it exists
    if os.path.isfile(DB_PATH):
        os.remove(DB_PATH)

    # Connect to the database
    conn = sqlite3.connect(DB_PATH)
    yield conn

    # Close the database connection
    conn.close()


@pytest.fixture(scope='function')
def db_cursor(db_connection):
    cursor = db_connection.cursor()

    # Create the Professor table
    cursor.execute("""
        CREATE TABLE Professor (
            PersNr INTEGER PRIMARY KEY,
            FirstName TEXT,
            LastName TEXT
        );
    """)

    # Insert a professor with PersNr 123, first name "Foo", and last name "Bar"
    cursor.execute("""
        INSERT INTO Professor (PersNr, FirstName, LastName)
        VALUES (123, 'Foo', 'Bar');
    """)

    # Commit the changes
    db_connection.commit()

    yield cursor

    # Rollback the changes
    db_connection.rollback()


def test_add_professor(db_cursor):

    conn = sqlite3.connect(DB_PATH)

    # Insert a professor with PersNr 234, first name "Donald", and last name "Duck"
    db_cursor.execute("""
        INSERT INTO Professor (PersNr, FirstName, LastName)
        VALUES (234, 'Donald', 'Duck');
    """)

    # Count the number of professors in the table
    db_cursor.execute("""
        SELECT COUNT(*) FROM Professor;
    """)
    num_professors = db_cursor.fetchone()[0]

    # Close the database connection
    conn.close()

    # Check that there are two professors in the table
    assert num_professors == 2, f"Expected 2 professors but found {num_professors}"


# def teardown_module(module):
#     # Remove the database file if it exists
#     if os.path.isfile(DB_PATH):
#         os.remove(DB_PATH)


# Print the whole table
def print_table(cursor, table_name):
    cursor.execute(f"SELECT * FROM {table_name}")
    print(cursor.fetchall())


print_table(db_cursor, 'Professor')
