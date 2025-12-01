from datetime import datetime
from django.shortcuts import render
from .models import ContactMessage
from django.core.mail import send_mail, EmailMultiAlternatives
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
        contact_message = ContactMessage(
            name=name,
            email=email,
            subject=subject,
            message=message,
            phone=phone
        )
        contact_message.save()
        msg = 'Your message has been sent successfully.'

        # Email Content
        subject_body = f"Thank You for Contacting Us {subject}"

        # render HTML email from template and create plain-text fallback
        html_content = render_to_string('email_template.html', {
            'name': name,
            'email': email,
            'subject': subject,
            'message': message,
        })
        text_content = (
            f"Dear {name},\n\n"
            f"Thank you for reaching out to us regarding '{subject}'. We have received your message and will get back to you shortly.\n\n"
            f"Best regards,\n"
            f"NewsMagazine Team"
        )
            # send email to user
        emails = EmailMultiAlternatives(
            subject=subject_body,
            body=text_content,
            from_email='madhavsharma88042@gmail.com',
            to=[email],
        )
        emails.attach_alternative(html_content, "text/html")
        emails.send(fail_silently=False)
        # send email to admin
        admin_subject = f"New Contact Form Submission from {name}"
        admin_message = (
            f"New message recieved from contact form :\n\n"
            f"Name : {name}\n"
            f"Email : {email}\n"
            f"Subject: {subject}\n"
            f"Phone: {phone}\n"
            f"Message : {message}\n"
        )

        # send admin email also as HTML (reuse template or create a simple admin view)
        admin_email = EmailMultiAlternatives(
            subject=admin_subject,
            body=admin_message,
            from_email='madhavsharma88042@gmail.com',
            to=['madhavsharma88041@gmail.com'],
        )
        admin_email.send(fail_silently=False)
    return render(request, 'contact.html', {'msg': msg, 'date': formatted_date})