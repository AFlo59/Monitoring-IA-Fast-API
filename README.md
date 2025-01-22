# File: README.md
# Monitoring Project

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone <repo-url>
   cd project
   ```

2. Set up the virtual environments:
   ```bash
   cd api
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt

   cd ../evidently
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. Run the project with Docker Compose:
   ```bash
   docker-compose up --build
   ```

4. Access the services:
   - API: http://localhost:8000
   - Prometheus: http://localhost:9090
   - Grafana: http://localhost:3000


project/
├── api/
│   ├── app.py
│   ├── model.pkl
│   ├── data/
│   │   ├── reference_data.csv
│   │   ├── test_data.csv
│   ├── tests/
│   │   ├── test_api.py
│   ├── requirements.txt
│   ├── .env
├── evidently/
│   ├── generate_reports.py
│   ├── data/
│   │   ├── production_data.csv
│   │   ├── reference_data.csv
│   ├── reports/
│   │   ├── report.html
│   │   ├── report.json
│   ├── requirements.txt
├── prometheus/
│   ├── prometheus.yml
│   ├── Dockerfile
├── grafana/
│   ├── dashboards/
│   │   ├── api_dashboard.json
│   │   ├── system_dashboard.json
│   ├── Dockerfile
├── model_training/
│   ├── train_model.ipynb
│   ├── requirements.txt
├── docker-compose.yml
├── README.md