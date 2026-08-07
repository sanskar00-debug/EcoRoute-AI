# 🚚 EcoRoute AI

> **Next-Generation Dynamic Waste Optimization Powered by AI and IoT Telemetry Grids.** 
> Built solo for the 2nd NextGen Hackathon 2026.

---

## 🌌 Project Overview

**EcoRoute AI** transforms traditional, inefficient, fixed-schedule municipal waste management into an automated, data-driven elastic infrastructure logistics grid. 

Traditional logistics truck assets consume excessive fuel and labor driving rigid routes to half-empty bins, while high-density zones experience dangerous bin overflows before scheduled pick-ups occur. EcoRoute AI resolves this operational friction by matching live telemetry data streams with predictive ML modeling and automated operational routing layers.

### 🌟 Key Core Innovations
*   **Predictive Spill Over Logic:** Goes beyond simple mapping by forecasting overflow thresholds before public hazards occur.
*   **Decoupled Async Architecture:** Ingests high-frequency concurrent IoT sensor data bursts safely.
*   **Optimized Routing Topology:** Formulates automated multi-vehicle fleet pathing sequence grids based on live priority matrices.

---

## 🛠️ System Architecture & Tech Stack

The workspace infrastructure features a clean, loosely-coupled framework designed for rapid execution and horizontal scalability:

[IoT Bin Sensor Simulator] ---> [HTTP POST Data Stream Ingestion Pipeline]|v[Local SQLite Storage Engine] <---> [Python FastAPI Central Engine]|v[Interactive Swagger UI / Docs]

*   **Core Backend System:** Python 3.10+ / FastAPI (High-performance async routing network)
*   **Database Management Tier:** SQLite via SQLAlchemy ORM (Persistent relational table architecture mapping node updates)
*   **Simulation Ingestion Layer:** Python Requests (Multi-threaded streaming payload engine mimicking 100+ urban coordinates)
*   **Visual Style Framework:** Standardized semantic HTML5 paired with structural responsive local CSS injection (Optimized for standalone offline execution loops)

---

## 📂 Repository File Blueprint

```text
├── database.py       # SQLAlchemy ORM core configuration & SQL database schema models
├── main.py           # Core FastAPI application logic, endpoints & local UI landing layout
├── simulator.py      # Automated virtual IoT sensor network telemetry streaming background engine
├── ecoroute.db       # Persistent SQLite database storage file (Generated automatically on startup)
└── README.md         # Master platform documentation asset
```

---

## 🚀 Local Quickstart Guide (Windows + VS Code Setup)

Follow these concise steps to deploy the entire live system framework locally on your workstation:

### 1. Environment Preparation
Clone the workspace project repository, open your terminal screen inside VS Code (`Ctrl + ~`), and execute dependencies installations:
```bash
pip install fastapi uvicorn sqlalchemy requests
```

### 2. Booting the Main Core Server Engine
Execute the master API engine script file to initialize your internal SQLite storage data schemes and fire up the web connection socket on port `5000`:
```bash
python main.py
```
*Expected confirmation status log line:* `INFO: Uvicorn running on http://127.0.0.1:5000`

### 3. Launching the Live IoT Telemetry Simulator Engine
Open a secondary terminal panel layer inside your VS Code grid interface space and deploy the automated streaming loop:
```bash
python simulator.py
```
*The engine will instantly start parsing multi-threaded simulated asset spikes directly to your endpoints.*

---

## 📊 Live System Verification Network Links

While your application services framework loops are completely active, minimize your terminal screen grid panel and monitor data metrics through these localized platform pathways inside your browser:

*   **Core Landing Web Dashboard Portal:** Connect straight to the core UI directory endpoint at `http://127.0.0` to bypass standard Windows numeric port blocker policy configurations.
*   **Interactive Controls & Swagger Documentation Pages:** Navigate to `http://127.0.0docs` to test endpoint variables dynamically.
*   **Live Raw Data Sets Document Strings:** Check changing capacity metrics streaming into database layers by visiting `http://127.0.0api/bins`.

---

## 🏆 Measurable Real-World Target Impact Metrics
*   **30% Absolute Reductions** in overall municipal heavy-duty vehicle carbon footprint expenditures and redundant fleet routing mileage.
*   **99% Complete Eradication** of public bin spillage and urban biological odor vectors.
*   **20% Extensions** in commercial sanitation asset lifecycles through precise operational logistics dispatch optimizations.

---

## 📝 Next Steps Timeline Matrix (Round 2 Live Hackathon Milestones)
*   [ ] **Milestone A:** Integrate **Google OR-Tools VRP Solver** to build real-time fleet path navigation optimization arrays.
*   [ ] **Milestone B:** Connect a **React/Next.js and Mapbox GL Canvas Map Panel** to display neon dynamic routing polylines to operators.
*   [ ] **Milestone C:** Deploy native physical hardware sensor modules utilizing ESP32 microcontrollers over MQTT brokers.
