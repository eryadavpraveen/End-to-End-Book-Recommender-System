# 📚 End-to-End Book Recommendation System (ML Pipeline)

This project is a **production-style, end-to-end Book Recommendation System** built using a **modular Machine Learning pipeline architecture**.  
It implements **collaborative filtering** using **K-Nearest Neighbors (KNN)** and is deployed using **Streamlit** for real-time recommendations.

The project follows **ML engineering best practices**, including configuration-driven design, logging, exception handling, and clear pipeline separation.

---

## 🚀 Project Highlights

- ✅ End-to-end ML pipeline (Ingestion → Validation → Transformation → Training)
- ✅ Collaborative Filtering using KNN
- ✅ YAML-based configuration (no hard-coded paths)
- ✅ Centralized logging & custom exception handling
- ✅ Reusable, modular, and scalable architecture
- ✅ Streamlit-based interactive UI
- ✅ Resume & interview-ready project structure

---

## 🧠 Problem Statement

Given user–book interaction data (ratings), recommend **similar books** to a user based on collaborative filtering.

---

## 🏗️ Project Architecture

User (Streamlit UI)<br>
↓<br>
Recommendation Engine<br>
↓<br>
Trained KNN Model<br>
↓<br>
Book Similarity (User–Item Matrix)<br>
<br>

---

## 📂 Project Folder Structure

books_recommender/<br>
│<br>
├── components/<br>
│ ├── stage_00_data_ingestion.py<br>
│ ├── stage_01_data_validation.py<br>
│ ├── stage_02_data_transformation.py<br>
│ └── stage_03_model_trainer.py<br>
│<br>
├── pipeline/<br>
│ └── training_pipeline.py<br>
│<br>
├── config/<br>
│ ├── config.yaml<br>
│ └── configuration.py<br>
│<br>
├── entity/<br>
│ └── config_entity.py<br>
│<br>
├── utils/<br>
│ └── util.py<br>
│<br>
├── logger/<br>
│ └── log.py<br>
│<br>
├── exception/<br>
│ └── exception_handler.py<br>
│<br>
├── artifacts/ # Auto-generated during training<br>
│<br>
├── app.py # Streamlit application<br>
├── setup.py<br>
└── README.md<br>
<br>

---

## 🔄 ML Pipeline Stages

### 1️⃣ Data Ingestion
- Downloads dataset from URL
- Extracts ZIP file
- Stores raw and ingested data

### 2️⃣ Data Validation
- Cleans and preprocesses data
- Filters:
  - Users with more than 200 ratings
  - Books with at least 50 ratings
- Saves cleaned data and serialized objects

### 3️⃣ Data Transformation
- Converts cleaned data into a **user–item pivot table**
- Handles missing values
- Saves transformed data for training and inference

### 4️⃣ Model Training
- Uses **K-Nearest Neighbors (KNN)**
- Trains on sparse user–item matrix
- Saves trained model as a serialized object

---

## 🤖 Recommendation Technique

**Collaborative Filtering (Item-Based)**

- Builds similarity between books using user ratings
- Uses `NearestNeighbors` from `scikit-learn`
- Recommends top-N similar books

---

## 🧪 Tech Stack

- **Python**
- **Pandas, NumPy**
- **Scikit-learn**
- **Streamlit**
- **YAML**
- **Pickle**
- **Logging**

---

## ⚙️ Configuration Management

All configurations are controlled via `config/config.yaml`, including:
- Dataset URL
- Artifact directories
- Model name
- Serialized object paths

This allows:
- Easy environment changes
- No code modification for path updates

---

## 🧾 Logging & Exception Handling

- Timestamped log files generated automatically
- Custom exception class reports:
  - File name
  - Line number
  - Error message

This makes debugging **production-friendly**.

---

## ▶️ How to Run the Project

Follow the steps below to set up and run the Book Recommender System.

---

### 1️⃣ Install Dependencies

Install all required Python packages using `requirements.txt`:

```bash
pip install -r requirements.txt

---

bash scripts/run_app.sh

