from google.appengine.ext.webapp import blobstore_handlers
from google.appengine.ext import ndb
import json
import logging
from template import template
import webapp2
import models


class VolunteerRegistrationHandler(webapp2.RequestHandler):
	def get(self):
		self.response.write(template("volunteer_registration_form.html", {}))

	def post(self):
		vol = models.Volunteer()
		vol.name = self.request.get("name")
		vol.email = self.request.get("email")
		vol.phone = self.request.get("phone")
		vol.role = self.request.get("role")

		vol.put()

		self.redirect("volunteer_confirmation")


class VolunteerConfirmationHandler(webapp2.RequestHandler):
	def get(self):
		self.response.write(template("volunteer_confirmation.html", {}))
