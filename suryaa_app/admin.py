from django.contrib import admin
from .models import Contact, Service, Topic, TopicContent, FAQ

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('s_no', 'name', 'email', 'phone', 'department', 'submitted_at')
    list_filter = ('department', 'submitted_at')
    search_fields = ('name', 'email', 'phone')
    ordering = ('id',)  # Order by serial number ascending (id)
    date_hierarchy = 'submitted_at'  # Adds calendar filter bar on top

    def s_no(self, obj):
        return obj.id
    s_no.short_description = 'S.No'
    s_no.admin_order_field = 'id'


class TopicContentInline(admin.TabularInline):
    model = TopicContent
    extra = 1


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    inlines = [TopicContentInline]
    list_display = ('s_no', 'title', 'service', 'created_at', 'modified_at')
    search_fields = ('title', 'service__title')
    list_filter = ('created_at', 'modified_at', 'service')
    ordering = ('id',)  # Order by serial number ascending (id)
    date_hierarchy = 'created_at'  # Calendar filter on created_at

    def s_no(self, obj):
        return obj.id
    s_no.short_description = 'S.No'
    s_no.admin_order_field = 'id'


class TopicInline(admin.TabularInline):
    model = Topic
    extra = 1


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('s_no', 'title', 'slug', 'created_at', 'modified_at')
    search_fields = ('title',)
    list_filter = ('created_at', 'modified_at')
    ordering = ('id',)  # Order by serial number ascending (id)
    inlines = [TopicInline]
    date_hierarchy = 'created_at'  # Calendar filter on created_at

    def s_no(self, obj):
        return obj.id
    s_no.short_description = 'S.No'
    s_no.admin_order_field = 'id'


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'service', 'order')
    list_filter = ('service',)
    search_fields = ('question', 'answer')
    ordering = ('order',)