# AgriAI: Edge-Enabled Precision Agriculture & Plant Health Rover

An end-to-end precision agriculture architecture combining tabular environmental machine learning with autonomous edge computer vision to optimize crop yield and prevent pathogen outbreaks.

## System Architecture

1. **Pre-Cultivation (Soil & Climate Intelligence):**
   - Multi-class classification trained on 2,200 agricultural records across 7 environmental features (N, P, K, pH, rainfall, temperature, humidity).
   - Evaluated Decision Tree baseline against Random Forest Classifier (achieved >99% validation accuracy).
   - Confidence probability distribution for top candidate crops.

2. **Post-Cultivation (Rover Vision & Spot Actuation):**
   - Optical leaf pathology detection to identify fungal/bacterial blight at the single-plant stage.
   - Micro-sprayer actuation logic: isolates diseased foliage and dispenses targeted fungicide via solenoid valve for 750ms bursts, eliminating broadcast pesticide runoff.

## Tech Stack
- **Machine Learning:** Scikit-Learn, Pandas, NumPy, Joblib
- **Interface / Telemetry:** Streamlit
- **Edge Deployment Logic:** Microcontroller telemetry simulation (ESP32/Solenoid)

## Getting Started
\`\`\`bash
git clone <your-repo-link>
cd AgriProject
python -m venv venv
source venv/bin/activate  # Or .\venv\Scripts\Activate on Windows
pip install -r requirements.txt
python train.py
streamlit run app.py
\`\`\`