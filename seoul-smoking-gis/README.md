# 🚬 Seoul Smoking Zone GIS

> *"Where are the legal smoking zones in Seoul — and how are they distributed?"*

This project visualizes **legally designated outdoor smoking areas** in Seoul, currently focusing on **Yongsan-gu** and **Yeongdeungpo-gu**.  
Using publicly available data and coordinate mapping, we generate an interactive map and analyze spatial patterns to support urban planning and public health awareness.

---

## 🎯 Project Objectives
- Collect public data on smoking zones from Seoul city  
- Convert address-based data to geographic coordinates (geocoding)  
- Visualize the spatial distribution on an interactive map  
- Compute distances between zones to analyze spatial coverage  
- Lay groundwork for future features like zone recommendation or coverage gap detection  

---

## 📍 Current Scope
This version covers **two districts only**:
- **Yongsan-gu** (용산구)  
- **Yeongdeungpo-gu** (영등포구)

> ⚠️ The original goal was to map smoking zones across **all 25 districts of Seoul**.  
> However, during data collection we discovered that:
> - Many districts provided **no public data at all**  
> - Some datasets were **incomplete or unstructured** (e.g., vague descriptions like "station front")  
> - Several sources were **not machine-readable or not suitable for geocoding**  
>  
> Because of these limitations, only districts with **sufficient and clean address data** were included in this version.  
> As a result, the analysis is currently **limited to two districts**, and the results cannot be generalized to all of Seoul.

---

## 🌐 Data Sources
- [서울 열린데이터 광장 (Seoul Open Data Portal)](https://data.seoul.go.kr)  
- [공공데이터 포털 (data.go.kr)](https://www.data.go.kr)  
- [Nominatim Geocoder (OpenStreetMap)](https://nominatim.org)  

---

## 🔧 Tech Stack
- `pandas`: data wrangling  
- `folium`: interactive mapping (Leaflet.js)  
- `geopy`: address-to-coordinate geocoding  
- `Jupyter Notebook`: analysis & visualization interface  
- `webbrowser`: automatic browser launch of saved maps  

---

## 🧱 Folder Structure
```bash

seoul-smoking-gis/
├── Data/                        # Raw and processed datasets (e.g., Yongsan CSV)
├── Output/                      # Generated HTML maps
├── notebooks/
│   └── Seoul_SmokingZones_Yongsan_Yeongdeungpo.ipynb
├── requirements.txt
├── .gitignore
└── README.md

```

## 🚀 How to Run
```bash

1. **Install dependencies**  
   Make sure the required Python packages are installed:
   
   pip install pandas folium geopy
2. Open the notebook
   Navigate to the notebooks/ directory and open:
   notebooks/Seoul_SmokingZones_Yongsan_Yeongdeungpo.ipynb
3. Run all cells
   The notebook will:
   📂 Load the smoking zone dataset from the Data/ folder
   🌐 Perform geocoding if latitude/longitude is missing
   🗺️ Generate an interactive map with Folium
   💾 Save the map to Output/ (e.g., yongsan_smoking_zones_map.html)
   🌍 Automatically open the map in your default web browser

```

