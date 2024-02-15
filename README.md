# Robot Navigation

**Robot navigation packages (Mapless navigation packages using SLAM method)**

This repository provides navigation packages for robots such as Turtlebot3 Burger and Husky unmanned vehicle.

## Dependencies

Before starting, ensure you have the following dependencies installed:

- ROS Noetic: [Installation Instructions](http://wiki.ros.org/noetic/Installation/Ubuntu)
- Catkin tools: [Installation Instructions](https://catkin-tools.readthedocs.io/en/latest/installing.html)

## Installation

### Step 1: Create a Catkin workspace

```bash
mkdir -p catkin_ws/src
```

### Step 2: Change directory to src

```bash
cd catkin_ws/src
```

### Step 3: Clone this repository

```bash
git clone https://github.com/SFU-MARS/robot_navigation.git
```

### Step 4: Change directory back to workspace

```bash
cd ..
```

### Step 5: Build the packages in workspace

```bash
catkin build
```
or
```bash
catkin_make
```

## Running Turtlebot3 Navigation in Simulation

### Step 1: Run launch file `turtlebot3_world.launch`

```bash
export TURTLEBOT3_MODEL=burger
roslaunch auto_nav turtlebot3_world.launch
roslaunch auto_nav turtlebot3_auto_nav.launch
```

This will run a Gazebo simulation alongside RViz. Use RViz UI to give goal destinations to the robot (2D Nav Goal).

## Running Husky Navigation in Simulation

Before following the steps below, make sure to install the following ROS packages:

- Husky desktop
- Husky simulator
- Husky navigation

Use the following commands to install each:

```bash
sudo apt-get update
sudo apt-get install ros-noetic-husky-desktop
sudo apt-get install ros-noetic-husky-simulator
sudo apt-get install ros-noetic-husky-navigation
```

### Step 1: Run launch file `husky_playpen.launch`

```bash
export HUSKY_LMS1XX_ENABLED=1
roslaunch husky_gazebo husky_playpen.launch
```

### Step 2: Run RViz launch file `view_robot.launch`

```bash
roslaunch rizz view_robot.launch
```

### Step 3: Run husky_auto_nav.launch

```bash
roslaunch husky_robot husky_auto_nav.launch
```

This will run a Gazebo simulation alongside RViz. Use RViz UI to give goal destinations to the robot (2D Nav Goal).