from django.db import models
from django.urls import reverse

class Contact(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    phone = models.CharField(max_length=15, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    department = models.CharField(
        max_length=20,
        choices=[
            ('Cardio', 'Cardio'),
            ('Neurology', 'Neurology'),
            ('Gynacology', 'Gynacology'),
        ],
        null=False,
        blank=False
    )
    message = models.TextField(blank=True)  # optional field

    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"
    


class Service(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, blank=True, null=True)
    image = models.ImageField(upload_to='service_images/', blank=True, null=True)
    image_url = models.URLField(blank=True, null=True)
    short_description = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('service_detail', args=[str(self.id)])

    @property
    def image_or_url(self):
        if self.image:
            return self.image.url
        return self.image_url

class Topic(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='topics')
    title = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class TopicContent(models.Model):
    CONTENT_TYPES = (
        ('para', 'Paragraph'),
        ('point', 'Point'),
        ('image', 'Image'),
        ('subtopic', 'Subtopic'),
    )
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='contents')
    content_type = models.CharField(max_length=10, choices=CONTENT_TYPES)
    text = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='topic_contents/', blank=True, null=True)
    image_or_url = models.URLField(max_length=500, blank=True, null=True)  # Added field for external URLs
    order = models.PositiveIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.content_type} for {self.topic.title}"
    

class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()
    service = models.ForeignKey('Service', on_delete=models.CASCADE, related_name='faqs')
    order = models.PositiveIntegerField(default=0)  # to control FAQ display order

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order', 'created_at']

    def __str__(self):
        return self.question