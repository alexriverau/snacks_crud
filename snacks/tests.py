from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from snacks.models import Snack


class SnackTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='tester', email='tester@email.com', password='pass')
        self.snack = Snack.objects.create(
            title='snack', purchaser=self.user, description='description'
        )

    def test_snack_list(self):
        url = reverse('snack_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_snack_detail(self):
        url = reverse('snack_detail')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'snack-detail.html')

    def test_snack_create(self):
        url = reverse('snack_create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'snack-create.html')

    def test_snack_update(self):
        url = reverse('snack_update')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'snack-update.html')

    def test_snack_delete(self):
        url = reverse('snack_delete')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'snack-delete.html')

    def test_string_representation(self):
        self.assertEqual(str(self.snack), 'snack')

    def test_fields(self):
        self.assertEqual(self.snack.title, 'snack')
        self.assertEqual(self.snack.purchaser, self.user)
        self.assertEqual(self.snack.description, 'description')
