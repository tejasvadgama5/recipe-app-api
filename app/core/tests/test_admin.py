from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase, Client

"""
django.test.Client: The test client is a Python class
that acts as a dummy Web browser,
allowing you to test your views and interact with your
Django-powered application programmatically.
django.urls.reverse :If you need to use something
similar to the url template tag in your code
"""


class AdminSiteTest(TestCase):

    # In this function, setup some tasks that need to be done before evey test
    def setUp(self):
        # Here we set all client, superuser and also user
        self.client = Client()  # Create new client Object
        self.admin_user = get_user_model().objects.create_superuser(
            # Create super user
            email="admin@suratappdev.com",
            password="admin123"
        )
        self.client.force_login(self.admin_user)  # login with super
        self.user = get_user_model().objects.create_user(
            # Create new user for testing
            email="test@suratappdev.com",
            password="test123",
            name="This is test name"
        )

    def test_users_listed(self):
        """Test that users are listed on user page"""
        url = reverse("admin:core_user_changelist")
        res = self.client.get(url)

        # Contains check response object contain name and email or not
        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)

    def test_user_change_page(self):
        """Test that the user edit page works"""
        url = reverse('admin:core_user_change', args=[self.user.id])
        # url call /admin/core/user/1
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)

    def test_create_user_page(self):
        """Test that the create user page works"""
        url = reverse('admin:core_user_add')
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)
