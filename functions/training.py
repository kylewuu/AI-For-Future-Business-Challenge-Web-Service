from imageai.Detection.Custom import DetectionModelTrainer
import tensorflow as tf

def image_detection():
  
    trainer = DetectionModelTrainer()
    trainer.setModelTypeAsYOLOv3()
    trainer.setDataDirectory(data_directory="resources\\apple_dataset")
    trainer.setTrainConfig(object_names_array=["apple", "damaged_apple"], batch_size=2, num_experiments=50, train_from_pretrained_model="resources\\pretrained-yolov3.h5")
    trainer.trainModel()

if tf.config.list_physical_devices('GPU'):
    physical_devices = tf.config.list_physical_devices('GPU')
    tf.config.experimental.set_memory_growth(physical_devices[0], enable=True)
    tf.config.experimental.set_virtual_device_configuration(physical_devices[0], [tf.config.experimental.VirtualDeviceConfiguration(memory_limit=4000)])

image_detection()