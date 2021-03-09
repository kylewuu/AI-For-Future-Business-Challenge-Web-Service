from imageai.Detection.Custom import CustomObjectDetection
import os

execution_path = os.getcwd()

detector = CustomObjectDetection()
detector.setModelTypeAsYOLOv3()
detector.setModelPath(detection_model_path="resources\\apple_dataset\\models\\detection_model-ex-004--loss-0036.693.h5") 
# detector.setModelPath(detection_model_path="resources\\detection_model-ex-028--loss-8.723.h5")
detector.setJsonPath(configuration_json="resources\\apple_dataset\\json\\detection_config.json")
detector.loadModel()

detections = detector.detectObjectsFromImage(input_image="resources\\images\\test-default.jpg", minimum_percentage_probability=60, output_image_path="resources\\images\\output\\test-default-new-custom-model.jpg")

print("\n" + "Detections: " + str(len(detections)) + "\n")

for detection in detections:
    print(detection["name"], " : ", detection["percentage_probability"], " : ", detection["box_points"])
