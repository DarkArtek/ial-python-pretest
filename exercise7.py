import requests
import json

emails = {
	"mario@example.com": "Mario Rossi",
	"luigi@gmail.com": "Luigi Bianchi",
	"test@example.com": "Test user",
	"test2@example.com": "Test User"
}

emails_2 = {}
for email, name in emails.items():
	if name in emails_2:
		emails_2[name].append(email)
	else:
		emails_2
