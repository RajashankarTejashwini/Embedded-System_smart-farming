# Embedded-System_smart-farming
This Python script simulates a monitoring and control system typically used in applications like smart farming or automated greenhouse environments. Here’s a detailed breakdown of the various components and functionalities of the script:

Variables and Thresholds
Threshold Values: Defined for temperature, moisture, and passive infrared (PIR) motion detection. These values are the limits beyond which actions will be triggered (e.g., turning on an alarm).
Initial States: Variables are set up for the alarm, LED, microcontroller state (either "ON" or "OFF"), and operation mode (either "MANUAL" or "AUTOMATIC").
Sensor Data
Sensor Data: Simulated data for temperature, moisture, PIR (motion detection), and water level. These values are used to demonstrate how the system reacts to different environmental factors.
Functions
send_message(message): Simulates sending a message, typically to inform a user or log an event.
switch_off_power(): Represents an action to cut electrical power, possibly as a safety measure or to conserve energy.
update_web_page(temp, moist, pir, water_lvl): Simulates updating a remote interface or web page with the current sensor readings. Useful for remote monitoring.
indicate_water_level(water_lvl): Simulates indicating the water level, potentially on a physical display at the site.
Main Logic
Check Sensor Thresholds: The script checks if any sensor readings exceed their predefined thresholds. If they do, it activates the alarm and the LED.
Communications and Actions:
Sends a message about the sensor threshold being exceeded.
Switches off power, perhaps as a preventive action against potential hazards.
Updates a web page with the current readings, keeping a remote user informed.
Operation Mode Check: Depending on the mode (MANUAL or AUTOMATIC), different actions are taken:
MANUAL Mode: Waits for a manual intervention (a button press) before toggling the microcontroller's power state.
AUTOMATIC Mode: Automatically toggles the microcontroller's power state based on sensor readings without waiting for user input.
Mode-Specific Logic
In MANUAL mode, it continuously checks for a button press before changing the microcontroller state.
In AUTOMATIC mode, it manages the microcontroller state automatically based on sensor conditions, turning it on or off as necessary.
Final Steps
Update Web Page: The script updates the web page again with sensor data, ensuring the information is current.
Indicate Water Level: Physically indicates the water level, which could be critical for managing water resources effectively.
Exit: Terminates the script.
This script demonstrates a basic framework for a sensor-based monitoring and control system which could be applied in various real-world scenarios, particularly where environmental conditions need to be closely managed.
