from django.test import TestCase
from myapp.models import models

# Create your tests here.


class UserTestCase(TestCase):
    def setUp(self):
        User.objects.create(name='John Doe', email='john@example.com', phone='1234567890', address='123 Main St')
        
    def test_user_creation(self):
        user = User.objects.get(name='John Doe')
        self.assertEqual(user.email, 'john@example.com')
        self.assertEqual(user.phone, '1234567890')
        self.assertEqual(user.address, '123 Main St')

class ProductTestCase(TestCase):
    def setUp(self):
        Product.objects.create(name='iPhone', description='Smartphone by Apple', price=999.99, image='iphone.jpg')
        
    def test_product_creation(self):
        product = Product.objects.get(name='iPhone')
        self.assertEqual(product.description, 'Smartphone by Apple')
        self.assertEqual(product.price, 999.99)
        self.assertEqual(product.image, 'iphone.jpg')

class OrderTestCase(TestCase):
    def setUp(self):
        user = User.objects.create(name='John Doe', email='john@example.com', phone='1234567890', address='123 Main St')
        product = Product.objects.create(name='iPhone', description='Smartphone by Apple', price=999.99, image='iphone.jpg')
        Order.objects.create(user=user, product=product, quantity=2, total_price=1999.98)
        
    def test_order_creation(self):
        order = Order.objects.get(user__name='John Doe')
        self.assertEqual(order.product.name, 'iPhone')
        self.assertEqual(order.quantity, 2)
        self.assertEqual(order.total_price, 1999.98)
