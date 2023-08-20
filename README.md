# GitHub
Task 1 - GitHub Task Description Manage GitHub scripts and documents Task 1 Screenshot

Task Preparation Create a folder named "Devasc_Skills" in the DEVASC virtual machine. Start a Git repository in the "Devasc_Skills" folder.

Task Implementation Created a local repository using the git init command. Created a GitHub repository named "Devasc_Skills_DO". Connected the local repository to the GitHub repository using git remote add origin https://github.com/eleedreez/devnet_skills_test. Uploaded the local files to GitHub after each task using appropriate Git commands.

Task Troubleshooting No major issues encountered during the implementation.

Task Verification Screenshot: GitHub Repository

# Task 2: Ansible
Task 2: Ansible Task Description Task 2 Screenshot

Task Preparation [...]

Task Implementation [...]

Task Troubleshooting [...]

Task Verification [...]

# Docker
## Task 3: Docker
## Task name: Create Docker Image with Apache2 and Ansible
## Task preparation:
Ensure you have Docker installed on your system.
Create an Ansible playbook (playbook.yml) to configure Apache2 and other necessary settings.
Prepare an index.html file and place it inside a directory named files, which will be copied to the Apache2 web server during container creation.
Create a Dockerfile to define the Docker image build process.
## Task implementation:
start by using the official Ansible base image (ubuntu:latest) to ensure Ansible is available within the container.
Install Ansible and other required packages within the Docker image.
Copy the Ansible playbook (playbook.yml) and the files directory to the container.
Set the working directory to the Ansible playbook directory (/ansible).
Run the Ansible playbook (playbook.yml) inside the container to configure Apache2 and other settings.
Install Apache2 within the container and expose port 8088.
Start the Apache2 service in the foreground to keep the container running.
## Task troubleshooting:
During the implementation of the Docker image creation, a few potential issues may arise:

**Ansible Playbook Errors:** Ensure that the Ansible playbook (playbook.yml) is correctly written and doesn't contain syntax errors or logical issues.
**Package Installation Issues**: Verify that all necessary packages are installed in the Docker image, including Ansible and Apache2.
File Copying Problems: Ensure that the index.html file is placed in the correct location (files directory) and is correctly copied to the Apache2 web server directory during the Ansible playbook execution.
**Port Mapping Conflicts:** If port 8088 is already in use on the host, the container may not start correctly. Ensure that the port is available or use a different port for mapping.
## Task verification:
After building and running the Docker image, I verify the results by:

Access the Apache2 web server by visiting http://localhost:8088 in my web browser. after which I was able to see the content of the index.html file served by Apache2.
Test the functionality of Apache2 by ensuring that it listens on port 8088 and responds to HTTP requests as expected.
checked that any modifications made to the Ansible playbook are correctly applied during the container creation process.
# Jenkins
# Task 4: Jenkins Task Description [...]

Task Preparation [...]

Task Implementation [...]

Task Troubleshooting [...]

Task Verification [...]

# restconf
# Task 5: restconf Task Description [...]

Task Preparation [...]

Task Implementation [...]

Task Troubleshooting [...]

Task Verification [...]

# Task 6: Webex Task Description Manage GitHub scripts and documents Task 6 Screenshot

**Task Preparation** To perform this task, I did the the following:

(i) create a Webex Teams account (ii) Webex Teams access token (iii) Installed Python on the system (iv) Installed requested library(pip install requests)

**Task Implementation** The following steps were taken:

(i) Imported the necessary libraries: python import requests Defined the Webex Teams API endpoint and access token:

api_url = "https://api.ciscospark.com/v1" access_token = "YmU5NjZjMGYtMDI5Ni00YWRmLThjZWUtMjc5Y2M2OTVlYzJiNGFlMzhlNmMtZTVh_PF84_58476986-544b-4c19-b57f-0d76391b2077" Created a Webex Teams space using the API:

def create_space(): url = api_url + "/rooms" headers = { "Authorization": "Bearer " + access_token, "Content-Type": "application/json" } data = { "title": "devasc_skills_DO", "type": "group" } response = requests.post(url, headers=headers, json=data) if response.status_code == 200: space_id = response.json().get("id") print("Space created successfully with ID:", space_id) return space_id else: print("Failed to create space") return None

Added members to the space:

def add_members(space_id): url = api_url + "/memberships" headers = { "Authorization": "Bearer " + access_token, "Content-Type": "application/json" } emails = ["", "yvan.rooseleer@biasc.be"] for email in emails: data = { "roomId": space_id, "personEmail": email } response = requests.post(url, headers=headers, json=data) if response.status_code == 200: print("Member added successfully:", email) else: print("Failed to add member:", email) Sent a message to the space:

def send_message(space_id): url = api_url + "/messages" headers = { "Authorization": "Bearer " + access_token, "Content-Type": "application/json" } data = { "roomId": space_id, "text": "Here are my screenshots of devasc skills-based exam" } response = requests.post(url, headers=headers, json=data) if response.status_code == 200: print("Message sent successfully") else: print("Failed to send message") Main function to run the script:

def main(): space_id = create_space() if space_id: add_members(space_id) send_message(space_id)

if name == "main": main()

**Task Troubleshooting** The following problem was encountered: The email address davidoluwaseun2000@yahoo.com could not be added as a member.

**Task Verification** The quality of the task result can be verified by checking the following: (i) Successful creation of the Webex Teams space with the assigned space ID. (ii) Successful addition of the member yvan.rooseleer@biasc.be to the space.

# Task 7: Bash
# Task 7: Bash Task Description Manage GitHub scripts and documents Task 7 Screenshot

**Task Preparation **To perform this task, I ensure the following:

(i) Have access to a network device that supports RESTCONF API. (ii) Install cURL on your Linux machine (if not already installed) using the package manager for your distribution.

**Task Implementation** To implement the RESTCONF API calls in Bash, I followed these steps:

(i) Create a bash script file. (ii) Define the necessary variables, such as the IP address of the host, RESTCONF credentials, data format, and interface details. (iii) Construct the REST API URLs for PUT and GET requests. (iv) Set the headers and authentication for the requests. (v) Prepare the payload data for the PUT request. (vi) Make the PUT request using cURL and capture the status code. (vii) Make the GET request using cURL and capture the status code and interface information. (viii) Output the results.

**Task Troubleshooting** Following troubleshooting steps:

(i) checked the connectivity to the host and ensure it is reachable from your Linux machine. (ii) verify the correctness of the RESTCONF credentials and API URLs. (iii) ensure cURL is installed and accessible from the command line. (iv) validate the payload data format and structure for the PUT request.

**Task Verification** Verified the quality of the result, follow these steps:

Run the bash script. Check the generated check_restconf_api.txt file for the output. Ensure that the output includes the current date, start and end markers, status codes, and interface information. Compare the obtained results with the expected behavior of the RESTCONF API.

# Task 10: Filtering DNAC Response Data
# Task 10: Filtering DNAC Response Data Description: Filtering DNAC Response Data

**Task Preparation** To perform this task, I needed: A virtual DEVASC virtual machine with an internet connection. Access to a Python execution environment.

**Task Implementation** I Copied the provided sample script to my Python execution environment. I replace the XXXXXXX placeholders in the script with suitable parameters, variables, keys, names, or code as instructed in the comments. Run the script. The script uses the DNAC API to retrieve network device information and filters the response data based on certain conditions. It then prints the filtered data to the console.

**Task Troubleshooting** While implementing this task, the following problems were encountered:

**(i) Incorrect credentials:** I make sure to provide the correct username and password for DNAC authentication. (ii) Network connectivity issues: I ensure that your virtual machine has an internet connection to communicate with the DNAC server.

**Task Verification** To verify the quality of the result, check if the script produces the expected output similar to the provided "DNAC OUTPUT TASK 10" in the task description. Successful execution of the script.
