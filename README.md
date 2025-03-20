HOW TO RUN THE PROGRAM

1. Open Anaconda Prompt and type the following commands:

``conda activate your_env (In this case, use yolo-env1)

2. Navigate to the folder where your model file is located:

``cd path/to/folder (Folder containing the file my_model.pt)

3. Make sure that the ultralytics library is installed in the created environment:

`` pip install ultralystics

4. Run the script with the appropriate parameters:

`` python your_script.py --model path_to_model.pt --source path_to_video.jpg --window_size 640x480

In this case:

* your_script.py can be:
    climbcheck.py
* path_to_model.pt should be:
    my_model.pt
* path_to_video.jpg should be:
    just place where you have your video (can be usb camera)

You can add parameter --thresh, it able you to set detecting confidence (deafult thresh is 0.7)


