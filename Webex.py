import requests
import os

# Webex Teams API endpoint
api_url = "https://api.ciscospark.com/v1"

# Webex Teams access token
access_token = "YmU5NjZjMGYtMDI5Ni00YWRmLThjZWUtMjc5Y2M2OTVlYzJiNGFlMzhlNmMtZTVh_PF84_58476986-544b-4c19-b57f-0d76391b2077"

# Create a Webex Teams space
def create_space():
    url = api_url + "/rooms"
    headers = {
        "Authorization": "Bearer " + access_token,
        "Content-Type": "application/json"
    }
    data = {
        "title": "devasc_skills_DO",
        "type": "group"
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        space_id = response.json().get("id")
        print("Space created successfully with ID:", space_id)
        return space_id
    else:
        print("Failed to create space")
        return None

# Add members to the space
def add_members(space_id):
    url = api_url + "/memberships"
    headers = {
        "Authorization": "Bearer " + access_token,
        "Content-Type": "application/json"
    }
    emails = ["ladanidris23@gmail.com", "yvan.rooseleer@biasc.be"]
    for email in emails:
        data = {
            "roomId": space_id,
            "personEmail": email
        }
        response = requests.post(url, headers=headers, json=data)
        if response.status_code == 200:
            print("Member added successfully:", email)
        else:
            print("Failed to add member:", email)

# Publish URL to the space
def publish_url(space_id):
    url = api_url + "/messages"
    headers = {
        "Authorization": "Bearer " + access_token,
        "Content-Type": "application/json"
    }
    message = "Here is the URL to my GitHub repository: https://github.com/eleedreez/devnet_skills_test"
    data = {
        "roomId": space_id,
        "markdown": message
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        print("URL published successfully")
    else:
        print("Failed to publish URL")

# Send message to the space
def send_message(space_id):
    url = api_url + "/messages"
    headers = {
        "Authorization": "Bearer " + access_token,
        "Content-Type": "application/json"
    }
    message = "Here are my screenshots of devasc skills-based exam"
    data = {
        "roomId": space_id,
        "markdown": message
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        print("Message sent successfully")
    else:
        print("Failed to send message")

# upload a file (screenshot) to the space
def upload_screenshot(space_id, screenshot_path):
    url = api_url + "/messages"
    headers = {
        "Authorization": "Bearer " + access_token,
    }
    files = {
        "roomId": (None, space_id),
        "files": open(screenshot_path, "rb")
    }
    response = requests.post(url, headers=headers, files=files)
    if response.status_code == 200:
        print("Screenshot uploaded successfully.")
    else:
        print("Failed to upload screenshot.")


# Main function
def main():
    space_id = create_space()
    if space_id:
        add_members(space_id)
        publish_url(space_id)
        send_message(space_id)
        #screenshot_path = "/path/to/screenshot.png"  # Update with the actual path of the screenshot file
        screenshot_path = "screenshot.png"  # Replace with the actual filename of the screenshot

        upload_screenshot(space_id,screenshot_path)

# Run the script
if __name__ == "__main__":
    main()