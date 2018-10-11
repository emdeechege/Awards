from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    url(r'^$', views.home,name='home'),
    url(r'^profile/(\d+)', views.profile, name='profile'),
    url(r'^new/profile$', views.add_profile, name='add_profile'),
    url(r'^upload/', views.update_project, name='upload'),
    url(r'^review/(?P<pk>\d+)',views.add_review,name='review'),
    url(r'^api/profiles/$', views.ProfileList.as_view()),
    url(r'^api/projects/$', views.ProjectList.as_view()),
    

]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
