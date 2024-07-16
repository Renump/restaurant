from django.urls import path ,include
from django.conf import settings
from django.conf.urls.static import static
from myapp import views


urlpatterns = [
    path('',views.home,name='home'),
path('',views.about,name='about'),
path('',views.menu,name='menu'),
path('',views.review,name='review'),
path('',views.downloadapp,name='downloadapp'),
    path('register/',views.RegistrationView.as_view(),name='signup'),
    path('login/',views.LoginView.as_view(),name='signin'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)