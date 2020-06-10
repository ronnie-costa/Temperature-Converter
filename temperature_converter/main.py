#IMPORT ALL FUNCTIONS
from converter import *
#IMPORT FUNCTION SLEEP 
from time import sleep
print('====================================')
print('\nTEMPERATURE CONVERTER\n')
print('====================================')
print('\nCHOOSE AN OPTION FROM THE MENU\n')
choice = 0

while choice !=13:
 try:
#MENU WITH OPTIONS FOR CONVERSION  
  choice = int(input('''
    Menu:
    1 - CELSIUS - KELVIN
    2 - CELSIUS - FAHRENHEIT
    3 - CELSIUS - RÉAUMUR
    4 - KELVIN - CELSIUS
    5 - KELVIN - FAHRENHEIT
    6 - KELVIN - RÉAUMUR
    7 - FAHRENHEIT - CELSIUS
    8 - FAHRENHEIT - KELVIN
    9 - FAHRENHEIT - RÉAUMUR
    10 - RÉAUMUR - CELSIUS
    11 - RÉAUMUR - KELVIN
    12 - RÉAUMUR - FAHRENHEIT
    13 - EXIT
     '''))
  if choice == 1:
  	celsius_kelvin()
  elif choice == 2:
    celsius_fahrenheit()
  elif choice == 3:
    celsius_reaumur()
  elif choice == 4:
    kelvin_celsius()
  elif choice == 5:
    kelvin_fahrenheit()
  elif choice == 6:
    kelvin_reaumur()
  elif choice == 7:
    fahrenheit_celsius()
  elif choice == 8:
    fahrenheit_kelvin()
  elif choice == 9:
    fahrenheit_reaumur()
  elif choice == 10:
    reaumur_celsius()
  elif choice == 11:
    reaumur_kelvin()
  elif choice == 12:
    reaumur_fahrenheit()
  elif choice == 13:
    print('SHUTDOWN...')
  else:
       print('INVALID OPTION ')
  sleep(2)#FUNCTION SLEEP (2 SECONDS FOR SHUTDOWN)
 except ValueError:
     print('ENTER NUMBERS ONLY')