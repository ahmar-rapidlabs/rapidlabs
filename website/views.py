# views.py

from django.core.mail import send_mail
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def send_email(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        # Extract form data
        company_name = data.get('companyName', '')
        host_email = data.get('email', '') 
        selected_categories = data.get('selectedCategories', [])
        additional_categories = data.get('additionalCategories', [])
        message = data.get('message', '')
        nl = '\n'
        
        # Compose email message
        email_message = f"Company Name: {company_name}\n"
        email_message += f"Email: {host_email}\n\n"
        email_message += "---------------------------------------------------------------\n"
        email_message += f"Services"
        email_message += "\n---------------------------------------------------------------\n"
        email_message += f"{nl.join(selected_categories)}{nl}"
        email_message += "---------------------------------------------------------------\n\n\n"

        email_message += "---------------------------------------------------------------\n"
        email_message += f"Additional Services - Timeline & Cost Information"
        email_message += "\n---------------------------------------------------------------\n"

        email_message += f"{nl.join(additional_categories)}{nl}"
        email_message += "---------------------------------------------------------------\n\n\n"
        email_message += f"Message: {message}\n"
        print(additional_categories)
        # Send email
        try:
            send_mail(
                'Testing. Please Dont reply',
                email_message,
                'contact@rapidlabs.ai', 
                # ['info@rapidlabs.ai', 'ahmaraamir33@gmail.com'],  
                ['ahmaraamir33@gmail.com'],
                fail_silently=False,
            )
            return JsonResponse({'message': 'Email sent successfully'})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)
