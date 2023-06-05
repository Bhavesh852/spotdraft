from .views import *
from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', index),
    path('home/', home),
    path('login/', LoginAPI.as_view()),
    path('logout/', LogoutAPI.as_view()),
    path('register/', RegisterAPI.as_view()),
    path('upload_pdf/', UploadPdf.as_view()),
    path('dashboard/', dashboard),
    path('comments/<int:pk>', comments),
    path('upload_comment/<int:pk>', UploadComment.as_view()),
    # path('homes/delete/<int:id>', delete_home),
    # path('homes/edit/<int:id>', edit_home),
    # path('homes/update/<int:id>', update_home),
    # path('homes/add', add_homes),

    path('reset_password/', 
		auth_views.PasswordResetView.as_view(template_name='user_auth/password_reset.html'),
		name='reset_password'),

	path('reset_password_sent/', 
		auth_views.PasswordResetDoneView.as_view(template_name='user_auth/password_reset_done.html'), 
		name='password_reset_done'),
	
	path('reset/<uidb64>/<token>/', 
		auth_views.PasswordResetConfirmView.as_view(template_name='user_auth/password_reset_confirm.html'), 
		name='password_reset_confirm'),
	
	path('reset_password_complete/', 
		auth_views.PasswordResetCompleteView.as_view(template_name='user_auth/password_reset_complete.html'), 
		name='password_reset_complete'),
]