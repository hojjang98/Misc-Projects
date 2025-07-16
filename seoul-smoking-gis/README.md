# 🚬 Seoul Smoking Zone GIS

> *"Where are the legal smoking zones in Seoul — and how are they distributed?"*

This project explores the geographic distribution of **legally designated smoking areas** across Seoul, South Korea.  
Using publicly available data and geocoding APIs, we visualize smoking zones on an interactive map and examine spatial patterns at the district level.

---

## 🎯 Project Goal

- Collect and clean open data related to legal smoking zones in Seoul  
- Convert location data into geographic coordinates (lat/lon)  
- Visualize the distribution of smoking zones using GIS tools  
- Provide an intuitive, map-based overview for public insight and policy support  

---

## 🌐 Data Sources

- **서울 열린데이터 광장**  
  Public datasets published by the Seoul Metropolitan Government  
  (e.g., smoking booths, outdoor public smoking zones)

- **공공데이터 포털**  
  National open data platform (data.go.kr) for smoking-related spatial datasets

- **Geocoding APIs**  
  For converting address-based location info into latitude/longitude coordinates  
  (e.g., Kakao, Naver, or Google Geocoding APIs)

---

## 🔧 Techniques Used

- `Pandas` for data wrangling  
- `Folium` for interactive mapping  
- `Open API` integration for address-to-coordinate conversion  
- `Jupyter Notebook` for development and exploration

---

## 🧱 Project Structure

```bash
seoul-smoking-gis/
├── data/               # Raw and processed datasets
├── notebooks/          # Mapping and analysis notebooks
├── src/                # Scripts (e.g., geocoding)
├── results/            # HTML maps, charts, visual summaries
└── README.md
