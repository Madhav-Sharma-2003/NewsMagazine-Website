from datetime import datetime
from django.shortcuts import render
from .models import ContactMessage
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

def contact_view(request):

    msg = ''

    # Ensure formatted_date is always available for the template/navbar
    today = datetime.now()
    formatted_date = today.strftime("%a. %d %b %Y")

    if request.method == "POST":
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        subject = request.POST.get('subject', '').strip()
        message = request.POST.get('message', '').strip()
        phone = request.POST.get('phone', '').strip()

    # Save the contact message
        ContactMessage.objects.create(
        name=name,
        email=email,
        phone=phone,
        subject=subject,
        message=message
    )
        msg = 'Your message has been sent successfully.'

        # Email Content
        subject_body = f"Thank You for Contacting Us {subject}"

        # render HTML email from template and create plain-text fallback
        user_html = render_to_string('email_template.html', {
            'name': name,
            'email': email,
            'subject': subject,
            'message': message,
        })
        user_plain = strip_tags(user_html)

        send_mail(
            subject= subject_body,
            message= user_plain,
            from_email= 'madhavsharma88042@gmail.com',
            recipient_list= [email],
            fail_silently= False,
            html_message=user_html,
        )

        admin_subject = f"New Contact Form Submission from {name}"
        admin_message = (
            f"New message recieved from contact form :\n\n"
            f"Name : {name}\n"
            f"Email : {email}\n"
            f"Subject: {subject}\n"
            f"Message : {message}\n"
        )

        # send admin email also as HTML (reuse template or create a simple admin view)
        admin_html = render_to_string('email_template.html', {
            'name': name,
            'email': email,
            'subject': subject,
            'message': message,
        })
        admin_plain = strip_tags(admin_html)

        send_mail(
            subject = admin_subject,
            message = admin_plain,
            from_email = 'madhavsharma88042@gmail.com',
            recipient_list= ['madhavsharma88041@gmail.com'],
            fail_silently= False,
            html_message=admin_html,
        )
    return render(request, 'contact.html', {'msg': msg, 'formatted_date': formatted_date})