from django.urls import URLPattern, path
import back.views

urlpatterns=[
    path('',back.views.login, name='login'),
    path('leave_register',back.views.leave_register, name='leave_register'),
    path('leave_approves',back.views.leave_approves,name='leave_approves')
]