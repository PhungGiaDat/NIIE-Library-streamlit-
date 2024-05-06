import pymysql
from database.connection import connect


def insert(query, data):
    connection = connect()
    cursor = connection.cursor()
    cursor.execute(query, data)
    connection.commit()
    connection.close()


def select(query):
    connection = connect()
    cursor = connection.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    connection.close()
    return data


def update(query, data):
    connection = connect()
    cursor = connection.cursor()
    cursor.execute(query, data)
    connection.commit()
    connection.close()


def remove(query, data):
    connection = connect()
    cursor = connection.cursor()
    cursor.execute(query, data)
    connection.commit()
    connection.close()
