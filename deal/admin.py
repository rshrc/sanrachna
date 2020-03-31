# from django.contrib import admin
# from deal.models import Material, Service, Associate, Prospect
#
#
# @admin.register(Prospect)
# class ProspectAdmin(admin.ModelAdmin):
#     model = Prospect
#     list_display = [
#         'user',
#         'organization',
#         'email',
#         'site_type',
#         'source_type',
#     ]
#
#
# @admin.register(Material)
# class MaterialAdmin(admin.ModelAdmin):
#     model = Material
#     list_display = [
#         'brand_name',
#         'material_name',
#         'type',
#         'unit',
#         'rate',
#         'description',
#     ]
#
#
# @admin.register(Service)
# class ServiceAdmin(admin.ModelAdmin):
#     model = Service
#     list_display = [
#         'type',
#         'service_name',
#         'description',
#         'rate_of_service',
#     ]
#
#
# @admin.register(Associate)
# class Associate(admin.ModelAdmin):
#     model = Associate
#     list_display = [
#         'user',
#         'type'
#     ]
