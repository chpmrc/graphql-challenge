from django.contrib import admin

from celebrityshop.honey.models import Costume, Celebrity


class CostumeAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'visibility', 'get_all_celebrities')
    list_filter = ('name', 'visibility')

    def get_all_celebrities(self, obj):
        return ', '.join([i.name for i in obj.celebrities.all()])
    get_all_celebrities.short_description = 'Celebrities'


class CelebrityAdmin(admin.ModelAdmin):
    list_display = ('name', 'age',)
    list_filter = ('name',)


admin.site.register(Costume, CostumeAdmin)
admin.site.register(Celebrity, CelebrityAdmin)