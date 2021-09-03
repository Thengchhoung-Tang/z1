# Copyright (c) 2021, z1 flexible solution and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class WorkoutMembership(Document):
	def before_save(self):
		if self.from_date > self.to_date:
			frappe.throw("Error! To Date must be greater than From Date!")
