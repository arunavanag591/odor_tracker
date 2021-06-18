## Setting up GPS Correction Station in U-center

Download <a href="https://www.u-blox.com/en/product/u-center">u-center</a> and install in Windows 10.


### Configuring the base station:

1) Connect the ZED-F9P chip that is going to be used as a base station to the laptop via usb.
2) Launch ucenter
3) From the top left hand corner, there should be a drop down menu (looks like two plugs). Click
on the arrow and select the COM port (usb port) that the chip is on. May take some trial and error depending
on where you plug it in. You know you have the chip selected when you see data on the right hand side of u center.
4) We are going to reset the chip to factory settings to ensure that we configure properly. You'llsee 3 cogs in
u center in the middle-top-right-ish side: one with a memory card next to it, one with a file, and one with a red mark.
Click the cog with the red mark. The Fix Mode (under Lat/Lon/Alt) should be 3D or 3D/GNSS
5) From the menu, select "View" then "Generation 9 Configuration View"
6) Select "Advanced Configuration"
7) On the right hand side menu, scroll down and select "Load from File". The configurations are under [zed-f9p-configuration](config/zed-f9p-configurations)
8) Select "F9P Base config C99". You should see a lot of values load under "Items to set"
9) Click "Send config changes". You should see checkmarks appear next to the Key Names in "Items to set"
10) Now, we have to correct the baudrate. On the left hand menu, you should see a lot of drop-down menus with the prefix "CFG-uxxx".
Select "CFG-UART1" and from its drop-down menu down click "CFG-UART1-BAUDRATE". Its current value is 460800 but needs to be 115200. Once
selected, on the right hand menu, change its "Value" to 115200 (1c200 in hex). Then, select "Set in RAM", "Set in BBR", and "Set in Flash".
11) Once done, click "Send Config Changes"
12) Now we need to tell the base station its position. Under "View", select "Configuration View" and from the left hand menu select
"TMODE3". Set "Mode" to 2 and under Fixed Position, select "Use Lat/Lon/Alt Position" and type in the Lat/Lon/Alt shown by the chip
on the far right hand side of ucenter.
13) On the lower left hand side, click "Send". If you did everything right, your "Fix Mode" show display TIME or TIME/GNSS.

### OPTIONAL

If you want to save the configuration to swap the chip over to a different power supply, it is doable. Make sure the antenna doesn't move tho.

1) Select "View" -> "Configuration View" , then on the left hand side select "CFG"
2) Select "Save Current Configuration" and under "Devices", Ctrl Click all options 0,1,2,4
3) Click "Send"

This is kinda experimental, so only try this as last resort I guess? And don't keep the gps powered off for more than a few seconds. It's kinda inconsistent.


### Quick Notes:

- The "RTK" LED on the chips are active low, so when the rover receives RTCM data, the RTK LED should start blinking/turn off.
- The chips can't hold onto config data for that long without power if you do that optional step. If they go too long without power, you have to repeat the proccess to 
configure them.
- The Base Station's antenna MUST NOT MOVE at all once its Lat/Lon/Alt is set. 
- Some things that affect the accuracy of RTCM corrections:   
  - How many obstructions there are near the antennas, how clear a view there is of the sky, how the weather is (especially smoke), etc. 
  - GPS antenna are finnicky at best, so try and place the base station up high and away from any obstacles like hills, laptops, bags, cars, etc. and don't forget to put a ground plate under each antenna.
- A difference in grounds between the two chpis (floating ground) may not be a problem since they communicate via bluetooth, so don't worry about it.