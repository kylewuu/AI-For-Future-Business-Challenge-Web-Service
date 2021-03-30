# AI for Future Business Challenge 2021

This application allows users to quickly see the quality and condition of their entire food and produce selection in their homes. The users will mount cameras in their pantries or throughout their kitchen, with proper views of whatever they want to monitor. The app then uses AI image detection and trained image detection models to show users the count, quality, and conditions of their foods. With this, users can see an overall score which can suggest to users which food to use or consume first. Having a central UI that displays this information allows users to not forget about food or be caught off guard when food spoils. This cuts down on food waste dramatically as well as saves money for the users as less food will be thrown out.

This is the web service part of the application. It contains the endpoints for the application as well as the trained AI model. 

## The AI

Using a large set of over two hundred annotated images of apples in various conditions, ImageAI, Tensorflow, and the object detection model YOLOv3, a model was trained that would be able to not only count how many apples are in an image but also indicate how many of those apples have defects. New images do not require any annotations and can be processed through our trained model.

This AI program is implemented as an API, along with other helpful APIs. This program is then packaged as a Docker image then uploaded to an Azure web service. Our program then runs on Azure listening for HTTP requests, capable of detecting for defects in new images of apples and storing the data in its own database.
