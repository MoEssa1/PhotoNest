# Family Photo Sharing

<img width="1278" alt="Screenshot 2024-08-14 at 01 03 57" src="https://github.com/user-attachments/assets/401952b7-7c5e-4b7a-9e75-b71c8b8347a3">
<img src="" alt="" width="600">

PhotoNest is an intuitive web application designed to provide a seamless experience for families to create, manage, and share their precious memories. Users can easily create profiles, upload photos, add captions, and tag images for easy retrieval. PhotoNest will also in the future include social features such as likes and social media integration, fostering a sense of community and connection among family members.

The live application can be viewed here:  
[https://photo-nest-a8d0a3c57905.herokuapp.com/](https://photo-nest-a8d0a3c57905.herokuapp.com/)

## Overview

- [Purpose and Target Audience](#purpose-and-target-audience)
- [User Stories](#user-stories)
  - [Implemented Features](#implemented-features)
  - [Future Features](#future-features)
- [Wireframe & Initial Design](#wireframe--initial-design)
- [Agile](#agile)
- [Design Choices](#design-choices)
  - [Colour Scheme](#colour-scheme)
  - [Typography](#typography)
  - [Home Page](#home-page)
- [Features](#features)
  - [Login](#login)
  - [Register/Sign Up](#registersign-up)
  - [Welcome Page / Gallery](#welcome-page--gallery)
  - [Add Photo](#add-photo)
  - [Edit Photo](#edit-photo)
  - [Delete Photo](#delete-photo)
  - [Filter Using Tags](#filter-using-tags)
- [Database Diagram](#database-diagram)
- [Data Models Used](#data-models-used)
- [Validation & Testing](#validation--testing)
  - [HTML Testing](#html-testing)
- [Responsiveness](#responsiveness)
- [Links](#links)
- [Tools & Technologies](#tools--technologies)
- [Languages](#languages)
- [Deployment](#deployment)
- [Bugs](#bugs)
- [Credits](#credits)

## Purpose and Target Audience

**Problem Statement:**  
In today's digital age, families often struggle to organise and share their photos in a centralised and user-friendly manner. Existing solutions either lack the necessary features for effective organisation or are too complex for everyday users. There is a need for a dedicated platform that simplifies the process of storing, tagging, and sharing family photos while maintaining a high level of user engagement and interactivity.

**Purpose:**  
The purpose of PhotoNest is to provide a user-friendly platform where families can effortlessly store, organise, and share their photos. By offering features such as profile creation, photo tagging, captioning, and social media integration, PhotoNest aims to enhance the way families interact with their digital memories. The platform will also foster a sense of community by allowing family members to like and comment on each other's photos in the future.

**Target Audience:**  
The primary target audience for PhotoNest includes:

- **Families:** Parents, grandparents, and children who want to preserve and share their memories in a private and organised manner.
- **Photographers:** Amateur and professional family photographers who need a platform to showcase their work to family members.
- **Social Media Users:** Individuals who frequently use social media and want a dedicated space to share personal photos with their family without the noise of public platforms.
- **Tech-Savvy Users:** People who are comfortable with technology and seek a more sophisticated tool for photo management than traditional photo albums.

By addressing the needs of these groups, PhotoNest aims to become the go-to platform for family photo management and sharing.

## User Stories

### Implemented Features

#### Profile Creation (Basic)
As a user, I can create an account that generates a default profile, so I can access and manage my photo collections.

- **Acceptance Criteria:**
  - Users can create an account with their first name, last name, and email address.
  - A default profile is created upon account creation.

#### Photo Upload
As a user, I can upload photos with captions and tags, so I can organize my photos and provide context for each image.

- **Acceptance Criteria:**
  - Users can upload photos from their device.
  - Users can add a caption to each photo.
  - Users can add up to three tags per photo.

#### Photo Management (CRUD)
As a user, I can edit and delete my photos, so I can manage my photo collection and ensure only the best photos are shared.

- **Acceptance Criteria:**
  - Users can edit the caption and tags of an uploaded photo.
  - Users can delete photos from their collection.
  - Users receive a confirmation prompt before a photo is permanently deleted.

#### Photo Tagging
As a user, I can tag my photos with specific keywords or phrases, so I can easily search and filter photos based on different occasions or themes.

- **Acceptance Criteria:**
  - Users can add tags to photos during the upload process.
  - Users can edit tags of an existing photo.
  - Users can search for photos using tags.

### Future Features

#### Profile Customisation
As a user, I want to be able to personalize my profile with additional details and social media links, so I can connect more meaningfully with my family members.

- **Planned Improvements:**
  - Users will be able to edit their profile information, including adding social media links.
  - Users will be able to upload and display a profile picture.

#### Group Photo Sharing
As a user, I want to group myself with particular family members, so photos shared will only be visible to those in the group.

- **Planned Features:**
  - Users will be able to create and join family groups.
  - Photos shared within a group will only be visible to group members.

#### Social Features (Likes)
As a user, I want to like my family members' photos, so I can show my appreciation and stay engaged with their updates.

- **Planned Features:**
  - Users will be able to like photos uploaded by other users.
  - The total number of likes will be displayed beneath each photo.
  - Users will be able to see which photos they have liked.

#### Search Functionality
As a user, I want to search for photos using tags, captions, or dates, so I can quickly find specific images from my collection.

- **Planned Features:**
  - Users will be able to search for photos by entering keywords in a search bar.
  - Search results will display photos that match the entered tags, captions, or dates.
  - Users will be able to filter search results by tags or date ranges.

## Wireframe & Initial Design:

In the initial stages of design, I utilized Balsamiq and Canva to create wireframes that guided the development of the application. Balsamiq allowed me to quickly sketch out the basic structure and layout of the interface with a focus on usability and user experience. Canva complemented this by enabling me to add visual details and polish the design concepts. Together, these tools helped me visualize the flow of the application and make informed decisions about the placement of key features and elements.

**Wireframes**
  ![Screenshot 2024-08-14 at 00 03 33](https://github.com/user-attachments/assets/2b6ac582-5ef3-4f17-8c87-3770e513e0a8)
  ![Screenshot 2024-08-14 at 00 16 39](https://github.com/user-attachments/assets/07e79883-74cd-4659-a241-9bc4a1f3856e)
  <img width="300" alt="Screenshot 2024-08-13 at 18 50 13" src="https://github.com/user-attachments/assets/f4a64252-02d8-4c57-b420-70c9e92f5450">
  <img width="300" alt="Screenshot 2024-08-13 at 18 50 23" src="https://github.com/user-attachments/assets/303e5132-6ad3-4515-981c-4f0c7faeff57">
  <img width="300" alt="Screenshot 2024-08-13 at 18 50 43" src="https://github.com/user-attachments/assets/fe4735c2-97a7-4288-97d4-79e996a37073">
  <img width="300" alt="Screenshot 2024-08-13 at 18 50 53" src="https://github.com/user-attachments/assets/9694ade2-bcca-4c05-a600-7e42add4421f">
  <img width="300" alt="Screenshot 2024-08-13 at 18 51 05" src="https://github.com/user-attachments/assets/1a6e1f22-f9e8-4ba7-9acf-3f73f1c2f750">



## Agile

Throughout this project, I applied Agile methodologies, a practice I became familiar with through our guided sessions and previous hackathons. These experiences provided me with a solid foundation in Agile principles, which I implemented consistently during development. I utilised GitHub's project board as a Kanban system to organise and track my tasks effectively. Additionally, I employed the **MOSCOW** method to prioritise features by importance, allowing me to focus on delivering a Minimum Viable Product (MVP) first. This approach ensured that I stayed on track, met my goals, and minimized distractions.

- **Kanban Board**
<img width="648" alt="Screenshot 2024-08-14 at 00 45 50" src="https://github.com/user-attachments/assets/915ff8a2-e9a8-4801-bb21-6835b5b1eab6">

## Design Choices:

### Colour Scheme:
- `#5e17eb` - Navbar
- `#bcbefa` - Logo
- Black - Buttons & Icons
- `#fed305` - Footer
- A colourful background picture with hints of rainbow colours was also used.
<img width="714" alt="Screenshot 2024-08-13 at 22 17 05" src="https://github.com/user-attachments/assets/22fb1646-1440-433f-998a-ecf0f407f102">


### Typography:

The chosen fonts for this project are `"Permanent Marker", cursive` and `"Fjalla One", sans-serif`. This combination was selected to balance creativity and readability. `"Permanent Marker"` offers a playful, handwritten style, making it ideal for headers or titles that need to stand out and convey a personal touch. Meanwhile, `"Fjalla One"` provides a clean and modern sans-serif style, ensuring that body text is highly legible and professional. Together, these fonts create a visually appealing contrast, enhancing both the user experience and the overall aesthetic of the application.
![Screenshot 2024-08-14 at 00 50 43](https://github.com/user-attachments/assets/a87b781c-71b1-4c37-9fac-ac383396162a)


### Home Page:

<img width="1278" alt="Screenshot 2024-08-14 at 01 03 57" src="https://github.com/user-attachments/assets/583f102b-db5b-438d-a917-7f09058191b9">


The home page of PhotoNest welcomes users with a vibrant and colorful design, featuring a visually engaging background with rainbow-like hues. The header displays the PhotoNest logo and easy navigation links for "Home," "Register," and "Login," allowing users to quickly access different parts of the application. The central section of the page prominently features a warm welcome message in the playful "Permanent Marker" font, drawing attention to the app's purpose.

Below the welcome message, an image is displayed within an oval frame, adding a personal touch and emphasizing the family-oriented theme of the platform. The introductory text provides a brief overview of PhotoNest, highlighting its role as an intuitive web application for families to create, manage, and share their cherished memories.

The footer includes the creator's name, along with social media icons, encouraging users to connect and explore further. Overall, the home page effectively sets the tone for the application, combining functionality with an inviting and user-friendly design.

## Features:

### Login:

<img width="641" alt="Screenshot 2024-08-14 at 01 09 00" src="https://github.com/user-attachments/assets/0db9744f-30dd-4894-ad04-504348b12298">

### Register/Sign Up:

<img width="641" alt="Screenshot 2024-08-14 at 01 08 50" src="https://github.com/user-attachments/assets/04118a84-2dab-477a-8f9a-318afda35002">

### Welcome Page / Gallery:

![Screenshot 2024-08-14 at 01 12 20](https://github.com/user-attachments/assets/9a853887-2ec5-416e-a485-d0462a930ab1)

### Add Photo:

![Screenshot 2024-08-14 at 01 14 21](https://github.com/user-attachments/assets/22fb1d21-0afc-4b49-b083-9ef4b2b4abad)

### Edit Photo:

![Screenshot 2024-08-14 at 01 16 45](https://github.com/user-attachments/assets/b1988a25-cb77-4ca5-8db0-3a99fdf0e507)

When users choose to edit a photo they have previously uploaded, the application provides a user-friendly interface that includes a preview thumbnail of the photo they are editing. This visual cue helps users easily identify the image they are working on. The tags that were originally selected for the photo are preselected, allowing users to see and adjust the current tags effortlessly. Users also have the option to create new tags, and any changes made during the editing process will overwrite the previous selections, ensuring that the photo's metadata is up-to-date and accurately reflects the user's intentions.

### Delete Photo:

![Screenshot 2024-08-14 at 01 22 05](https://github.com/user-attachments/assets/6abd4f03-c7a6-42ee-a679-beb405b1130d)

### Filter Using Tags:

![Screenshot 2024-08-14 at 01 22 46](https://github.com/user-attachments/assets/80f58d6a-23ba-4680-a3e3-e79b2e367d8e)


## Database Diagram:

To design the database diagram for my project, I used Luna Modeler. This tool allowed me to visually map out the relationships between various entities in my application, ensuring that the data structure was both efficient and logically sound. Luna Modeler’s intuitive interface made it easy to define the fields, set relationships, and visualize how different components like users, profiles, photos, and tags would interact within the database. This diagram was crucial in guiding the development of the backend architecture of my application.
<img width="830" alt="Screenshot 2024-08-03 at 00 33 47" src="https://github.com/user-attachments/assets/d8b9dba2-98e9-4ac9-9640-4b2296672329">

## Data Models Used:

- `OneToOneField`
- `ManyToMany`
- `CharField`
- `ForeignKey`
- `DateTimeField`
- `ImageField`
- `PositiveIntegerField`

## Validation & Testing:

### HTML Testing:

I used the W3C HTML Validator to ensure that all my HTML code was up to standard. The validator confirmed that everything passed except for one issue on the page where individual photos are displayed. The error was due to the images not having an alt attribute, which is essential for accessibility and screen readers. In the future, I plan to enhance this feature by allowing users to provide an alt attribute when they upload their photos. This will not only resolve the validation error but also improve the accessibility of the application for all users.

![Screenshot 2024-08-14 at 01 46 19](https://github.com/user-attachments/assets/173f50f7-ac2d-4d6e-98f1-ed19b935fdef)

The W3C CSS Validator also Passed.

![Screenshot 2024-08-14 at 02 05 37](https://github.com/user-attachments/assets/38685757-de7c-4ff9-8f50-1229a27a0e80)

## Responsiveness:

The application has been thoroughly tested for responsiveness across various browsers to ensure a seamless user experience on different devices. This testing included Google Chrome on both desktop and mobile, Firefox, and Safari on mobile. The design and functionality were consistently maintained, ensuring that users can easily navigate and interact with the application regardless of their browser or device.

<img width="400" alt="Screenshot 2024-08-03 at 00 33 47" src="https://github.com/user-attachments/assets/dce25d27-3165-4f55-9110-3df5dfa31e67">
<img width="400" alt="Screenshot 2024-08-03 at 00 33 47" src="https://github.com/user-attachments/assets/6945849c-c8ab-42a7-b39e-46d35a826c5b">
<img width="400" alt="Screenshot 2024-08-03 at 00 33 47" src="https://github.com/user-attachments/assets/46f73630-aeb6-4422-9dc3-f8320f6efea4">
<img width="400" alt="Screenshot 2024-08-03 at 00 33 47" src="https://github.com/user-attachments/assets/52c57070-8614-40fa-8f51-556954585973">

![Screenshot 2024-08-14 at 02 37 42](https://github.com/user-attachments/assets/054dff2c-1bc1-496e-b4d5-daa789938fcd)
![Screenshot 2024-08-14 at 02 38 03](https://github.com/user-attachments/assets/1b053c07-eec8-4535-9064-7f63cb67f8cd)
![Screenshot 2024-08-14 at 02 38 21](https://github.com/user-attachments/assets/cc483302-9f65-4565-b804-315d3f0664f1)
![Screenshot 2024-08-14 at 02 38 52](https://github.com/user-attachments/assets/4b828fec-245c-401f-80fd-f43a5abc1d5b)

## Links:

- **Deployment:** [https://photo-nest-a8d0a3c57905.herokuapp.com/](https://photo-nest-a8d0a3c57905.herokuapp.com/)
- **GitHub Repository:** [https://github.com/MoEssa1/PhotoNest](https://github.com/MoEssa1/PhotoNest)
- **Kanban Board:** [https://github.com/users/MoEssa1/projects/4](https://github.com/users/MoEssa1/projects/4)

### Tools & Technologies

- **Python**: Utilized as the back-end programming language for application logic and data handling.
- **Git**: Employed for version control, managing changes with commands like `git add`, `git commit`, and `git push`.
- **GitHub**: Served as the platform for secure online code storage and collaboration.
- **GitHub Pages**: Used to host the deployed front-end of the application.
- **Gitpod**: A cloud-based IDE leveraged for development and seamless coding experience.
- **Bootstrap**: Implemented as the front-end framework to ensure modern responsiveness and provide pre-built components.
- **Postgres**: Selected as the primary database for data storage and retrieval.
- **Heroku**: Used for deploying the entire project, providing a reliable and scalable hosting environment.
- **Cloudinary**: Utilized for storing static files and managing images online.
- **Balsamiq**: Applied for wireframing and prototyping during the initial design phase.
- **Canva**: Used alongside Balsamiq for creating design elements and additional wireframes.
- **Google Fonts**: Incorporated to enhance typography with web-friendly fonts.
- **Favicon**: Implemented to improve brand recognition and visual identity in browser tabs.
- **Font Awesome**: Used to add scalable vector icons that enhance the user interface.


### Languages:

- **Front End:** HTML, CSS/Bootstrap
- **Back End:** Python/Django

## Deployment:

I successfully deployed my application on Heroku, utilising its reliable and scalable hosting environment. This allowed me to manage and run my app seamlessly, ensuring that it is accessible online with robust performance and easy maintenance.

## Bugs:

During development, I encountered several bugs, ranging from database connection issues to UI inconsistencies. However, through diligent debugging, testing, and iteration, I was able to resolve all of them, ensuring the application runs smoothly and functions as intended.

## Credits:

This project wouldn't have seen the light of day without the amazing support and resources I had access to. Big shoutout to the LMS learning syllabus — it was my go-to guide throughout, especially those blog walkthroughs that saved me more than once. Being able to jump back and revisit topics whenever I got stuck was a game-changer.

I can't thank the Code Institute crew enough, especially Lewis, David, and Spencer. These guys were absolute legends, always there to guide me, offer feedback, or just cheer me on. Their patience and expertise kept me on track and motivated.

Of course, the vast world of documentation and YouTube tutorials played a huge part too. Whenever I hit a snag or needed a different perspective, there was always a video or article ready to help me out.

Last but not least, a massive thanks to Unsplash.com for the stunning photos that brought my album to life. Their collection added that extra touch of beauty to the project.

