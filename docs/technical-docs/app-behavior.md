---
title: App Behavior
parent: Technical Docs
nav_order: 2
---

{: .label }
[Jane Dane]

# [App behavior]

AnimeSphere provides an interactive platform guiding users through an intuitive login system, the creation and participation in chatrooms, as well as additional information and contact pages. The app is built on a combination of Python, SQLite, HTML, CSS, and JavaScript to deliver a rich user experience.

**App Behavior:**

**Landing Page and Login System:**

Upon launching the AnimeSphere app, users are directed to the landing page, which offers options for registration and login.
Registration and login information is verified. During registration, if the data does not already exist in the database, it is stored. If the user already exists, a message indicating that the username is already taken is displayed.
In case of incorrect password or username input, an error message is displayed.
If the login credentials are correct and verified in the database, users are redirected to the homepage. This logic is implemented in Python.


**Homepage with Chatrooms:**

On the homepage, users see a list of all available chatrooms.
New chatrooms can be created by entering a name and uploading a profile picture. The data is sent via an HTML form to a Python route, which stores it in the database. Subsequently, a new chatroom window is created with predefined HTML and CSS.


**Navigation and Tab Bar:**

At the top of the app, there is a navigation bar with tabs for "Home," "About AnimeSphere," "Contact Us," and "Log out." This navbar is present on all pages of the app.
Navigation between pages is facilitated through simple HTML links embedded in the tabs of the navigation bar.


**Search Functionality for Chatrooms:**

Users have the option to search for specific chatrooms next to the navbar.
The user enters the desired term into the search form, which is sent to a Python route via HTML.
In the Python route, the term is searched for in the database. If the term is found, all other chatrooms are hidden, and only those that match the search term are displayed.
This provides users with a targeted selection of chatrooms that match their search criteria, facilitating navigation and interaction within the app.


**Chat Functionality:**

Each chatroom utilizes the same HTML document, with individual messages organized in the database.

Whenever a message is sent, it is stored in the database and associated with the specific chatroom where the message was sent.

The sent message is then sent to a Python route and stored in the database within the Python code.

The algorithm responsible for displaying messages is implemented as a for-loop within the HTML document. This loop iterates through the messages stored in the database for the respective chatroom and presents them to users.

Additionally, whenever a message is sent, the scroll bar automatically moves to the bottom, ensuring that users always see the latest message first. This facilitates tracking of the conversation and ensures a seamless user experience.


**About AnimeSphere and Contact Us Pages:**

On the "About AnimeSphere" page, users can find information about the philosophy behind AnimeSphere, the company's values, and its mission. This information is statically displayed on the page.

The "Contact Us" page allows users to contact support by filling out and submitting a form. The entered information, such as name, email address, and message, is sent to an appropriate Python route.

Within the Python route, the information from the contact form is processed and stored in the database, enabling efficient and timely support for the users.


**Log-out Function:**

The "Log out" function allows users to securely end their current session. Upon logging out, they are automatically redirected to the Landingpage via a simple HTML link. This redirection is designed to provide users with a seamless transition from their logged-in session back to the starting point of the app, where they have the option to log in again.

<details open markdown="block">
{: .text-delta }
<summary>Table of contents</summary>
+ ToC
{: toc }
</details>























