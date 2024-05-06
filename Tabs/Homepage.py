import streamlit as st
from Tabs.Books import app
def center_image(image_path, width):
    # Tạo một container để căn giữa hình ảnh
    container = st.empty()
    
    # Thêm hình ảnh vào container
    container.image(image_path, caption='Book Rental Service', width=width, use_column_width=True)

    # Đảm bảo hình ảnh được căn giữa bằng cách thêm một khoảng trắng trống vào đầu container
    container.write("")

def app():
     # Tiêu đề chào mừng
    st.markdown("""
        <style>
        .centered {
            display: flex;
            justify-content: center;
        }
        </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="centered"><h1>My Library</h1></div>', unsafe_allow_html=True)

    # Đường dẫn đến hình ảnh và chiều rộng mong muốn
    st.image(image="https://tusachonthihay.com/wp-content/uploads/2023/04/Picsart_23-04-22_14-21-59-998.jpg", caption='Books for new programmers', width=100, use_column_width=True)
    book_image = "https://tusachonthihay.com/wp-content/uploads/2023/04/Picsart_23-04-22_14-21-59-998.jpg"  # Thay thế URL bằng URL thực tế của hình ảnh sách
    image_width = 100

    # Gọi hàm để căn giữa hình ảnh
    center_image(book_image, image_width)

   # Kiểm tra xem nút "Explore Now" có được nhấn hay không
    option = st.button("Explore Now")
    if option:
        pass
        

if __name__ == "__main__":
    app()
