import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import time
from database.Query import select

def fetch_book_data():
    # Query to fetch book data from the database
    query = """
        SELECT BOOKS.BOOKS_TITLE,BOOKS.QUANTITY
        FROM BOOKS
    """
    # Fetch data using the select method from your database module
    book_data = select(query)
    return book_data


def plot_book_quantity(book_data):
    # Convert fetched data to a DataFrame
    df = pd.DataFrame(book_data, columns=['Book_Quantity', 'Book_Title'])
    
    # Group by book title and sum the book quantity
    book_quantity_count = df.groupby('Book_Title')['Book_Quantity'].sum().reset_index()

    # Plotting the bar chart
    plt.figure(figsize=(15, 8))
    plt.bar(x='Book_Quantity', height='Book_Title', data=book_quantity_count, color='skyblue')
    plt.xlabel('Number of Books')
    plt.ylabel('Book Title')
    plt.title('Number of Books by Title')
    plt.tight_layout()

    # Show the plot
    st.pyplot(plt)

def app():
    # Introduction to the Library Management System
    st.header("Welcome to the NIIE Library Management System!")
    st.write("This system is designed to help manage and organize the library's resources, including books, members, and borrowing records. With this application, you can easily search for books, check their availability status, and manage borrowing transactions.")

    st.subheader("Key Features:")
    st.write("- Book Catalog: Browse and search for books in the library's collection.")
    st.write("- Member Management: Add, update, and manage library member information.")
    st.write("- Borrowing Management: Issue and return books, track borrowing records, and manage due dates.")
    st.write("- Reporting and Analysis: Generate reports and analyze library usage data.")

    st.subheader("Getting Started:")
    st.write("To get started, simply navigate through the side menu to access the different features of the system. If you have any questions or need assistance, please contact the library staff.")

    st.write("We hope you find this system useful and enjoy your experience at the NIIE Library!")

    st.markdown("---")
    st.write("Here is a summary of the number of books available in the library by title:")
    # Fetch book data from the database
    book_data = fetch_book_data()

    # Plot the bar chart
    plot_book_quantity(book_data)

if __name__ == "__main__":
    app()