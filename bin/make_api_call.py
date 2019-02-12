import requests, json

class ApiCall:
	"This class creates a new API call to an Aruba API endpoint. Region Name is required."

	def __init__(self, region='unknown'):

		self.region = region

		# Set up API Auth
		with open('config.json', 'r') as config:
			cfg = json.load(config)
		self.amp_fqdn = cfg[self.region]['amp_fqdn']
		self.amp_url = 'https://' + self.amp_fqdn + '/'
		user = cfg[self.region]['user']
		pw = cfg[self.region]['pw']

		# Set up request data & request headers
		self.data = 'credential_0=' + user + '&credential_1=' + pw + '&destination=/&login=Log In'
		self.headers = {'Content-Type': 'application/x-www-form-urlencoded','Cache-Control':'no-cache'}

	def makeApiCall(self):

		# Set up API session
		ampsession = requests.Session()
		loginamp = ampsession.post(self.amp_url + 'LOGIN',headers=self.headers, data=self.data, verify=False)

		# Make API request
		result=ampsession.get(self.amp_url + 'ap_list.xml',headers=self.headers, verify=False)

		if result:
			return result

	def handleResult(self):

		result = self.makeApiCall()
		if result.status_code == 200:
			content = result.content
			return content
