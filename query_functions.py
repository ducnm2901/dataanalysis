import mysql.connector
import streamlit as st
import pandas as pd
from mysql.connector import Error

#connection

# ✅ Hàm Kết Nối MySQL
def create_connection():
    try:
        conn = mysql.connector.connect(
            host="123.30.136.246",
            user="vfyhrrzs_ducnm",
            password="Tuan2010@",
            database="vfyhrrzs_MAAC"
        )
        return conn
    except Error as e:
        st.error(f"❌ Lỗi kết nối MySQL: {e}")
        return None
    
    