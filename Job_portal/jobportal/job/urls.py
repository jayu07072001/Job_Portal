from django.urls import path
from job import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('',views.home, name='home'),
    path('contact/',views.contact,name="contact"),
    path('about/',views.about,name='about'),
    path('user_login/',views.user_login,name='user_login'),
    path('recruiter_login/',views.recruiter_login,name='recruiter_login'),
    path('signup_jobseeker/',views.signup_jobseeker,name='signup_jobseeker'),
    path('signup_recruiter/',views.signup_recruiter,name='signup_recruiter'),
    path('user_home/',views.user_home,name='user_home'),
    path('user_about/',views.user_about,name='user_about'),
    path('user_contact/',views.user_contact,name='user_contact'),
    path('Logout/',views.Logout,name='Logout'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)