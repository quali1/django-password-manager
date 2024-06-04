from celery import shared_task
from django.utils import timezone
from datetime import timedelta
from .models import UserProfileToken


@shared_task
def delete_expired_tokens():
    expiration_time = timezone.now() - timedelta(minutes=30)
    UserProfileToken.objects.filter(created_at__lt=expiration_time).delete()
