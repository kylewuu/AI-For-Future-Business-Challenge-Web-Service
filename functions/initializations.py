import tensorflow as tf
from imageai.Detection.Custom import CustomObjectDetection

def init():
    # temporarily disable if not using local machine with GPU
    # if tf.config.list_physical_devices('GPU'):
    #         physical_devices = tf.config.list_physical_devices('GPU')
    #         tf.config.experimental.set_memory_growth(physical_devices[0], enable=True)
    #         tf.config.experimental.set_virtual_device_configuration(physical_devices[0], [tf.config.experimental.VirtualDeviceConfiguration(memory_limit=5000)])

    detector = CustomObjectDetection()
    detector.setModelTypeAsYOLOv3()
    detector.setModelPath(detection_model_path="resources\\apple_dataset\\models\\detection_model-ex-036--loss-0017.781.h5") 
    detector.setJsonPath(configuration_json="resources\\apple_dataset\\json\\detection_config.json")
    detector.loadModel()

    return detector