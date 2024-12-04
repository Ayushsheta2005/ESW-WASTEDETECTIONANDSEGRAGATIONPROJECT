import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from io import BytesIO

# Configure Streamlit page
st.set_page_config(
    page_title="Live Waste Detection Analytics",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Define colors for types
type_colors = {'Recyclable': '#2ecc71', 'Non-Recyclable': '#3498db', 'Hazardous': '#e74c3c'}

# Load and process data
@st.cache_data(ttl=10)  # Cache the data for 10 seconds
def load_data():
    data = pd.read_csv("detection_history.csv", parse_dates=["timestamp"])
    data['time'] = data['timestamp'].dt.strftime('%H:%M:%S')
    return data

def generate_bar_chart(data):
    type_counts = data['type'].value_counts()
    fig, ax = plt.subplots(figsize=(5, 3))
    type_counts.plot(kind='bar', color=[type_colors[t] for t in type_counts.index], ax=ax)
    ax.set_title("Item Count by Type", fontsize=12)
    ax.set_ylabel("Count", fontsize=10)
    ax.set_xlabel("Type", fontsize=10)
    ax.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    return fig

def generate_line_chart(data):
    time_counts = data.groupby(['time', 'type']).size().unstack(fill_value=0)
    fig, ax = plt.subplots(figsize=(8, 4))
    time_counts.plot(marker='o', color=[type_colors[t] for t in time_counts.columns], ax=ax)
    ax.set_title("Item Frequency Over Time", fontsize=12)
    ax.set_ylabel("Count", fontsize=10)
    ax.set_xlabel("Time", fontsize=10)
    ax.grid()
    ax.legend(title="Type", fontsize=8)
    plt.tight_layout()
    return fig

def generate_pie_chart(data):
    type_counts = data['type'].value_counts()
    fig, ax = plt.subplots(figsize=(5, 5))
    type_counts.plot(kind='pie', autopct='%1.1f%%', colors=[type_colors[t] for t in type_counts.index], ax=ax)
    ax.set_title("Item Distribution by Type", fontsize=12)
    ax.set_ylabel("")  # Hide y-label for better display
    plt.tight_layout()
    return fig

def generate_heatmap(data):
    time_item_counts = data.groupby(['time', 'item']).size().unstack(fill_value=0)
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.heatmap(time_item_counts, cmap="Blues", annot=False, cbar=True, linewidths=0.5, ax=ax)
    ax.set_title("Heatmap of Items Detected Over Time", fontsize=12)
    ax.set_xlabel("Item", fontsize=10)
    ax.set_ylabel("Time", fontsize=10)
    plt.tight_layout()
    return fig

# Display data and charts
st.title("📊 Live Waste Detection Analytics")
st.markdown("This dashboard updates automatically as new waste detection data is added to the system.")

# Load data
data = load_data()

# Display charts
st.sidebar.header("Visualization Options")
chart_type = st.sidebar.selectbox(
    "Select Chart Type",
    ["Bar Chart", "Line Chart", "Pie Chart", "Heatmap"]
)

if chart_type == "Bar Chart":
    st.pyplot(generate_bar_chart(data))
elif chart_type == "Line Chart":
    st.pyplot(generate_line_chart(data))
elif chart_type == "Pie Chart":
    st.pyplot(generate_pie_chart(data))
elif chart_type == "Heatmap":
    st.pyplot(generate_heatmap(data))

# Download CSV option
st.sidebar.header("Download Data")
csv_buffer = BytesIO()
data.to_csv(csv_buffer, index=False)
st.sidebar.download_button(
    label="📥 Download CSV",
    data=csv_buffer.getvalue(),
    file_name="detection_history.csv",
    mime="text/csv"
)

st.sidebar.info("This dashboard reloads every time new data is added.")
