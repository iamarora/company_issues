from django.contrib.auth.models import User, Group
from django.contrib import admin
from djangoapp.models import Companies


class CompaniesAdmin(admin.ModelAdmin):
    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def no_of_issues(self, obj):
        no_of_issues = 0
        for k in self.list_filter:
            if getattr(obj, k) is True:
                no_of_issues += 1
        return no_of_issues

    def issues(self, obj):
        issues = []
        for k in self.list_filter:
            if getattr(obj, k) is True:
                issues.append(' '.join(k.split('_')).title())
        return ', '.join(issues)

    list_display  = (
        'name', 'ticker_symbol', 'issues', 'no_of_issues'
    )
    list_filter  = (
        'animal_testing', 'nuclear_weapons', 'coal_power', 'rainforest_destruction'
    )
    search_fields = ('name', 'ticker_symbol')


# Register your models here.
admin.site.register(Companies, CompaniesAdmin)


# De-Register models not required.
admin.site.unregister(Group)
admin.site.unregister(User)
