"""this is the module for pox controller, used for time measurment"""
'''
Coursera:
- Software Defined Networking (SDN) course
-- Programming Assignment: Layer-2 Firewall Application

Professor: Nick Feamster
Teaching Assistant: Arpit Gupta
'''

from pox.core import core
import pox.openflow.libopenflow_01 as of
from pox.lib.revent import *
from pox.lib.util import dpidToStr
from pox.lib.addresses import EthAddr
from collections import namedtuple
import os
import csv
import time

log = core.getLogger()

class Timer (EventMixin):

    def __init__ (self):
        self.listenTo(core.openflow)
        log.debug("Enabling Timer Module")

    def _handle_ConnectionUp (self, event):
    	connection = time.time()
    	hours = int((connection / (60*60)) % 24)
    	minutes = int((connection / 60) % 60)
    	seconds = int(connection % 60)
    	dec_seconds = int((connection * 100) % 100)
    	with open("time.txt","w") as measurment:
    		measurment.write("Controller connected at %d:%d:%d:%d" % (hours,minutes,seconds,dec_seconds))
    	log.debug("Controller connected at %d:%d:%d:%d" % (hours,minutes,seconds,dec_seconds))
        log.debug("Timer installed on %s", dpidToStr(event.dpid))

def launch ():
    '''
    Starting the Timer module
    '''
    core.registerNew(Timer)
