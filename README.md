# 🚀 Real-Time CNN Classification with Kafka, TensorFlow & FastAPI

This project builds a real-time multi-class image classification pipeline using:

- **TensorFlow CNN** trained on **Hugging Face Food-101** dataset
- **Apache Kafka** for real-time streaming from a live webcam
- **FastAPI** for serving the model as a REST API
- **Docker** for clean, portable deployment

---

## 🧾 About the Project

**Goal:**  
Train a CNN model on a high-quality image dataset (Food-101), then deploy it for real-time image classification using a live camera stream via Kafka.

**Pipeline Overview:**
[Webcam] → [Kafka Producer] → [Kafka Topic] → [Kafka Consumer] → [CNN Model] → [Prediction Output]


- Live image feed from webcam is streamed through Kafka.
- Pre-trained TensorFlow model classifies the incoming images.
- Predictions are returned via terminal or FastAPI endpoint.

---

## 📂 Project Structure

RealTime-CNN-Classification/ ├── Data/ # Raw data if needed ├── Kafka/ │ ├── producer.py # Basic file producer │ ├── producer_camera.py # Live webcam → Kafka │ ├── consumer.py # Basic receiver │ ├── consumer_batch_predict.py # Batch prediction w/ CNN ├── Models/ │ └── saved_model/ # Trained TF model ├── Notebooks/ │ ├── data_preprocessing.ipynb │ ├── model_training.ipynb │ └── kafka_integration.ipynb ├── deployment/ │ ├── main.py # FastAPI app │ ├── model_loader.py # Load & infer from CNN │ ├── Dockerfile # Docker support ├── visualizations/ │ ├── accuracy_loss_plot.png │ └── confusion_matrix.png ├── .gitignore ├── requirements.txt ├── README.md └── LICENSE (optional)

---

## 🛠️ Tech Stack

| Tool/Framework      | Purpose                           |
|---------------------|------------------------------------|
| **TensorFlow/Keras**| Deep learning model training       |
| **Kafka (kafka-python)** | Real-time image streaming    |
| **Hugging Face Datasets** | Food-101 open dataset       |
| **FastAPI**         | Lightweight REST API for inference |
| **OpenCV**          | Image processing and camera input  |
| **Docker**          | Containerization                   |
| **Jupyter Notebook**| Research and training              |
| **Python**          | Core scripting and automation      |

---

## 🚀 Getting Started

### 1. Clone the Repository

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

## 🧠 Model Training (Food-101)
Open the notebook:
```bash
Notebooks/model_training.ipynb
```
Loads Food-101 dataset via Hugging Face

Preprocesses and trains a custom CNN architecture

Saves trained model to Models/saved_model/

### 4. Stream images from webcam
```bash
python Kafka/producer_camera.py
```
and

### 5. Start Batch Consumer with CNN Model
```bash
python Kafka/consumer_batch_predict.py

```
---

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
[Kafka Producer (Webcam/Files)] ↓ [Kafka Topic] ↓ [Kafka Consumer → TensorFlow CNN] ↓ [Prediction Output (Terminal or FastAPI)]
```

👩‍💻 Author
Narges