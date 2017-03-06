from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
from splinter import Browser


class TestBaseViews(StaticLiveServerTestCase):
    """Integration test suite for testing the views in the app: base.

    Test the url for home and the basefiles like robots.txt and humans.txt

    Attributes
    ----------
    browser : Browser
        Driver to navigate through websites and to run integration tests.
    """

    def setUp(self):
        """Initialize the browser, before running the tests.
        """
        self.browser = Browser('chrome')

    def tearDown(self):
        """At the end of tests, close the browser
        """
        self.browser.quit()

    def test_home(self):
        """Test for url 'base:home'.

        Visit the url of name 'home' and check it loads the content
        """
        self.browser.visit(self.live_server_url + reverse('home'))
        self.assertTrue(self.browser.is_text_present('Hello, world!'))

    def test_robots(self):
        """Test for url 'base:base_files(robots.txt)'.

        Visit the url of robots.txt and check it loads the file
        """
        self.browser.visit(self.live_server_url + reverse('base_files',
                           kwargs={'filename': 'robots.txt'}))
        self.assertTrue(self.browser.is_text_present('robotstxt'))

    def test_humans(self):
        """Test for url 'base:base_files(humans.txt)'.

        Visit the url of humans.txt and check it loads the file
        """
        self.browser.visit(self.live_server_url + reverse('base_files',
                           kwargs={'filename': 'humans.txt'}))
        self.assertTrue(self.browser.is_text_present('humanstxt'))
