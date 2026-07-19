import tensorflow as tf
from tensorflow.keras.preprocessing import image_dataset_from_directory
from utils.preprocessing import data_augmentation
from utils.model import build_model

# Dataset Path
DATASET_PATH = "dataset/PlantVillage"

# Training Dataset
train_dataset = image_dataset_from_directory(
    DATASET_PATH,
    validation_split=0.2,
    subset="training",
    seed=42,
    image_size=(224, 224),
    batch_size=32
)

# Validation Dataset
validation_dataset = image_dataset_from_directory(
    DATASET_PATH,
    validation_split=0.2,
    subset="validation",
    seed=42,
    image_size=(224, 224),
    batch_size=32
)

print("\n✅ Dataset Loaded Successfully!")
print("Classes:", train_dataset.class_names)
print("Total Classes:", len(train_dataset.class_names))
# Check Augmentation
for images, labels in train_dataset.take(1):
    augmented_images = data_augmentation(images)

print("Image Augmentation Applied Successfully!")
# Build Model
model = build_model(len(train_dataset.class_names))

# Compile Model
model.compile(
    optimizer="adam",
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"]
)

# Model Summary
model.summary()
# -------------------------
# Train Model
# -------------------------
history = model.fit(
    train_dataset,
    validation_data=validation_dataset,
    epochs=20
)

# -------------------------
# Save Model
# -------------------------
model.save("models/crop_disease_model.keras")

print("\n✅ Model Training Completed!")
print("✅ Model Saved Successfully!")