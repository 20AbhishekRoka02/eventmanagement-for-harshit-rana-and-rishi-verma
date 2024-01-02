from django.db import models
import uuid
# Create your models here.
class Contact(models.Model): 
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField("name",max_length=255,default="user")
    email = models.EmailField("email")
    phone = models.CharField("phone number",max_length=10,default=None, null=True)
    subject = models.CharField("subject", max_length=40, default="subject")
    message = models.TextField()
    # password = models.CharField("password", max_length=255,default=None, null=True)
    # is_admin = models.BooleanField("is admin", default=False)
    
    def save(self, *args, **kwargs):
        # Call the parent class's save method to perform the actual save operation
        super().save(*args, **kwargs)

        # Access the user ID after saving
        contact_id = self.id
        return str(contact_id)

    def __str__(self):
        return str(self.id)
    
    class Meta:
        verbose_name = "contact"
        verbose_name_plural = "contacts"
    


