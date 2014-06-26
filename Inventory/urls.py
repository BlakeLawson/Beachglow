from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'sales_record.views.display_results', name='results'),
    url(r'^chart/', 'chart_test.views.chart'),
    url(r'^admin/', include(admin.site.urls)),
)
