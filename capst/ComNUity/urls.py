from django.urls import path,include
from django.contrib.auth.views import LogoutView
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


from . import views
urlpatterns = [
    path('', views.index),
    path('home/' ,views.home,name="home"),
    path('dash/',views.dash,name="dash"),
    path('accounts/', include('allauth.urls')),
    path('logout/',LogoutView.as_view()),
    path('admin/', admin.site.urls),
    #path('', views.signIn),
    path('postsignIn/', views.postsignIn),
    path('signUp/', views.signUp, name="signup"),
    path('logout/', views.logout, name="log"),
    path('postsignUp/', views.postsignUp),
    path('profile/', views.profile,name="profile"),
    path('createprofile/', views.createprofile),
    path('showprofile/', views.showprofile, name="showprofile"),
    path('edprofile/',views.edprofile,name="edprofile"),
    path('editprofile/',views.editprofile,name="editprofile"),
    path('createblog/',views.createblog, name="createblog"),
    path('addblog/',views.addblog, name="addblog"),
    path('makeblog/',views.makeblog)
   

]+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)

