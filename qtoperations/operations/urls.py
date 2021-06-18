from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='inicio'),
    path('empresas/', views.EmpresasListView.as_view(), name='empresas'),
    path('crear-empresa/', views.EmpresasCreateView.as_view(), name='crear-empresa'),
    path('customers/', views.CustomerListView.as_view(), name='customers'),
    path('create-customer/', views.CustomerCreateView.as_view(), name='create-customer'),
    path('services/', views.ServicesListView.as_view(), name='services'),
    path('create-service/', views.ServicesCreateView.as_view(), name='create-service'),
    path('solicitud/', views.SolicitudListView.as_view(), name='solicitud'),
    path('create-request/', views.SolicitudCreateView.as_view(), name='create-request'),
    path('levantamientos/', views.SurveyListView.as_view(), name='levantamientos'),
    path('create-survey/', views.SurveyCreateView.as_view(), name='create-survey'),
    path('reports/', views.ReportListView.as_view(), name='reports'),
    path('create-report/', views.ReportCreateView.as_view(), name='create-report'),
    path('levels/', views.LevelListView.as_view(), name='levels'),
    path('create-level/', views.LevelCreateView.as_view(), name='create-level'),
    path('cadastral/', views.CadastralListView.as_view(), name='cadastral'),
    path('create-cadastral/', views.CadastralCreateView.as_view(), name='create-cadastral'),
    path('replant/', views.ReplantListView.as_view(), name='replant'),
    path('create-replant/', views.ReplantCreateView.as_view(), name='create-replant'),
    path('editcompany/<int:pk>', views.EmpresaUpdateView.as_view(), name='edit-company'),

]
