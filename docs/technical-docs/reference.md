---
title: Reference
parent: Technical Docs
nav_order: 4
---

{: .label }
[Jane Dane]

# [Reference documentation]
{: .no_toc }


<details open markdown="block">
{: .text-delta }
<summary>Table of contents</summary>
+ ToC
{: toc }
</details>

## [Section / module]
-------------------------------------------------------------------------------------------------------------
### `func submit_support_request():`

**Route:** `/submit_support_request/`

**Methods:** `POST`

**Purpose:** 

**Functional purpose:** The function processes POST requests to the route /submit_support_request. When a user requests support via a form on the website, the entered information such as name, email, subject, and message is extracted from the form.

**Processing the request:** The function checks if all required fields have been filled out. If not, an error message is displayed and the user is redirected back to the contact page.

**Saving the request:** If all fields are filled out, a new support request is created and saved in the database.

**Redirection and success message::** After successfully processing the request, the user is redirected to the contact page and receives a success message. 

**(Important Note: Despite a potential minor error or typo, while the success message may not be displayed as intended, the data is still forwarded and stored in the database. However, an error message regarding the support request will still be displayed.)**
                                      

**Sample output:**

Success message (typically): "Your support request has been submitted successfully." (failed)


Error message: "All fields are required."

![Info Missing](/docs/technical-docs/doc-img/infomissing.png "info-missing")

------------------------------------------------------------------------------------------------
### `home():`

**Route:** `/`

**Methods:** `POST`, `GET`

**Purpose:** 
This function is designed to manage the login and registration process within a web application by validating user inputs, storing user data in a database, and providing appropriate feedback to the user.

**Sample output:**

"Please enter user name and password!"

![Username and Password Output](/docs/technical-docs/doc-img/Username-PW.png "Username and Password Output")

"Your user has been registered!"

![Registered Output](/docs/technical-docs/doc-img/registered.png "Registered Output")

"This username already exists!"

![Already Exists Output](/docs/technical-docs/doc-img/us-already-exists.png "Already Exists Output")

"Username or password is incorrect!"

![False Data Output](/docs/technical-docs/doc-img/falsedata.png "False Data Output")

------------------------------------------------------------------------------------------------
### `rooms():`

**Route:** `/rooms`

**Methods:** `GET`

**Purpose:** 

The function first checks if the user is logged in by looking for a username in the session. Users who are not logged in are redirected to the home page. For logged-in users, the function retrieves all chat rooms from the database. If a search term is provided, it filters the chat rooms to only show those that match the search criteria. If no chat rooms are found or the search yields no results, an appropriate message is displayed. Finally, the function renders an HTML page that presents the chat rooms (or a message if none were found). This functionality allows users to view existing chat rooms and search for specific chat rooms.

**Sample output:**

1. **Gerenderte HTML-Seite mit allen Chaträumen**

<ul>
  <li>Chatroom 1</li>
  <li>Chatroom 2</li>
  <li>Chatroom 3</li>
</ul>


![Chatroomliste](/docs/technical-docs/doc-img/Chatroomliste.png "Chatroomliste")



2. **Gerenderte HTML-Seite mit gefilterten Chaträumen**

<ul>
  <li>Chatroom 2 - Filtered Result</li>
  <li>Chatroom 3 - Filtered Result</li>
</ul>


![filtered-chatroomlist](/docs/technical-docs/doc-img/filtered-chatroomlist.png "filtered-chatroomlist")


3. **Nachricht über keine Suchergebnisse**

<p>No chatrooms found!</p>

![no-chatrooms-found](/docs/technical-docs/doc-img/no-chatrooms-found.png "no-chatrooms-found")