from django.urls import path
# from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path('application', views.ApplicationView.as_view(template_name='application.html'), name = 'application-page'),
    path('', views.index, name = 'index'),
    path('clubs', views.clubs, name = 'clubs-page')
]