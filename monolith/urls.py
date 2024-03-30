from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index_blank'),
    path('index.html', views.index, name='index'),

    path('buttons.html', views.buttons, name='buttons'),
    path('cards.html', views.cards, name='cards'),
    path('utilities-color.html', views.utilities_colors, name='utilities_colors'),
    path('utilities-border.html', views.utilities_border, name='utilities_border'),
    path('utilities-animation.html', views.utilities_animation, name='utilities_animation'),
    path('utilities-other.html', views.utilities_other, name='utilities_other'),

    path('login.html', views.login, name='login'),
    path('register.html', views.register, name='register'),
    path('forgot-password.html', views.forgot_password, name='forgot_password'),

    path('404.html', views.not_found, name='404'),
    path('blank.html', views.blank, name='blank'),

    path('charts.html', views.charts, name='charts'),
    path('tables.html', views.tables, name='tables'),
]
