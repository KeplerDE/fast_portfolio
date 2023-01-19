from django.urls import path

from . import views

app = "portfolio"


urlpatterns = [

    path("", views.index, name="index"),
    # path("projects", views.projects, name="projects"),
    # path("experiences", views.experiences, name="services"),
    path("blogs", views.blogs, name="blogs"),
    path("contact", views.contact, name="contact")

]