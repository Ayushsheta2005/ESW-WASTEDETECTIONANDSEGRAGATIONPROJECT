import matplotlib.pyplot as plt

# Example data (replace with your model's outputs)
categories = ['Recyclable', 'Non-Recyclable', 'Hazardous']
counts = [45, 30, 25]

# Pie chart
plt.figure(figsize=(8, 6))
plt.pie(counts, labels=categories, autopct='%1.1f%%', colors=['green', 'blue', 'red'], startangle=90)
plt.title('Waste Detection Summary')
plt.show()

# Bar graph
plt.figure(figsize=(8, 6))
plt.bar(categories, counts, color=['green', 'blue', 'red'])
plt.title('Waste Detection Summary')
plt.xlabel('Categories')
plt.ylabel('Count')
plt.show()
