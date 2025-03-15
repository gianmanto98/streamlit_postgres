import streamlit as st

st.title("PostgreSQL Query App")

conn = st.connection("my_database", type="sql")

# Test connection with a simple query
query = "SELECT 1;"
conn.query(query)

st.success("Connected to PostgreSQL successfully!")

# Query input box
query = st.text_area("Enter your SQL query:", "SELECT * FROM film LIMIT 10")

# Execute query button
if st.button("Execute Query"):
    try:
        df = conn.query(query)  # Fetching data
        st.dataframe(df)  # Display results
    except Exception as e:
        st.error(f"Error: {e}")

