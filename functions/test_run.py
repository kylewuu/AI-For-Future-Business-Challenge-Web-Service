from imageai.Detection.Custom import CustomObjectDetection
import os

execution_path = os.getcwd()

detector = CustomObjectDetection()
detector.setModelTypeAsYOLOv3()
detector.setModelPath(detection_model_path="resources\\apple_dataset\\models\\detection_model-ex-005--loss-0034.281.h5")
detector.setJsonPath(configuration_json="resources\\apple_dataset\\json\\detection_config.json")
detector.loadModel()

detections = detector.detectObjectsFromImage(input_image="resources\\images\\test2-damaged.jpg", minimum_percentage_probability=60, output_image_path="resources\\imagesm\\output\\test2-new-custom-model.jpg")

for detection in detections:
    print(detection["name"], " : ", detection["percentage_probability"], " : ", detection["box_points"])
