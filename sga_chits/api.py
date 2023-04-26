# import frappe

# @frappe.whitelist(allow_guest=True)
# def api_token_auth():
# 	frappe.log_error(frappe.form_dict)
# 	# return "Hello"
# 	# data = json.loads(frappe.request.data)
# 	email_id = "hello"
# 	frappe.log_error(email_id)
# 	user_id = str(hash(email_id))
# 	frappe.response.data = {
# 	"token": "fccf12db1865258:91a863f6c988613",
# 	"user_id": user_id,
# 	"user_info": {
# 		"user_id": user_id,
# 		"role": "admin",
# 		"user_name": None,
# 		"user_type": None,
# 		"is_existing_user": False,
# 		"message": "Successfully created account",
# 		"profile_completion_status": {
# 		"basic_info": False,
# 		"profile_file_upload": True
# 		},
# 		"profile_progress_percentage": 0,
# 		"is_account_active": True,
# 		"profile_reviewed": False,
# 		"route_link": "/profile/basic-details",
# 		"dashboard_access": False,
# 		"country_name": "India",
# 		"currency_code": "INR",
# 		"curreny_symbol": "INR",
# 		"dail": 91
# 	}
# 	}
