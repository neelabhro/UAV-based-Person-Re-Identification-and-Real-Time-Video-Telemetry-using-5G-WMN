# UAV-based-Person-Re-Identification-and-Real-Time-Video-Telemetry-using-5G-WMNs
[![Documentation Status](https://ieeexplore.ieee.org/document/9071078)
1. Install ROS Melodic (Requires Ubuntu 18.04) (http://wiki.ros.org/melodic/Installation/Ubuntu)
2. Install OpenVino 2021.1.110 (https://docs.openvinotoolkit.org/2021.1/openvino_docs_install_guides_installing_openvino_apt.html)
3. Install Python 3.7.x
4. git clone https://github.com/neelabhro/UAV-based-Person-Re-Identification-and-Real-Time-Video-Telemetry-using-5G-WMN.git
5. Download test video (https://drive.google.com/file/d/11vW1rH13Y8bF1uZtQcPSv6k9odPGbYOv/view?usp=sharing) and place it to the cloned folder with the rest of the files.
6. Go to the cloned directory using the terminal.
7. pip install -r requirements.txt
8. Run Rosmaster at the base station.
9. Run camfeed.py on each of the UAVs equipped with a USB webcam. Make sure to install ROS Melodic on each of these UAVs.
10.Subscribe to all the ROS topics to get live streams from the webcams at the base station.
11. python3.7 app.py -i cam (for webcam) or python3.7 app.py -i test.mp4
