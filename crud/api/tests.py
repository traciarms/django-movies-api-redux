
# Create your tests here.
from django.contrib.auth.models import User
from rest_framework.test import APIRequestFactory, APITestCase

# Using the standard RequestFactory API to create a form POST request
from api.views import ListCreateView, DetailAndUpdate
from movie.models import Movie


class TestAPIEndPoints(APITestCase):

    def setUp(self):
        user = User.objects.create_user("test2", "test@user.com", "123456")
        self.top_gun = Movie.objects.create(title="Top gun", owner=user)
        self.fast_times = Movie.objects.create(title="fast times", owner=user)
        self.stripes = Movie.objects.create(title="stripes", owner=user)


    # def testPost(self):
    #     self.setUp()
    #     factory = APIRequestFactory()
    #     request = factory.post('/movies/',
    #                            {'title': 'Movie title', 'owner': 'owner'}, format='json')
    #     view = ListCreateView.as_view()
    #     response = view(request)
    #     return self.assertEquals(response.content, {'title':'Movie title', 'owner':'owner'})
    #
    # def testPut(self):
    #     factory = APIRequestFactory()
    #     request = factory.put('/movies/1/', {'title': 'Movie Title',
    #                                          'owner': 'owner'})
    #     view = DetailAndUpdate.as_view()
    #     response = view(request)
    #     return self.assertEquals(response.content, {'title':'Movie title', 'owner':'owner'})

    def testGet(self):
        factory = APIRequestFactory()
        request = factory.get('/movies/2/')
        view = ListCreateView.as_view()
        response = view(request)
        response.render()
        self.assertContains(response, "Top gun")




