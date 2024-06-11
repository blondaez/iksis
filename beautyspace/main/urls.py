from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='home'),
    path('blog/', views.blog, name='blog'),
    path('blog_entry/', views.blog_entry, name='blog_entry'),
    path('inject/', views.inject, name='inject'),
    path('estet/', views.estet, name='estet'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('user_profile/', views.user_profile, name='user_profile'),
    path('admin_profile/', views.admin_profile, name='admin_profile'),
    path('profile_info/', views.profile_info, name='profile_info'),
    path('service_new/', views.service_new, name='service_new'),
    path('record_new/', views.record_new, name='record_new'),
    path('records_free/', views.records_free, name='records_free'),
    path('book_record/<int:record_id>/', views.book_record, name='book_record'),
    path('records_response/', views.records_response, name='records_response'),
    path('book_response_record/<int:record_id>/', views.book_response_record, name='book_response_record'),
    path('records_today/', views.records_today, name='records_today'),
    path('complete_record/<int:record_id>/', views.complete_record, name='complete_record'),
    path('cancel_record/<int:record_id>/', views.cancel_record, name='cancel_record'),
    path('records_all/', views.records_all, name='records_all'),
    path('cancel_record_all/<int:record_id>/', views.cancel_record_all, name='cancel_record_all'),
    path('blog_new/', views.blog_new, name='blog_new'),
    path('blog_entry/', views.blog_entry, name='blog_entry'),
    path('blog/', views.blog, name='blog'),
    path('blog/<int:id>/', views.blog_detail, name='blog_detail')
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
