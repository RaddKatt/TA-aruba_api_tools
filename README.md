# TA-aruba_api_tools
This Splunk Technical Add-On is used to build a dynamic lookup table of Aruba WAPs by querying a set of Aruba API endpoints.

This Technical Add-On queries the Aruba API endpoints configured in config.json for all Wireless Access Points (WAPs), and transforms the XML results into a Splunk-friendly table format. By default, a saved search is configured to run at 3am every morning to output the results to a lookup file, 'aruba_wap_list.csv'.

Built on Splunk Version 7.2.3, Build 06d57c595b80
