'''
this program is used to determine the country or location of a provided phone number
'''
import phonenumbers

# import geocoder
from phonenumbers import geocoder

# specify the phonenumber
a= input('Enter phone number:')

# clcoding.com
phonenumber = phonenumbers.parse(a)

# display the location of phone number
print(geocoder.description_for_number(phonenumber,'en'))