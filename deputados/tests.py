from django.test import RequestFactory, TestCase


class DeputadoTest(TestCase):
    # https://docs.djangoproject.com/en/4.1/intro/tutorial05/
    # https://docs.djangoproject.com/en/4.1/topics/testing/advanced/
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()

    
