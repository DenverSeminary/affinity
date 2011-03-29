#!/usr/bin/python2

import db

user = {}
user['username'] = 'swasheck'
user['first_name'] = 'Seth'
user['last_name'] = 'Washeck'
user['address'] = '123 Main St.'
user['city'] = 'Springfield'
user['state'] = 'CO'
user['zip'] = '90210'
user['email'] = 'email@example.com'


db.save_user(user)

categories = ['Recreational Activities (Outdoor)', 'Recreational Activities (Indoor)', 'Community Groups', 'Academic Groups',
	'Spiritual Groups']
	
db.save_list('category',categories)
