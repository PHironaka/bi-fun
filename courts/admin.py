from django.contrib import admin
from .models import Court


class CourtAdmin(admin.ModelAdmin):
    list_display = ('title', 'location', 'location_map',)

    def location_map(self, instance):
        if instance.location is not None:
            return '<img src="http://maps.googleapis.com/maps/api/staticmap?center=%(latitude)s,%(longitude)s&zoom=%(zoom)s&size=%(width)sx%(height)s&maptype=roadmap&markers=%(latitude)s,%(longitude)s&sensor=false&visual_refresh=true&scale=%(scale)s" width="%(width)s" height="%(height)s">' % {
                'latitude': instance.location.latitude,
                'longitude': instance.location.longitude,
                'zoom': 15,
                'width': 100,
                'height': 100,
                'scale': 2
            }
    location_map.allow_tags = True


admin.site.register(Court, CourtAdmin)


