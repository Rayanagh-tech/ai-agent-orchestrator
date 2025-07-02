🎯 PROJECT OVERVIEW
🧠 Project Goal
Develop a 3D conversational agent for Unity, capable of:

✅ Understanding natural language

✅ Dynamically extracting knowledge from documents (PDF, DOCX, TXT)

✅ Reacting in real time with immersive behavior and speech

🔧 Tech Stack
Layer	Technologies
🎮 Frontend	Unity + UnityWebRequest (mock UI)
🧠 AI Backend	Python (FastAPI microservices)
🔌 APIs	LLM, Retrieval, STT, TTS (modular REST APIs)
🐳 DevOps	Docker, Kubernetes, GitHub Actions
📡 Deployment	Minikube (local) or GCP/AWS (cloud-ready)
📈 Monitoring (optional)	Prometheus, Grafana
📄 Documentation	GitHub Wiki, Postman, Google Docs

🗂️ PROJECT STRUCTURE
ai-agent-orchestrator/
│
├── services/                  # Microservices
│   ├── llm_service/           # Mocked LLM generator
│   ├── retrieval_service/     # Document QA or RAG interface (WIP)
│   ├── stt_service/           # Speech-to-text mock
│   └── tts_service/           # Text-to-speech mock
│
├── k8s/                       # Kubernetes manifests
│   ├── namespace.yaml
│   ├── llm/
│   │   ├── deployment.yaml
│   │   └── service.yaml
│   ├── stt/
│   │   ├── deployment.yaml
│   │   └── service.yaml
│   ├── tts/
│   │   ├── deployment.yaml
│   │   └── service.yaml
│   └── ingress/
│       └── ingress.yaml       # Unified routing (optional)
│
├── docker-compose.yml         # For local multi-service dev
├── tests/
│   └── test_latency.py        # Python test for API response time
│
├── ci/
│   └── github-actions.yml     # CI/CD pipeline for Docker build/test
│
├── docs/
│   ├── architecture.md        # System flow & data pipeline
│   └── api_spec.md            # Endpoints documentation
│
└── README.md


🔁 WORKFLOW OVERVIEW
🔸 AI Pipeline (Backend):
text
Copy code
[Unity UI] → [LLM API] → [RAG Engine (doc retrieval)] → [TTS/STT]
🔸 DevOps Pipeline:
text
Copy code
Dev → Docker build → GitHub Actions → Deploy to K8s → Monitor