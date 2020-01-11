from django.shortcuts import render
from item.models import *
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
    all_cats = Category.objects.all()

    return render(request, 'page/index.html', locals())


def catalog(request, cat_slug):
    cat = Category.objects.get(name_slug=cat_slug)
    all_items = Item.objects.filter(category=cat)
    all_cats = Category.objects.all()
    return render(request, 'page/catalog.html', locals())

def about_us(request):
    about_active = 'orangelink'
    all_cats = Category.objects.all()
    return render(request, 'page/about.html', locals())

def contacts(request):
    contacts_active = 'orangelink'
    all_cats = Category.objects.all()
    return render(request, 'page/contacts.html', locals())

def how_it_works(request):
    work_active = 'orangelink'
    all_cats = Category.objects.all()
    return render(request, 'page/how_it_works.html', locals())

def order_delivery(request):
    order_active = 'orangelink'
    all_cats = Category.objects.all()
    return render(request, 'page/order_delivery.html', locals())

def reviews(request):
    reviews_active = 'orangelink'
    all_cats = Category.objects.all()
    return render(request, 'page/reviews.html', locals())

def cart(request):
    cart_active = 'orangelink'
    all_cats = Category.objects.all()
    return render(request, 'page/cart.html', locals())
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