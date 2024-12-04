from ultralytics import YOLO
import time
import streamlit as st
import cv2
from helper import (
    initialize_session_state,
    update_detection_history,
    display_detection_stats,
    format_time_elapsed,
    save_detection_history_to_csv
)
import settings
import threading
from datetime import datetime

# Configure Streamlit page
st.set_page_config(
    page_title="Waste Detection App",
    page_icon="♻️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
    <style>
    .stRecyclable {
        background-color: rgba(46, 204, 113, 0.2);
        padding: 15px;
        border-radius: 5px;
        border-left: 5px solid #2ecc71;
        margin: 10px 0;
    }
    .stNonRecyclable {
        background-color: rgba(231, 76, 60, 0.2);
        padding: 15px;
        border-radius: 5px;
        border-left: 5px solid #e74c3c;
        margin: 10px 0;
    }
    .stHazardous {
        background-color: rgba(241, 196, 15, 0.2);
        padding: 15px;
        border-radius: 5px;
        border-left: 5px solid #f1c40f;
        margin: 10px 0;
    }
    .detection-stats {
        font-size: 24px;
        font-weight: bold;
        margin: 10px 0;
    }
    .stButton button {
        width: 100%;
        margin: 5px 0;
    }
    .css-1d391kg {
        padding-top: 3rem;
    }
    </style>
    """, unsafe_allow_html=True)

def sleep_and_clear_success():
    """Clear detection messages after a delay"""
    time.sleep(3)
    st.session_state['recyclable_placeholder'].empty()
    st.session_state['non_recyclable_placeholder'].empty()
    st.session_state['hazardous_placeholder'].empty()

def load_model(model_path):
    """Load YOLO model with custom configuration"""
    try:
        model = YOLO(model_path)
        return model
    except Exception as e:
        st.error(f"Error loading model: {str(e)}")
        return None

def classify_waste_type(detected_items):
    """
    Classify detected items into waste categories
    Returns sets of recyclable, non-recyclable, and hazardous items
    """
    recyclable_items = set(detected_items) & set(settings.RECYCLABLE)
    non_recyclable_items = set(detected_items) & set(settings.NON_RECYCLABLE)
    hazardous_items = set(detected_items) & set(settings.HAZARDOUS)
    return recyclable_items, non_recyclable_items, hazardous_items

def remove_dash_from_class_name(class_name):
    """Format class names for display"""
    return class_name.replace("_", " ").title()

def _display_detected_frames(model, st_frame, image):
    """Process and display detected frames with object detection"""
    # Resize image to maintain aspect ratio
    image = cv2.resize(image, (640, int(640*(9/16))))
    
    # Initialize session state variables if not exists
    if 'unique_classes' not in st.session_state:
        st.session_state['unique_classes'] = set()
    if 'recyclable_placeholder' not in st.session_state:
        st.session_state['recyclable_placeholder'] = st.sidebar.empty()
    if 'non_recyclable_placeholder' not in st.session_state:
        st.session_state['non_recyclable_placeholder'] = st.sidebar.empty()
    if 'hazardous_placeholder' not in st.session_state:
        st.session_state['hazardous_placeholder'] = st.sidebar.empty()

    # Get confidence threshold from session state
    confidence_threshold = st.session_state.get('confidence_threshold', 0.6)
    
    # Perform detection
    res = model.predict(image, conf=confidence_threshold)
    names = model.names
    detected_items = set()

    for result in res:
        new_classes = set([names[int(c)] for c in result.boxes.cls])
        if new_classes != st.session_state['unique_classes']:
            st.session_state['unique_classes'] = new_classes
            detected_items.update(st.session_state['unique_classes'])
            
            # Classify detected items
            recyclable_items, non_recyclable_items, hazardous_items = classify_waste_type(detected_items)
            
            # Update detection history
            update_detection_history(detected_items)
            
            # Display detected items with icons
            if recyclable_items:
                items_str = "\n- ".join(remove_dash_from_class_name(item) for item in recyclable_items)
                st.session_state['recyclable_placeholder'].markdown(
                    f"<div class='stRecyclable'>♻️ Recyclable Items:\n\n- {items_str}</div>",
                    unsafe_allow_html=True
                )
            
            if non_recyclable_items:
                items_str = "\n- ".join(remove_dash_from_class_name(item) for item in non_recyclable_items)
                st.session_state['non_recyclable_placeholder'].markdown(
                    f"<div class='stNonRecyclable'>🚫 Non-Recyclable Items:\n\n- {items_str}</div>",
                    unsafe_allow_html=True
                )
            
            if hazardous_items:
                items_str = "\n- ".join(remove_dash_from_class_name(item) for item in hazardous_items)
                st.session_state['hazardous_placeholder'].markdown(
                    f"<div class='stHazardous'>⚠️ Hazardous Items:\n\n- {items_str}</div>",
                    unsafe_allow_html=True
                )
            
            # Display real-time metrics
            col1, col2, col3 = st.sidebar.columns(3)
            col1.metric("♻️", len(recyclable_items))
            col2.metric("🚫", len(non_recyclable_items))
            col3.metric("⚠️", len(hazardous_items))
            
            # Clear detection messages after delay
            threading.Thread(target=sleep_and_clear_success).start()

    # Display the frame with detections
    res_plotted = res[0].plot()
    st_frame.image(res_plotted, channels="BGR", use_column_width=True)

def play_webcam(model):
    """Main function to handle webcam feed and detection"""
    initialize_session_state()
    
    # Sidebar settings
    st.sidebar.markdown("### 🎯 Detection Settings")
    confidence_threshold = st.sidebar.slider(
        "Detection Confidence",
        min_value=0.0,
        max_value=1.0,
        value=0.6,
        step=0.05,
        help="Adjust the confidence threshold for object detection"
    )
    st.session_state.confidence_threshold = confidence_threshold
    
    if st.sidebar.button("📁 Export Detection History to CSV"):
        save_detection_history_to_csv()

    
    # Camera controls
    col1, col2 = st.columns([3, 1])
    with col1:
        start_button = st.button('▶️ Start Detection', key='start_detection', use_container_width=True)
    with col2:
        stop_button = st.button('⏹️ Stop', key='stop_detection', use_container_width=True)
    
    if start_button:
        st.session_state.detection_active = True
    if stop_button:
        st.session_state.detection_active = False
        return
    

    

    
    if st.session_state.get('detection_active', False):
        try:
            vid_cap = cv2.VideoCapture(settings.WEBCAM_PATH)
            st_frame = st.empty()
            
            while vid_cap.isOpened() and st.session_state.detection_active:
                success, image = vid_cap.read()
                if success:
                    _display_detected_frames(model, st_frame, image)
                    display_detection_stats()
                else:
                    vid_cap.release()
                    st.error("Failed to read from webcam")
                    break
            
            vid_cap.release()
            
        except Exception as e:
            st.sidebar.error(f"Error accessing webcam: {str(e)}")

if __name__ == "__main__":
    st.title("♻️ Smart Waste Detection System")
    st.markdown("""
    This application helps identify and classify different types of waste materials in real-time using your webcam.
    Position items in front of the camera and the system will automatically categorize them as recyclable, 
    non-recyclable, or hazardous materials.
    """)
    
    # Load model
    model = load_model(settings.DETECTION_MODEL)
    if model:
        play_webcam(model)

