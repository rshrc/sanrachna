from django.contrib import admin
from prospect.models import Prospect


@admin.register(Prospect)
class ProspectAdmin(admin.ModelAdmin):
    model = Prospect

    class Meta:
        fields = [
            'full_name',
            'organization',
            'mobile_number',
            'email',
            'site_type',
            'source_type'
        ]
