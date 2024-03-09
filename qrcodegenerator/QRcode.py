# Import QRCode from pyqrcode 
import pyqrcode 
import png 
from pyqrcode import QRCode 


# String which represents the QR code 
myupi = "sm30122000-1@okicici"

# Generate QR code 
url = pyqrcode.create(myupi) 

# Create and save the svg file naming "myqr.svg" 
# url.svg("myqr.svg", scale = 8) 

# Create and save the png file naming "myqr.png" 
url.png('myqr.png', scale = 6) 
