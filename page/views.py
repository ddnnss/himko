from django.shortcuts import render

def index(request):
    show_tags = True
    title = 'Главная'
    description = ''
    keywords = ''


    return render(request, 'page/index.html', locals())

def test3(request):
    resp = req.get("http://specsintez-pro.ru/")

    soup = BeautifulSoup(resp.text, 'html')
    main_structure = {}
    cats = []
    subcats = {}
    all_cats = soup.find_all("div", class_='block-catalog')

    for cat in all_cats:
        cat_slug = cat.get('id')
        print(cat_slug)
        cat_name = cat.find('h2').text.capitalize()
        print(cat_name)
        for item in cat.find_all('div',class_='sredstvo'):
            prices = []
            image = item.find('img').get('src')
            print(image)
            item_text1 = item.find('div', id='readmore').find('p').prettify(formatter="html")
            print(item_text1)
            item_text2 = item.find('div', id='readmore').find('div').prettify(formatter="html")
            print(item_text2)
            item_prices = item.find('div', class_='sr-text').find_all('span')
            for price in item_prices:
                prices.append(price.text)
            print(prices)