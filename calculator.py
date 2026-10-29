def temperatureConversion(degrees, fahrenheitOrCelcius):
    # Validate that degrees can be converted to a float
    try:
        degreesAsFloat = float(degrees)
    except ValueError:
        print('Please enter a valid numeric value to perform conversion')
        return None

    # Check if the temperature type is valid
    conversionType = fahrenheitOrCelcius.capitalize()
    if conversionType != 'Fahrenheit' and conversionType != 'Celcius':
        print('Please enter a valid temperature type either Fahrenheit or Celcius to perform conversion')
        return None

    # Perform the conversion based on the type
    if conversionType == 'Fahrenheit':
        # Fahrenheit to Celsius formula: (F - 32) * 5/9
        result = (degreesAsFloat - 32) * (5 / 9)
        print(str(result) + " Celsius")
    else:
        # Celsius to Fahrenheit formula: (C * 9/5) + 32
        result = (degreesAsFloat * (9 / 5)) + 32
        print(str(result) + " Fahrenheit")

    return result

def currencyConversion(amount, dollarOrEuro):
    exchangeRate = .92

    # Validate that amount can be converted to a float
    try:
        amountAsFloat = float(amount)
    except ValueError:
        print('Please enter a valid numeric value to perform conversion')
        return None

    # Check if the currency type is valid
    currencyType = dollarOrEuro.capitalize()
    if currencyType != 'Dollar' and currencyType != 'Euro':
        print('Please enter a valid currency type either Dollar or Euro to perform conversion')
        return None

    # Perform the conversion based on the type
    if currencyType == 'Dollar':
        # Dollar to Euro formula: (D * exchangeRate)
        result = amountAsFloat * exchangeRate
        print(str(result) + " Euros")
    else:
        # Euro to Dollar formula: (E / exchangeRate)
        result = amountAsFloat / exchangeRate
        print(str(result) + " Dollars")
    
    return result

conversionType = input("Enter the type of conversion you would like to perform. For temperature conversion enter 1 For currency conversion enter 2: ")

if conversionType != "1" and conversionType != "2":
    print('Please enter a valid input either 1 or 2 to select the conversion type')

elif conversionType == "1":
    temperature = input("Enter the degrees you would like to convert: ")
    conversionType = input("Enter Fahrenheit or Celcius: ")
    temperatureConversion(temperature, conversionType)

else:
    amount = input("Enter the currency amount you would like to convert: ")
    conversionType = input("Enter Dollar or Euro: ")
    currencyConversion(amount, conversionType)