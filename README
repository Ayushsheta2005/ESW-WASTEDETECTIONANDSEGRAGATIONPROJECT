
# **Smart Waste Segregator Model (SSM)**

### *Developed by*: *TEAM SHETA_KE_KPTAANZ* UNDER GUIDANCE OF Prof Sachin Chaudhari , SCPRC IIITH   
*Team members* - **Ayush Sheta**, **Shivam Gupta** , **Kavya Bhalodi** , **Soham Sadavarte** (CONTRIBUTION LISTED IN FINAL PPT ON HOME DIR)


## **Introduction**
The **Smart Waste Segregator Model (SSM)** is a comprehensive solution designed to address waste management challenges by automating waste detection, classification, and segregation. Leveraging advanced computer vision techniques and hardware integration, SSM classifies waste into three categories: **Recyclable**, **Non-Recyclable**, and **Hazardous**, enabling efficient waste disposal and promoting environmental sustainability.

---

## **Objectives**
- Automatically detect and classify waste using advanced deep learning algorithms and computer vision techniques.
- Efficiently segregate waste into three broad categories: **Recyclable**, **Non-Recyclable**, and **Hazardous**.
- Enhance recycling efficiency and environmental sustainability.
- Utilize scalable hardware-software integration to address real-world waste management challenges.

---

## **Solution Pipeline**

### 1. **Data Input**
Real-time waste images are captured using camera modules and fed into a deep learning model for classification.

### 2. **Image Classification**
- The **YOLOv8-based computer vision model** classifies waste into:
  - **Recyclable**: Cardboard boxes, plastic bottles, aluminum cans, etc.
  - **Non-Recyclable**: Plastic bags, snack wrappers, plastic containers, etc.
  - **Hazardous**: Batteries, light bulbs, etc.

### 3. **Waste Disposal**
The system directs waste to the appropriate bin or disposal mechanism based on its classification.

### 4. **Waste Segregation**
Segregates waste into distinct bins for further processing or disposal.

---

## **Project Timeline and Progress**
| **Task**                     | **Status**   | **Details**                                                                 |
|------------------------------|--------------|-----------------------------------------------------------------------------|
| **Data Collection**          | Completed    | 4566 images collected and annotated (1213 from IIITH campus + 3000 public datasets). |
| **Dataset Creation**         | Completed    | Annotated using Roboflow, covering 15 waste classes divided into 3 categories. |
| **Preprocessing & Augmentation** | Completed | Augmented data increased to 11289 images with horizontal-vertical flips.    |
| **Model Training**           | Completed    | Trained YOLOv8 on the dataset for real-time waste classification.           |
| **Model Testing**            | Completed    | Achieved 95% accuracy in real-world scenarios with areas for improvement.   |
| **QIDK Kit Integration**     | In Progress  | Deployed model on QIDK, but real-time rectangular boundary visualization remains challenging. |
| **Hardware Implementation**  | Upcoming     | Complete system integration for real-time deployment.                       |
| **Dataset Expansion**        | In Progress  | Adding more diverse examples to improve model robustness.                   |

---


### **Challenges Addressed**
- **Over-Augmentation**: Resolved misclassification issues from excessive augmentation.
- **Lighting Sensitivity**: Improved model robustness under variable lighting conditions.
- **Hardware Constraints**: Optimized model size for deployment on the QIDK platform.

---

## **Future Scope**
1. **Dataset Expansion**: Collecting diverse waste images to improve classification.
2. **Model Optimization**: Fine-tuning for better accuracy on challenging waste types.
3. **Hardware Implementation**: Deploying at public spaces like airports for real-life applications.
4. **Light Sensitivity Adjustments**: Enhancing model performance under varying lighting conditions.

---

## **How to Run the Code**

### **Prerequisites**
1. Install **Python 3.8+**.
2. Install the following libraries:
   - `YOLOv8`
   - `Roboflow`
   - `Streamlit`
   - `OpenCV`
3. Ensure you have the QIDK Kit ready for hardware integration.

### **Steps to Execute**
1. Clone the repository:
   ```bash
   git clone <repository-link>
   cd waste-detection
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. **Launch the Streamlit web app**:
   ```bash
   streamlit run app.py
   ```
4. **Hardware Integration (QIDK)**:
   - Follow the setup guide provided in the QIDK Kit documentation.
   - Deploy the model onto the hardware using the provided scripts.

---


---


## **Folders in the Repository**

### **1. waste_detection**
- Contains the **normal web application** for waste detection using YOLOv8.
- Provides standard waste detection and classification features.
- **Recommended for most users** due to its simplicity and low latency.

### **2. newwastedetection**
- Includes an **advanced version** of the web application with additional features:
  - **Detailed data analysis** with graphs and insights.
  - **Performance metrics visualization** for research and academic purposes.
- **High Latency**: The advanced features make this version slower.
- **Use Case**: Ideal when **complete data analysis** is required, as demonstrated in the final presentation (FinalPPT).

**Note**: Unless explicitly required for detailed analysis, it is recommended to use the `waste_detection` folder for routine operations.

---


## **Web Application Features**
- **Real-Time Detection**: Automatically draws rectangular boundaries around waste objects.
- **User Notifications**: Suggests appropriate bins for disposal based on classification.
- **Color Coding**: User-friendly bin color schemes for easy identification.
- **Graphical Analysis**: Displays performance metrics (accuracy, precision, etc.) using visual graphs.

---

## **Resources Used**
1. **Roboflow**: Image annotation and dataset management.
2. **YOLOv8 Framework**: Efficient real-time waste classification.
3. **QIDK Kit**: Hardware integration for waste sorting.
4. **Public Datasets**: Expanded training dataset with diverse waste images.

---

## **Conclusion**
The Smart Waste Segregator Model is a significant step toward addressing India’s waste crisis. With its robust waste classification capabilities and hardware-software integration, the SSM is poised to revolutionize waste management, making it efficient, scalable, and environmentally sustainable.

For further improvements, focus areas include dataset diversification, model optimization, and full hardware implementation.

--- 



Here's how you can present the **Smart Waste Segregator Model (SSM)** document with the names of all members added after the title:

---

