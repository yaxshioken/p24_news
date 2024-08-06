from django.db.models import TextChoices
class Choices(TextChoices):
    DRAFT="df","DRAFT"
    PUBLISHED="pb","PUBLISHED"
    