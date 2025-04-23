# 🚀 Real-Time CNN Classification with Kafka & TensorFlow

Built a deep learning pipeline for real-time multi-class image classification, integrating TensorFlow CNNs with Kafka streaming and training on Hugging Face open datasets.

---

## 📚 Table of Contents
- [About the Project](#about-the-project)
- [Project Structure](#project-structure)
- [Tech Stack](#tech-stack)
- [Getting Started](#getting-started)
- [Kafka Setup](#kafka-setup)
- [Model Training](#model-training)
- [Results](#results)
- [Future Work](#future-work)
- [Acknowledgements](#acknowledgements)
- [Author](#author)

---

## 📖 About the Project

---

## 🧾 About the Project

**Goal**: Build an end-to-end deep learning system that can classify images in real-time as they stream through Kafka.

- Live image feed (e.g., webcam) → Kafka → CNN → FastAPI → Response
- CNN trained on Hugging Face **Food-101** dataset
- Real-time predictions via REST API

---

**Key Highlights:**

---
RealTime-CNN-Classification/
├── Data/                         # Raw data if needed
├── Kafka/
│   ├── producer.py              # Basic file producer
│   ├── producer_camera.py       # Live webcam → Kafka
│   ├── consumer.py              # Basic receiver
│   ├── consumer_batch_predict.py # Batch prediction w/ CNN
├── Models/
│   └── saved_model/             # Trained TF model
├── Notebooks/
│   ├── data_preprocessing.ipynb
│   ├── model_training.ipynb
│   └── kafka_integration.ipynb
├── deployment/
│   ├── main.py                  # FastAPI app
│   ├── model_loader.py          # Load & infer from CNN
│   ├── Dockerfile               # Docker support
├── visualizations/
│   ├── accuracy_loss_plot.png
│   └── confusion_matrix.png
├── .gitignore
├── requirements.txt
├── README.md
└── LICENSE (optional)

---

## 🛠️ Tech Stack

| Tool/Framework | Purpose |
|----------------|---------|
| TensorFlow/Keras | Deep learning model training |
| Kafka (kafka-python) | Real-time data ingestion |
| Hugging Face Datasets | Open-source datasets |
| Python | Scripting and automation |
| Matplotlib / Seaborn | Visualization |
| Jupyter Notebook | Experimentation |

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/RealTime-CNN-Classification.git
cd RealTime-CNN-Classification
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. (Optional) Start Kafka locally
```bash
# Start Zookeeper
zookeeper-server-start.sh config/zookeeper.properties

# Start Kafka server
kafka-server-start.sh config/server.properties

```
### 4. Stream images from webcam
```bash
python Kafka/producer_camera.py
```
and

### 5. Batch inference with TensorFlow model:
```bash
python Kafka/consumer_batch_predict.py

```
### 6. Model training
```bash
# Run notebook
Notebooks/model_training.ipynb
```
CNN trained on Food-101 (101 classes) and Model saved to Models/saved_model/

## 🌐 Deployment with FastAPI

```bash
cd deployment
uvicorn main:app --reload
```
## 📍 Endpoint:
http
POST http://localhost:8000/predict

## 🐳 Docker Support
```bash
# Build Docker image
docker build -t fastapi-cnn .

# Run the container
docker run -p 8000:8000 fastapi-cnn
```

and ✅ After running, the FastAPI server will be accessible at: http://localhost:8000/docs
and Use the built-in Swagger UI for quick testing and documentation.

---

Let me know if you want a version that includes **Docker Compose**, or if you'd like help creating an `openapi.json` spec file too!


## 🧱 Architecture

```text
[Kafka Producer (Webcam/Files)] 
          ↓
     [Kafka Topic]
          ↓
[Kafka Consumer → TensorFlow CNN]
          ↓
[Prediction Output (Terminal or API)]

