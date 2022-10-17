## This repository serves as storage for a project I completed while attending the Coding Dojo bootcamp
### My project which is named Keystone MMA is a website that I built using Python, Flask, MySQL, HTML, CSS, and Javascript after completing the first programming stack I ever learned
### The goal was to not only create a website with basic information about the business, but to also create a user experience area that members of the gym can use to chronical and review different techniques learned during BJJ classes. 
### At completion the project was originally launced on Heroku, however, due to changing policies, it has since been removed
### Below you will find descriptions of the website and the work that I did to complete it

## Home Page:
![image](https://user-images.githubusercontent.com/107221772/194883875-eee6de55-bcff-4f75-8d17-131eb7ee3bb0.png)
- The top of the home page was created using CSS flex properties. The navigation links are fully functional and will take you to different parts of the website
![image](https://user-images.githubusercontent.com/107221772/194884213-bd4915f2-b052-460b-b301-62cc25a43fd0.png)
- This is the main content on the homepage, I utilized a plug in to connect the businesses facebook page so users can view pertinent updates
## About and Schedule
- The about and schedule page were built using HTML/CSS and a provide basic descriptions of the business to the users
## Contact
- For the contact page I added, and utilize the Google Maps API to include the location of the gym
- Users can manipulate the map using the tools provided by Google
- I was also able to include a custom map marker
![image](https://user-images.githubusercontent.com/107221772/194884930-ea6f50d2-b939-4b47-bcc3-3aa1e0e4aed0.png)
## My Account
- Clicking this button will bring you to a page in which you can either register for the website or login
- Upon completing either task you will be redirected to the members only portion of the website
- Once logged in session is used to track user activity, and you can go to any portion of the website, then return to the members only area without issue
- If someone attempts to navigate to a members only area and they are not logged in the will be redirected to the My Account page to login/register
![image](https://user-images.githubusercontent.com/107221772/194886155-1ecc63be-3892-44ba-a1a8-095a4358ea63.png)
- When creating an account hashing and bcryt are utilized prior to the users password being stored in the database
- REGEX is used for both the email and password, ensuring that certain standards are met
![image](https://user-images.githubusercontent.com/107221772/194886416-c4a0b699-34a2-4a5b-b55e-01d7bea25be6.png)
![image](https://user-images.githubusercontent.com/107221772/194886538-5cf16cd5-cd3a-494f-bd26-e99193c267c9.png)
- Validations are also applied to both the register and login boxes
## Dashboard
- Upon logging in users are brought to there dashboard where they update/delete their account, and add/view techniques in the database
- Users can also view BJJ news by clicking the button which takes them to a different portion of the website
- Upon clicking update users are brought to an update page in which they can update their name, phone number, and email in the database
- Deleting a user removes them from the database and clears session
![image](https://user-images.githubusercontent.com/107221772/194887400-2e4e5f6f-cf88-47ed-b3dc-6dac5b9f15bc.png)
## View Techniques
- On this page you can view all of the techniques that have been entered into the database
- There is also a search bar that you can use to find a specific technique
= Any user can view a technique, but only the user that created a technique can edit or delete it from the database
![image](https://user-images.githubusercontent.com/107221772/196205650-fed0c1a6-fb53-4176-9fcd-454b81ae60bd.png)
## Adding a technique
- Upon clicking this button you will be brought to a page where you can create your own techniques
- A technique will consist of mulitple categories, most of which have to be included in order to pass validations
- You can also include a url to an instructional video
![image](https://user-images.githubusercontent.com/107221772/196207731-0078e62c-ef87-48d7-b875-03bd545eb656.png)
## Viewing a single technique
- Upon clicking on a specific technique you will be brought to it's page
- Information on the page include its name, move type, instructions, difficulty level, and a url link if one is included
![image](https://user-images.githubusercontent.com/107221772/196206063-c39bc8df-469d-4eb1-b55f-997c8ef20704.png)
## Editing a technique
- clicking this button will bring you to a page where you can update your technique
= validations are included when trying to update
![image](https://user-images.githubusercontent.com/107221772/196206462-982e3ac4-31dd-48af-a6cf-9361ca0b8e70.png)
## BJJ News
- Link directing you to a portion of the website where another website is embedded
- The website was embedded using an iframe
![image](https://user-images.githubusercontent.com/107221772/196206721-a3fca9f1-666c-43b2-9368-84ebeb1adc9c.png)
## Log out
- After logging in, and while navigating the portion of the website where you have to be logged in a logout button is displayed
- Clicking this button will log you out and redirect you the homepage
- If you are navigating anywhere else on the website a 'My Account' button will be displayed instead which brings you back to the dashboard



