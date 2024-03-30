from django.test import SimpleTestCase
from django.urls import reverse, resolve
from monolith.views import *

class TestUrls(SimpleTestCase):

    def test_index_blank_url_is_resolved(self):
        url = reverse('index_blank')
        self.assertEqual(resolve(url).func, index)

    def test_index_url_is_resolved(self):
        url = reverse('index')
        self.assertEqual(resolve(url).func, index)

    def test_buttons_url_is_resolved(self):
        url = reverse('buttons')
        self.assertEqual(resolve(url).func, buttons)

    def test_cards_url_is_resolved(self):
        url = reverse('cards')
        self.assertEqual(resolve(url).func, cards)
    
    def test_utilities_colors_url_is_resolved(self):
        url = reverse('utilities_colors')
        self.assertEqual(resolve(url).func, utilities_colors)
    
    def test_utilities_border_url_is_resolved(self):
        url = reverse('utilities_border')
        self.assertEqual(resolve(url).func, utilities_border)

    def test_utilities_animation_url_is_resolved(self):
        url = reverse('utilities_animation')
        self.assertEqual(resolve(url).func, utilities_animation)
    
    def test_utilities_other_url_is_resolved(self):
        url = reverse('utilities_other')
        self.assertEqual(resolve(url).func, utilities_other)
    
    def test_login_url_is_resolved(self):
        url = reverse('login')
        self.assertEqual(resolve(url).func, login)
    
    def test_register_url_is_resolved(self):
        url = reverse('register')
        self.assertEqual(resolve(url).func, register)
    
    def test_forgot_password_url_is_resolved(self):
        url = reverse('forgot_password')
        self.assertEqual(resolve(url).func, forgot_password)

    def test_404_url_is_resolved(self):
        url = reverse('404')
        self.assertEqual(resolve(url).func, not_found)
    
    def test_blank_url_is_resolved(self):
        url = reverse('blank')
        self.assertEqual(resolve(url).func, blank)
    
    def test_charts_url_is_resolved(self):
        url = reverse('charts')
        self.assertEqual(resolve(url).func, charts)
    
    def test_tables_url_is_resolved(self):
        url = reverse('tables')
        self.assertEqual(resolve(url).func, tables)