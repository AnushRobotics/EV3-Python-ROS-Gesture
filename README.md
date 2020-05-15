# EV3-Python-ROS-Gesture
Controlling Ev3 Pick and Place Robot using ROS

DEPENDENCIES 
 -webcam
 -ROS kinectics
 -OPENCV

to run the code,follow the commands

cd catkin_ws/src
git clone https://github.com/AnushRobotics/EV3-Python-ROS-Gesture git
$ cd ..
$ catkin_make

then simply run the code roslaunch gesture_teleop teleop.launch.

then you will get the output accordingly

• Five fingers - Pick ( Bend Down, raise and Pick the Object)
• Two fingers - (turn left)
• Three fingers - (turn right)
• No fingers - Place( Bend Down and Place the Object)

