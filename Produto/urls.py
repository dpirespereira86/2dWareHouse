from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views
from rest_framework.routers import SimpleRouter

router_produto = SimpleRouter()
router_produto.register('',views.ProdutoViewSet)
router_produto.register('familia',views.FamiliaViewSet)

urlpatterns = [

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)