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
- Validations are also applied to both the register and login boxes
![image](https://user-images.githubusercontent.com/107221772/194886416-c4a0b699-34a2-4a5b-b55e-01d7bea25be6.png)
![image](https://user-images.githubusercontent.com/107221772/194886538-5cf16cd5-cd3a-494f-bd26-e99193c267c9.png)
