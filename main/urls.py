from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('about/', views.about, name='about'),
    path('property/', views.proPerty, name="property"),
    path('property_single', views.property, name="propertySingle"),
    path('agents/', views.agent, name="agents"),
    path('agents_single/', views.agentSingle, name="agentSinge"),
    path('blog/', views.blog, name="blog"),
    path('blog_single/', views.blogSingle, name="blogSingle"),
    path('contact/', views.contact, name="contact"),
]