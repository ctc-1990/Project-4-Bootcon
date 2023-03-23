#Imports shodan pythyon library
import shodan

#Define ShodanAPI
SHODAN_API_KEY = "I19izm8Cdwc6ITz7Yu7mj3YRywn0vzBs"

api = shodan.Shodan(SHODAN_API_KEY)

#Define what the script should try to search for
try:
#Search Shodan(everything after "api.search" is a variable parameter)
        results = api.search('net:"8.8.0.0/16" product:"tomcat"')
#Loop through results of search and output IP adresses that match search criteria
        for result in results['matches']:
            print('%s' % result['ip_str'])
except shodan.APIError as e:
                print('Error: %s' % e)
