import streamlit as st
import requests
import json
import time


def get_books_api():
    api_endpoint = "https://www.googleapis.com/books/v1/volumes?q=your_search_term"
    response = requests.get(api_endpoint)
    if response.status_code == 200: ## success status
        data = response.json()
        if isinstance(data, dict) and "items" in data:
            return data["items"]
        else:
            return []
    else:
        return []

def display_books(books):
    for book in books:
        volume_info = book.get("volumeInfo", {})
        title = volume_info.get("title", "Unknown Title")
        image_links = volume_info.get("imageLinks", {})
        thumbnail = image_links.get("thumbnail", "")
        info_link = volume_info.get("infoLink", "#")

        # Display book information
        col1, col2 = st.columns([1, 4])
        with col1:
            if thumbnail:
                st.image(thumbnail, caption=title)
            else:
                st.write("Không có hình ảnh")
        with col2:
            st.write(f"**Liên kết:** [{title}]({info_link})")

def app():
    # Display page title
    st.title("Books")

    while True:
        # Call the API and display images of books
        books = get_books_api()
        display_books(books)

        # Sleep for a specified refresh interval
        time.sleep(10)
        st.rerun()
          # Adjust this value as needed

if __name__ == "__main__":
    app()