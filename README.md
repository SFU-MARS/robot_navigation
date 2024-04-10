# ZED
## Using ZED camera with ROS



The ZED camera, produced by Stereolabs, is known for its advanced features that make it suitable for various computer vision and depth sensing applications. 

- Stereo Vision and Depth Sensing
- High-Resolution RGB Imaging
- Compact and Lightweight Design

## Features

- ROS Wrapper for ZED
- Depth Sensing and Point Clouds:
- Camera Calibration and TF Support
- Stereo Image and RGB Data Streams
- Integration with ROS Navigation Stack

This guide is simply compiling other guides and based on my trial and error experience.
From [Stereolabs Docs](https://www.stereolabs.com/docs/ros) and [ROS and ZED](https://www.stereolabs.com/docs/ros)

> I have used ROS-Noetic running on UBUNTU 20.04.6 LTS
> using dual boot with a windows PC.
> I am using a ZED camera, but I will be using a ZED2 soon
> so the guide will be updated accordingly.

## ZED SDK

Download the ZED SDK from [Stereolabs Downloads](https://www.stereolabs.com/developers/release)
I am using the Linux version

```sh
cd path/to/download/folder
sudo apt install zstd
chmod +x ZED_SDK_Ubuntu22_cuda11.8_v4.0.0.zstd.run
./ZED_SDK_Ubuntu22_cuda11.8_v4.0.0.zstd.run
```
Note that the chmod and run command will be different depending on the SDK version you download 



## Packages Installation
CUDA is a nvidia library that you require for running the ZED camera.
Before downloading run the commands below to find which version of CUDA you should download
```sh
source /etc/lsb-release
UBUNTU_VERSION=ubuntu${DISTRIB_RELEASE/./}
```
Now go to [NVIDIA cuda download](https://developer.nvidia.com/cuda-toolkit-archive) and download the appropriate version. Now Restart your laptop. Note that if you have UEFI enabled by default then you will have to do more steps to allow the changes to be made. Please find a guide online for this.

Next we will download the ZED-ros-wrapper
>zed-ros-wrapper: the main package that provides the ZED ROS Wrapper node
>zed-ros-interfaces: the package declaring custom topics, services and actions
>zed-ros-examples: a support package that contains examples and tutorial
>

If you don't already have catkin_ws setup then follow this tutorial [wiki](https://wiki.ros.org/catkin/Tutorials/create_a_workspace). Otherwise continue
```sh
cd ~/catkin_ws/src
git clone --recursive https://github.com/stereolabs/zed-ros-wrapper.git
cd ../
catkin_make
source ./devel/setup.bash
```

Now we will download ZED-interfaces

```sh
cd ~/catkin_ws/src
git clone https://github.com/stereolabs/zed-ros-interfaces.git
cd ../
catkin_make
source ./devel/setup.bash
```
For this you don't need an nvidia gpu but for the following you will require one.

Last Download zed-example
```sh
cd ~/catkin_ws/src
git clone https://github.com/stereolabs/zed-ros-examples.git
cd ../
catkin_make
source ./devel/setup.bash
```
## Running ZED nodes

Open a terminal and use roslaunch to start the ZED node:

| Camera | launch command |
| ------ | ------ |
| ZED |  roslaunch zed_wrapper zed.launch |
| ZED mini | roslaunch zed_wrapper zedm.launch|
| ZED 2 | roslaunch zed_wrapper zed2.launch |
| ZED 2i | roslaunch zed_wrapper zed2i.launch |


## Displaying Output

RVIZ is a useful visualization tool in ROS. Using RVIZ, we can visualize the ZED output.


Using ZED

```sh
 roslaunch zed_display_rviz display_zed.launch
```

Using ZED mini

```sh
roslaunch zed_display_rviz display_zedm.launch
```

Using ZED2

```sh
roslaunch zed_display_rviz display_zed2.launch
```

Using ZED2i
```sh
roslaunch zed_display_rviz display_zed2i.launch
```

#### Dynamically edit camera parameters



```sh
rosrun rqt_reconfigure rqt_reconfigure
```

Generating pre-built zip archives for distribution:

```sh
gulp build dist --prod
```
## To use the custom built node

This node publishes the distance of detection objects by subscribing to the topic od_dection from the "roslaunch zed_display_rviz display_zed2.launch" node.
To use this simply build a new folder in catkin_ws/src 
```sh
touch PublishDistance.py 
```
and paste the contents of the python file into this. Then in the catkin_ws directory run

```sh
catkin_build
```

and now the packages should be built.

Now to run the newly build node: RUN THE ZED2 rviz NODE IN ONE TERMINAL AND IN THE OTHER:
```sh
rosrun PublishDistance.py
```




[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)

   [dill]: <https://github.com/joemccann/dillinger>
   [git-repo-url]: <https://github.com/joemccann/dillinger.git>
   [john gruber]: <http://daringfireball.net>
   [df1]: <http://daringfireball.net/projects/markdown/>
   [markdown-it]: <https://github.com/markdown-it/markdown-it>
   [Ace Editor]: <http://ace.ajax.org>
   [node.js]: <http://nodejs.org>
   [Twitter Bootstrap]: <http://twitter.github.com/bootstrap/>
   [jQuery]: <http://jquery.com>
   [@tjholowaychuk]: <http://twitter.com/tjholowaychuk>
   [express]: <http://expressjs.com>
   [AngularJS]: <http://angularjs.org>
   [Gulp]: <http://gulpjs.com>

   [PlDb]: <https://github.com/joemccann/dillinger/tree/master/plugins/dropbox/README.md>
   [PlGh]: <https://github.com/joemccann/dillinger/tree/master/plugins/github/README.md>
   [PlGd]: <https://github.com/joemccann/dillinger/tree/master/plugins/googledrive/README.md>
   [PlOd]: <https://github.com/joemccann/dillinger/tree/master/plugins/onedrive/README.md>
   [PlMe]: <https://github.com/joemccann/dillinger/tree/master/plugins/medium/README.md>
   [PlGa]: <https://github.com/RahulHP/dillinger/blob/master/plugins/googleanalytics/README.md>
