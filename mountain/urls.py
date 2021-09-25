from django.urls import path

from mountain.views import register, user_login, user_logout, HomeTrail, TrailsByDifficulty, ViewTrail, TrailDetailView, \
    TrailUpdateView, TrailDeleteView, TrailCreateView

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('', HomeTrail.as_view(), name='home'),
    path('difficulty/<int:difficulty_id>/', TrailsByDifficulty.as_view(), name='difficulty'),
    path('trail_list/<int:pk>/', ViewTrail.as_view(), name='trail_list'),
    path('trail_detail/<int:pk>/', TrailDetailView.as_view(), name='trail_detail'),
    path('trail_update_form/<int:pk>/', TrailUpdateView.as_view(), name='trail_update_form'),
    path('trail_check_delete/<int:pk>/', TrailDeleteView.as_view(), name='trail_check_delete'),
    path('trail_create_form/', TrailCreateView.as_view(), name='trail_create_form'),
    # path('trail_confirm_delete/', TrailDeleteView.as_view(), name='trail_confirm_delete'),
]
