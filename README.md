# robotics_project

Clone the folder and build the package.
```sh
$ catkin_make
```
Launch the test.launch file and wait until you get a map big enough. 
```sh
$ roslaunch turtlebot3_gazebo test.launch
```
Save the map.

```sh
$ rosrun map_server map_saver -f ~/map
```
Quit the process. In a new terminal lunch the navigation.lunch file.
```sh
$ roslaunch turtlebot3_navigation navigation.launch map_file:=$HOME/map.yaml 
```
At this point in a new terminal run the allignment.py node and once the robot is alligned quit the process.
```sh
rosrun navigation alignment.py
```
To conlcude run the navigation.py node. If the node is not able to find the goal.txt file, change the path from local to gloabal. 

```sh
rosrun navigation navigation.py
```
