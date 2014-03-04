from django.contrib import admin
from eventex.core.models import Speaker, Contact, Talk

class ContactInline(admin.TabularInline):
	model = Contact
	extra = 1#abre sempre com 1 linha para trabalhar. Se quiser iniciar com 5, basta por 5 no value

class SpeakerAdmin(admin.ModelAdmin):
	inlines = [ContactInline,]
	prepopulated_fields = {'slug': ('name',)}#garante o preenchimento automatico do slug, baseado no nome digitado
	
admin.site.register(Speaker, SpeakerAdmin)
admin.site.register(Talk)