from search_command import SearchCommand
from make_api_call import *
from parse_xml_response import *

def getResults():

	# Get results from the AMER Aruba API
	api_call = ApiCall('AMER')
	aplist = api_call.handleResult()
	results_amer = parseXmlContent(aplist, api_call.region, api_call.amp_fqdn)

	# Get results from the EMEA Aruba API
	api_call = ApiCall('EMEA')
	aplist = api_call.handleResult()
	results_emea = parseXmlContent(aplist, api_call.region, api_call.amp_fqdn)

	# Get results from the APAC Aruba API
	api_call = ApiCall('APAC')
	aplist = api_call.handleResult()
	results_apac = parseXmlContent(aplist, api_call.region, api_call.amp_fqdn)

	results = results_amer + results_emea + results_apac

	return results

class getArubaWaps(SearchCommand):

    def __init__(self):

        # Save the parameters
        self.results = getResults()

        # Initialize the class
        SearchCommand.__init__( self, run_in_preview=True, logger_name='getarubawaps')

    def handle_results(self, results, session_key, in_preview):
        self.output_results(self.results)

if __name__ == '__main__':
    getArubaWaps.execute()
