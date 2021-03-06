from django import forms

from .models import doctor_checkup
from initializer.models import qr_map

class DoctorCheckupForm(forms.ModelForm):
	unique_num = forms.CharField(widget = forms.HiddenInput())

	class Meta:
		model = doctor_checkup
		fields = ['prescription',
				  'comments',
				  'temperature',
				  'bp_systolic',
				  'bp_diastolic',
				  'height',
				  'weight']

		labels = {
			'prescription': 'Prescriptions',
			'bp_systolic': 	'Blood Pressure (systolic)',
			'bp_diastolic': 'Blood Pressure (diastolic)',
			'height':		'Height (in centimeters)',
			'weight':		'weight (in kilograms)'
		}
		
	def clean_unique_num(self):
		unique_num = self.cleaned_data['unique_num']
		try:
			print(unique_num[:-1])
			qr_map.objects.get(unique_num__startswith=unique_num[:-1])
			return unique_num
		except:
			raise forms.ValidationError('Unique number %s does not exist'%(unique_num))
