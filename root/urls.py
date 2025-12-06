from django.urls import path, include
from . import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from .views import newsletter_view


app_name = 'root'

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path('blog/', include(('blog.urls', 'blog'), namespace='blog')),
    path('newsletter', newsletter_view, name = 'newsletter')
]

# برای توسعه محلی
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
