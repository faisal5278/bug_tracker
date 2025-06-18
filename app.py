
import sqlite3
import pandas as pd
import streamlit as st
import plotly.express as px


conn = sqlite3.connect('bug_tracker.db')
cursor = conn.cursor()


df = pd.read_sql_query("SELECT * FROM bugs", conn)

st.set_page_config(page_title="Bug Tracker Dashboard", layout="wide")
st.title("🐞 Mini Bug Tracker Dashboard")


st.subheader("📊 Bug Summary")
col1, col2, col3 = st.columns(3)
col1.metric("🐞 Open Bugs", df[df['status'] == 'Open'].shape[0])
col2.metric("✅ Closed Bugs", df[df['status'] == 'Closed'].shape[0])
col3.metric("🔥 High Severity", df[df['severity'] == 'High'].shape[0])


st.sidebar.header("🔎 Filter Bugs")
status_filter = st.sidebar.selectbox("Status", options=["All", "Open", "Closed"])
severity_filter = st.sidebar.selectbox("Severity", options=["All", "Low", "Medium", "High"])
module_filter = st.sidebar.selectbox("Module", options=["All"] + sorted(df['module'].unique().tolist()))


filtered_df = df.copy()
if status_filter != "All":
    filtered_df = filtered_df[filtered_df["status"] == status_filter]
if severity_filter != "All":
    filtered_df = filtered_df[filtered_df["severity"] == severity_filter]
if module_filter != "All":
    filtered_df = filtered_df[filtered_df["module"] == module_filter]


st.subheader("📈 Visual Insights")
chart_col1, chart_col2 = st.columns(2)


with chart_col1:
    status_counts = df['status'].value_counts().reset_index()
    status_counts.columns = ['status', 'count']
    fig1 = px.pie(status_counts, names='status', values='count', title='Bug Status Distribution')
    st.plotly_chart(fig1, use_container_width=True)


with chart_col2:
    severity_counts = df['severity'].value_counts().reset_index()
    severity_counts.columns = ['severity', 'count']
    fig2 = px.bar(severity_counts, x='severity', y='count', color='severity',
                  title='Bug Count by Severity', labels={'severity': 'Severity', 'count': 'Count'})
    st.plotly_chart(fig2, use_container_width=True)


st.subheader("📋 Bug List")
st.dataframe(filtered_df)

# Download
st.download_button("⬇️ Download CSV", filtered_df.to_csv(index=False), "bugs.csv")

conn.close()