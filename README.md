HOW TO RUN THE PROGRAM

1. Open Anaconda Prompt and type the following commands:

``conda activate your_env (In this case, use yolo-env1)

2. Navigate to the folder where your model file is located:

``cd path/to/folder (Folder containing the file my_model.pt)

3. Make sure that the ultralytics library is installed in the created environment:

`` pip install ultralystics

4. Run the script with the appropriate parameters:

`` python your_script.py --model path_to_model.pt --source path_to_image.jpg --window_size 640x480

In this case:

* your_script.py can be:
    photo_detect.py – to run the program with images
    camera_detect.py – to run the program with a camera
* path_to_model.pt should be:
    my_model.pt
* path_to_image.jpg should be:
    ../climbing_images/photo.jpg

TO DO:

* Train the model with new images and the new label human_without_rope

* Add checking if the climber is safe and displaying an alert - MUST BE FIXED ONLY


conda activate yolo-env1
cd Desktop\climbcheck_using_yolo\my_model

python camera_detect.py --model my_model.pt --source ../climbing_images/climbing_video.mp4

python camera_detect.py --model my_model.pt --source ../climbing_images/climbing_video3.mp4 --thresh 0.2
