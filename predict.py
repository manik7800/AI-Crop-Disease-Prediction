import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image

# -----------------------------
# Load Trained Model
# -----------------------------
model = tf.keras.models.load_model("models/crop_disease_model.keras")

# -----------------------------
# Class Names
# -----------------------------
class_names = [
    "Pepper__bell___Bacterial_spot",
    "Pepper__bell___healthy",
    "Potato___Early_blight",
    "Potato___Late_blight",
    "Potato___healthy",
    "Tomato_Bacterial_spot",
    "Tomato_Early_blight",
    "Tomato_Late_blight",
    "Tomato_Leaf_Mold",
    "Tomato_Septoria_leaf_spot",
    "Tomato_Spider_mites_Two_spotted_spider_mite",
    "Tomato__Target_Spot",
    "Tomato__Tomato_YellowLeaf__Curl_Virus",
    "Tomato__Tomato_mosaic_virus",
    "Tomato_healthy"
]

# -----------------------------
# Image Path
# -----------------------------
image_path = "images/test.jpg"

# -----------------------------
# Load Image
# -----------------------------
img = image.load_img(image_path, target_size=(224, 224))

# Convert Image to Array
img_array = image.img_to_array(img)

# Add Batch Dimension
img_array = np.expand_dims(img_array, axis=0)

# Normalize Image
img_array = img_array / 255.0

# -----------------------------
# Prediction
# -----------------------------
prediction = model.predict(img_array)

predicted_class = np.argmax(prediction)

confidence = np.max(prediction) * 100

print("=" * 50)
print("Disease :", class_names[predicted_class])
print(f"Confidence : {confidence:.2f}%")
print("=" * 50)