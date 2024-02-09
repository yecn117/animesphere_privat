---
title: Design Decisions
nav_order: 3
---

{: .label }
[Jane Dane]

# [Design decisions]
{: .no_toc }

<details open markdown="block">nte
{: .text-delta }
<summary>Table of contents</summary>
+ ToC
{: toc }
</details>

## 01: [Title]

### Meta

Status
: **Work in progress** - Decided - Obsolete

Updated
: DD-MMM-YYYY

--------------------------------------------------------------------------------------------------------------------

### Problem statement

[Describe the problem to be solved or the goal to be achieved. Include relevant context information.]

**1. Problem Statement: Selection of a Suitable Authentication Method:**

The goal would be to implement a secure, user-friendly, and efficient method for authenticating potential users, allowing them to register and log in to access the app and its features, such as browsing chatrooms and sending messages.

**Security:** The authentication method must ensure that user data is protected and unauthorized access is prevented.

**User-Friendliness:** The method should be simple and intuitive to achieve high acceptance among users and make the registration and login process as smooth as possible.

**Scalability:** The chosen solution should be capable of handling a growing number of users without losing performance.

--------------------------------------------------------------------------------------------------------------------

**2. Problem Statement: Database structure**

The goal is to design a robust and scalable database structure for the chat application that enables efficient management of user data, chatrooms, and messages. The database structure should encompass the following main entities and their relationships:

User Accounts: Capturing user information such as username and password (hashed) among other relevant details. The structure should also support mechanisms for authenticating and authorizing users.

Chatrooms: Management of chatrooms, including their titles, descriptions, members, and possibly specific settings like visibility, access rights, and moderators.

Message Histories: Storing messages exchanged in chatrooms, including the content of the message, timestamp, sender, and associated chatroom IDs.

The database structure must be flexible enough to accommodate changes and expansions, such as adding new chatrooms, managing user roles, or implementing message encryption. It should also enable efficient data querying and manipulation to ensure smooth and fast performance of the application, even with growing data volumes and an increasing number of users. Ultimately, the database structure should be the core of the chat application, ensuring reliable and secure storage and management of information to enable an optimal user experience.


--------------------------------------------------------------------------------------------------------------------

**3. Problem Statement: Frontend technology:**

The goal is to choose suitable technologies for developing the user interface of a web application. The challenge lies in creating a simple and user-friendly interface that looks good and works across various devices. It involves making decisions to ensure that the website loads quickly, is easy to use, and looks appealing. This includes selecting tools and technologies that facilitate development and enable easy updating and maintenance of the website. Ultimately, we want to ensure that users have a positive experience when visiting the website and that the frontend development proceeds smoothly.

--------------------------------------------------------------------------------------------------------------------


### Decision

[Describe **which** design decision was taken for **what reason** and by **whom**.]

 **1. Design-Decision (Authentication method)**

 We focused on implementing a secure and user-friendly authentication method using password hashing with pbkdf2:sha256. This decision was based on the need to ensure a high level of security by securely storing user passwords, which is essential especially in today's climate where privacy and security are of paramount importance. The choice struck a balance between robust security and efficient performance without compromising user experience. By storing only hashed passwords, we effectively protect user data from potential data breaches. At the same time, the system remains responsive and scalable through efficient implementation in Python and SQLite. This strategy allows room for future expansions, such as the introduction of two-factor authentication, without the need for extensive overhaul of the application's basic architecture.

Decided by Yakub

--------------------------------------------------------------------------------------------------------------------

**2. Design-Decision (Database structure)**

The decision to structure the database, despite the teacher's directive to use SQLite, was based on the necessity to ensure an efficient and logically coherent organization of data that optimally supports the functionalities of the chat app. By dividing it into four main tables - User, Chatroom, Message, and Support - a clear separation of the different data categories was achieved, which improves both data integrity and query efficiency. The User table allows for the unique identification of users, while the Chatroom table provides the basis for creating and managing various chatrooms. The Message table forms the core of communication by associating messages with the corresponding users and chatrooms. Finally, the Support table serves to manage user inquiries, which is essential for customer support and feedback management. This structuring not only supports the basic requirements of the app, such as user authentication, message transmission, and support requests but is also flexible enough to integrate future expansions and functionalities. The decision to develop such a detailed and well-thought-out database structure, despite the directive to use SQLite, has given us a deeper understanding of the requirements for a scalable and user-friendly chat app.

Decided by Luka

--------------------------------------------------------------------------------------------------------------------
**3. Design-Decision (Frontend technology)**

The decision to design the frontend using specific CSS libraries demonstrates an effort to develop a vibrant and appealing design. A significant part of these efforts included the integration of the Bootstrap library, which played a fundamental role in shaping the user interface. Utilizing Bootstrap allowed us not only to accelerate development but also to ensure that our web application operates smoothly on various devices and screen sizes, which is essential for providing a responsive and accessible user experience. However, we found that not everything went smoothly, and the responsive design did not always work as expected. Nevertheless, this experience was not in vain, as it enabled us to gain valuable insights and improve our skills in user interface development. Through these design decisions, we aim to enhance user engagement and promote a positive perception of the application.

Decided by Yakub


--------------------------------------------------------------------------------------------------------------------
### Regarded options

[Describe any possible design decision that will solve the problem. Assess these options, e.g., via a simple pro/con list.]

**To 1. Design Decision (Authentication method)**

An alternative design decision for the authentication method could be the use of OAuth to enable authentication through external services such as Google, Facebook, or Twitter.

| Pro                                        | Cons                                       |
|--------------------------------------------|--------------------------------------------|
| + Enhanced access for various user groups    | - Increased complexity of the application    |
| + Privacy-focused login options              | - Additional maintenance effort              |
| + Targeting specific audiences               | - Potentially confusing user experience      |
|                                            | - High dependency on external services       |


**Evaluation:**

Developing custom authentication provides us with the opportunity to delve deeply into the security aspects of web development. It allows us to learn from the ground up how user data is securely stored and managed. We can gain hands-on experience with password hashing and integrating a database like SQLite. This option promotes a comprehensive understanding of authentication processes and strengthens our skills in backend development. However, we are aware that this method can be time-consuming and requires a high level of care to avoid security vulnerabilities.

On the other hand, implementing OAuth through the use of external services like Google or Facebook offers a faster and potentially more secure solution. This method allows us to focus on other aspects of app development as we need to worry less about the details of authentication. OAuth could improve the user-friendliness of our app by enabling users to sign in with existing accounts, lowering the barrier to entry. However, there is concern that by choosing this method, we might miss out on the opportunity to gain deeper insights into authentication technology.

Ultimately, we believe that opting for custom authentication is most suitable for our study project. Despite the potentially higher effort and greater challenge, we see it as a valuable opportunity to deepen our understanding and skills in web development. This decision aligns with our main goal of learning through practical experience, even if it means we need to engage more deeply in addressing security concerns. We are confident that the learning outcomes associated with this decision will be invaluable for our future careers as developers.

--------------------------------------------------------------------------------------------------------------------

**To 2. Design-Decision (Database structure)**

An alternative design decision for the database structure could involve using a document-oriented approach, such as MongoDB, instead of a relational database structure.

| Pro                                  | Cons                                 |
|--------------------------------------|--------------------------------------|
| + Flexibility in sata storage        | - Less strict data integrity         |
| + Rapid development                  | - Complexity of queries increases.   |
| + Scalability                        | -  Security concerns                 |


**Evaluation:**

The use of a document-oriented database like MongoDB could be more efficient than the original relational structure in some scenarios. This approach offers flexibility and scalability for applications with large, variable data sets such as a chat app. However, challenges with data integrity and security can arise, as document-oriented databases offer less stringent mechanisms. The complexity in queries and less established ACID transactions are also considerations.

After carefully weighing the pros and cons of both approaches, we conclude that using SQLite better suits the project's requirements and the app's schema itself. Opting for SQLite provides a solid foundation for a relational database structure that enables well-structured and interconnected data. This is crucial for managing user accounts, chatrooms, messages, and support requests in our chat app. Additionally, SQLite offers easier setup and integration, which is particularly advantageous for a study project that may have limited resources and time.

--------------------------------------------------------------------------------------------------------------------

**To 3. Design-Decision ()**

| Pro                                      | Con                                             |
|------------------------------------------|-------------------------------------------------|
| + Enables variables and mixins,          | - Requires learning Sass                        |
|   making CSS more efficient and          | - Needs to be compiled into CSS, adding an      |
|   maintainable                           |   additional step in the development process    |
| + Promotes reusable code and helps       | - Additional tooling dependencies               |
|   keep stylesheets organized             |                                                 |
| + Allows for advanced designs and        |                                                 |
|   features                               |                                                 |



**Evaluation:**

Overall, complementing Bootstrap with Sass provides a powerful combination that gives developers more control and flexibility in designing the frontend. The ability to keep the code clean, organized, and maintainable while leveraging advanced styling features makes Sass a valuable addition to any frontend project.

However, utilizing the advanced features of Sass was not necessarily required as the project was already well-supported by the robust CSS features of Webkit. Additionally, the CSS library offered numerous useful design features, such as background image animation with background-clip, which were implemented in the code. Nonetheless, the time investment required to delve into Sass was deemed not worthwhile as the existing CSS and Bootstrap features were already sufficient to meet the project's design requirements.