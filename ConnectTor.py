#!/usr/bin/python

import urllib, urllib2
import socks
import socket
import sys
import commands

# Connect Tor Network

def GET_MY_IP_Address():
	return commands.getoutput("/sbin/ifconfig").split("\n")[1].split(':')[1].split(" ")[0]

def Connect_Tor():
	while True:			
		try:
			token = 1
			socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", 9050)
			socket.socket = socks.socksocket

			url = 'http://ifconfig.me/ip'
			request = urllib2.Request(url)
			request.add_header('Cache-Control','max-age=0')
			response = urllib2.urlopen(request)
			nowip = response.read()
			userip = GET_MY_IP_Address()
			print "Connect Tor Network Complete. \n"
			print "Ethernet IP Address : " + userip + "\n" + "\033[0;31mSet Tor IP Address : " + nowip + "\033[0m <c0derab1e>"
		except:
			toto = "false"
			return toto

		if token == 1:
			break

if __name__ == '__main__':
	url = sys.argv[1]
	#print "Connecting Tor Network... Please Wait..."
	Connect_Tor()
