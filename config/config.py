from rest_framework import serializers

MATERIAL_TYPES = (
    ('CHEAP', 'CHEAP'),
    ('EXPENSIVE', 'EXPENSIVE')
)

SERVICE_TYPES = (
    ('CHEAP', 'CHEAP'),
    ('EXPENSIVE', 'EXPENSIVE')
)

ASSOCIATE_TYPES = (
    ('SUPERVISOR', 'SUPERVISOR'),
    ('VENDOR', 'VENDOR'),
    ('LABOR', 'LABOR'),
)

SITE_TYPES = (
    ('COMMERCIAL', 'COMMERCIAL'),
    ('OFFICE', 'OFFICE'),
    ('HOME', 'HOME')
)

SOURCE_TYPES = (
    ('ONLINE', 'ONLINE'),
    ('OFFLINE', 'OFFLINE'),
)

PROSPECT_TYPES = (
    ('LEAD', 'LEAD'),
    ('CLIENT', 'CLIENT'),
    ('CANCEL', 'CANCEL'),
)

MATERIAL_FIELDS = ['id', 'sno', 'particulars', 'quantity', 'unit', 'rate', 'prospect']
SERVICE_FIELDS = ['id', 'name', 'unit', 'rate', 'prospect']
PROSPECT_FIELDS = ['id', 'full_name', 'organization', 'email', 'mobile_number', 'site_type', 'source_type']
ASSOCIATE_FIELDS = ('id', 'full_name', 'organization', 'mobile_number', 'email')
