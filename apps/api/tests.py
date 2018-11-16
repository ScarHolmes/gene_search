from django.test import TestCase, RequestFactory
from .models import *
from . import views
import json

class Variant_TestCase_Create(TestCase):
	def setUp(self):
		Variant.objects.create(gene="test", nucleotide_change="test_nuc_change", protein_change="test_pro_change",other_mappings="",url="test_url")
		Variant.objects.create(gene="test2", nucleotide_change="test_nuc_change2", protein_change="test_pro_change2",other_mappings="",url="test_url2")

	def test_retrieve_variant(self):
		test = Variant.objects.get(gene="test")
		test2 = Variant.objects.get(gene="test2")
		self.assertEqual(test.nucleotide_change, 'test_nuc_change')
		self.assertEqual(test2.protein_change, 'test_pro_change2')

class Variant_TestCase_Search(TestCase):
	def setUp(self):
		self.factory = RequestFactory()
		request = self.factory.get('/api/upload_info?file_name=variants_test_2.csv')
		response = views.upload_info(request)
		self.assertEqual(response.status_code, 200)
		count = len(Variant.objects.all())
		self.assertEqual(count, 2)

	def test_perform_search(self):
		request = self.factory.get('/api/perform_search?search_by=CDKL5')
		response = views.perform_search(request)
		self.assertEqual(response.status_code, 200)
		results = json.loads(response.content)['results']
		self.assertEqual(len(results), 1)
		self.assertEqual(results[0]['gene'], 'CDKL5')

class Variant_TestCase_Upload(TestCase):
	def setUp(self):
		count = len(Variant.objects.all())

	def test_preform_upload(self):
		first_count = len(Variant.objects.all())
		self.factory = RequestFactory()
		request = self.factory.get('/api/upload_info?file_name=variants_test_2.csv')
		response = views.upload_info(request)
		self.assertEqual(response.status_code, 200)
		count = len(Variant.objects.all())
		self.assertNotEqual(first_count, count)

class Variant_TestCase_Purge(TestCase):
	def setUp(self):
		self.factory = RequestFactory()
		request = self.factory.get('/api/upload_info?file_name=variants_test_2.csv')
		response = views.upload_info(request)
		self.assertEqual(response.status_code, 200)
		count = len(Variant.objects.all())
		self.assertEqual(count, 2)

	def test_purge_db(self):
		first_count = len(Variant.objects.all())
		request = self.factory.get('/api/purge_db')
		response = views.purge_db(request)
		self.assertEqual(response.status_code, 200)
		count = len(Variant.objects.all())
		self.assertNotEqual(first_count, count)

 