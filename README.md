
# 🏢 Smart Building Digital Twin – Real-Time Environmental Monitoring System

This project implements a **Digital Twin** for a Smart Building using real-time simulated sensor data (temperature, humidity, luminosity, and presence detection). It leverages **FastAPI**, **Grafana**, and **Streamlit** to monitor and visualize indoor environmental quality.

---

## 🔍 What is a Digital Twin?

A **Digital Twin** is a digital replica of a physical system. In this project, the twin simulates the internal environment of a building by continuously generating and visualizing data from virtual sensors. It allows for:

- Real-time monitoring of building conditions  
- Visualization of sensor trends  
- Improved energy and space management  

---

## 🧠 Use Case – Smart Building Monitoring

In real-world smart buildings, digital twins are used to:

- Optimize heating/cooling systems based on occupancy and temperature  
- Monitor air quality and lighting conditions  
- Detect anomalies (e.g., unusual temperature spikes or occupancy changes)  
- Provide dashboards to facility managers for decision-making  

---

## 🏗️ System Architecture

The system consists of three key components:

| Component     | Technology | Role                                |
|---------------|------------|-------------------------------------|
| Data Generator| FastAPI    | Simulates sensor data via API       |
| Dashboard     | Streamlit  | Visualizes data in real-time        |
| Monitoring    | Grafana    | Live dashboard with historical view |

```
       +------------------------+
       |  FastAPI Data Server   |
       | (Simulated Sensor API)|
       +-----------+------------+
                   |
         HTTP GET /data (JSON)
                   |
        +----------v-----------+
        |    Streamlit App     |
        |  (Live Visualization)|
        +----------------------+
                   |
        +----------v-----------+
        |      Grafana         |
        |  (Time-Series Dash)  |
        +----------------------+
```

---

## ⚙️ How It Works

### 1️⃣ FastAPI – Data Generator

Simulates and exposes sensor data via `/data` endpoint.

```json
{
  "temperature": 22.8,
  "humidity": 45.2,
  "luminosity": 360,
  "presence": true,
  "timestamp": "2025-05-20T14:30:25"
}
```

### 2️⃣ Streamlit Dashboard

Visualizes the data from the API in real-time using interactive charts and metrics.

### 3️⃣ Grafana Dashboard

- Uses `smart_building_dashboard.json`
- Displays time-series data (temperature, humidity, etc.)
- Customizable dashboards

---

## 🚀 Getting Started

### 📦 Clone the Repository

```bash
git clone https://github.com/Manel-Ben-Hassen/SmartBuilding_DigitalTwin.git
cd SmartBuilding_DigitalTwin
```

### 🐳 Run with Docker Compose

```bash
docker-compose up --build -d
```

### 🔎 Access the Services

| Service     | URL                        |
|-------------|----------------------------|
| FastAPI     | http://localhost:8000/docs |
| Streamlit   | http://localhost:8501      |
| Grafana     | http://localhost:3000      |

Grafana default login: `admin` / `admin`

---

## 📁 Project Structure

```
SmartBuilding_DigitalTwin/
│
├── app/
│   └── streamlit_app.py          # Streamlit dashboard
│   └── Dockerfile
│
├── fastapi_data_generator/
│   └── main.py                   # FastAPI data simulator
│   └── Dockerfile
│
├── grafana/
│   └── provisioning/
│       └── dashboards/
│           └── smart_building_dashboard.json
│
├── docker-compose.yml
└── README.md
```

---

## 📊 Technologies Used

- **Python**
- **FastAPI** – Lightweight web API framework
- **Streamlit** – Fast data app UI
- **Grafana** – Real-time dashboards
- **Docker** – Containerized environment

---

## ✍️ Author

**Manel Ben Hassen** – [GitHub](https://github.com/Manel-Ben-Hassen)

---

## 📃 License

This project is open-source and free to use for academic and demonstration purposes.
