import pygame
import sys
import pygwidgets

# ---------------------------------------------------------
# Initialize pygame
# ---------------------------------------------------------
pygame.init()
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 350
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Temperature Converter")
clock = pygame.time.Clock()

# ---------------------------------------------------------
# Create Widgets
# ---------------------------------------------------------
inputTemp = pygwidgets.InputText(window, (50, 50), width=120)

# IMPORTANT: Use group='scale' (NOT groupName)
radioF = pygwidgets.TextRadioButton(window, (50, 100), 'Convert to Fahrenheit', 'scale')
radioC = pygwidgets.TextRadioButton(window, (250, 100), 'Convert to Celsius', 'scale')


# Default selection
radioF.setValue(True)

convertButton = pygwidgets.TextButton(window, (50, 150), 'Convert')

outputText = pygwidgets.DisplayText(window, (50, 220), '', fontSize=28, textColor=(0, 0, 150))


# ---------------------------------------------------------
# Conversion Function
# ---------------------------------------------------------
def doConversion():
    userInput = inputTemp.getValue()

    # Validate input
    try:
        temp = float(userInput)
    except ValueError:
        outputText.setValue("Enter a valid number")
        return

    # Determine conversion direction
    if radioF.getValue():
        # Celsius → Fahrenheit
        result = temp * (9/5) + 32
        outputText.setValue(f"{temp:.2f} °C = {result:.2f} °F")
    else:
        # Fahrenheit → Celsius
        result = (temp - 32) * (5/9)
        outputText.setValue(f"{temp:.2f} °F = {result:.2f} °C") 