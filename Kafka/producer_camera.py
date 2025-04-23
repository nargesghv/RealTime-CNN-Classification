import cv2, base64, json
from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda x: json.dumps(x).encode()
)

cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    _, buf = cv2.imencode('.jpg', frame)
    encoded = base64.b64encode(buf).decode()
    producer.send("image-topic", value={"image": encoded})
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
