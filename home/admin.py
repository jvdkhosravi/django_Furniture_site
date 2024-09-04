from django.contrib import admin

from home.models import NewsletterSubscription, Testimonial, WhyChooseUs, WhyChooseUsImage, WeHelpSection


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('quote', 'author_name', 'author_title')
    search_fields = ('quote', 'author_name', 'author_title')
    list_filter = ('author_title',)
    readonly_fields = ('id',)
    fieldsets = (
        (None, {
            'fields': ('quote', 'author_name', 'author_title', 'author_image')
        }),
    )
    # Customize the actions dropdown menu
    actions = ['delete_selected']

    def delete_selected(self, request, queryset):
        for obj in queryset:
            obj.delete()

    delete_selected.short_description = "حذف گزینه های انتخاب شده"


@admin.register(NewsletterSubscription)
class NewsletterSubscriptionAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subscribed_at')
    search_fields = ('name', 'email')
    list_filter = ('subscribed_at',)
    readonly_fields = ('id', 'subscribed_at')
    fieldsets = (
        (None, {
            'fields': ('name', 'email')
        }),
    )
    # Customize the actions dropdown menu
    actions = ['delete_selected', 'export_as_csv']

    def delete_selected(self, request, queryset):
        for obj in queryset:
            obj.delete()

    delete_selected.short_description = "حذف گزینه های انتخاب شده"

    def export_as_csv(self, request, queryset):
        import csv
        from django.http import HttpResponse

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="newsletter_subscriptions.csv"'

        writer = csv.writer(response)
        writer.writerow(['Name', 'Email', 'Subscribed At'])

        for obj in queryset:
            writer.writerow([obj.name, obj.email, obj.subscribed_at])

        return response

    export_as_csv.short_description = "خروجی csv برای گزینه های انتخاب شده"


@admin.register(WhyChooseUs)
class WhyChooseUsAdmin(admin.ModelAdmin):
    list_display = ('title', 'ordering')
    search_fields = ('title',)
    list_editable = ('ordering',)
    fieldsets = (
        (None, {
            'fields': ('icon', 'title', 'description', 'ordering')
        }),
    )


@admin.register(WhyChooseUsImage)
class WhyChooseUsImageAdmin(admin.ModelAdmin):
    list_display = ('alt_text',)
    search_fields = ('alt_text',)
    fieldsets = (
        (None, {
            'fields': ('image', 'alt_text')
        }),
    )


@admin.register(WeHelpSection)
class WeHelpSectionAdmin(admin.ModelAdmin):
    list_display = ('title',)
    fieldsets = (
        (None, {
            'fields': (
                'grid_1_image', 'grid_2_image', 'grid_3_image', 'title', 'description', 'list_item_1', 'list_item_2',
                'list_item_3', 'list_item_4')
        }),
    )
