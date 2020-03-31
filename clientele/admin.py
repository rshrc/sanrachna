from django.contrib import admin
from clientele import models


@admin.register(models.Prospect)
class ProspectAdmin(admin.ModelAdmin):
    model = models.Prospect

    class Meta:
        fields = [
            'full_name'
            'organization'
            'email'
            'mobile_number'
            'site_type'
            'source_type'
        ]


@admin.register(models.Lead)
class LeadAdmin(ProspectAdmin):
    model = models.Lead

    class Meta:
        fields = [
            'full_name'
            'organization'
            'email'
            'mobile_number'
            'site_type'
            'source_type'
        ]


@admin.register(models.Client)
class ProspectAdmin(ProspectAdmin):
    model = models.Client

    class Meta:
        fields = [
            'full_name'
            'organization'
            'email'
            'mobile_number'
            'site_type'
            'source_type'
        ]
