# Create sort_contacts function

# for dictionary return tuples using enumerate function
# as in contacts_list = list(enumerate(contacts, 1)) <= puts the tennis players in order
# but here we want tuples. 

def sort_contacts(contacts_dict): 
    
# To Do: Take a dictionary of contacts {} or contacts() as a parameter

    key_list = []
    for key in contacts_dict.keys():
        key_list.append(key)
#    print(key_list)
    key_list.sort()
#    print(key_list)
    
    sorted_contact_list = []
    contact = ()
    
    for key in key_list:
        
        contact_phone_email = list(contacts_dict[key])
        
        contact = (key, contact_phone_email[0], contact_phone_email[1])
        sorted_contact_list.append(contact)
        
    return sorted_contact_list
    


#if __name__ == "__main__":
#    main()

# The code below is just for your testing purposes. Make sure you pass all the tests.
# In Vocareum, only put code for the sort_contacts function above
from test import testEqual

testEqual(sort_contacts({"Horney, Karen": ("1-541-656-3010", "karen@psychoanalysis.com"),
        "Welles, Orson": ("1-312-720-8888", "orson@notlive.com"),
        "Freud, Anna": ("1-541-754-3010", "anna@psychoanalysis.com")}), [('Freud, Anna', '1-541-754-3010',
        'anna@psychoanalysis.com'), ('Horney, Karen', '1-541-656-3010', 'karen@psychoanalysis.com'),
        ('Welles, Orson', '1-312-720-8888', 'orson@notlive.com')])
#testEqual(sort_contacts({"Summitt, Pat": ("1-865-355-4320", "pat@greatcoaches.com"),
#    "Rudolph, Wilma": ("1-410-5313-584", "wilma@olympians.com")}),
#    [('Rudolph, Wilma', '1-410-5313-584', 'wilma@olympians.com'),
#    ('Summitt, Pat', '1-865-355-4320', 'pat@greatcoaches.com')])
#testEqual(sort_contacts({"Dinesen, Isak": ("1-718-939-2548", "isak@storytellers.com")}),
#    [('Dinesen, Isak', '1-718-939-2548', 'isak@storytellers.com')])
#testEqual(sort_contacts({"Rimbaud, Arthur": ("1-636-555-5555", "arthur@notlive.com"),
#    "Swinton, Tilda": ("1-917-222-2222", "tilda@greatActors.com"),
#    "Almodovar, Pedro": ("1-990-622-3892", "pedro@filmbuffs.com"), "Kandinsky, Wassily":
#    ("1-333-555-9999", "kandinsky@painters.com")}), [('Almodovar, Pedro', '1-990-622-3892',
#    'pedro@filmbuffs.com'), ('Kandinsky, Wassily', '1-333-555-9999', 'kandinsky@painters.com'),
#    ('Rimbaud, Arthur', '1-636-555-5555', 'arthur@notlive.com'), ('Swinton, Tilda',
#    '1-917-222-2222', 'tilda@greatActors.com')])
