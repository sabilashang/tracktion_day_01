from machine import Pin, I2C
import time
import ssd1306

# Set the OLED dimensions
oled_width = 128
oled_height = 64

# Initialize I2C with the SDA and SCL pins (Pins 21 and 22 are commonly used)
i2c = I2C(0, scl=Pin(22), sda=Pin(21), freq=400000)

# Initialize the OLED display using I2C
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

# Function to make text appear larger and centered
def large_centered_text(oled, text, size=2):
    # Calculate text dimensions
    char_width = 8  # Standard font width per character
    char_height = 8  # Standard font height
    text_width = len(text) * char_width
    
    # Calculate center position
    x_center = (oled_width - text_width) // 2
    y_center = (oled_height - char_height) // 2
    
    # Draw text multiple times with offsets to create larger appearance
    for dx in range(size):
        for dy in range(size):
            oled.text(text, x_center - dx, y_center - dy)
            oled.text(text, x_center + dx, y_center - dy)
            oled.text(text, x_center - dx, y_center + dy)
            oled.text(text, x_center + dx, y_center + dy)

# Clear the OLED screen
oled.fill(0)

# Display the text large and centered
large_centered_text(oled, "SDG", size=1)

# Show the text on the OLED
oled.show()

# Wait before clearing
time.sleep(10)

# Clear the display
oled.fill(0)
oled.show()
