# TURTLEBOT2 GUIDE


I am using Ubuntu 20.04 running ROS noetic. Please download ROS noetic prior to this guide from [ROS noetic](https://wiki.ros.org/noetic/Installation/Ubuntu)

- I first used a turlebot3 then moved on to a turtlebot2 because it has more power, speed and it can carry more weight/more modular.
- In this guide I will simply list how you can get turtlebot2 working on Ubuntu20.04 with ROS noetic.
- Last I will give an example test run to check if your installation was correct and if the topics are being published and recieved properly.
- Currently I am trying to use a ZED camera along with the turtlebot2 (10 March), after succesfully doing so I will update this guide.

## Making the workspace
- If you have already done this then skip this section.

```sh
mkdir ~/catkin_ws
cd catkin_ws
mkdir -p src
catkin_make
cd src
```

>  This is the folder where you will modify, build, and. install catkin 
>  build, and. install catkin packages




## Installing the required turtlebot repositories

I am using [turtlebot github](https://github.com/turtlebot/turtlebot). The following is simply the terminal commands to download them. The repository contains all the packages and drivers to run the turtlebot2.

```sh
git clone https://github.com/turtlebot/turtlebot.git
git clone https://github.com/turtlebot/turtlebot_msgs.git
git clone https://github.com/turtlebot/turtlebot_apps.git
git clone https://github.com/turtlebot/turtlebot_simulator
```

This repository includes software for controlling the robot's base, sensors, and other peripherals. It contains launch files, configuration files, and utilities for setting up and using a TurtleBot.

- turtlebot_msgs - Message definitions used for communication between various components of the TurtleBot system. These messages define the structure of data exchanged between different nodes in a TurtleBot system.
Common message types include sensor readings, control commands, robot state information, and more.
- turtlebot_apps - Higher-level applications and demos for TurtleBot robots.
This repository may contain pre-built software packages or scripts that demonstrate specific functionalities of TurtleBots.
- turtlebot_simulator - Higher-level applications and demos for TurtleBot robots. This repository may contain pre-built software packages or scripts that demonstrate specific functionalities of TurtleBots. Examples of applications could include mapping and navigation demos, teleoperation interfaces, interactive behaviors, and more.

## Install kobuki packages

The Kobuki base is the mobile platform in TurtleBot 2 robots. It features a differential drive system, wheel encoders, IMU, and expansion ports. This base provides mobility and flexibility, allowing users to build and customize their TurtleBot for various robotic applications.

```sh
git clone https://github.com/yujinrobot/yujin_ocs.git
mv yujin_ocs/yocs_cmd_vel_mux yujin_ocs/yocs_controllers yujin_ocs/yocs_velocity_smoother .
rm -rf yujin_ocs
```

Adding the battery monitor packages

```sh
git clone https://github.com/ros-drivers/linux_peripheral_interfaces.git
mv linux_peripheral_interfaces/laptop_battery_monitor ./
rm -rf linux_peripheral_interfaces
```
Finally install kobuki

```sh
git clone https://github.com/yujinrobot/kobuki.git
```

## Remaining dependacncies and packages

```sh
sudo apt install liborocos-kdl-dev -y
sudo apt install ros-noetic-joy 
rosdep install --from-paths . --ignore-src -r -y
```

Now run catkin_make to check if everything was installed properly and build all the code. Run catkin_make in the catkin_ws/src directory.

```sh
cd ..
catkin_make
```

Download LDS-01 module

```sh
sudo apt install ros-noetic-hls-lfcd-lds-driver -y
```

Download 3d sensor module ( I believe you need this for ZED)
```sh 
sudo apt install ros-noetic-openni2-launch -y
sudo apt install ros-noetic-depthimage-to-laserscan -y
```

source the bash files 
```sh
echo source "$HOME/catkin_ws/devel/setup.bash" >> ~/.bashrc
sudo adduser $USER dialout
```
