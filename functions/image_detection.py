from imageai.Detection.Custom import DetectionModelTrainer

def image_detection():
    trainer = DetectionModelTrainer()
    trainer.setModelTypeAsYOLOv3()
    trainer.setDataDirectory(data_directory="resources\\apple_dataset")
    trainer.setTrainConfig(object_names_array=["apple", "damaged_apple"], batch_size=8, num_experiments=50, train_from_pretrained_model="resources\\pretrained-yolov3.h5")
    trainer.trainModel()

image_detection()