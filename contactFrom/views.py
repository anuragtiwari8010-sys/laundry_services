from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from contactFrom.models import Contact


def submit_contact(request):
    if request.method == 'POST':
        try:
            name = request.POST.get('name')
            email = request.POST.get('email')
            subject = request.POST.get('subject')
            message_text = request.POST.get('message')
            attachment = request.FILES.get('attachment')
            
            # Validate form data
            if not all([name, email, subject, message_text]):
                if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                    return JsonResponse({
                        'success': False, 
                        'message': 'All fields are required!'
                    }, status=400)
                messages.error(request, 'All fields are required!')
                return redirect('contact.html')
            
            # Create and save the contact form data to database (include attachment if provided)
            contact = Contact.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=message_text,
                attachment=attachment
            )
            
            # Send email via SMTP Gmail
            try:
                email_subject = f"New Contact Form Submission: {subject}"
                email_body = f"""
New contact form submission:

Name: {name}
Email: {email}
Subject: {subject}

Message:
{message_text}
"""
                send_mail(
                    subject=email_subject,
                    message=email_body,
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[settings.EMAIL_HOST_USER],
                    fail_silently=False,
                )
            except Exception as email_error:
                # Log email error but don't fail the contact submission
                print(f"Email sending error: {str(email_error)}")
            
            # Return success response
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({
                    'success': True, 
                    'message': 'Thank you! Your message has been saved successfully. We will contact you soon!'
                })
            else:
                messages.success(request, 'Thank you! Your message has been saved successfully. We will contact you soon!')
                return redirect('contact.html')
                
        except Exception as e:
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({
                    'success': False, 
                    'message': f'Error: {str(e)}'
                }, status=500)
            messages.error(request, f'Error saving message: {str(e)}')
            return redirect('contact.html')
    
    return redirect('contact.html')
