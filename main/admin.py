from django.contrib import admin
from .models import AdvUser, Review, Contacts, Feedback, Sale, Masters

admin.site.register(AdvUser)


class AdminReview(admin.ModelAdmin):
    list_display = ['name', 'done', 'age', 'created', 'email', 'tel', 'review', 'slug', 'image']
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ['created', ]
    list_editable = ('done',)


admin.site.register(Review, AdminReview)


class AdminContacts(admin.ModelAdmin):
    list_display = ['name', 'address', 'tel', 'social', 'email', 'contact', 'image', 'slug']
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ['name', ]


admin.site.register(Contacts, AdminContacts)


class AdminFeedback(admin.ModelAdmin):
    list_display = ["name", "tel", "email", "theme", "contact", 'slug']
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ['id', ]


admin.site.register(Feedback, AdminFeedback)


class AdminSale(admin.ModelAdmin):
    list_display = ["name", "percentage", "word", "comment", "image", 'tag', 'slug']
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ['id', ]


admin.site.register(Sale, AdminSale)


class AdminMasters(admin.ModelAdmin):
    list_display = ["name", "comment", 'tag', 'slug', 'photo1', 'diploma1', 'diploma2', 'diploma3', 'diploma4',
                    'example1', 'example2', 'example3', 'example4']
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ['id', ]


admin.site.register(Masters, AdminMasters)