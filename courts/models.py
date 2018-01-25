from __future__ import unicode_literals


from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse
from django.db.models.signals import pre_save, post_save
from django.utils import timezone
from django.utils.safestring import mark_safe
from django.utils.text import slugify
from django.contrib.contenttypes.models import ContentType
from geoposition.fields import GeopositionField


class CourtManager(models.Manager):
    def active(self, *args, **kwargs):
        # Post.objects.all() = super(PostManager, self).all()
        return super(CourtManager, self).filter(draft=False).filter(publish__lte=timezone.now())


def upload_location(instance, filename):
    #filebase, extension = filename.split(".")
    #return "%s/%s.%s" %(instance.id, instance.id, extension)
    CourtModel = instance.__class__
    new_id = CourtModel.objects.order_by("id").last().id + 1
    """
    instance.__class__ gets the model Post. We must use this method because the model is defined below.
    Then create a queryset ordered by the "id"s of each object, 
    Then we get the last object in the queryset with `.last()`
    Which will give us the most recently created Model instance
    We add 1 to it, so we get what should be the same id as the the post we are creating.
    """
    return "%s/%s" %(new_id, filename)


# Create your models here.
class Court(models.Model):
    # Regular Django fields corresponding to the attributes in the
    # world borders shapefile.
    title = models.CharField(max_length=50)   
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1) 
    slug = models.SlugField(unique=True, default="")
    image = models.ImageField(upload_to=upload_location, 
        null=True, 
        blank=True, 
        width_field="width_field", 
        height_field="height_field")
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    content = models.CharField(max_length=140, default='SOME STRING')
    address = models.CharField(max_length=255)
    location = GeopositionField(blank=True)

    # Returns the string representation of the model.
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("courts:detail", kwargs={"slug": self.slug})



    @property
    def get_content_type(self):
        instance = self
        content_type = ContentType.objects.get_for_model(instance.__class__)
        return content_type    
            

def create_slug(instance, new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = Court.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug    

def pre_save_court_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)



pre_save.connect(pre_save_court_receiver, sender=Court)        