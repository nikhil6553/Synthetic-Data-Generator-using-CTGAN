# Synthetic Data Generator using CTGAN

A Streamlit-based web application for generating privacy-preserving synthetic tabular data using the CTGAN (Conditional Tabular GAN) model.

This project demonstrates how Generative Adversarial Networks (GANs) can be used to generate realistic synthetic datasets while preserving statistical properties and protecting sensitive information. The application is designed for healthcare, finance, IoT security, predictive maintenance, and other privacy-sensitive domains.

---

# Features

- Generate synthetic tabular data using a pretrained CTGAN model
- Interactive Streamlit web interface
- Upload trained `.pkl` CTGAN model
- Generate customizable number of synthetic samples
- Real-time dataset preview
- Statistical summary of generated data
- Interactive visualizations
- Download generated data as:
  - CSV
  - Excel
- Supports mixed tabular data types

---

# Technologies Used

- Python
- Streamlit
- CTGAN
- Pandas
- NumPy
- OpenPyXL
- Pickle

---

# Project Structure

```text
project/
│
├── app.py
├── ctgan_model.pkl
├── requirements.txt
└── README.md
```

---

# Installation

## Clone Repository

```bash
git clone <your-repository-url>
cd <repository-folder>
```

---

# Install Dependencies

```bash
pip install -r requirements.txt
```

Or manually install:

```bash
pip install streamlit pandas numpy ctgan openpyxl
```

---

# Train CTGAN Model

Example training code:

```python
from ctgan import CTGAN
import pandas as pd
import pickle

# Load dataset
data = pd.read_csv("dataset.csv")

# Train model
model = CTGAN(epochs=100)
model.fit(data)

# Save model
with open("ctgan_model.pkl", "wb") as f:
    pickle.dump(model, f)
```

---

# Run the Application

```bash
streamlit run app.py
```

The application will start locally at:

```text
http://localhost:8501
```

---

# How to Use

1. Run the Streamlit app
2. Upload trained CTGAN `.pkl` model
3. Select number of synthetic samples
4. Click:
   Generate Synthetic Data
5. View generated synthetic dataset
6. Download generated data

---

# Synthetic Data Generation Workflow

```text
Original Dataset
        ↓
Data Preprocessing
        ↓
CTGAN Model Training
        ↓
Model Serialization (.pkl)
        ↓
Streamlit Deployment
        ↓
Synthetic Data Generation
```

---

# Applications

This project can be used in:

- Healthcare synthetic patient records
- Financial transaction simulation
- Fraud detection research
- IoT intrusion detection systems
- Predictive maintenance
- Cybersecurity research
- Machine learning model training
- Privacy-preserving data sharing

---

# Privacy Preservation

The project focuses on privacy-preserving synthetic data generation:

- Protects sensitive information
- Reduces risk of direct data leakage
- Maintains statistical similarity with real datasets
- Useful for GDPR and privacy-compliant research

---

# CTGAN Overview

CTGAN (Conditional Tabular GAN) is a GAN-based model specifically designed for tabular data generation.

Key capabilities:

- Handles mixed numerical and categorical data
- Preserves feature relationships
- Handles imbalanced categorical distributions
- Produces realistic synthetic records

---

# Evaluation Metrics

Synthetic data quality can be evaluated using:

- Statistical Similarity
- Wasserstein Distance
- Jensen-Shannon Divergence
- Machine Learning Utility
- Privacy Risk Assessment
- Detection Score

---

# Future Enhancements

- Upload custom datasets dynamically
- Train CTGAN inside Streamlit app
- Real vs Synthetic comparison dashboard
- Privacy risk analysis
- Differential Privacy integration
- Multiple GAN model support
- Docker deployment
- Cloud deployment

---

# References

- Ian Goodfellow, “Generative Adversarial Nets”, NeurIPS 2014
- Lei Xu, “Modeling Tabular Data using Conditional GAN”, NeurIPS 2019
- Cynthia Dwork, “Differential Privacy”, ICALP 2006

CTGAN Documentation:
https://docs.sdv.dev/sdv/single-table-data/modeling/synthesizers/ctgansynthesizer

Streamlit:
https://streamlit.io/

---

# Developed By

Nikhil Kumar Singh  
B.Tech Computer Science & Engineering  
Amity University Uttar Pradesh

---

# License

This project is developed for academic and research purposes.
