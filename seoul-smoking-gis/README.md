# 🚬 Seoul Smoking Zone GIS

> *"Where are the legal smoking zones in Seoul — and how are they distributed?"*

This project visualizes **legally designated outdoor smoking areas** in Seoul, starting with **Yongsan-gu**.  
Using publicly available data and coordinate mapping, we generate an interactive map and analyze spatial patterns to support urban planning and public health awareness.

---

## 🎯 Project Objectives

- Collect public data on smoking zones from Seoul city
- Convert address-based data to geographic coordinates
- Visualize the spatial distribution on an interactive map
- Compute distances between zones for further analysis
- Lay groundwork for future zone recommendation or coverage assessment

---

## 📍 Current Scope

This version focuses on **Yongsan-gu** (용산구) only.  
Other districts (구) may be added in future updates for city-wide analysis.

---

## 🌐 Data Sources

- [서울 열린데이터 광장 (Seoul Open Data Portal)](https://data.seoul.go.kr)
- [공공데이터 포털 (data.go.kr)](https://www.data.go.kr)
- [Nominatim Geocoder (OpenStreetMap)](https://nominatim.org)

---

## 🔧 Tech Stack

- `pandas`: data wrangling  
- `folium`: interactive mapping (leaflet.js)  
- `geopy`: address-to-coordinate geocoding  
- `Jupyter Notebook`: analysis & visualization interface  
- `webbrowser`: automatic browser launch of saved maps

---

## 🧱 Folder Structure

```bash
seoul-smoking-gis/
├── Data/                        # Raw and processed datasets (e.g., Yongsan CSV)
├── Output/                      # Generated HTML maps
├── Yongsan-gu Smoking Zone Mapping.ipynb  # Main notebook
└── README.md

## 🚀 How to Run

1. **Install dependencies**  
   Make sure the following Python packages are installed:
   - pandas  
   - folium  
   - geopy  

   Example command:  
   pip install pandas folium geopy

2. **Open the notebook**  
   Launch Jupyter Notebook or VS Code and open:  
   `Yongsan-gu Smoking Zone Mapping.ipynb`

3. **Run all cells**  
   The notebook will:
   - 📂 Load the public smoking zone dataset from the `Data/` folder  
   - 🌐 Perform geocoding if latitude/longitude is missing  
   - 🗺️ Generate an interactive map using Folium  
   - 💾 Save the map to `Output/yongsan_smoking_zones_map.html`  
   - 🌍 Automatically open the map in your default web browser
