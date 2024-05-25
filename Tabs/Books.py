import streamlit as st
import requests

# Hàm lấy dữ liệu sách từ Google Books API với từ khóa tìm kiếm
def get_books_api(search_term):
    api_endpoint = f"https://www.googleapis.com/books/v1/volumes?q={search_term}"
    response = requests.get(api_endpoint)
    if response.status_code == 200:  
        data = response.json()  
        if isinstance(data, dict) and "items" in data:
            return data["items"]  
        else:
            return []  
    else:
        return []  

# Hàm hiển thị thông tin sách lên giao diện Streamlit
def display_books(books):
    for index, book in enumerate(books):
        volume_info = book.get("volumeInfo", {})  
        title = volume_info.get("title", "Unknown Title")  
        description = volume_info.get("description", "No description available.")  
        image_links = volume_info.get("imageLinks", {})  
        thumbnail = image_links.get("thumbnail", "")  
        info_link = volume_info.get("infoLink", "#")  

        # Hiển thị thông tin sách
        col1, col2 = st.columns([1, 4])  
        with col1:
            if thumbnail:
                st.image(thumbnail, caption=title, width=149)  
            else:
                st.write("Không có hình ảnh")  
        with col2:
            st.write(f"**Title:** {title}")  

            # Hiển thị một phần của mô tả sách và nút "Xem thêm" với ID duy nhất
            max_description_length = 150  # Số ký tự tối đa hiển thị ban đầu
            widget_id = f"show_description_{index}"  # Tạo ID duy nhất cho mỗi nút
            button_label = "Xem thêm" if len(description) > max_description_length else "Xem thêm"

            # Tạo hoặc lấy trạng thái của nút "Xem thêm" cho sách hiện tại từ session state
            state_key = f"description_state_{index}"
            if state_key not in st.session_state:
                st.session_state[state_key] = False  # Mặc định ẩn mô tả

            # Kiểm tra trạng thái của nút "Xem thêm" và hiển thị mô tả tương ứng
            if st.button(button_label, key=widget_id):
                st.session_state[state_key] = not st.session_state[state_key]  # Đảo ngược trạng thái khi nút được nhấn

            # Hiển thị mô tả tùy thuộc vào trạng thái của nút "Xem thêm"
            if st.session_state[state_key]:
                st.write(f"**Mô tả:** {description}")  
            else:
                st.write(f"**Mô tả:** {description[:max_description_length]}...")

            st.write(f"**LinkBook:** [{title}]({info_link})")

# Hàm chính của ứng dụng
def app():
    st.title("The Books My Library")

    topics = [
        "Python Programming", 
        "Data Science", 
        "Machine Learning", 
        "Artificial Intelligence", 
        "Web Development", 
        "Java Programming",
        "C++ Programming",
        "JavaScript Programming",
        "Ruby Programming",
        "Go Programming",
        "SQL",
        "Object Oriented Programming (OOP)",
        "HTML",
        "CSS",
        "PHP",
        "Swift",
        "Kotlin",
        "R Programming",
        "MATLAB",
        "Assembly Language",
        "Shell Scripting",
        "React.js",
        "Vue.js",
        "Angular",
        "Django",
        "Flask",
        "Spring Framework",
        "Node.js",
        "Express.js",
        "TensorFlow",
        "PyTorch",
        "Keras",
        "Scikit-learn",
        "Pandas",
        "NumPy",
        "Matplotlib",
        "Seaborn",
        "Plotly",
        "Bokeh",
        "Jupyter Notebook",
        "Apache Spark",
        "Hadoop",
        "MongoDB",
        "MySQL",
        "PostgreSQL",
        "SQLite",
        "Docker",
        "Kubernetes",
        "Git",
        "GitHub",
        "GitLab",
        "Bitbucket"
    ]

    selected_topic = st.selectbox("Chọn chủ đề", topics)

    books = get_books_api(selected_topic)
    display_books(books)

if __name__ == "__main__":
    app()