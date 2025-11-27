# Raspberry Pi 3D Advent Christmas Tree

## File - advent_xmas.py

The [Raspberry Pi 3D Christmas Tree](https://thepihut.com/products/3d-xmas-tree-for-raspberry-pi) has 25 LEDs:

1. 24 red LEDs
2. 1 yellow star LED

The advent program is quite simple, for each day in December a new red LED light switches on, for example December 1st - 1 LED, 2nd December - 2 LEDs etc...

Every 30 seconds the lights will randomly pick different LED lights to switch on. 

The star LED is always lit, although for the 12 days of christmas, the star LED will also twinkle

During the rest of the year, the star LED will light up and pulse.

My starting point for this project was taken from [https://gitlab.wijman.net/](https://gitlab.wijman.net/raspberry-pi/3d-christmas-tree/-/blob/main/build-up_to_christmas.sh)


## File - xmas.py

Very basic while true loop to fade the LEDs in and out.

The star LED is always switched on.

## File - cron

Simple script to start a cron job for the python script

At the terminal type to edit the cron:

<span style="color: #4a5bf2ff; font-family: Courier New; ">sudo crontab -e</span>

See link: [Setting up cron jon on the Raspberry Pi](https://bc-robotics.com/tutorials/setting-cron-job-raspberry-pi/?srsltid=AfmBOoorVp697avlYOwwSPL_7PZ07LdZZA2pZR5kvso2rpgExxpGtoop)

## Set timesync with sync to RAM

Running systemd-timesyncd at boot cannot be wrtten to store when the SD card is readonly.

I am running a Raspberry Pi Zero 2 W and when the Raspberry Pi boots it runs time sync to refresh the date/time.

I add a RAM disk to write the time sync state (running SD Card in readonly mode).

Open command window open:

<span style="color: #4a5bf2ff; font-family: Courier New; ">sudo nano /etc/fstab</span>

add the line:
....

<span style="color: #4a5bf2ff; font-family: Courier New; ">tmpfs /var/lib/systemd/timesync tmpfs nosuid,nodev,noexec,size=1M 0 0</span>

....
exit and save

Enable time sync by typing:

<span style="color: #4a5bf2ff; font-family: Courier New; ">sudo systemctl enable systemd-timesyncd</span>


## Headless and set SD card readonly

Guidelines to set the Raspberry pi into headless mode, see [link](https://itsfoss.com/raspberry-pi-gui-boot/)

To convert SD card to readonly if plugged into headless interface, see [link](https://core-electronics.com.au/guides/read-only-raspberry-pi/)

Note that if the SD card is in readonly mode the the date will NOT update to the next day. 

