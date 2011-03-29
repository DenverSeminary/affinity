#!/usr/bin/python2

import redis

r = redis.Redis(host='lindev')

def flush_db():
	r.flush()

def save_user_profile(user_data):
	for key, value in user_data.iteritems():
		r.hset('user:profile:%s' % user_data['username'], key, value)

def save_list(list_name, list_data):	
	for item in list_data:
		r.rpush(list_name.replace(' ', '.'), item)
		
def get_list(list_name):
	return r.lrange(list_name.replace(' ', '.'), 0, r.llen(list_name.replace(' ', '.')))
