import barcode
from barcode.writer import ImageWriter

#define content of the barcode as a string
number = input('Enter the code to generate the barcode') #clcoding.com

#Get the required barcode foemat
barcode_format = barcode.get_barcode_class('upc')

# Generate the barcode and render as image
my_barcode = barcode_format(number, writer=ImageWriter())

#Save barcode as png
my_barcode.save('generated_barcode')