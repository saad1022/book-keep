from django import forms
from .models import Entry
from datetime import date



now = date.today()

class DateInput(forms.DateInput):
	input_type = 'date'
	initial = now


account_choices = [('Bike Maintenance','Bike Maintenance'),('Bike Petrol','Bike Petrol'),('Bills','Bills'),
('Car Maintenance','Car Maintenance'),('Car Petrol','Car Petrol'),('Ciggrate','Ciggrate'),('Food','Food'),
('Food - Out','Food - Out'),('Groceries','Groceries'),('Hair Saloon','Hair Saloon'),('Home Account(Given)','Home Account(Given)'),
('Home Account(Received)','Home Account(Received)'),('Income','Income'),('Loan(Given)','Loan(Given)'),('Loan(Received)','Loan(Received)'),('Medical','Medical'),('Others','Others'),
('Packet','Packet'),('Repair & Fixing','Reapir & Fixing'),('Shopping','Shopping')]

head_choices  = [('Saad','Saad'),('Home','Home')]


class EntryForm(forms.ModelForm):
	class Meta:
		model = Entry
		fields = ('head','account' , 'amount' ,'reason'    )
		
		widgets = {

			'head' : forms.Select(choices=head_choices, attrs={'class':'form-control','placeholder':'Enter Account'}),
			'account' : forms.Select(choices=account_choices, attrs={'class':'form-control','placeholder':'Enter Account'}),
			'amount' : forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Amount'}),
			'reason' : forms.Textarea(attrs={'class':'form-control'}),
		}



class EditEntryForm(forms.ModelForm):
	class Meta:
		model = Entry
		fields = ('head','account' , 'amount' , 'reason' ,  )
		
		widgets = {

			'head' : forms.Select(choices=head_choices, attrs={'class':'form-control','placeholder':'Enter Account'}),
			'account' : forms.Select(choices=account_choices, attrs={'class':'form-control','placeholder':'Enter Account'}),
			'amount' : forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Amount'}),
			'reason' : forms.Textarea(attrs={'class':'form-control'}),			
		}		