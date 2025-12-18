"""
URL configuration for laundry project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from laundry import views
from laundry.views import countriesData
from ourservice import views as service_views
from contactFrom import views as contact_views
from BlogArticles import views as blog_views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomePage),
    path('index.html', views.HomePage),  # Handle /index.html requests
    # Template files (match the original HTML filenames used in the template lython inks)
    path('about.html', views.AboutPage),
    path('service.html', views.ServicePage),
    path('pricing.html', views.PricingPage),
    path('blog.html', blog_views.get_blog_articles, name='blog_list'),
    path('blog/<int:article_id>/', blog_views.get_article_detail, name='article_detail'),
    path('single.html', views.SinglePage),
    path('contact.html', views.ContactPage),
    # Contact form submission
    path('submit-contact/', contact_views.submit_contact, name='submit_contact'),
    # Test email endpoint
    # Countries endpoints — accept both correct and misspelled paths, with and without trailing slash
    path('countries', countriesData, name='countries_no_slash'),
    path('countries/', countriesData, name='countries'),
    path('countreis', countriesData, name='countreis_no_slash'),
    path('countreis/', countriesData, name='countreis'),
    path('api/', include('product.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
