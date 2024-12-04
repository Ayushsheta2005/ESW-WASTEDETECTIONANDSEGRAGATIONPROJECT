from pathlib import Path
import sys

# Path configuration
file_path = Path(__file__).resolve()
root_path = file_path.parent
if root_path not in sys.path:
    sys.path.append(str(root_path))
ROOT = root_path.relative_to(Path.cwd())

# ML Model configuration
MODEL_DIR = ROOT / 'weights'
DETECTION_MODEL = MODEL_DIR / 'best.pt'

# Webcam configuration
# WEBCAM_PATH = "192.0.0.2:8080/video"  # Use 0 for default webcam
WEBCAM_PATH = 0  # Use 0 for default webcam


# Detection categories
RECYCLABLE = [
    'cardboard_box',
    'can',
    'plastic_bottle',
    'scrap_paper',
    'cardboard_bowl',
    'glass_bottle',
    'newspaper',
    'aluminum_can'
]

NON_RECYCLABLE = [
    'plastic_bag',
    'plastic_cup',
    'snack_bag',
    'plastic_box',
    'straw',
    'plastic_cup_lid',
    'plastic_spoon',
    'plastic_bottle_cap',
    'styrofoam_container',
    'candy_wrapper'
]

HAZARDOUS = [
    'battery',
    'light_bulb',
    'paint_can',
    'electronic_waste',
    'chemical_container',
    'aerosol_can'
]

# Detection Settings
MIN_CONFIDENCE = 0.4
DEFAULT_CONFIDENCE = 0.6
MAX_CONFIDENCE = 0.9

# Display Settings
DISPLAY_WIDTH = 640
DISPLAY_HEIGHT = 480



# N stick
# H battery
# H chemical_spray_can
# N plastic_box
# R plastic_bottle
# H chemical_plastic_bottle
# N cardboard_bowl
# N straw
# R plastic_bottle_cap
# N plastic_cup
# N scrap_plastic
# N plastic_bag
# N scrap_paper
# R can
# N snack_bag
# H light_bulb
# N plastic_spoon
# H chemical_plastic_gallon
# N plastic_cup_lid
# H paint_bucket
# R cardboard_box

# R cardboard_box
# R can
# N plastic_bag
# N scrap_paper
# N stick
# N plastic_cup
# N snack_bag
# R plastic_bottle_cap
# N plastic_box
# H battery
# N straw
# H chemical_spray_can
# N plastic_cup_lid
# R plastic_bottle
# R reuseable_paper
# N scrap_plastic
# H chemical_plastic_bottle
# H chemical_plastic_gallon
# N cardboard_bowl
# H light_bulb
# N plastic_cultery
# H paint_bucket
# types of waste