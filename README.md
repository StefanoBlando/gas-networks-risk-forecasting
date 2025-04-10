# Gas Network Risk Forecasting

This project was developed during the **Hera Group Data Hackathon** and focuses on predicting gas leak risks across pipeline segments using real-world geospatial and operational data. The aim is to support predictive maintenance strategies and improve infrastructure safety.

## 🚀 Project Goals

- Integrate geospatial, temporal, and operational features from gas distribution networks  
- Predict monthly leak occurrences at the subsystem (CODSISTEMA) level  
- Provide a binary classifier (leak/no-leak) and a regression model (expected leak count)  
- Generate synthetic data to enhance training via CTGAN and TimeGAN

## 📦 Dataset Overview

Data was provided by Hera Group for hackathon use only and includes:  
- **Pipeline characteristics**: geometry, materials, diameter, installation year  
- **Leak events**: timestamped gas leak reports linked to segments (IDSAP)  
- **Risk levels**: monthly risk score (0-100) per segment from predictive models  

> **Note**: Due to licensing restrictions, raw data files are not shared in this repository.

# Gas Network Risk Forecasting

This project was developed during the **Hera Group Data Hackathon** and focuses on predicting gas leak risks across pipeline segments using real-world geospatial and operational data. The goal is to support predictive maintenance strategies and improve infrastructure safety.

---

## 🚀 Project Goals

- Integrate geospatial, temporal, and operational features from gas distribution networks  
- Predict monthly leak occurrences at the subsystem (CODSISTEMA) level  
- Provide both a binary classifier (leak/no-leak) and a regression model (expected leak count)  
- Generate synthetic data to enhance training via **CTGAN** and **TimeGAN**

---

## 📦 Dataset Overview

The dataset (not included) was provided by Hera Group for hackathon purposes and includes:

- **Pipeline characteristics**: geometry, materials, diameter, installation year  
- **Leak events**: timestamped gas leak reports linked to segments (`IDSAP`)  
- **Risk levels**: monthly risk score (0–100) per segment, from predictive models  

> ⚠️ **Note**: Raw data files are proprietary and not included in this repository.

---

## 🧰 Repository Structure

```bash
gas-network-risk-forecasting/
├── README.md
├── requirements.txt
├── .gitignore
│
├── notebooks/
│   ├── 01_data_preprocessing.ipynb
│   ├── 02_feature_engineering.ipynb
│   ├── 03_model_training.ipynb
│   └── 04_synthetic_data_generation.ipynb
│
├── src/
│   ├── data_loading.py
│   ├── preprocessing.py
│   ├── feature_engineering.py
│   ├── modeling.py
│   └── synthetic.py
│
├── data/
│   └── raw/              # Place original parquet files here (not included)
│
└── outputs/
    └── predictions/      # Model outputs and visualizations

    

## ⚙️ Technologies & Models

- **Languages**: Python (pandas, scikit-learn, LightGBM, geopandas)  
- **Modeling**: Binary classification + regression (zero-inflated pipeline)  
- **Generative**: CTGAN and TimeGAN for synthetic data  
- **Visualization**: seaborn, matplotlib, plotly

## 🧪 How to Use

1. Clone this repo:  
```bash
git clone https://github.com/your-username/gas-network-risk-forecasting.git
cd gas-network-risk-forecasting
```

2. Install dependencies:  
```bash
pip install -r requirements.txt
```

3. Place the raw data files in `data/raw/`  

4. Run notebooks or modular scripts in the `src/` folder

## 🔐 Data Access

This project uses proprietary datasets provided by Hera Group for hackathon purposes only.  
To reproduce results, please request access from the organizers or use analogous public datasets.

## 🧭 Future Work

- Improving explainability (XAI) and causality estimation  
- Testing models on new years or broader regions  
- Incorporating weather and pressure sensors data

## 📩 Contact

For more information or collaboration, feel free to reach out via [GitHub](https://github.com/your-username).
