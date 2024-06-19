from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    return HttpResponse("""
    <h1> ЯShop </h1>
    
    <a href="/">Главная</a>
    <a href="/products">Товары</a>
    <a href="/aboutus">О нас</a>
    <div style="border: 1px black colid">
        <h2>Люстра</h2>
        <img src="https://lightstar.ru/image/cache/import_files/21/21c007da42b311e68111c81f66f678b0_01708609f51411e68114c81f66f678b0-350x350.webp"/>
        <p>Люстра - это светильник</p>
    </div>
    <div style='border: 5px black solid'>
    <h2>ПК</h2>
    <p>oh my pccccc</p>
    <img src='https://www.vosem56.ru/upload/iblock/ed1/ed1c1f6785b1d1352869dad005cd0222.png'>
    </div>
    """)


