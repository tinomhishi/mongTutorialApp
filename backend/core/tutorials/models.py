import uuid

from django.db import models

from users.models import User 
from core.model import BaseModel


class Tutorial(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField()
    is_published = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name="tutorials")
