## The First Section of this tutorial is about setting up VICON. At the end there is a link to an existing guide that helps connect ROS with ViCON using a datastream API and a ROS bridge.
## Documentation

This guide is meant to be used in tandem with the actual user guide and tutorials.

### Pre-Process
- The cameras require 30-60 minutes to warm up. Before doing anything else, switch the cameras on.
- Turn on the active wand to check the 5 lights at the top. This represents the battery life of the wand. If it is low, turn it off, plug it in, and charge it.
- Helpful mocap suit marker placement guidance links:
  - [Place markers on a performer](https://docs.vicon.com/display/Shogun110/Place+markers+on+a+performer)
  - [How to mocap a performer using a Vicon system](https://mocappys.com/how-to-mocap-a-performer-using-a-vicon-system/#gsc.tab=0)
  - [Marker placement guide (PDF)](http://mocap.cs.cmu.edu/markerPlacementGuide.pdf)

### Capture Process (ShoGun Live)
- Open the ShoGun Live software on the computer.
- Select all cameras with shift+click. Mask all, wait 5-10 seconds, stop masking.
- Have someone hold the Active wand and turn it on. Click “start Wave” and have them walk around the lab, slowly swinging the wand from the low end of the “T” in a wide, sweeping figure 8 shape. Watch the screen- in the bottom right corner there is a progress bar for the calibration.
- **IMPORTANT NOTE:** After the calibrating wand wave, do not remove the wand from the space visible to the cameras. Immediately after doing the wand wave, set the origin.
- To check if the cameras are calibrated, go to the Log window and see if the camera calibration file is saved.
- Select all of the “dots” representing the wand using shift + click, and then click Start set Origin, then click Set origin.
- Create Prop: Select all markers on the prop- note that it must have 4 or more markers attached.
- If the capture is being used for visualization or presentation purposes, export the video to .mov format.

### Post-Capture Processing (ShoGun Post)
- If you have exported the file in .vcf, .x2d, and .mcp format, see [this video](#) (Use the .mcp format).

### Troubleshooting
#### Issue: The cameras are not being recognized by the ShoGun software
- **Potential solution:**
  - Wait 5-10 more min for the cameras to warm up.
  - Check that the cameras are on and functioning.
  - Reboot the software by right-clicking “Vicon Cameras” and selecting “Reboot System Hardware”, and then right-clicking “Local Vicon System” and selecting “Reboot System Hardware”.

#### Issue: The wand is not being recognized by the cameras
- **Potential solution:**
  - Redo the calibrating wand wave process and then place the wand at the origin spot right away.
  - If this does not work, check that the wand's lights are all on, and check the side of the wand that goes on the floor to see if the screws in each arm are evenly tightened.
 
## Credits to Bermett and Trinity.
[Link to connect ROS with VICON tutorial](http://wiki.ros.org/vicon_bridge)
