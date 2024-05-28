import pymysql


def connect():
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password="#######",
        database="library_management",
    )
    if connection:
        print("Database connected")
    return connection


if __name__ == "__main__":
    connect()
