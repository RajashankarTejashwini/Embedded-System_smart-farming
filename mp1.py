# Define the threshold values 
temperature_threshold = 30 	# Celsius 
moisture_threshold = 50 		# % 
pir_threshold = 1 		# detected or not detected 

# Define the initial state of the alarm and LED 
alarm_state = False 
led_state = False 

# Define the initial state of the microcontroller 
microcontroller_state = "OFF" 
# Define the initial state of the mode 
mode = "MANUAL" 

# Define the sensor data 
temperature = 25 	# Celsius 
moisture = 60 		# % 
pir = 0 			# not detected 
water_level = 80 	# % 

# Define functions for sending messages, switching off power, updating web page, and indicating water level 
def send_message(message): 
	print("Sending message:", message) 

def switch_off_power(): 
	print("Switching off power...")
def update_web_page(temp, moist, pir, water_lvl): 
	print("Updating web page with sensor data...") 
	print("Temperature:", temp, "Celsius") 
	print("Moisture:", moist, "%") 
	print("PIR:", "detected" if pir else "not detected") 
	print("Water level:", water_lvl, "%") 
def indicate_water_level(water_lvl): 
	print("Water level indication:", water_lvl, "%") 

# Check the sensor data against the threshold values 
if temperature > temperature_threshold or moisture < moisture_threshold or pir > pir_threshold:
# Turn on the alarm and LED 
	alarm_state = True 
	led_state = True 

# Send a message to the farmer 
message = "Alarm: Sensor threshold exceeded" 
send_message(message) 

# Automatically switch off the power 
switch_off_power() 

# Update the web page with the sensor data 
update_web_page(temperature, moisture, pir, water_level) 

# Check the mode of operation 
if mode == "MANUAL": 
# Wait for the button press from the Android application 
	def button_pressed(): 
		return True # Simulate button press 
	while not button_pressed(): 
		pass # Do nothing 

# Toggle the state of the microcontroller 
	if microcontroller_state == "OFF": 
		microcontroller_state = "ON" 
	else: microcontroller_state = "OFF" 

# Send a message to the farmer 
	message = f"Microcontroller state: {microcontroller_state}" 
	send_message(message) 
elif mode == "AUTOMATIC": 

# Check if the microcontroller should be switched on or off 
	if (temperature > temperature_threshold or moisture < moisture_threshold or pir > 	pir_threshold) and microcontroller_state == "OFF": 
# Turn on the microcontroller 
		microcontroller_state = "ON" 

# Send a message to the farmer 
		message = "Microcontroller switched on" 
		send_message(message) 

# Send an alert message to the user through the GSM module 
		alert_message = "Automatic mode activated" 
		send_message(alert_message) 
elif (temperature <= temperature_threshold and moisture >= moisture_threshold and pir <= pir_threshold) and microcontroller_state == "ON": 
# Turn off the microcontroller 
	microcontroller_state = "OFF" 
# Send a message to the farmer 
	message = "Microcontroller switched off" 
	send_message(message) 

# Update the web page with the sensor data 
update_web_page(temperature, moisture, pir, water_level) 

# Indicate the level of water inside a tank or the water resource
indicate_water_level(water_level)

# Exit the program 
exit()