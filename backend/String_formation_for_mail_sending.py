def String_formation_for_mail_sending(Domain, Name, EmailID, Contact, prefer_Mode_of_Contact, Project_Domain, Project_Description):
    data = {
        "Domain": Domain,
        "Name": Name,
        "Email_ID": EmailID,
        "Contact_Number": Contact,
        "Preferred_Mode_of_Contact": prefer_Mode_of_Contact,
        "Project_Domain": Project_Domain,
        "Project_Description": Project_Description,
    }
    
    formatted_string = (
        f"Domain: {data['Domain']}\n"
        f"Name: {data['Name']}\n"
        f"Email ID: {data['Email_ID']}\n"
        f"Contact Number: {data['Contact_Number']}\n"
        f"Preferred Mode of Contact: {data['Preferred_Mode_of_Contact']}\n"
        f"Project Domain: {data['Project_Domain']}\n"
        f"Project Description: {data['Project_Description']}"
    )
    
    return formatted_string


# # Example usage
# Domain = "example.com"
# Name = "John Doe"
# EmailID = "john.doe@example.com"
# Contact = "123-456-7890"
# prefer_Mode_of_Contact = "Email"
# Project_Domain = "Web Development"
# Project_Description = "Building a new company website."

# formatted_string = String_formation_for_mail_sending(Domain, Name, EmailID, Contact, prefer_Mode_of_Contact, Project_Domain, Project_Description)
# print(formatted_string)
