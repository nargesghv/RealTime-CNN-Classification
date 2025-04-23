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

**Goal:**
- Build a real-time machine learning pipeline where new image data is streamed through Kafka topics and classified by a CNN model.
- Achieve high validation accuracy using transfer learning (EfficientNet).
- Train on a Hugging Face open-source image dataset.

**Key Highlights:**
- 🛠️ Real-time image ingestion using Apache Kafka
- 🧠 Deep learning with CNNs + EfficientNet backbone
- 🔥 Data augmentation, regularization, transfer learning
- 📈 Hugging Face Datasets for high-quality training data

---

## 🏛️ Project Structure

RealTime-CNN-Classification/ ├── Data/ ├── Kafka/ ├── Models/ ├── NoteBooks/ ├── Scripts/ ├── visualizations/ ├── README.md ├── requirements.txt ├── .gitignore

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

