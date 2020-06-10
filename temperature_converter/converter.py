def celsius_kelvin():
    print ('CELSIUS - KELVIN')    
    celsius = float(input("ENTER TEMPERATURE: "))
    kelvin = celsius + 273.15
    print(f"{celsius} ºCELSIUS = {kelvin:.2f} ºKELVIN")

def celsius_fahrenheit():
    print ('CELSIUS - FAHRENHEIT')
    celsius = float(input("ENTER TEMPERATURE: "))
    fahrenheit = ((9 * celsius) / 5) + 32
    print(f"{celsius} ºCELSIUS = {fahrenheit:.2f} ºFAHRENHEIT")

def celsius_reaumur():
    print ('CELSIUS - RÉAUMUR')
    celsius = float(input("ENTER TEMPERATURE: "))
    reaumur = celsius * 4/5
    print(f"{celsius} ºCELSIUS = {reaumur:.2f} ºRÉAUMUR")

def kelvin_celsius():
    print ('KELVIN - CELSIUS')
    kelvin = float(input("ENTER TEMPERATURE: "))
    celsius = kelvin - 273.15
    print(f"{kelvin} ºKELVIN = {celsius:.2f} ºCELSIUS")

def kelvin_fahrenheit():
    print ('KELVIN - FAHRENHEIT')
    kelvin = float(input("ENTER TEMPERATURE: "))
    fahrenheit = (kelvin - 273.15) * 9/5 + 32
    print(f"{kelvin} ºKELVIN = {fahrenheit:.2f} ºFAHRENHEIT")

def kelvin_reaumur():
    print ('KELVIN - RÉAUMUR')
    kelvin = float(input("ENTER TEMPERATURE: "))
    reaumur = (kelvin - 273.15) * 0.8
    print(f"{kelvin} ºKELVIN = {reaumur:.2f} ºRÉAUMUR")

def fahrenheit_celsius():
    print ('FAHRENHEIT - CELSIUS')
    fahrenheit = float(input("ENTER TEMPERATURE: "))
    celsius = (fahrenheit - 32) * 5/9
    print(f"{fahrenheit} ºFAHRENHEIT = {celsius:.2f} ºCELSIUS")

def fahrenheit_kelvin():
    print ('FAHRENHEIT - KELVIN')
    fahrenheit = float(input("ENTER TEMPERATURE: "))
    kelvin = (fahrenheit - 32) * 5/9 + 273.15
    print(f"{fahrenheit} ºFAHRENHEIT = {kelvin:.2f} ºKELVIN!")

def fahrenheit_reaumur():
    print ('FAHRENHEIT - RÉAUMUR')
    fahrenheit = float(input("ENTER TEMPERATURE: "))
    reaumur = (fahrenheit - 32) * 4/9
    print(f"{fahrenheit} ºFAHRENHEIT = {reaumur:.2f} ºRÉAUMUR")

def reaumur_celsius():
    print ('RÉAUMUR - CELSIUS')
    reaumur = float(input("ENTER TEMPERATURE: "))
    celsius = reaumur * 5/4
    print(f"{reaumur} ºRÉAUMUR = {celsius:.2f} ºCELSIUS")

def reaumur_kelvin():
    print ('RÉAUMUR - KELVIN')
    reaumur = float(input("ENTER TEMPERATURE: "))
    kelvin = reaumur * 5/4 + 273.15
    print(f"{reaumur} ºRÉAUMUR = {kelvin:.2f} ºKELVIN!")

def reaumur_fahrenheit():
    print ('RÉAUMUR - FAHRENHEIT')
    reaumur = float(input("ENTER TEMPERATURE: "))
    fahrenheit = reaumur * 9/4 + 32
    print(f"{reaumur} ºRÉAUMUR = {fahrenheit:.2f} ºFAHRENHEIT")