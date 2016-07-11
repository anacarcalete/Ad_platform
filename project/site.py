import requests
import json
import unirest
from pymongo import MongoClient

url = 'http://wikisensing.org/WikiSensingServiceAPI/'
serviceKey = 'KarunMatharuV5UGndFEUeTddB9o4GmKw'
def getQuery(url):
    headers = {'Accept' : 'application/json'}
    response = requests.get(url, headers = headers)
    return response

def getsmt():
	
	customURL = url + serviceKey + '/' + 'webBrowsing' + '/' + str(10)
	response = getQuery(customURL)
	return response

def printResponse(response):
    print '---------------RESPONSE---------------'
    print response
    if response.status_code == 200:
        print '-------------RESPONSE BODY------------'
        print json.dumps(response.json(), indent = 4)
    print ''


def getLinkCategories(site_name):
	url = "https://enclout-dmoz.p.mashape.com/show.json?auth_token=Vs5_-zExrpLc_SymWMiT&url="
	response = unirest.get(url+site_name,
		headers={
		"X-Mashape-Key": "xrLJ2Gzg1bmshbTvNBkEysKpEM5op1XjyzPjsnHGAnY9zDthFj",
		"Accept": "application/json"
		}
		)
	return response


def getCategories(site_name):
	response = getLinkCategories(site_name)
	cat_list = {}
	for r in response.body['dmoz_categories']:
		if r['Category'] == 'NOT_FOUND':
			continue
		t = r['Category'].replace(":", '')
		x = t.split();
		
		for i in x:
			
			n = x.count(i)
			
			cat_list[i] = n
	return cat_list

	



#print res['sensorRecords'][1]['sensorObject'][3]['value'] 



def format_response(res):
	siteList = []
	for i in xrange(len(res['sensorRecords'])):
		#print i+1
		#print  res['sensorRecords'][i]['sensorObject'][3]['value'] 
		siteList.append(res['sensorRecords'][i]['sensorObject'][3]['value'])
	sites = []
	for site in siteList:
		s = site[7:]
		
		w = 'www.'
		if s[0:4]!= w:
			s = w+s
			
		new_s = ''
		for l in xrange(len(s)):
			if s[l] == '/':
				new_s = s[:l]
				break
			
		sites.append(new_s)
	return sites

#print sites	
def number_of_times_visited(sites):
	tuples = []
	for s in sites:
		n = sites.count(s)
		print s
		print getCategories(s)
		x = (s, n)
		if not x in tuples:
	 		tuples.append((s,n))
	return tuples



def cat_all_sites(sites):
	all_cat = {}
	for s in sites:
		cats = getCategories(s)
		for c in cats.keys():
			if c in all_cat.keys():
				all_cat[c] += cats[c]
			else:
				all_cat[c] = cats[c]
	return all_cat


def find_one(site, db):
	return db.find({'link':site})


def get_first_ads(sites, db):
	ret = []
	for s in sites:
		ret_sites = find_one(s, db)
		ret = ret + ret_sites
	return ret

		





response = getsmt()
res = response.json()
sites = format_response(res)
client = MongoClient('localhost', 27017)
name = 'form-data'
db = client['form-data']
cursor = db['form']
d = find_one('http://google.com', cursor)
for c in d:
	print c


#print tuples	

#print tuples[1][0]
		

