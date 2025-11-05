from django.shortcuts import render
from .models import ContactMessage
from datetime import datetime

# Create your views here.
def contact_view(request):
    success = False
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        ContactMessage.objects.create(name = name, email = email, phone = phone, subject = subject, message = message)
        success = True

    # Add formatted_date to context so the navbar (shared template) can show the date like other pages
    today = datetime.now()
    formatted_date = today.strftime("%a. %d %b %Y")
    return render(request, 'contact.html', {'success': success, 'formatted_date': formatted_date})
