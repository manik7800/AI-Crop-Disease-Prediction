# 🌿 AI Crop Disease Prediction System

An AI-powered Crop Disease Prediction System built using **TensorFlow, EfficientNetB0, Streamlit, and SQLite**. The application predicts diseases from crop leaf images and provides disease information, treatment recommendations, prevention tips, prediction history, and downloadable PDF reports.

---

## Features

-  Predict crop diseases from leaf images
-  Upload image or capture using camera
-  EfficientNetB0 Deep Learning Model
-  Confidence Score
-  Disease Symptoms
-  Treatment Recommendations
-  Prevention Tips
-  Download PDF Report
-  Prediction History (SQLite Database)
-  Dashboard with Charts
-  Export Prediction History as CSV

---

## Tech Stack

- Python
- Streamlit
- TensorFlow / Keras
- EfficientNetB0
- SQLite
- Pandas
- Plotly
- ReportLab

---

##  Dataset

**PlantVillage Dataset**

- Total Images: **20,638**
- Classes: **15**
- Crops:
  - 🍅 Tomato
  - 🥔 Potato
  - 🫑 Bell Pepper

---

##  Model Information

| Model | EfficientNetB0 |
|--------|----------------|
| Input Size | 224 × 224 |
| Epochs | 20 |
| Training Accuracy | 97.43% |
| Validation Accuracy | **97.75%** |

---

##  Project Structure

```text
Crop_Disease_Prediction/
│
├── app.py
├── train.py
├── predict.py
├── database/
├── models/
├── utils/
├── images/
├── dataset/
├── requirements.txt
└── README.md
```

---

##  Installation

### Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/AI-Crop-Disease-Prediction.git
```

### Open Project

```bash
cd AI-Crop-Disease-Prediction
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
streamlit run app.py
```

---

##  Application Features

- Disease Detection
- Confidence Score
- Disease Information
- Symptoms
- Treatment
- Prevention
- Prediction History
- Dashboard
- PDF Report Generation
- CSV Export

---

##  Supported Diseases

### 🍅 Tomato

- Healthy
- Bacterial Spot
- Early Blight
- Late Blight
- Leaf Mold
- Septoria Leaf Spot
- Spider Mites
- Target Spot
- Tomato Mosaic Virus
- Tomato Yellow Leaf Curl Virus

### 🥔 Potato

- Healthy
- Early Blight
- Late Blight

### 🫑 Bell Pepper

- Healthy
- Bacterial Spot

---

##  Future Improvements

- Real-world dataset support (PlantDoc)
- Mobile-friendly interface
- Multi-language support
- Fertilizer recommendation
- Weather-based disease alerts
- Cloud deployment

---

##  Author

**Manik Chand**

B.Tech CSE (Artificial Intelligence)

Aspiring Data Analyst & AI Developer

 Email: chandmanik819@gmail.com

🔗 LinkedIn:
https://www.linkedin.com/in/manik-chand-56271a286

---

##  If you like this project

Please ⭐ Star this repository and share it with others.