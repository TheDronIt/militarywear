from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
import random
from .models import *

def index__page(request):
	data = {
		"Products__popular": products_by_tag("Популярно")[:4],
		"Tags": Tag.objects.filter(Visible_status="Отображать"),
		"Nav_category": nav_category()
	}
	return render(request, 'page/index.html', data)


def catalog__page(request):
	catalog__list = Category.objects.all().order_by("id")

	data = {
		"Catalog__list": catalog__list,
		"Nav_category": nav_category()
	}
	return render(request, 'page/catalog.html', data)


def product_catalog__page(request, id):
	product_catalog__list = Product.objects.filter(Category__id=id)
	CategoryName = Category.objects.get(id=id)

	data = {
		"Product_catalog__list": product_catalog__list,
		"CategoryName": CategoryName,
		"Nav_category": nav_category()
	}
	return render(request, 'page/product_catalog.html', data)


def product__page(request, id):
	product = Product.objects.get(id=id)
	
	if request.method == "POST":
		if request.POST['button']:
			if request.POST['button'] == "В корзину":
				product = Product.objects.get(id=id)
				size = request.POST['Size']
				if product_in_basket(request, id, size) == False:
					db = Basket(session_key = session_key(request), product_id=id, product_size=request.POST['Size'], product_value=1)
					db.save()
					return redirect("/product/"+str(id))


				else:
					return redirect("/basket")	
			elif request.POST['button'] == "Добавлено":
				return redirect("/basket")
				
	data = {
		"Product": product,
		"Recommendations": Recommendations()[:4],
		"Nav_category": nav_category()
	}
	return render(request, 'page/product.html', data)


def delivery__page(request):
	data = {
		"Nav_category": nav_category()
	}
	return render(request, 'page/delivery.html', data)


def contacts__page(request):
	data = {
		"Nav_category": nav_category()
	}
	return render(request, 'page/contacts.html', data)


def basket__page(request):
	user_product = Basket.objects.filter(session_key=session_key(request)).order_by('id')
	#about_product = Product.objects.get()
	product_list = []
	for product_el in user_product:
		product = Product.objects.get(id=int(product_el.product_id))
		product_list.append(
			dict(
				Id=product.id,
				Name=product.Name,
				Link="/product/"+str(product.id),
				Image=product.Image.url,
				Value=product_el.product_value,
				Size=product_el.product_size,
				Articul=product.Articul,
				Price=product.Price,
				Full_price=product.Price * product_el.product_value,
			))


	if request.method == "POST":
		if request.POST['button']:
			button = request.POST['button']
			if button == "+" or button == "-" or button == "✖":
				
				product_id = request.POST['product_id']
				product_size = request.POST['product_size']
				print(product_id)
				
				
				if button == "+":
					Basket.objects.filter(session_key=session_key(request)).filter(product_id=product_id).filter(product_size=product_size).update(product_value = int(product_value(request))+1)
				
				elif button == "-":
					Basket.objects.filter(session_key=session_key(request)).filter(product_id=product_id).filter(product_size=product_size).update(product_value = int(product_value(request))-1)
					if product_value(request) < 1:
						Basket.objects.filter(session_key=session_key(request)).filter(product_size=product_size).filter(product_id=product_id).delete()
				
				elif button == "✖":
					Basket.objects.filter(session_key=session_key(request)).filter(product_size=product_size).filter(product_id=product_id).delete()

				return HttpResponseRedirect("/basket")
	
	data = {
		'Product_list': product_list,
		'BasketPrice': basket_price(request),
		"Nav_category": nav_category()
	}
	return render(request, 'page/basket.html', data)	


def search__page(request):
	query = ""
	query_result = ""

	if request.method:
		if request.method == "GET":
			if request.GET['q']:
				query = request.GET['q']
				query_result = Product.objects.filter(Name__icontains=query)
				print(query_result)
	data = {
		"Nav_category": nav_category(),
		"Query_result": query_result,
		"Query": query
	}
	return render(request, 'page/search.html', data)	






def session_key(request):
	session_key = request.session.session_key
	if not session_key:
		request.session.cycle_key()
	return session_key;


def product_in_basket(request, id, size):
	product = Basket.objects.filter(session_key=session_key(request)).filter(product_id=id).filter(product_size=size)#добавить провеку по size
	if len(product) >= 1:
		return True
	else:
		return False


def basket_price(request):
	basket = Basket.objects.filter(session_key=session_key(request))
	full_price = 0
	for product in basket:
		full_price = (Product.objects.get(id=product.product_id).Price * product.product_value) + full_price
	return full_price


def product_value(request):
	product_id = request.POST['product_id']
	product_size = request.POST['product_size']

	product_value = Basket.objects.filter(session_key=session_key(request)).filter(product_size=product_size).get(product_id=product_id).product_value
	return product_value


def products_by_tag(tag):
	product_list = Product.objects.filter(Tags__Name=tag)
	return product_list


def nav_category():
	category = Category.objects.filter(Show_nav="Отображать").order_by("id")
	return category


def Recommendations():
	recommendation = Product.objects.filter(Recommendation="Отображать").order_by("?")
	return recommendation


def make_order(request):
	pass