# 🏢 Smart Building Digital Twin – Real-Time Environmental Monitoring System

This project implements a **Digital Twin** for a Smart Building using real-time sensor data (temperature, humidity, CO2, occupancy, energy consumption). It leverages **FIWARE**, **CrateDB**, **Grafana**, and **Streamlit** to monitor and visualize indoor environmental quality.

---

## 🔍 What is a Digital Twin?

A Digital Twin is a real-time virtual replica of a physical asset or process. In this project, we simulate and visualize building telemetry data to:

- Monitor air quality and energy consumption
- Detect anomalies or inefficiencies
- Enable smart building management

---

## 🧠 Real-World Context

Digital Twins are widely used in smart cities and green buildings to ensure:

- **Energy efficiency**
- **Healthy indoor air quality**
- **Occupant comfort and productivity**

---

## 🧩 Architecture Overview

```text
[Sensors Simulator (FastAPI)]
          |
          v
[FIWARE Orion Context Broker] ---> [MongoDB]
          |                              |
          v                              v
   [QuantumLeap] -----------------> [CrateDB]
          |
          v
    [Grafana / Streamlit]
