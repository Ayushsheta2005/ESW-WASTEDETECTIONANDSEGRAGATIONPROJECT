from datetime import datetime
import streamlit as st
import csv
from pathlib import Path
from settings import RECYCLABLE, NON_RECYCLABLE, HAZARDOUS


def initialize_session_state():
    """Initialize all session state variables"""
    if 'detection_history' not in st.session_state:
        st.session_state.detection_history = []
    if 'total_items_detected' not in st.session_state:
        st.session_state.total_items_detected = 0
    if 'start_time' not in st.session_state:
        st.session_state.start_time = datetime.now()
    if 'detection_active' not in st.session_state:
        st.session_state.detection_active = False

def update_detection_history(detected_items):
    """Update detection history with new detections"""
    timestamp = datetime.now()
    st.session_state.detection_history.append({
        'timestamp': timestamp,
        'items': detected_items
    })
    st.session_state.total_items_detected += len(detected_items)

def format_time_elapsed(start_time):
    """Format elapsed time into human-readable string"""
    elapsed = datetime.now() - start_time
    hours, remainder = divmod(int(elapsed.total_seconds()), 3600)
    minutes, seconds = divmod(remainder, 60)
    
    if hours > 0:
        return f"{hours}h {minutes}m {seconds}s"
    elif minutes > 0:
        return f"{minutes}m {seconds}s"
    else:
        return f"{seconds}s"

def display_detection_stats():
    """Display detection statistics in sidebar"""
    if st.session_state.total_items_detected > 0:
        elapsed_time = format_time_elapsed(st.session_state.start_time)
        duration = datetime.now() - st.session_state.start_time
        minutes = max(duration.total_seconds() / 60, 0.1)  # Avoid division by zero
        
        st.sidebar.markdown("### 📊 Detection Statistics")
        st.sidebar.markdown(f"""
            * **Total Items:** {st.session_state.total_items_detected}
            * **Detection Rate:** {(st.session_state.total_items_detected / minutes):.1f}/min
            * **Session Time:** {elapsed_time}
            * **Items/Hour:** {int(st.session_state.total_items_detected * 60 / minutes)}
        """)

def save_detection_history_to_csv(file_path="detection_history.csv"):
    """Save the detection history to a CSV file."""
    file_path = Path(file_path)
    headers = ["timestamp", "item", "type"]
    
    # Open the file and write the data
    with file_path.open(mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(headers)  # Write headers
        
        for entry in st.session_state.get('detection_history', []):
            timestamp = entry['timestamp'].strftime('%Y-%m-%d %H:%M:%S')
            for item in entry['items']:
                item_type = (
                    "Recyclable" if item in RECYCLABLE else
                    "Non-Recyclable" if item in NON_RECYCLABLE else
                    "Hazardous" if item in HAZARDOUS else
                    "Unknown"
                )
                writer.writerow([timestamp, item, item_type])
    
    st.sidebar.success(f"Detection history saved to {file_path.resolve()}")

