# robot_navigation
Robot navigation packages (Mapless navigation packages using slam method)  
  
Currently supported robots:  
=> Turtlebot3 Burger (Can be easily applied to other models)  
=> Husky unmanned vehicle  
  
Install the following dependencies before starting:  
- Ros Noetic  
  http://wiki.ros.org/noetic/Installation/Ubuntu  
- Catkin tools  
  https://catkin-tools.readthedocs.io/en/latest/installing.html  

After installing dependencies:  
  
Step 1: Create a Catkin workspace   
- mkdir -p catkin_ws/src

Step 2: Change directory to src  
- cd catkin_ws/src

Step 3: Clone this repository
- git clone https://github.com/SFU-MARS/robot_navigation.git

Step 4: Change directory back to workspace  
- cd ..

Step 5: Build the packages in workspace
- catkin build (alternative `catkin_make`)


Further steps to run Turtlebot3 navigation in simulation:

Step 1: Run launch file turtlebot3_world.launch
Run the following commands in terminal within `catkin_ws` directory
- export TURTLEBOT3_MODEL=burger
- roslaunch auto_nav turtlebot3_world.launch
- roslaunch auto_nav turtlebot3_auto_nav.launch

This should run a gazebo simulation alongside rviz.  
Use Rviz UI to give goal destination to robot (2D Nav Goal)


Further steps to run Husky navigation in simulation:  
# Before the following steps make sure to install the following ros packages.
- Husky desktop
- Husky simulator
- Husky navigation

Use following commands to install each:  
-  sudo apt-get update  
-  sudo apt-get install ros-noetic-husky-desktop  
-  sudo apt-get install ros-noetic-husky-simulator  
-  sudo apt-get install ros-noetic-husky-navigation  


Step 1: Run launch file husky_playpen.launch  
Step 2: Run rviz launch file view_robot.launch  

Run the following commands in terminal within `catkin_ws` directory for step 1 and step 2:    
- export HUSKY_LMS1XX_ENABLED=1;  roslaunch husky_gazebo husky_playpen.launch  
- roslaunch rizz view_robot.launch
- roslaunch husky_robot husky_auto_nav.launch

This should run a gazebo simulation alongside rviz.  
Use Rviz UI to give goal destination to robot (2D Nav Goal)