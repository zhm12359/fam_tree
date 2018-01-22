from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.IndexView, name='index'),
    url('import', views.ImportView, name='import'),
    url('BigTreeView', views.BigTreeView, name='bigtreeview'),
    url('assign', views.AssignView, name='assign'),


]