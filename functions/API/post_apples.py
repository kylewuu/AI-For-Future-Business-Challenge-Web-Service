import base64
from classes.Apples import *


def process_apples(detector, img_string):

    imgdata = base64.b64decode(img_string)
    # docker change
    # filename = 'resources\\temp_db\\temp_image.jpg'
    filename = 'temp_image.jpg'
    with open(filename, 'wb') as f:
        f.write(imgdata)

    detections = detector.detectObjectsFromImage(
        input_image=filename, minimum_percentage_probability=65, output_image_path="resources\\images\\output\\test3-custom.jpg")

    damaged_apples_count = 0
    undamaged_apples_count = 0
    total_apples_count = 0

    for detection in detections:
        if (detection['name'] == 'damaged_apple'):
            damaged_apples_count += 1

        elif (detection['name'] == 'apple'):
            undamaged_apples_count += 1

        total_apples_count += 1

        # print(detection["name"], " : ", detection["percentage_probability"], " : ", detection["box_points"])

    apples = Apples(total_apples_count, damaged_apples_count)

    return {"total_apples_count": apples.total_apples_count, "damaged_apples_count": apples.damaged_apples_count}
