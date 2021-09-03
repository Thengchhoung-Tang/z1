# Copyright (c) 2021, z1 flexible solution and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document

class WorkoutMember(Document):
	def before_save(self):
		self.full_name = f'{self.first_name or""} {self.last_name or""}'
