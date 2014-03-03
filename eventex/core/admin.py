from django.contrib import admin
from eventex.core.models import Speaker, Contact

class ContactInline(admin.TabularInline):
	model = Contact
	extra = 1

class SpeakerAdmin(admin.ModelAdmin):
	inlines = [ContactInline,]
	prepopulated_fields = {'slug': ('name',)}#garante o preenchimento automatico do slug, baseado no nome digitado
	
admin.site.register(Speaker, SpeakerAdmin)
