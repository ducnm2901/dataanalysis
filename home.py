import streamlit as st
import pandas as pd
import mysql.connector
from mysql.connector import Error   
from query_functions import create_connection #view_all_data  # Import hàm từ query.py
# ================== CẤU HÌNH GIAO DIỆN ==================
st.set_page_config(page_title="📊 DUC NGUYEN", layout="wide")

# ================== QUẢN LÝ TRANG ==================
#st.sidebar.title("Chuyển trang")
page = st.sidebar.radio("", ["Upload sale data", "Trang 2", "Trang 3"])

# ================== TRANG 1 ==================
# 
# # ✅ Gọi hàm kết nối
conn = create_connection()

if conn:
    st.success("✅ Kết nối MySQL thành công!")
else:
    st.error("❌ Không thể kết nối đến MySQL!")

# ✅ Hàm nhập CSV vào MySQL
def insert_data_to_mysql(table_name, df):
    conn = create_connection()
    if conn is not None:
        cursor = conn.cursor()

        # 🔹 Xác định cột ngày cần chuyển đổi
        date_columns = [df.columns[i - 1] for i in [3, 11, 12, 13, 43, 44] if i - 1 < len(df.columns)]
        
        for col in date_columns:
            df[col] = pd.to_datetime(df[col], errors='coerce').dt.strftime('%Y-%m-%d %H:%M:%S')  # Chuyển về chuỗi

        # 🔹 Tạo bảng nếu chưa có
        create_table_query = f"CREATE TABLE IF NOT EXISTS {table_name} ("
        for column in df.columns:
            col_type = "DATETIME" if column in date_columns else "VARCHAR(255)"
            create_table_query += f"{column} {col_type},"
        create_table_query = create_table_query.rstrip(',') + ")"
        cursor.execute(create_table_query)

        # 🔹 Chèn dữ liệu
        for _, row in df.iterrows():
            sql = f"INSERT INTO {table_name} ({', '.join(df.columns)}) VALUES ({', '.join(['%s'] * len(row))})"
            cursor.execute(sql, tuple(row))

        conn.commit()
        cursor.close()
        conn.close()
        st.success(f"✅ Dữ liệu đã được nhập vào bảng '{table_name}' thành công!")




# 🔹 Trang 1 - Nhập CSV (Có Sidebar)
if page == "Upload sale data":
    st.title("📂 Upload CSV vào MySQL")

    # Sidebar chỉ hiển thị trong trang 1
    st.sidebar.header("📤 Nhập dữ liệu vào MySQL")
    uploaded_file = st.sidebar.file_uploader("Chọn tệp CSV", type=["csv"])
    table_name = st.sidebar.text_input("🗄️ Nhập tên bảng MySQL", value="ShopeeOrders")

    if uploaded_file is not None and table_name:
        df = pd.read_csv(uploaded_file)
        
        # Hiển thị bản xem trước dữ liệu
        st.subheader("📌 Xem trước dữ liệu:")
        st.dataframe(df.head())

        # Nút nhập dữ liệu vào MySQL trong sidebar
        if st.sidebar.button("⬆️ Nhập vào MySQL"):
            insert_data_to_mysql(table_name, df)




# ================== TRANG 2 ==================
elif page == "Trang 2":
    st.title("📊 Trang 2")
    st.sidebar.subheader("⚙️ Cài đặt Trang 2")
    #slider_value = st.sidebar.slider("Điều chỉnh giá trị", 0, 100, 50)
    #st.write(f"🔹 Giá trị hiện tại: {slider_value}")
    #st.write("💡 Đây là nội dung trang 2.")

    # ✅ Lấy dữ liệu từ MySQL
    def get_data():
        conn = create_connection()
        if conn is not None:
            query = "SELECT * FROM Orders"  # Thay bằng tên bảng
            df = pd.read_sql(query, conn)
            conn.close()
            return df
        return pd.DataFrame()

    import streamlit.components.v1 as components

    # ✅ Xóa dòng theo ID
    def delete_data(row_id):
        conn = create_connection()
        if conn is not None:
            cursor = conn.cursor()
            cursor.execute(f"DELETE FROM Orders WHERE Id = {row_id}")  # Thay bằng tên bảng
            conn.commit()
            conn.close()
            st.experimental_rerun()  # Refresh lại trang sau khi xóa
    
    # ✅ Hiển thị dữ liệu với nút XÓA
    df = get_data()
    
    if not df.empty:
        df["Xóa"] = df["Id"].apply(lambda x: f'<button onclick="delete_row({x})">🗑️</button>')
        st.write("### Dữ liệu từ MySQL")
        st.write(df.to_html(escape=False), unsafe_allow_html=True)
        
        # ✅ JavaScript để xử lý xóa
        components.html(
            """
            <script>
            function delete_row(row_id) {
                var xhr = new XMLHttpRequest();
                xhr.open("GET", "/?delete=" + row_id, true);
                xhr.send();
                location.reload();
            }
            </script>
            """,
            height=0,
        )
    
    # ✅ Kiểm tra URL để thực hiện xóa
    if "delete" in st.experimental_get_query_params():
        row_id = st.experimental_get_query_params()["delete"][0]
        delete_data(row_id)



# ================== TRANG 3 ==================
elif page == "Trang 3":
    st.title("🎨 Trang 3")
    st.sidebar.subheader("⚙️ Cài đặt Trang 3")
    text_input = st.sidebar.text_input("Nhập nội dung")
    st.write(f"📝 Nội dung nhập vào: {text_input}")
    st.write("💡 Đây là nội dung trang 3.")
