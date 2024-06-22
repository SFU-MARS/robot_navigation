# TurtleBot 2 and 3 Directory

This directory contains code and resources for both TurtleBot 2 and TurtleBot 3 platforms. As the project progresses, further branches will be created to include custom-built code specific to each platform.

## Branches

- **master**: Contains general resources, code, and documentation applicable to both TurtleBot 2 and 3.
- **turtlebot2**: Custom-built code and resources specifically tailored for TurtleBot 2.
- **turtlebot3**: Custom-built code and resources specifically tailored for TurtleBot 3.


# System Setup Guide for VICON and TurtleBot3

## Accounts and Passwords:
- **Computer**: 
  - **Account**: administrator
  - **Password**: vicon
- **Laptop**: 
  - **Account**: marslab
  - **Password**: autolab2024
- **TurtleBot3**: The robot used in this project.

- ---

## Preparations for the Game:

### Laptop Setup (If using Your Own Laptop)
1. **Install Ubuntu 20.04**:
   - Use the [Ubuntu 20.04 image](https://releases.ubuntu.com/20.04/) and [install it on your PC](https://ubuntu.com/tutorials/install-ubuntu-desktop#1-overview).

2. **Install ROS Noetic**:
   - After setting up the system, open the terminal and run the following commands:
     ```bash
     sudo apt update
     sudo apt upgrade
     wget https://raw.githubusercontent.com/ROBOTIS-GIT/robotis_tools/master/install_ros_noetic.sh
     chmod 755 ./install_ros_noetic.sh 
     bash ./install_ros_noetic.sh
     ```
   - Install additional ROS and Turtlebot3 packages:
     ```bash
     sudo apt-get install ros-noetic-joy ros-noetic-teleop-twist-joy \
       ros-noetic-teleop-twist-keyboard ros-noetic-laser-proc \
       ros-noetic-rgbd-launch ros-noetic-rosserial-arduino \
       ros-noetic-rosserial-python ros-noetic-rosserial-client \
       ros-noetic-rosserial-msgs ros-noetic-amcl ros-noetic-map-server \
       ros-noetic-move-base ros-noetic-urdf ros-noetic-xacro \
       ros-noetic-compressed-image-transport ros-noetic-rqt* ros-noetic-rviz \
       ros-noetic-gmapping ros-noetic-navigation ros-noetic-interactive-markers
     sudo apt install ros-noetic-dynamixel-sdk
     sudo apt install ros-noetic-turtlebot3-msgs
     sudo apt install ros-noetic-turtlebot3
     ```

3. **Configure Network**:
   - Use `ifconfig` to get the IP address of the PC (make sure to connect to your chosen WiFi).
   - Update ROS IP settings in `~/.bashrc`:
     ```bash
     nano ~/.bashrc
     ```
   - Modify the address of `localhost` in the `ROS_MASTER_URI` and `ROS_HOSTNAME` with the acquired IP address.
     ```bash
     export ROS_MASTER_URI=http://{IP_ADDRESS}:11311
     export ROS_HOSTNAME={IP_ADDRESS}
   - Apply changes:
     ```bash
     source ~/.bashrc
     ```

### SBC (Raspberry Pi of TurtleBot3) Setup:
1. **Burn TurtleBot3 SBC Image**:
   - Burn the TurtleBot3 SBC image into the microSD card located in the Raspberry Pi of TurtleBot3.
   - You may need a microSD card reader if you PC do not have a microSD slot.
   - Follow [instructions](https://emanual.robotis.com/docs/en/platform/turtlebot3/sbc_setup/#sbc-setup)

2. **Configure WiFi Network**:
   - Connect to the chosen WiFi on the laptop and get your laptop’s IP address using `ifconfig`.
   - Connect the Raspberry Pi to the laptop using HDMI for monitor and USB for keyboard input.
   - Log in Raspberry Pi with:
     - **ID**: ubuntu
     - **Password**: turtlebot
   - Modify the network configuration:
     ```bash
     cd /media/$USER/writable/etc/netplan
     sudo nano 50-cloud-init.yaml
     ```
   - Replace `WIFI_SSID` and `WIFI_PASSWORD` with your chosen WiFi SSID and password (*this is to connect to chosen WiFi in Raspberry Pi).
     ```yaml
     network:
      version: 2
      renderer: networkd
      ethernets:
        eth0:
          dhcp4: yes
          dhcp6: yes
          optional: true
      wifis:
        wlan0:
          dhcp4: yes
          dhcp6: yes
          access-points:
            WIFI_SSID:
              password: WIFI_PASSWORD

   - After connect to WiFi, you should get the Raspberry Pi’s IP address using `ifconfig`.
   - Edit the `.bashrc` file to update ROS IP settings:
     ```bash
     nano ~/.bashrc
     ```
   - Modify `ROS_MASTER_URI` and `ROS_HOSTNAME` with the corresponding IP addresses.
     ```bash
     export ROS_MASTER_URI=http://{IP_ADDRESS_OF_LAPTOP}:11311
     export ROS_HOSTNAME={IP_ADDRESS_OF_RASPBERRY_PI}
     ```
   - Apply changes:
     ```bash
     source ~/.bashrc
     ```

---

## After setting up the laptop, Raspberry Pi and network, it is time to connect Devices:
1. **Connect to the Same WiFi**:
   - Ensure the computer, laptop, and TurtleBot3 are connected to the same WiFi network `TP-LINK_2B36`:
     - **WiFi Password**: 38291432

2. **Launch ROS on the Laptop**:
   - Start ROS core:
     ```bash
     roscore
     ```
   - Connect the laptop to the TurtleBot3:
     ```bash
     ssh -X ubuntu@{IP_ADDRESS_OF_THE_TURTLEBOT}
     ```
   - Run the TurtleBot3 launch file:
     ```bash
     roslaunch turtlebot3_bringup turtlebot3_robot.launch
     ```
   - Connect VICON with the laptop:
     ```bash
     roslaunch vicon_bridge
     ```
3. **To be filled**:

---

## Tips:
1. ROS is not compatible with virtual environment managers (e.g., conda).
2. If the IP address of Raspberry Pi is not displayed or only present initially (probably because only use battery causes low voltage, then  Raspberry Pi  may turn off wifi function), try switching to another local network (e.g., using your mobile hotspot).
3. Turtlebot 3 needs to get the laptop's WLAN IP address for connection. If you use VirtualBox on your laptop, it may recognize the host machine's WLAN IP address as an Ethernet IP address and only show the Ethernet IP address. Therefore, when you need to obtain the WLAN IP in VirtualBox, you can use the Ethernet IP address.
