"""This program parse an osm xml file and inserts the data in a MongoDB database """
import sys
import os
import time
import pymongo
from datetime import  datetime

from pymongo import MongoClient
from xml.etree.cElementTree import iterparse

class OsmHandler(object):
    def __init__(self):