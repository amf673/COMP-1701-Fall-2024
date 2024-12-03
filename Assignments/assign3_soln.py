# 
# 
# COMP 1701 Fall 2024 
# 
# Assignment 3 Diagnoses
# 

import math

ORAL_TEMP_FEVER               = 37.8
UNDERARM_TEMP_FEVER           = 37.2
HEART_RATE_VARIABILITY_CUTOFF = 50
CORTISOL_CUTOFF               = 25.0
ORAL                          = 'o'
UNDERARM                      = 'u'

def compute_HRV(interval1: float, interval2: float, interval3: float) -> float:
   """
   compute heart rate variability
   parameters:
       interval1, interval2, and interval3: three successive heart beat intervals, in ms
   returns:
       the heart rate variability
   """
   diff1 = interval1 - interval2
   diff2 = interval2 - interval3
   avg_sq_diff = (diff1 ** 2 + diff2 ** 2) / 2
   hrv = math.sqrt(avg_sq_diff)

   return hrv


def temperature_is_fever(temperature: float, site: str) -> bool:
   """
   determines whether a given temperature and test site represents fever
   parameters:
       temperature: the recorded temperature in °C
       site: either "oral" or "underarm"
   returns: True if an oral temp is at least 37.8°, or an underarm temp is at least 37.2°
   """
   
   return (temperature >= ORAL_TEMP_FEVER and site == ORAL) or (temperature >= UNDERARM_TEMP_FEVER and site == UNDERARM)


def has_fever() -> bool:
   """
   Asks the user for their body temperature and where it was measured, and
   returns True if they have a fever
   """
   temperature = float(input("Enter your temperature (°C):"))
   site = input("Was the temperature measured Orally (O) or Underarm (U)? (enter O or U): ").lower()
   
   return temperature_is_fever(temperature, site)


def has_nausea() -> bool:
   """
   asks the user if they are experiencing nausea, and
   returns their response as a boolean
   """

   return input("Are you experiencing nausea? (enter y or n): ").lower() == 'y'


def has_low_HRV() -> bool:
   """
   asks the user to enter three successive heartbeat intervals, in ms
   returns True if these intervals represent a HRV less than 50 ms
   """
   print('Please enter 3 heartbeat intervals in ms…')
   interval1 = float(input('Enter first interval: '))
   interval2 = float(input('Enter second interval: '))
   interval3 = float(input('Enter third interval: '))
   hrv = compute_HRV(interval1, interval2, interval3)

   return hrv < HEART_RATE_VARIABILITY_CUTOFF


def has_high_cortisol() -> bool:
   """
   asks the user to enter their cortisol level
   returns True if the level is above 25.0
   """
   cortisol = float(input('Enter cortisol level in mcg/dL: '))
   
   return cortisol > CORTISOL_CUTOFF


def main() -> None:
   """
   Runs the diagnostic program, and prints out the final diagnosis
   """
   diagnosis = "error"

   if has_fever():
      if has_nausea():
         diagnosis = "flu"
      else:
         diagnosis = "infection"
   elif has_low_HRV() and has_high_cortisol():
      diagnosis = 'stress'
   else:
      diagnosis = 'healthy'

   print(f"Diagnosis: {diagnosis}")


main()
