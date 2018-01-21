from app import app
import unittest

# You will not test data in the database only in the browser and codes
class FlaskTestCase(unittest.TestCase):

	def test_index(self):
		tester = app.test_client(self)
		response = tester.get('/login', content_type='html/text')
		self.assertEqual(response.status_code, 200)

	def test_login(self):
		tester = app.test_client(self)
		response = tester.get('/login', content_type='html/text')
		self.assertTrue(b'Login' in response.data)

	# test to make sure that the login details are correct
	def test_login_detail(self):
		tester = app.test_client(self)
		response = tester.post('/login',
								 data=dict(username='dilmac',
								 password='admin123'),
								 follow_redirects = True)
		self.assertIn(b'You were just logged in!', response.data)

	# make sure that (Wrong login details, please try again) is correct when details is wrong
	def test_wrong_login_detail(self):
		tester = app.test_client(self)
		response = tester.post('/login',
								 data=dict(username='admin',
								 password='admin12'),
								 follow_redirects = True)
		self.assertIn(b'Wrong login details, please try again', response.data)

	# make sure the message (You were just logged out) display are correct when you logout.
	def test_logout_message(self):
		tester = app.test_client(self)
		response = tester.post('/login',
								 data=dict(username='dilmac',
								 password='admin123'),
								 follow_redirects = True)
		response = tester.get('/logout', follow_redirects=True)
		self.assertIn(b'You were just logged out!', response.data)

	# Test main page when is open required to login
	def test_home_page_required(self):
		tester = app.test_client(self)
		response = tester.get('/', follow_redirects=True)
		self.assertTrue(b'You need to login first' in response.data)

	# check is the post news in the main page
	def test_post_news(self):
		tester = app.test_client(self)
		response = tester.post('/login',
								 data=dict(username='dilmac',
								 password='admin123'),
								 follow_redirects = True)
		self.assertIn(b'Python', response.data)



if __name__ == '__main__':
	unittest.main()

