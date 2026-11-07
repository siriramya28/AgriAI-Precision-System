# 🌾 AgriAI: Precision Crop Selection & Autonomous Edge Sprayer

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://agriai-precision-system.streamlit.app)
[![GitHub Repo](https://img.shields.io/badge/GitHub-Repository-181717?logo=github)](https://github.com/siriramya28/AgriAI-Precision-System)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

An end-to-end precision agriculture platform combining tabular environmental machine learning with an autonomous edge-actuated robotic spot-sprayer simulation to prevent chemical runoff and optimize agricultural yield.

---

## 📌 Problem Statement
Traditional agricultural management relies heavily on uniform broadcast chemical spraying and trial-and-error crop selection. This causes severe chemical runoff, degrades soil biodiversity, and incurs high operational costs. **AgriAI** addresses both the pre-sowing and post-cultivation cycles through targeted artificial intelligence.

---

## ⚙️ System Architecture

### 1. Pre-Cultivation: Soil & Climate Crop Recommendation
* **Dataset:** 2,200 multi-parameter agricultural field records.
* **Input Features (7):** Nitrogen ($N$), Phosphorus ($P$), Potassium ($K$), Temperature, Humidity, Soil pH, and Rainfall.
* **Algorithms Evaluated:** Baseline Decision Tree vs. 100-estimator **Random Forest Classifier**.
* **Performance:** Achieved **~99% validation accuracy** with multi-class probability confidence scores across 22 distinct crop categories.

### 2. Post-Cultivation: Autonomous Rover & Micro-Spraying
* Simulates an edge rover optical sensor feed scanning plant foliage in real time.
* Isolates foliar fungal/bacterial pathogens (e.g., *Alternaria solani* / Early Blight).
* Triggers localized solenoid valve micro-spraying in controlled **750ms bursts**, conserving ~90% active chemical suspension relative to conventional uniform broadcast treatments.

---

## 🛠️ Tech Stack

* **Language:** Python
* **Machine Learning:** Scikit-Learn, Pandas, NumPy, Joblib
* **Web Interface & Telemetry:** Streamlit
* **Image Processing:** Pillow (PIL)
* **Deployment:** Streamlit Community Cloud

---

## 🚀 Local Installation & Setup

1. **Clone the repository:**
   ```bash
git clone [https://github.com/siriramya28/AgriAI-Precision-System.git](https://github.com/siriramya28/AgriAI-Precision-System.git)
cd AgriAI-Precision-System