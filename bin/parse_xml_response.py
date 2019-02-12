import xml.etree.ElementTree as ET

def parseXmlContent(aplist, region, amp_fqdn):
	results = []

	# get xml tree as xml content
	tree=ET.fromstring(aplist)

	# get child tags in each ap
	# for each ap in xml
	for i in range(0, len(tree)):

		result = {}
		result['region'] = region
		result['amp_fqdn'] = amp_fqdn

		# for each child element of the ap
		for j in range(0,len(tree.getchildren()[i])):
			child_tag = tree.getchildren()[i].getchildren()[j].tag
			child_text = tree.getchildren()[i].getchildren()[j].text

			if (child_text != None) and (child_tag != 'radio'):
				result[child_tag] = child_text
		
		results.append(result)

	return results