from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from .forms import ContactForm
from django.contrib import messages
from django.core.mail import send_mail
from .models import *

def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

def appoinment(request):
    return render(request, 'main/appoinment.html')

def blogsidebar(request):
    return render(request, 'main/blog-sidebar.html')

def blogsingle(request):
    return render(request, 'main/blog-single.html')

def confirmation(request):
    return render(request, 'main/confirmation.html')

def contact(request):
    return render(request, 'main/contact.html')

def departmentsingle(request):
    return render(request, 'main/department-single.html')

def department(request):
    return render(request, 'main/department.html')

def doctorsingle(request):
    return render(request, 'main/doctor-single.html')

def doctor(request):
    return render(request, 'main/doctor.html')

def group_topic_contents(contents):
    grouped = []
    point_group = []
    for content in contents:
        if content.content_type == 'point':
            point_group.append(content)
        else:
            if point_group:
                grouped.append({'type': 'point_group', 'items': point_group})
                point_group = []
            grouped.append({'type': content.content_type, 'item': content})
    if point_group:
        grouped.append({'type': 'point_group', 'items': point_group})
    return grouped

def service(request):
    services = Service.objects.all()  # fetch all service objects from DB
    return render(request, 'main/service.html', {'services': services})

def service_detail(request, slug):
    service = get_object_or_404(Service, slug=slug)
    topics = service.topics.all()

    # Group contents as before
    topics_with_grouped_contents = []
    for topic in topics:
        ordered_contents = topic.contents.all().order_by('order')
        grouped_contents = group_topic_contents(ordered_contents)
        topics_with_grouped_contents.append({
            'topic': topic,
            'grouped_contents': grouped_contents,
        })

    # Fetch FAQs related to this service
    faqs = service.faqs.all()  # related_name in FAQ model

    context = {
        'service': service,
        'topics_with_grouped_contents': topics_with_grouped_contents,
        'faqs': faqs,
    }

    return render(request, 'main/service_detail.html', context)

# def map_view(request):
#     return render(request, 'map_template.html', {
#         'google_maps_api_key': settings.GOOGLE_MAPS_API_KEY,
#     })



def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_instance = form.save()  # Save to DB

            # Prepare email content
            subject = f"Contact Form Submission from {contact_instance.name}"
            message = (
                f"Name: {contact_instance.name}\n"
                f"Email: {contact_instance.email}\n"
                f"Phone: {contact_instance.phone}\n"
                f"Department: {contact_instance.department}\n"
                f"Message: {contact_instance.message}\n"
                f"Submitted at: {contact_instance.submitted_at.strftime('%Y-%m-%d %H:%M')}"
            )

            send_mail(
                subject,
                message,
                settings.DEFAULT_FROM_EMAIL,
                [settings.ADMIN_EMAIL],
                fail_silently=False,
                reply_to=[contact_instance.email]
            )

            messages.success(request, "Thank you for contacting us! We will get back to you soon.")
            return redirect('suryaa_app:appoinment')
    else:
        form = ContactForm()
    return render(request, 'index.html', {'form': form})