#!/usr/bin/python

import requests
import json
import sys
import wikisensingRequests as wr
import os


url = 'http://wikisensing.org/WikiSensingServiceAPI/'
serviceKey = 'KarunMatharuV5UGndFEUeTddB9o4GmKw'


options = ['Sensor List', 'Retrive All Data', 'Retrieve Latest Data', 'User Metada', 'Create Sensor' ,'Delete Sensor', 'Quit']


def main():
	while True:
		os.system('clear')
		print ''
		print '**************************'
		print '*  WIKISENSING REQUESTER *'
		print '**************************'
		print ''
		print 'This program retrieves data from the WikiSensing server'
		print 'Your service key is: ' + serviceKey
		menu()


# The programs main menu
def menu():
		print ''
		for i in range(len(options)):
			print str(i) + ' : ' + str(options[i])
		print ''
		# get user input and check if correct
		print 'Please select an option from the list above'
		inp = getInput(len(options)-1)
		opts(inp)


def opts(inp):
	os.system('clear')
	if inp == 0: # Sensor List
		printSensorList()
	elif inp == 1: # Retrieve All Data
		sensorName = selectSensor()
		response = wr.getAllData(sensorName)
		wr.printResponse(response)
	elif inp == 2: # Retrieve Latest Data
		sensorName = selectSensor()
		print 'Enter the numer of updates to retrieve (0 for all)'
		print "Sensors name...."
		print sensorName
 		noUpdates = getInput();
		response = wr.getLatestData(sensorName, noUpdates)
		wr.printResponse(response)
	elif inp == 3: # User Metadata
		response = wr.getUserMetadata()
		wr.printResponse(response)
	elif inp == 4: # Create Sensor
		createSensor()
	elif inp == 5: # Delete Sensor
		print 'Select a sensor to delete'
		sensorName = selectSensor()
		print 'Deleting \'' + sensorName + '\' sensor cannot be undone'
		if authenticate():
			response = wr.deleteSensor(sensorName)
			wr.printResponse(response)
			print 'Sensor Deleted'
		else:
			print 'Sensor Not Deleted'
	elif inp == 6: # Quit 
		sys.exit()
	print ''
	raw_input('Press Enter to return to main menu ')



def createSensor():
	print 'Existing Sensors'
	sensors = printSensorList()
	name = ''
	while name == '':
		print 'Enter the name of new sensor: '
		name = getStringInput()
		if name in sensors:
			print "'" + name + "' already exists"
			name = ''
	print 'Enter a description of the sensor:'
	description = getStringInput()
	response = wr.registerSensor(name, description)
	wr.printResponse(response)


def getStringInput():
	inp = ''
	while (len(inp) == 0):
		inp = raw_input()
		checkQuit(inp)
		if (inp == ''):
			print 'Input must contain characters: '
			print 'Enter input or x to quit'
	return inp


def authenticate():
	inp = raw_input("Are you sure you want to continue? Enter 'yes': ")
	if inp == 'yes':
		return True
	else:
		return False


def selectSensor():
	os.system('clear')
	print ''
	sensors = printSensorList()
	if len(sensors) == 0:
		return False
	print ''
	print 'Please select a sensor from the list above'
	inp = getInput(len(sensors)-1)
	return sensors[inp]


# returns the number of sensors for the given user serviceKey
def printSensorList(sk = serviceKey):
	sensors = wr.getSensorList(sk)
	if len(sensors) > 0:
		for i in range(len(sensors)):
			print str(i) + ' : ' + str(sensors[i])
	return sensors


def getInput(maximum = 0):
	inp = -1
	while inp < 0:
		if maximum:
			inp = raw_input('Enter a value between 0-' + str(maximum) + ': ')
		else:
			inp = raw_input('Enter a number: ')
		inp = checkInput(inp, maximum)
	return inp


# check input and ensure it in in the range 0-max
# parameter maximum is 0 when there should be no limit
def checkInput(inp, maximum = 0):
	if inp == '':
		return -1
	checkQuit(inp)
	try:
		val = int(inp)
	except ValueError:
		print 'Input must be a positive number: '
		print 'Or enter x to quit'
		return -1
	if maximum:
		if val < 0 or val > maximum:
			print 'Input must be a integer between 0-' + str(maximum)
			return -1
	elif val < 0:
		print 'Input must be positive'
		return -1
	return val




def checkQuit(inp):
	if inp == 'X' or inp == 'x':
		print "Exiting"
		sys.exit()
	#if input == 'M' or input == 'm':
	#	menu():

if __name__ == '__main__':
	main()



