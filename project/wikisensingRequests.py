#!/usr/bin/python

import requests
import json


filename = 'filename'

url = 'http://wikisensing.org/WikiSensingServiceAPI/'
serviceKey = 'KarunMatharuV5UGndFEUeTddB9o4GmKw'


def jsonFromFile(filename):
    json_data = open('./' + filename + '.json', 'r').read()
    bodyData = json.loads(json_data)
    body = json.dumps(bodyData)
    return body

def getQuery(url):
    headers = {'Accept' : 'application/json'}
    response = requests.get(url, headers = headers)
    return response

def postQuery(url, body):
    response = requests.post(url,
        headers={'Content-type': 'application/json', 'Accept': 'text/plain'},
        data = body
        )
    return response

def deleteQuery(url):
    headers = {'Accept' : 'application/json'}
    response = requests.delete(url, headers = headers)
    return response

def printResponse(response):
    print '---------------RESPONSE---------------'
    print response
    if response.status_code == 200:
        print '-------------RESPONSE BODY------------'
        print json.dumps(response.json(), indent = 4)
    print ''

def writeResponse(response, filename = 'response'):
    with open('./' + filename + '.json', 'w') as outfile:
        json.dump(response.json(), outfile, sort_keys = True, indent = 4,
            ensure_ascii=False)

def registerSensorFile(file = 'jsonBody'):
    body = jsonFromFile(file)
    print ''
    print body
    print ''
    customURL = url + serviceKey
    response = postQuery(customURL, body)
    printResponse(response)

def postData(sensorId, file = 'jsonBody'):
    body = jsonFromFile(file)
    print ''
    print body
    print ''
    customURL = url + serviceKey + '/' + sensorId
    response = postQuery(customURL, body)
    printResponse(response)
    print ''
    print response

# retrives a sensors metadata
def getUserMetadata():
    response = getQuery(url + serviceKey)
    #printResponse(response)
    return response

# returns all data from a sensor
def getAllData(sensorId):
    customURL = url + serviceKey + '/' + sensorId
    response = getQuery(customURL)
    if response.status_code != 200:
        print 'Error in GET request'
        return None
    # printResponse(response)
    return response

# Retrives latest data from the sensor
# Size is for the number of latest updates to return
# 0 will return all data from the sensor
def getLatestData(sensorId, size=1):
    customURL = url + serviceKey + '/' + sensorId + '/' + str(size)
    response = getQuery(customURL)
    # printResponse(response)
    return response

# Deletes a sensor and all its data
def deleteSensor(sensorId):
    customURL = url + serviceKey + '/' + sensorId 
    response = deleteQuery(customURL)
    #printResponse(response)
    return response

# Registers a new sensor named sensorId parameter and optional description
def registerSensor(sensorId, description = ''):
    print 'Registering Sensor: ' + sensorId 
    body = json.dumps({"sensorId": sensorId, "sensorObject": [{"fieldName":"description", "value": description}]})
    print '------------BODY------------'
    print body
    print ''
    response = postQuery(url + serviceKey, body)
    #printResponse(response)
    return response

# returns a list sensors registred on wikisensing for the 
# given service Key
def getSensorList(serviceKey = serviceKey):
    response = getQuery(url + serviceKey)
    if response.status_code != 200:
        print 'Error in GET request'
        printResponse(response)
        return []
    jsonData = json.loads(response.text)
    if jsonData['sensor'] == []:
        print 'No data for user, or incorrect ServiceKey'
        return []
    sensorList = []
    for sensor in jsonData['sensor']:
        sensorList.append(str(sensor['sensorId']))
    return sensorList






