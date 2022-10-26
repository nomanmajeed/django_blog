from django.urls import path

from .views import home

urlpatterns = [
    path('', home.home_page, name="home"),
    path('login/', home.login_view, name="login_view"),
    path('register/', home.register_view, name="register_view"),
    path('add-blog/', home.add_blog, name="add_blog"),
    path('blog-detail/<slug>', home.blog_detail, name="blog_detail"),
    path('see-blog/', home.see_blog, name="see_blog"),
    path('blog-delete/<id>', home.blog_delete, name="blog_delete"),
    path('blog-update/<slug>/', home.blog_update, name="blog_update"),
    path('logout-view/', home.logout_view, name="logout_view"),
    # path('verify/<token>/', home.verify, name="verify")
]