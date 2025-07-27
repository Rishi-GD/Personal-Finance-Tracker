# Personal Finance Tracker using Streamlit

import streamlit as st
import pandas as pd
import datetime

st.set_page_config(page_title="💰 Personal Finance Tracker", layout="centered")

st.title("💰 Personal Finance Tracker")
st.markdown("Track your daily expenses, income, and analyze your spending habits.")

# Initialize session state
if "data" not in st.session_state:
    st.session_state.data = []

# Input section
with st.form("entry_form", clear_on_submit=True):
    col1, col2 = st.columns(2)
    with col1:
        amount = st.number_input("Amount (₹)", min_value=0.0, format="%.2f")
    with col2:
        category = st.selectbox("Category", ["Food", "Transport", "Bills", "Entertainment", "Shopping", "Salary", "Other"])
    
    entry_type = st.radio("Type", ["Expense", "Income"], horizontal=True)
    date = st.date_input("Date", datetime.date.today())
    description = st.text_input("Description")

    submitted = st.form_submit_button("Add Entry")
    if submitted:
        st.session_state.data.append({
            "Date": date,
            "Amount": amount,
            "Category": category,
            "Type": entry_type,
            "Description": description
        })
        st.success("Entry added!")

# Show data
if st.session_state.data:
    df = pd.DataFrame(st.session_state.data)
    st.subheader("📊 Finance Summary")
    total_expense = df[df["Type"] == "Expense"]["Amount"].sum()
    total_income = df[df["Type"] == "Income"]["Amount"].sum()
    balance = total_income - total_expense

    col1, col2, col3 = st.columns(3)
    col1.metric("Total Income", f"₹{total_income:.2f}")
    col2.metric("Total Expense", f"₹{total_expense:.2f}")
    col3.metric("Net Balance", f"₹{balance:.2f}")

    st.subheader("📋 All Entries")
    st.dataframe(df.sort_values("Date", ascending=False), use_container_width=True)
