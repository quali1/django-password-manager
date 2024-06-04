from celery import shared_task
from django.utils import timezone
from datetime import timedelta
from .models import UserProfileToken


@shared_task
def delete_token(token_id):
    try:
        token = UserProfileToken.objects.get(id=token_id)
        token.delete()
    except UserProfileToken.DoesNotExist:
        pass


@shared_task
def delete_expired_tokens():
    now = timezone.now()
    expiration_time = now - timedelta(minutes=30)
    UserProfileToken.objects.filter(created_at__lt=expiration_time).delete()
