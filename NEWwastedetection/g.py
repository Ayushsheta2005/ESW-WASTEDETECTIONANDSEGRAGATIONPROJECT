import pandas as pd
import matplotlib.pyplot as plt

# Load CSV data
data = pd.read_csv("detection_history.csv", parse_dates=["timestamp"])

# Define colors for types
type_colors = {'Recyclable': '#2ecc71', 'Non-Recyclable': '#3498db', 'Hazardous': '#e74c3c'}

# Add a time column for time-based analysis
data['time'] = data['timestamp'].dt.strftime('%H:%M:%S')

# ---------- Graphs ----------

# 1. Item Count by Type (Bar Chart)
plt.figure(figsize=(8, 6))
type_counts = data['type'].value_counts()
type_counts.plot(kind='bar', color=[type_colors[t] for t in type_counts.index])
plt.title("Item Count by Type", fontsize=14)
plt.ylabel("Count", fontsize=12)
plt.xlabel("Type", fontsize=12)
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# 2. Item Frequency Over Time (Line Chart)
plt.figure(figsize=(12, 6))
time_counts = data.groupby(['time', 'type']).size().unstack(fill_value=0)
time_counts.plot(marker='o', color=[type_colors[t] for t in time_counts.columns], ax=plt.gca())
plt.title("Item Frequency Over Time", fontsize=14)
plt.ylabel("Count", fontsize=12)
plt.xlabel("Time", fontsize=12)
plt.xticks(rotation=45)
plt.grid()
plt.legend(title="Type")
plt.show()

# 3. Item Distribution by Type (Pie Chart)
plt.figure(figsize=(8, 8))
type_counts.plot(kind='pie', autopct='%1.1f%%', colors=[type_colors[t] for t in type_counts.index])
plt.title("Item Distribution by Type", fontsize=14)
plt.ylabel("")  # Hide y-label for better display
plt.show()

# 4. Top Detected Items (Horizontal Bar Chart)
plt.figure(figsize=(8, 6))
item_counts = data['item'].value_counts()
item_counts.head(10).plot(kind='barh', color='#3498db')  # Neutral blue for mixed items
plt.title("Top 10 Detected Items", fontsize=14)
plt.xlabel("Count", fontsize=12)
plt.ylabel("Item", fontsize=12)
plt.gca().invert_yaxis()  # Invert y-axis for better readability
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.show()

# 5. Stacked Bar Chart for Type Over Time
plt.figure(figsize=(12, 6))
time_type_counts = data.groupby(['time', 'type']).size().unstack(fill_value=0)
time_type_counts.plot(kind='bar', stacked=True, color=[type_colors[t] for t in time_type_counts.columns], ax=plt.gca())
plt.title("Stacked Item Count by Type Over Time", fontsize=14)
plt.ylabel("Count", fontsize=12)
plt.xlabel("Time", fontsize=12)
plt.xticks(rotation=45)
plt.legend(title="Type")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# 6. Heatmap of Items Detected Over Time
import seaborn as sns
time_item_counts = data.groupby(['time', 'item']).size().unstack(fill_value=0)
plt.figure(figsize=(12, 8))
sns.heatmap(time_item_counts, cmap="Blues", annot=False, cbar=True, linewidths=0.5)
plt.title("Heatmap of Items Detected Over Time", fontsize=14)
plt.xlabel("Item", fontsize=12)
plt.ylabel("Time", fontsize=12)
plt.xticks(rotation=45)
plt.show()

# 7. Daily Summary (Grouped by Type)
plt.figure(figsize=(8, 6))
daily_summary = data.groupby([data['timestamp'].dt.date, 'type']).size().unstack(fill_value=0)
daily_summary.plot(kind='bar', stacked=True, color=[type_colors[t] for t in daily_summary.columns], ax=plt.gca())
plt.title("Daily Summary of Waste Categories", fontsize=14)
plt.ylabel("Count", fontsize=12)
plt.xlabel("Date", fontsize=12)
plt.xticks(rotation=45)
plt.legend(title="Type")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
