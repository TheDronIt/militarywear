from django.db import models
from django.contrib import admin
from django.core.validators import MaxValueValidator, MinValueValidator 

class Tag(models.Model):
	class Meta:
		verbose_name = 'Ярлыки'
		verbose_name_plural = 'Ярлыки'
	
	Visible_status_list = [
		("Отображать", "Отображать"),
		("Не отображать", "Не отображать")
	]

	Name = models.CharField(verbose_name="Название", max_length=50)
	Visible_status = models.CharField(max_length=50, choices=Visible_status_list, default="Не отображать", verbose_name="Блок на главной")

	def __str__(self):
			return str(self.Name)


class Size(models.Model):
	class Meta:
		verbose_name = 'Размеры'
		verbose_name_plural = 'Размеры'
	
	Name = models.CharField(verbose_name="Размер", max_length=50)

	def __str__(self):
			return str(self.Name)


class ProductImage(models.Model):
	class Meta:
		verbose_name = 'Изображения товаров'
		verbose_name_plural = 'Изображения товаров'
	Image = models.ImageField(upload_to='product/images/', blank=True)

	def __str__(self):
			return str(self.Image)


class Category(models.Model):
	class Meta:
		verbose_name = 'Категории'
		verbose_name_plural = 'Категории'

	Show_nav_list = [
		("Отображать", "Отображать"),
		("Не отображать", "Не отображать")
	]

	Name = models.CharField(verbose_name="Название", max_length=50)
	Image = models.ImageField(verbose_name="Изображение", upload_to='category/')
	Show_nav = models.CharField(max_length=50, choices=Show_nav_list, default="Не отображать", verbose_name="Отображать в меню")

	def __str__(self):
		return str(self.Name)


class Manufacturer(models.Model):
	class Meta:
		verbose_name = 'Производитель'
		verbose_name_plural = 'Производитель'
	Name = models.CharField(verbose_name="Производитель", max_length=50)
	Country = models.CharField(verbose_name="Страна", max_length=50)

	def __str__(self):
		return str(self.Name)


class Product(models.Model):
	class Meta:
		verbose_name = 'Товар'
		verbose_name_plural = 'Товар'

	Availability_list = [
		("Есть в наличии", "Есть в наличии"),
		("Нет в наличии", "Нет в наличии")
	]
	UsedCondition = [
		("Новое", "Новое"),
		("Б/У", "Б/У")
	]
	Recommendation_list = [
		("Отображать", "Отображать"),
		("Не отображать", "Не отображать")
	]

	Name = models.CharField(verbose_name="Название", max_length=50)
	Image = models.ImageField(verbose_name="Изображение", upload_to='product/')
	Images = models.ManyToManyField(ProductImage, verbose_name="Изображения товара", blank=True)

	Category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Категория")
	Articul = models.CharField(verbose_name="Артикул", max_length=50)
	Manufacturer = models.ForeignKey(Manufacturer, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Производитель")
	Availability = models.CharField(max_length=50, choices=Availability_list, default="Нет в наличии", verbose_name="Наличие")
	UsedCondition = models.CharField(verbose_name="Состояние", max_length=50)
	Sizes = models.ManyToManyField(Size, verbose_name="Размеры в наличии", blank=True)
	Tags = models.ManyToManyField(Tag, verbose_name="Ярлыки", blank=True)
	Recommendation = models.CharField(max_length=50, choices=Recommendation_list, default="Не отображать", verbose_name="Рекомендации")
	About = models.TextField(blank=True, verbose_name="Описание")
	Sale = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)], verbose_name="Скидка")
	Price = models.IntegerField(verbose_name="Цена")

	def __str__(self):
		return str(self.Name)



class Basket(models.Model):
	class Meta:
		verbose_name = 'Корзина (system)'
		verbose_name_plural = 'Корзина (system)'

	session_key = models.CharField(max_length=120)
	product_id = models.CharField(max_length=120)
	product_value = models.IntegerField()
	product_size = models.CharField(max_length=120, blank=True)

	def __str__(self):
		return str(self.id)


class Order(models.Model):
	class Meta:
		verbose_name = "Заказы"
		verbose_name_plural = "Заказы"

	Delivery_type_list = [
		("Самовывоз", "Самовывоз"),
		("Доставка", "Доставка")
	]
	Payment_type_list = [
		("При получении", "При получении"),
		("Онлайн", "Онлайн")
	]
	Payment_status_list = [
		("Не оплачено", "Не оплачено"),
		("Оплачено", "Оплачено")
	]

	FIO = models.CharField(verbose_name="ФИО", max_length=50)
	Phone = models.CharField(verbose_name="Телефон", max_length=50)
	Email = models.CharField(verbose_name="Email", max_length=50)
	
	Products = models.TextField(verbose_name='Заказ')


	Delivery_type = models.CharField(max_length=50, choices=Delivery_type_list, verbose_name="Тип доставки")

	Region = models.CharField(verbose_name="Область", max_length=50)
	City = models.CharField(verbose_name="Город", max_length=50)
	Post_index = models.CharField(verbose_name="Почтовый индекс", max_length=50)
	Address = models.CharField(verbose_name="Адрес", max_length=50)

	Payment_type = models.CharField(max_length=50, choices=Payment_type_list, verbose_name="Тип оплаты")
	Payment_status = models.CharField(max_length=50, choices=Payment_status_list, default="Не оплачено", verbose_name="Статус оплаты")

	Price = models.IntegerField(verbose_name='Итоговая цена')