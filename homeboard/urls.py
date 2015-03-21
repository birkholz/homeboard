from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework import routers

from home import views as home_views
from chores import views as chores_views
from chat import views as chat_views


router = routers.DefaultRouter()
# Home
router.register(r'users', home_views.UserViewSet)
router.register(r'homes', home_views.HomeViewSet)
router.register(r'members', home_views.MemberViewSet)
# Chores
router.register(r'chores', chores_views.ChoreViewSet)
router.register(r'assignments', chores_views.AssignmentViewSet)
# Chat
router.register(r'messages', chat_views.MessageViewSet)


urlpatterns = patterns('',
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^docs/', include('rest_framework_swagger.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
