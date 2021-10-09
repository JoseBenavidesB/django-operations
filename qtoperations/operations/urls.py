from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='inicio'),
    path('empresas/', views.EmpresasListView.as_view(), name='empresas'),
    path('create-company/', views.EmpresasCreateView.as_view(), name='crear-empresa'),
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
    path('editcustomer/<int:pk>', views.CustomerUpdateView.as_view(), name='edit-customer'),
    path('editservices/<int:pk>', views.ServicesUpdateView.as_view(), name='edit-service'),
    path('editrequest/<int:pk>', views.SolicitudUpdateView.as_view(), name='edit-request'),
    path('editsurvey/<int:pk>', views.SurveyUpdateView.as_view(), name='edit-survey'),
    path('editreport/<int:pk>', views.ReportUpadateView.as_view(), name='edit-report'),
    path('editlevel/<int:pk>', views.LevelUpdateView.as_view(), name='edit-level'),
    path('editcadastral/<int:pk>', views.CadastralUpdateView.as_view(), name='edit-cadastral'),
    path('editreplant/<int:pk>', views.ReplantUpdateView.as_view(), name='edit-replant'),
    path('login/', views.LoginFormView.as_view(), name='login'),
    path('logout/', views.LogoutFormView.as_view(), name='logout'),
    path('<int:pk>', views.ReportDetailView.as_view(), name='detail'),
    path('<str:servicio>/<int:id>', views.complete_request, name='complete-request'),
    path('apt/create-correction', views.CorrectionCreateView.as_view(), name='create-correction'),
    path('apt/corrections', views.CorrectionListView.as_view(), name='corrections'),
    path('apt/correction/<int:pk>', views.CorreccionUpdateView.as_view(), name='edit-correction'),
    path('quote/create-quote', views.QuoteCreateView.as_view(), name='create-quote'),
    path('quote/list-quotes', views.QuoteListView.as_view(), name='quotes'),
    path('quote/edit-quote/<int:pk>', views.QuoteUpdateView.as_view(), name='edit-quotes'),
    path('payment/create-pay', views.PaymentCreateView.as_view(), name='create-pay'),
    path('payment/update-pay/<int:pk>', views.PaymentUpdateView.as_view(), name='update-pay'),
    path('payment/payments', views.PaymentListView.as_view(), name='payments'),
    path('preliminar/create-preliminary', views.PreliminaryCreateView.as_view(), name='create-preliminary'),
    path('preliminar/preliminaries', views.PreliminaryListView.as_view(), name='preliminaries'),
    path('preliminar/update/<int:pk>', views.PreliminaryUpdateView.as_view(), name='edit-preliminary'),
    
    
    




]
