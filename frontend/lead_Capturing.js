function lead_Capturing(domain,name, emailID, Contact, Preffect_Mode_of_Contact, Project_Domain, Project_Description){
    // Define the data you want to send
    const leadData = {
        Domain: domain, 
        Name: name,
        EmailID: emailID,
        Contact: Contact,
        Prefered_Mode_of_Contact: Preffect_Mode_of_Contact,
        Project_Domain:  Project_Domain,
        Project_Description: Project_Description
    };

    // Define the URL of your FastAPI endpoint
    const url = "http://lemobot2.netlify.app/Lead_Capture";

    // Send POST request using fetch API
    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(leadData),
    })
    .then(response => response.json())
    .then(data => {
        console.log('Success:', data);
        // Handle success response here
    })
    .catch((error) => {
        console.error('Error:', error);
        // Handle error here
    });
}
