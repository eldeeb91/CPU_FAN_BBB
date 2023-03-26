#!/usr/bin/python3

import Adafruit_BBIO.PWM as PWM
print(PWM)
import Adafruit_BBIO.ADC as ADC
print(ADC)
import math
import time
ADC.setup()
PWMPin="P8_13"
PWM.start(PWMPin, 30, 2000)
Condition='Startup'
print(f"Condition={Condition}")
time.sleep(2)
TempThershold=30
#### Thermistor ####
R1=10e3			# Series Resistance
Ro=100e3		# Thermistor Resistance @ 25 
Vcc=1.8			# ADC V_REF
Beta=3950		# Beta Coff for the ADC
T0=289
analogPin="P9_40"

NUMSAMPLES=3

while(1):
#	DC=input("What Duty Cycle Would You Like (0-100)? ")
#	DC=int(DC)
#	PWM.start(PWMPin,DC,Freq)

	samples=[0,0,0,0]
	for i in range(NUMSAMPLES):
		samples[i] = ADC.read_raw(analogPin);
#		print(f"ADC_RAW={samples[i]}")
		samples[i]=(1.8/4095)*samples[i]
		time.sleep(0.2);

	# average all the samples out
	average = 0;
	for i in range(NUMSAMPLES):
		average += samples[i];

	average /= NUMSAMPLES

	VRT = average
	VR=Vcc-VRT
	RT = VRT / (VR/R1); 			# Resistance of the Thermistor
	ln=math.log(RT/Ro)
	TX = (1 / ((ln / Beta) + (1 / T0)));	# Temperature from thermistor
	temp =  TX - 273.15;                	# Conversion to Celsius
	temp = round(temp,2)

	if temp >= TempThershold: # Temp >= 30
		Duty=100
		Freq=10000
		Condition='Run'
	elif temp < TempThershold-4: # Temp < 26 
		Duty=00
		Freq=100
		Condition='off'
	else:
		Duty=100
		Freq=10000
		Condition="Run2"
	PWM.start(PWMPin,Duty,Freq)
	print(f"Condition={Condition}, Temp={temp}, Duty={Duty}, Freq={Freq}")
	time.sleep(0.25)

PWM.stop(PWMPin)
PWM.cleanup()
