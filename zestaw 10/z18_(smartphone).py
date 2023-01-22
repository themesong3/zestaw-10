import new_contact as nc
import contact_list as cl

contact1 = nc.new_contact("Adam Smith", "abc@gmail.com", "789-534-872")
contact2 = nc.new_contact("Jana Green", "xyz@gmail.com", "937-589-268")

contact_list = cl.ContactList()
contact_list.add_contact(contact1)
contact_list.add_contact(contact2)

contact_list.display_contacts()