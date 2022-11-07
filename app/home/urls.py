from django.urls import path

from .views import home, blog

urlpatterns = [
    path('', home.home_page, name="home"),
    path('login/', home.login_view, name="login_view"),
    path('register/', home.register_view, name="register_view"),
    path('add-blog/', blog.add_blog, name="add_blog"),
    path('blog-detail/<slug>', blog.blog_detail, name="blog_detail"),
    path('see-blog/', blog.see_blog, name="see_blog"),
    path('blog-delete/<id>', blog.blog_delete, name="blog_delete"),
    path('blog-update/<slug>/', blog.blog_update, name="blog_update"),
    path('logout-view/', home.logout_view, name="logout_view"),
    path('verify/<token>/', home.verify, name="verify")
]