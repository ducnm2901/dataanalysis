import streamlit as st

# Tạo sidebar menu
st.sidebar.title("📌 Menu Điều Hướng")
main_page = st.sidebar.radio("Chọn Trang Chính:", ["🏠 Home", "📊 Sale Data", "💸 Expense Data"])

# =================== TRANG HOME ===================
if main_page == "🏠 Home":
    st.title("🏠 Home Page")
    st.write("Chào mừng bạn đến với ứng dụng phân tích dữ liệu!")

# =================== TRANG SALE DATA ===================
elif main_page == "📊 Sale Data":
    st.title("📊 Sale Data")

    # Tạo menu con cho Sale Data
    sale_page = st.radio("Chọn mục:", ["📌 Overview", "📦 Product Sales", "🧑‍💼 Customer Analysis"])

    if sale_page == "📌 Overview":
        st.subheader("📌 Tổng Quan Doanh Số")
        st.write("Trang này hiển thị tổng quan về doanh thu và doanh số.")

    elif sale_page == "📦 Product Sales":
        st.subheader("📦 Sản Phẩm Bán Chạy")
        st.write("Trang này hiển thị dữ liệu về sản phẩm bán chạy nhất.")

    elif sale_page == "🧑‍💼 Customer Analysis":
        st.subheader("🧑‍💼 Phân Tích Khách Hàng")
        st.write("Trang này hiển thị thông tin về khách hàng.")

# =================== TRANG EXPENSE DATA ===================
elif main_page == "💸 Expense Data":
    st.title("💸 Expense Data")
    st.write("Trang này hiển thị dữ liệu về chi phí và phân tích chi tiêu.")


