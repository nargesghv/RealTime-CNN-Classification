from kafka import KafkaConsumer
import json, base64, numpy as np, tensorflow as tf, cv2

consumer = KafkaConsumer('image-topic',
    bootstrap_servers='localhost:9092',
    value_deserializer=lambda x: json.loads(x.decode()))

model = tf.keras.models.load_model('../Models/saved_model/')
batch, BATCH_SIZE = [], 8

for msg in consumer:
    data = msg.value['image']
    img_bytes = base64.b64decode(data)
    img = cv2.imdecode(np.frombuffer(img_bytes, np.uint8), 1)
    img = cv2.resize(img, (224, 224)) / 255.0
    batch.append(img)
    if len(batch) == BATCH_SIZE:
        preds = model.predict(np.array(batch))
        for p in preds:
            print("Predicted class:", np.argmax(p))
        batch.clear()
