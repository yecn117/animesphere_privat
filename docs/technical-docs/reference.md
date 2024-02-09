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

Success message (typically): "Your support request has been submitted successfully."
Error message: "All fields are required."

------------------------------------------------------------------------------------------------
### `home():`

**Route:** `/`

**Methods:** `POST`, `GET`

**Purpose:** 
This function is designed to manage the login and registration process within a web application by validating user inputs, storing user data in a database, and providing appropriate feedback to the user.

**Sample output:**

"Please enter user name and password!"

"Your user has been registered!"

"This username already exists!"

"Username or password is incorrect!"
