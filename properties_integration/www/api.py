import frappe

@frappe.whitelist()
def copy_role(role, copy_role):
    docs = []
    for d in frappe.get_all("DocPerm", fields="*", filters=dict(role=copy_role)):
        custom_perm = frappe.new_doc("Custom DocPerm")
        d.role = role
        custom_perm.update(d)
        custom_perm.insert(ignore_permissions=True)
        docs.append(d.parent)

    frappe.db.commit()
    return docs

   