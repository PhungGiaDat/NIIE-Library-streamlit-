import pymysql


def connect():
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password="Pgd05092004@",
        database="library_management",
    )
    if connection:
        print("Database connected")
    return connection


if __name__ == "__main__":
    connect()
