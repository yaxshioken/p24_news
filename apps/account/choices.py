from django.db.models import TextChoices
class RoleChoices(TextChoices):
    PUBLISHER='pb','Publisher',
    WRITER='wr','WRITER',
    MEMBER='mb','Member',
