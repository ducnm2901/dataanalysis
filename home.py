import streamlit as st

# ======== Thiết kế giao diện bằng HTML & CSS ========
st.markdown(
    """
    <style>
        /* CSS cho header */
        .main-title {
            font-size: 36px;
            font-weight: bold;
            text-align: center;
            color: #ff4b4b;
            padding: 10px;
        }
        /* Sidebar */
        .sidebar .sidebar-content {
            background-color: #f8f9fa;
            padding: 20px;
            border-radius: 10px;
        }
        /* Chỉnh style radio button */
        .stRadio > label {
            font-size: 18px;
            font-weight: bold;
            color: #007bff;
        }
        /* Link màu xanh */
        a {
            color: #ff4b4b;
            text-decoration: none;
            font-weight: bold;
        }
        a:hover {
            text-decoration: underline;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# ======== Sidebar với Icon & Hiệu Ứng ========
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/4252/4252041.png", width=100)
st.sidebar.title("📌 **Menu Điều Hướng**")
main_page = st.sidebar.radio("Chọn Trang:", ["🏠 Home", "📊 Sale Data", "💸 Expense Data"])

# ======== TRANG HOME ========
if main_page == "🏠 Home":
    st.markdown('<h1 class="main-title">🏠 Home Page</h1>', unsafe_allow_html=True)
    st.write("🎉 **Chào mừng bạn đến với ứng dụng phân tích dữ liệu!**")
    st.write("Ứng dụng giúp bạn theo dõi doanh thu, sản phẩm và chi tiêu.")

# ======== TRANG SALE DATA ========
elif main_page == "📊 Sale Data":
    st.sidebar.subheader("🔽 **Chọn trang con trong Sale Data:**")
    sale_page = st.sidebar.radio("", ["📌 Overview", "📦 Product Sales", "🧑‍💼 Customer Analysis"])

    st.markdown('<h1 class="main-title">📊 Sale Data</h1>', unsafe_allow_html=True)
    
    if sale_page == "📌 Overview":
        st.subheader("📌 Tổng Quan Doanh Số")
        st.write("Trang này hiển thị tổng quan về doanh thu và doanh số.")

    elif sale_page == "📦 Product Sales":
        st.subheader("📦 Sản Phẩm Bán Chạy")
        st.write("Trang này hiển thị dữ liệu về sản phẩm bán chạy nhất.")

    elif sale_page == "🧑‍💼 Customer Analysis":
        st.subheader("🧑‍💼 Phân Tích Khách Hàng")
        st.write("Trang này hiển thị thông tin về khách hàng.")

# ======== TRANG EXPENSE DATA ========
elif main_page == "💸 Expense Data":
    st.markdown('<h1 class="main-title">💸 Expense Data</h1>', unsafe_allow_html=True)
    st.write("Trang này hiển thị dữ liệu về chi phí và phân tích chi tiêu.")

