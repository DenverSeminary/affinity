#!/usr/bin/python2

import redis

r = redis.Redis(host='localhost')

def save_user(user_data):
	for key, value in user_data.iteritems():
		r.hset('user:profile:%s' % user_data['username'], key, value)

def save_list(list_name, list_data):	
	for item in list_data:
		r.rpush(list_name, item)
