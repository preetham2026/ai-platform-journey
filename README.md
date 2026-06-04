# 🐄 Ritham Dairy Farm - AI Platform Project

A full-stack AI-powered farm management system built to demonstrate
end-to-end AI Platform Engineering skills.

## 🚀 Live Demo
- API running on AWS EC2
- Kubernetes orchestrated with 5 pods
- CI/CD pipeline via GitHub Actions

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Language | Python 3.11 |
| API | Flask REST API |
| Database | SQLite |
| AI | AWS Bedrock (Llama 3) |
| Container | Docker |
| Orchestration | Kubernetes |
| Cloud | AWS EC2 |
| CI/CD | GitHub Actions |
| Data Analysis | Pandas |
| Visualization | Matplotlib |

## 📁 Project Structure
ai-platform-journey/
├── day1_project.py      # Farm profit calculator
├── day2_project.py      # Cow production tracker
├── day3_project.py      # Dictionary based system
├── day4_project.py      # Smart alert system
├── day5_project.py      # Live weather API
├── day6_project.py      # Full farm dashboard
├── day8.py              # Pandas data analysis
├── day9.py              # Data visualizations
├── day10.py             # OOP with classes
├── day11.py             # SQLite database
├── day12.py             # Flask REST API
├── day14.py             # AWS Bedrock AI
├── day15.py             # AI chat assistant
├── Dockerfile           # Container config
├── k8s-deployment.yaml  # Kubernetes config
├── test_farm.py         # Automated tests
└── .github/workflows/   # CI/CD pipeline
## 🌐 API Endpoints

| Endpoint | Description |
|----------|-------------|
| GET / | Farm info |
| GET /cows | All cows |
| GET /cows/healthy | Healthy cows |
| GET /cows/sick | Sick cows + vet alert |
| GET /cows/stars | Top producers |
| GET /cows/<name> | Single cow profile |
| GET /barns | Barn performance |
| GET /revenue | Financial summary |
| GET /alerts | All farm alerts |

## 🤖 AI Features
- AWS Bedrock integration with Llama 3
- AI farm consultant answers questions
- Live farm data context fed to AI
- Intelligent cow retirement recommendations

## 📊 Data Analysis
- Pandas DataFrame analysis
- 5 professional matplotlib charts
- Barn performance comparison
- Breed productivity analysis
- Revenue forecasting

## ☸️ Kubernetes
- 3-5 replica deployment
- LoadBalancer service
- Auto-scaling capability
- Zero downtime rolling updates

## 🔄 CI/CD Pipeline
- Automated on every GitHub push
- Python dependency testing
- Docker image build verification
- API health check
- Automatic deployment

## 🚀 How to Run

### Local
```bash
pip install -r requirements.txt
python day12.py
```

### Docker
```bash
docker build -t ritham-farm-api .
docker run -p 5000:5000 ritham-farm-api
```

### Kubernetes
```bash
kubectl apply -f k8s-deployment.yaml
kubectl get pods
```

## 👨‍💻 Built By
Sri Hari Preetham Dammai
- Senior DevOps & AI Platform Engineer
- AWS Certified Solutions Architect
- 8+ years enterprise infrastructure experience
- Email: preetham959@gmail.com
