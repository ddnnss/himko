import json

from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from item.models import *
from cart.models import *
from .models import Callback
from django.contrib import messages

def index(request):
    index_active='orangelink'
    show_tags = True
    title = 'Главная'
    description = ''
    keywords = ''
    s_key = request.session.session_key
    print('guest')
    if not s_key:
        request.session.cycle_key()
    print(s_key)
    all_cats = Category.objects.all().order_by('order_num')

    return render(request, 'page/index.html', locals())


def catalog(request):
    catalog_active = 'orangelink'

    all_cats = Category.objects.all().order_by('order_num')
    return render(request, 'page/all_category.html', locals())

def catalog_inner(request, cat_slug):
    catalog_active = 'orangelink'
    all_cats = Category.objects.all().order_by('order_num')
    cat = Category.objects.get(name_slug=cat_slug)
    if cat.page_h1:
        h1= cat.page_h1
    else:
        h1 = cat.name
    title = cat.page_title
    description = cat.page_description
    keywords = cat.page_keywords
    all_items = Item.objects.filter(category=cat)

    return render(request, 'page/catalog.html', locals())

def item(request, cat_slug,item_slug):
    item = get_object_or_404(Item,name_slug=item_slug)
    all_cats = Category.objects.all().order_by('order_num')
    return render(request, 'page/item.html', locals())
    pass

def about_us(request):
    about_active = 'orangelink'
    all_cats = Category.objects.all().order_by('order_num')
    return render(request, 'page/about.html', locals())

def contacts(request):
    contacts_active = 'orangelink'
    all_cats = Category.objects.all().order_by('order_num')
    return render(request, 'page/contacts.html', locals())

def how_it_works(request):
    work_active = 'orangelink'
    all_cats = Category.objects.all().order_by('order_num')
    return render(request, 'page/how_it_works.html', locals())

def order_delivery(request):
    order_active = 'orangelink'
    all_cats = Category.objects.all().order_by('order_num')
    return render(request, 'page/order_delivery.html', locals())

def reviews(request):
    reviews_active = 'orangelink'
    all_cats = Category.objects.all().order_by('order_num')
    return render(request, 'page/reviews.html', locals())

def cart(request):
    cart_active = 'orangelink'
    all_cats = Category.objects.all().order_by('order_num')
    return render(request, 'page/cart.html', locals())

def order(request):
    return_dict = {}
    print(request.POST)
    s_key = request.session.session_key
    text = ''
    a = json.loads(request.POST.get('items'))
    for x in a:
        str = f'{a[x][0]} - {a[x][1]} : {a[x][2]} шт. \n'
        text+=str
    order = Order.objects.create(name=request.POST.get('form_name'),
                         email=request.POST.get('form_email'),
                         phone=request.POST.get('form_phone'),
                         order=text)
    print(order.id)
    items = Cart.objects.filter(client=s_key)
    items.delete()
    return_dict['order'] = order.id
    return JsonResponse(return_dict)

def robots(request):
    robotsTxt = f"User-agent: *\nDisallow: /admin/\nHost: https://specsintez-pro.ru/\nSitemap: https://specsintez-pro.ru/sitemap.xml"
    return HttpResponse(robotsTxt, content_type="text/plain")

def callback(request):
    print(request.POST)
    if not request.POST.get('agree') and not request.POST.get('message'):
        Callback.objects.create(name=request.POST.get('name'),
                             email=request.POST.get('email'),
                             phone=request.POST.get('phone'),
                                item=request.POST.get('item')
                                )
        messages.success(request, 'Спасибо, форма успешно отправлена')
        print('send')
    else:
        print('not send')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def remove(request,id):
    s_key = request.session.session_key
    cart = Cart.objects.filter(client=s_key,id=id)
    print(cart)
    cart.delete()

    return HttpResponseRedirect('/cart/')

def make_slug(request):
    items = Item.objects.all()
    for i in items:
        print(i.name)
        i.save()
"""



wb = load_workbook(filename='c:/sites/items1.xlsx')
    sheet = wb.active

    max_row = sheet.max_row

    max_column = sheet.max_column
    for i in range(1, max_row + 1):
        cat = sheet.cell(row=i, column=1).value
        print(cat)
        name = sheet.cell(row=i, column=2).value
        print(name)
        image = sheet.cell(row=i, column=3).value
        text1 = sheet.cell(row=i, column=4).value
        text2 = sheet.cell(row=i, column=5).value
        price = sheet.cell(row=i, column=6).value
        maincat = Category.objects.get(name_slug=cat)
        print(maincat)
        print(image)
        item = Item.objects.create(
                            name=name,
                            image='item/{}'.format(image),
                            text1=text1,
                            text2=text2,
                            price=price)
        item.category.add(maincat)


wb = load_workbook(filename='c:/sites/cats.xlsx')
    sheet = wb.active

    max_row = sheet.max_row

    max_column = sheet.max_column
    for i in range(1, max_row + 1):

        print(sheet.cell(row=i, column=1).value)
        print(sheet.cell(row=i, column=2).value)
        Category.objects.create(name=sheet.cell(row=i, column=1).value,name_slug=sheet.cell(row=i, column=2).value)
"""