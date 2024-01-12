from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path("", views.ProdutoApiView.as_view()),
    path("familia/", views.FamiliaApiView.as_view()),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)