from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.contrib import admin

schema_view = get_schema_view(
    openapi.Info(
        title="Your API",
        default_version='v1',
        description="API documentation",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@yourapi.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('admin/', admin.site.urls, name='django_admin_page'),
    path('api/v1/login/', include('login.urls'), name='login'),
    path('api/v1/admin/', include('admin_page.urls'), name='admin'),
    path('api/v1/authors/', include('authors.urls'), name='authors'),
    path('api/v1/books/', include('books.urls'), name='books'),
    path('api/v1/borrow/', include('borrows.urls'), name='borrow'),
    path('api/v1/reservation/', include('reservations.urls'), name='reservation'),
    path('api/v1/search/', include('search.urls'), name='search'),
    path('api/v1/profile/', include('user_profile.urls'), name='user_profile'),
    path('api/v1/review/', include('reviews.urls'), name='reviews_and_ratings')
]
