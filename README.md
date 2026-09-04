# Temuco PM₂.₅ Pipeline Prototype

Minimal reproducible notebook used to test an open research workflow:

**Jupyter → GitHub → Streamlit → Zenodo**

The notebook estimates the main treatment-group effects on indoor PM₂.₅ for residential heating and insulation scenarios in Temuco, Chile.

## Main comparison

Reference group:

- Firewood – No Insulation

Treatment groups:

- Pellet only
- Insulation only
- Pellet + Insulation

The notebook performs:

1. Data loading and minimal preprocessing
2. Stabilized multinomial generalized propensity-score (GPS) weighting
3. Main GPS-weighted PM₂.₅ regression
4. Extraction of treatment-group effects
5. One summary plot with 95% confidence intervals

## Files

- `Temuco_Main_PM25_Pipeline_Prototype.ipynb` — main analysis notebook
- `requirements.txt` — Python dependencies

## Data

The notebook expects the file:

`Panel_03112025.xlsx`

For this pipeline test, the dataset is **not included in the public repository**.

To run the notebook locally, place the Excel file in the same folder as the notebook or update the file path in the setup cell.

## Run locally

Create a Python environment and install the dependencies:

```bash
pip install -r requirements.txt
```

Then open the notebook with Jupyter:

```bash
jupyter notebook Temuco_Main_PM25_Pipeline_Prototype.ipynb
```

## Purpose

This repository is a small prototype for building a public and reproducible research output. The next step is to reuse the same scientific logic in a lightweight interactive Streamlit application.
