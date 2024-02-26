---
title: App Structure
parent: Technical Docs
nav_order: 1
---

# [App structure, incl. context]

### 1. env Directory:
The `env` directory houses the virtual environment for the Python application, creating an isolated setting for the Animesphere app. This ensures that all necessary Python libraries and dependencies can be installed and managed specifically for the project without affecting the system or the environments of other projects. The subdirectories and the `pyvenv.cfg` file contribute to making the setup reproducible and consistent across different development environments.

### 2. font Directory:
The `font` directory is crucial for the visual appearance of the Animesphere app. By providing custom fonts, it helps create a unique and appealing design that enhances the user experience, offers Font Awesome for iconographic elements, and visually supports the Animesphere brand.

### 3. instance Directory:
The `instance` directory contains the app's database file and is central to data storage. The database allows for the persistent storage of user data, chat logs, and other important information. This is essential for features such as user authentication, message history, and managing chat rooms.

### 4. static Directory:
The `static` directory stores static files like CSS and images needed for the styling and design of the application. Organizing into subdirectories (css and img) allows for a clear separation between style sheets and media files. This facilitates the maintenance and updating of the app, enabling quick access to the required resources.

- css Subdirectory: Stores the CSS files that ensure a uniform and appealing design of the web pages.
- img Subdirectory: Hosts images and videos that enrich the visual appearance of the app, along with specific folders for chat rooms and randomly selected images that contribute to personalizing the user experience.

### 5. templates Directory:
The `templates` directory contains HTML templates for the various pages of the Animesphere app. The close linkage of HTML documents with corresponding CSS files (same name) simplifies development and maintenance by creating a clear connection between design and structure. This promotes efficient workflow and helps maintain clarity.

### 6. main.py File:
The `main.py` file is the core of the Animesphere app. It integrates the entire business logic, route management, and server configuration. The decision to consolidate all application logic into a single file contributes to the clarity and simplification of the code. This facilitates understanding of the application flow and supports maintenance as well as troubleshooting.
