
from django.urls import path
from . import views
from django.views.generic.base import RedirectView

urlpatterns = [
    path('', views.index, name='index'),
    path('index.html', RedirectView.as_view(url='/', permanent=False), name='index1'),
    path('index.php', RedirectView.as_view(url='/', permanent=False), name='index2'),
    path('catalog/', views.catalog, name='catalog'),
    path('catalog/<cat_slug>/', views.catalog_inner, name='catalog_inner'),
    path('catalog/<cat_slug>/<item_slug>/', views.item, name='item'),
    path('about/', views.about_us, name='about_us'),
    path('delivery/', views.delivery, name='delivery'),
    path('product/', views.product, name='product'),
    path('contacts/', views.contacts, name='contacts'),
    path('how_it_works/', views.how_it_works, name='how_it_works'),
    path('order_delivery/', views.order_delivery, name='order_delivery'),
    path('reviews/', views.reviews, name='reviews'),
    path('cart/', views.cart, name='cart'),
    path('order/', views.order, name='order'),
    path('callback/', views.callback, name='callback'),
    path('kv/', views.kv, name='kv'),
    path('kv1/', views.kv1, name='kv1'),
    path('stroika_quiz/', views.stroika_quiz, name='stroika_quiz'),
    path('diz_quiz/', views.diz_quiz, name='diz_quiz'),
    path('bfl_quiz/', views.bfl_quiz, name='bfl_quiz'),
    path('bfl_callback/', views.bfl_callback, name='bfl_callback'),
    path('stroika_callback/', views.stroika_callback, name='stroika_callback'),
    path('cb_form/', views.cb_form, name='cb_form'),
    path('robots.txt', views.robots, name='robots'),
    path('remove/<id>', views.remove, name='remove'),
    path('make_slug_dfp217230lf', views.make_slug, name='make_slug'),
    path('search/', views.search, name='search'),
    # path('test/', views.test, name='test'),
    # path('test1/', views.test1, name='test1')


    # path('login/', views.login, name='login'),
    # path('logout/', views.logout_page, name='logout'),
    # path('profile/<nickname_req>', views.profile, name='profile'),
    # path('del_message/', views.del_message, name='del_message'),
    # path('bonus_pack/', views.bonus_pack, name='bonus_pack'),
    # path('about_us/', views.about_us, name='about_us'),
    # path('rules/', views.rules, name='rules'),
    # path('add_to_player_balance/', views.add_to_player_balance, name='add_to_player_balance'),
    # path('about_bonus_pack/', views.about_bonus_pack, name='about_bonus_pack'),




    # path('statistic/', views.statistic, name='statistic'),

]
