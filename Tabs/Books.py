import streamlit as st

def app():
    # Hiển thị tiêu đề của trang
    st.title("Books")

    # Hiển thị thông tin về cuốn sách
    st.header("Cuốn sách: Kiến Thức Nghề Lập Trình ")
    st.write("Mô tả: ")
    st.write("– Cung cấp A-Z kiến thức và nghề lập trình, đầy đủ, chi tiết. Từ đó giúp người mới bắt đầu biết mình sẽ phải học gì, làm gì tiếp theo, ko bị hoang mang trong 1 núi thông tin khổng lồ trên mạng")
    st.write("– Giúp người mới bắt đầu đi đúng hướng, học đúng chỗ, tránh mất thời gian")
    st.write("– Giúp định hướng rõ ràng trong nghề lập trình: Học xong sẽ theo lĩnh vực nào trong nghề lập trình, làm việc ở đâu, mức lương bao nhiêu, cần phải chuẩn bị những gì")
    st.write("– Ngoài ra được trang trị những kiến thức mới nhất về các công nghệ đang là xu hướng như mới nhất, cách ứng dụng khác vào công việc lập trình")
    st.write("– Được lắng nghe chia sẻ thực từ người trong nghề đi làm trên 6 năm kinh nghiệm")
if __name__ == "__main__":
    app()
