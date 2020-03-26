from django.shortcuts import render, redirect
from django.core.mail import send_mail

# Create your views here.
def home(request):
	return render(request, 'home.html', {})

def about(request):
	return render(request, 'about.html', {})

def service(request):
	return render(request, 'service.html', {})

def pricing(request):
	return render(request, 'pricing.html', {})

def contact(request):
	if request.method == 'POST':
		message_name = request.POST['message-name']
		message_email = request.POST['message-email']
		message = request.POST['message']

		message += '\n\nReplay to me at: ' +message_email
		# send an email
		''' send_mail(
			'Message From ' + message_name,	# subject
			message,						# message
			message_email,					# from email
			['to_email@gmail.com'],			# to email
		) '''

		return render(request, 'contact.html', {
			'message_name': message_name
		})

	return render(request, 'contact.html', {})

def appointment(request):
	if request.method == 'POST':
		your_name = request.POST['your-name']
		your_phone = request.POST['your-phone']
		your_email = request.POST['your-email']
		your_address = request.POST['your-address']
		your_schedule = request.POST['your-schedule']
		your_date = request.POST['your-date']
		your_message = request.POST['your-message']

		message = your_message + '\n\n'
		message += 'This is my information:\n'
		message += '\tName: ' + your_name + '\n'
		message += '\tPhone: ' + your_phone + '\n'
		message += '\tAddress: ' + your_address + '\n'
		message += '\tDate: ' + your_date + '\n'
		message += '\tSchedule: ' + your_schedule
		message += '\n\nReplay to me at: ' +your_email
		# send an email
		''' send_mail(
			'Appointment Request',		# subject
			message,					# message
			your_email,					# from email
			['to_email@gmail.com'],		# to email
		) '''

		return render(request, 'appointment.html', {
			'your_name': your_name,
			'your_phone': your_phone,
			'your_email': your_email,
			'your_address': your_address,
			'your_schedule': your_schedule,
			'your_date': your_date,
			'your_message': your_message
		})

	return redirect(home)
