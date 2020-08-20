import json
import base64
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from item.models import *
from cart.models import *
from .models import Callback
from django.contrib import messages
from django.core.mail import send_mail
from django.template.loader import render_to_string
from .forms import *

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
    print('request.subdomain', request.subdomain)
    return render(request, 'page/index.html', locals())


def catalog(request):
    catalog_active = 'orangelink'
    pageTitle='Каталог Спецсинтез - продажа профессиональной химии в москве и МО'
    pageDescription='Каталог Спецсинтез - продажа профессиональной химии в москве и МО'
    all_cats = Category.objects.all().order_by('order_num')
    return render(request, 'page/all_category.html', locals())

def catalog_inner(request, cat_slug):
    catalog_active = 'orangelink'
    all_cats = Category.objects.all().order_by('order_num')
    cat = Category.objects.get(name_slug=cat_slug)
    if cat.page_h1:
        h1 = f'{cat.page_h1}' # в {request.subdomain.townAlias}'
    else:
        h1 = f'{cat.name}' # в {request.subdomain.townAlias}'
    pageTitle = f'Каталог профессиональной химии {cat.name.lower()} от компании Спецсинтез в Москве И МО'
    pageDescription = f'   В нашем интернет магазине Вы можете купить профессиональную химию {cat.name.lower()} по низкой цене , с доставкой по России!'
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

def delivery(request):
    about_active = 'orangelink'
    all_cats = Category.objects.all().order_by('order_num')
    return render(request, 'page/delivery.html', locals())

def product(request):
    about_active = 'orangelink'
    all_cats = Category.objects.all().order_by('order_num')
    return render(request, 'page/product.html', locals())

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
    form = NewOrderForm(request.POST, request.FILES)
    s_key = request.session.session_key
    text = ''
    a = json.loads(request.POST.get('items'))
    new_order = None
    for x in a:
        str = f'{a[x][0]} - {a[x][1]} : {a[x][2]} шт. \n'
        text+=str
    if form.is_valid():
        new_order = form.save(commit=False)
        new_order.order = text
        new_order.save()

    print(new_order.id)
    items = Cart.objects.filter(client=s_key)
    items.delete()
    return_dict['order'] = new_order.id
    return JsonResponse(return_dict)

def robots(request):
    subdomain = request.subdomain
    if subdomain and not request.homedomain:
        robotsTxt = f"User-agent: *\nDisallow: /admin/\nHost: {settings.PROTOCOL}{subdomain.name}.{settings.MAIN_DOMAIN}.ru/\nSitemap:{settings.PROTOCOL}{subdomain.name}.{settings.MAIN_DOMAIN}.ru/sitemap.xml"
    else:
        robotsTxt = f"User-agent: *\nDisallow: /admin/\nHost: {settings.PROTOCOL}{settings.MAIN_DOMAIN}.ru/\nSitemap: {settings.PROTOCOL}{settings.MAIN_DOMAIN}.ru/sitemap.xml"

    return HttpResponse(robotsTxt, content_type="text/plain")

def callback(request):
    print(request.POST)
    if not request.POST.get('agree') and not request.POST.get('message') and not request.POST.get('name') == '' and not request.POST.get('phone') == '':
        if request.POST.get('phone'):
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

@csrf_exempt
def kv(request):

    # body_unicode = request.body.decode('utf-8')
    # body = json.loads(body_unicode)
    # print(body)

    msg_html = render_to_string('email/kviz.html', {'type': request.GET.get("type"),
                                                        'theme': request.GET.get("theme"),
                                                        'mess': request.GET.get("mess"),
                                                        'q1': request.GET.get("q1"),
                                                        'q2': request.GET.get("q2"),
                                                        'q3': request.GET.get("q3"),
                                                        'q4': request.GET.get("q4"),
                                                        'q5': request.GET.get("q5"),
                                                        'q6': request.GET.get("q6")})

    send_mail(f'Заполнен квиз на сайте http://{request.GET.get("type")}.ru', None, 'asupport@astrapromo.ru',
              ['igor@astrapromo.ru'],
              fail_silently=False, html_message=msg_html)
    return HttpResponseRedirect(f'http://{request.GET.get("type")}.ru/thanks.html')

def kv1(request):
    msg_html = render_to_string('email/kviz1.html', {
                                                    'q1': request.GET.get("q1"),
                                                    'q2': request.GET.get("q2"),
                                                    'q3': request.GET.get("q3"),
                                                    'q4': request.GET.get("q4"),
                                                    'q5': request.GET.get("q5"),
                                                    'q6': request.GET.get("q6"),
                                                    'q7': request.GET.get("q7"),
                                                    'q8': request.GET.get("q8"),
                                                    'type': request.GET.get("type")})

    send_mail(f'Заполнен квиз ', None, 'asupport@astrapromo.ru',
              ['igor@astrapromo.ru'],
              fail_silently=False, html_message=msg_html)
    return HttpResponseRedirect(f'http://remont.astralid2.ru/thanks.html')

def stroika_quiz(request):
    print(request.GET)
    sq = None
    price_per_m = 0
    start_price = 0
    end_price = 0
    sqq = None
    sq = None
    typ=''
    b64=''

    msg_html = render_to_string('email/stroika_q.html', {
                                                    'return_url':request.GET.get("return_url"),
                                                    'q0': request.GET.get("q0"),
                                                    'q1': request.GET.get("q1"),
                                                    'q2': request.GET.get("q2"),
                                                    'q3': request.GET.get("q3"),
                                                    'q4': request.GET.get("q4"),
                                                    'q5': request.GET.get("q5"),
                                                    'q6': request.GET.get("q6"),
                                                    'q7': request.GET.get("q7"),
                                                    'q8': request.GET.get("q8"),
                                                    'type': request.GET.get("type")})

    send_mail(f'Заполнен квиз ', None, 'asupport@astrapromo.ru',
              ['igor@astrapromo.ru'],
              fail_silently=False, html_message=msg_html)

    if request.GET.get("q1") != 'Пока не знаю':
        s_temp = request.GET.get("q1").split(' ')
        sqq = s_temp[0].split('-')




    if request.GET.get("q2") != 'Пока не знаю' and sqq:
        if request.GET.get("q2") == 'Косметический':
            typ='kos'
            price_per_m = 9000
        if request.GET.get("q2") == 'Капитальный':
            typ='kap'
            price_per_m = 11000
        if len(sqq) > 1:
            start_price = int(sqq[0]) * price_per_m
            end_price = int(sqq[1]) * price_per_m
        else:
            start_price = int(sqq[0]) * price_per_m

        if not sqq:
            start_price = 0

        print(sq,sqq,start_price,end_price)

        str =(f'{start_price},{end_price},{typ},{request.GET.get("q7")},{sqq}').encode('utf8')
        base64_bytes = base64.b64encode(str)
        b64 = base64_bytes.decode('ascii')
        return HttpResponseRedirect(f'{request.GET.get("return_url")}/thanks.html?cid={b64}')
    else:
        return HttpResponseRedirect(f'{request.GET.get("return_url")}/thanks.html')



def diz_quiz(request):
    print(request.GET)

    msg_html = render_to_string('email/diz_q.html', {
                                                    'return_url':request.GET.get("return_url"),
                                                    'show_room': request.GET.get("show_room"),
                                                    'q1': request.GET.get("q1"),
                                                    'q2': request.GET.get("q2"),
                                                    'q3': request.GET.get("q3"),
                                                    'q4': request.GET.get("q4"),
                                                    'q5': request.GET.get("q5"),
                                                    'q6': request.GET.get("q6"),
                                                    'q7': request.GET.get("q7"),
                                                    })

    send_mail(f'Заполнен квиз на сайте дизайна', None, 'asupport@astrapromo.ru',
              ['igor@astrapromo.ru'],
              fail_silently=False, html_message=msg_html)

    return HttpResponseRedirect(f'{request.GET.get("return_url")}/thanks.html')


def cb_form(request):
    msg_html = render_to_string('email/cb_form.html', {
                                                    'p': request.GET.get("phone"),
                                                    'n': request.GET.get("name"),
                                                   })

    send_mail(f'Запрос на обратный звонок', None, 'asupport@astrapromo.ru',
              ['igor@astrapromo.ru'],
              fail_silently=False, html_message=msg_html)
    return HttpResponseRedirect(f'http://remont.astralid2.ru/?sent={request.GET.get("type")}')

def stroika_callback(request):
    msg_html = render_to_string('email/stroika_cb.html', {
                                                    'p': request.GET.get("phone"),
                                                    't': request.GET.get("type"),
                                                    's': request.GET.get("s"),
                                                    's1': request.GET.get("s1"),
                                                   })

    send_mail(f'Запрос на обратный звонок', None, 'asupport@astrapromo.ru',
              ['igor@astrapromo.ru'],
              fail_silently=False, html_message=msg_html)
    return HttpResponseRedirect(f'{request.GET.get("return_url")}?sent=done')

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

def search(request):
    request_unicode = request.body.decode('utf-8')
    request_body = json.loads(request_unicode)
    print(request_body)
    cities = Item.objects.filter(name__contains=request_body['query'].capitalize())

    return_dict = list()
    for i in cities:
        try:
            return_dict.append({'url': i.get_absolute_url(), 'name': i.name})
        except:
            pass
    return JsonResponse(return_dict, safe=False)
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
