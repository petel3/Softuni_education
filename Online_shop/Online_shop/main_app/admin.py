from django.contrib import admin

from Online_shop.main_app.models import Plant, Flower, Souvenir, Jewelry, AskQuotation


@admin.register(Plant)
class PlantsAdmin(admin.ModelAdmin):
    list_display = ('name', 'type')


@admin.register(Flower)
class FlowersAdmin(admin.ModelAdmin):
    list_display = ('name', 'type')


@admin.register(Souvenir)
class SouvenirsAdmin(admin.ModelAdmin):
    list_display = ('name', 'type')


@admin.register(Jewelry)
class JewelsAdmin(admin.ModelAdmin):
    list_display = ('name', 'materials')

@admin.register(AskQuotation)
class AskQuotationAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'email_to_contact','user_key')
