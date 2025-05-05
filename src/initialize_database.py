from database_connection import get_database_connection

def create_tables(connection):
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE Users (
            username text primary key,
            wins integer
        );
    """)

    connection.commit()

def add_users(connection):
    cursor = connection.cursor()

    cursor.execute("INSERT INTO Users (username, wins) values (?, ?)", ("player1", 0))
    cursor.execute("INSERT INTO Users (username, wins) values (?, ?)", ("player2", 0))

    connection.commit()

def drop_tables(connection):
    cursor = connection.cursor()

    cursor.execute("""
        drop table if exists Users;
    """)

    connection.commit()

def initialize_database():
    connection = get_database_connection()

    drop_tables(connection)
    create_tables(connection)
    add_users(connection)


if __name__ == "__main__":
    initialize_database()
