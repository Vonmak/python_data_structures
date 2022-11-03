
# class BookingForm(forms.ModelForm):

#     def __init__(self,*args,**kwargs):
#         super(BookingForm,self).__init__(*args,**kwargs)
#         self.fields['book_date'].label = "book Date"
#         self.fields['book_time'].label = "book Time"

#     def clean(self):
#         cleaned_data = super(BookingForm,self).clean()
#         booking_number = f"{cleaned_data.get('book_date'):%Y%m%d}{cleaned_data.get('book_time'):%H%M}"
#         # if Book.objects.filter(booking_number=booking_number).exists():
#         #     raise forms.ValidationError("Requested slot is already booked, please choose another time")
#         if Book.objects.filter(booking_number=booking_number).exists():
#             today = datetime.today()
#             d = today.day
#             m = today.month
#             y = today.year
            
#             # Retrieve today's bookings
#             today_bookings = Book.objects.filter(book_date__year=y,book_date__month=m, book_date__day=d)

#             # A list of today's bookings time slot (take only hours)
#             # Return something like <QuerySet [{'delivery_date__hour': 11}, ...]>
#             today_time_slot = today_bookings.values('book_date')
#             # Convert it to list of hours values since the utility function accept list.
#             today_time_slot_list = [h['book_date'] for h in list(today_time_slot)]
#             # The line above return something like [9, 11, ...]
            
#             all_time_slot = [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]

#             # Now we can call the utility function `check_free_time`
#             available_slot = check_free_time(all_time_slot, today_time_slot_list)
#             if available_slot:  # The are some available slot (list not empty)
#                 # I use python3.6 f-string to format the message
#                 # Note that the list is in a raw format ([8,11,12]), you can do better like ['8h:00', '11h:00', '12h:00']
#                 message = f"Requested slot is already booked, please choose another time in {available_slot}."
#                 raise forms.ValidationError(message)
#             else:  # The list is empty, all slot are taken
#                 message = "The are not available slot for this booking today."
#                 raise forms.ValidationError(message)

    
#     class Meta:
#         model = Book
#         fields = ('book_date','book_time')
#         widgets = {
#             'book_date': forms.DateInput(attrs={'type': 'date'}),
#             'book_time':forms.Select(choices=HOUR_CHOICES)
#         }