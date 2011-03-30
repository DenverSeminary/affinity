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

db.flush_db()

db.save_user_profile(user)

categories = ['Recreational Activities (Outdoor)', 'Recreational Activities (Indoor)', 'Community Groups', 'Academic Groups',
	'Spiritual Groups']
	
db.save_list('category',categories)

print db.get_list('category')

activities = ['Hiking','Biking','Climbing','Camping']

db.save_list('Recreational Activities (Outdoor)', activities)

print 'Recreational Activities (Outdoor): ', db.get_list('Recreational Activities (Outdoor)')

print db.get_user_profile('swasheck')
