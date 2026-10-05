Name : Goeij Angelatika Goeyanto

NPM : 2506656772

Class : PBP A+


### Assignment 1

1. Yes, I used semantic HTML5 elements such as <main>, <section>, and <header> in my porfolio. For example, I seperated my profile and organizational experience into a different <section>.

Using semantic elements helped me structure the static website based on the overall content, which makes the HTML easier to read and maintain because I can immediately which part of the code that I am currently working on. It also made it easier to insert CSS into parts of the website without relying entirely on generic <div> elements.

Through this, I learned that semantic help us make the code look more organized to the point that it is aesthetically pleasing to the eyes, and the structure is very easy to understand which will be easier if developed further in the future.

2. One of my main challenges and the one that i spent the most time on was modifying the cursor. At first, my custom cursor did not appear even though the CSS code was correct. Trying to spot out all the possible mistakes, I realized that the problem was probably not with the code itself but with the image file that I was using. Turns out to be the file dimentions to be too large for the cursor. 

After modifiying the image, I was able to change the cursor of my choice. This experience taught me that if something does not work, its probably not the code itself, but can come from external factors such as image dimentions, file formats, etc. 

3. Since my website is static, the interaction that I can give is limited. Currently, I have added hover animation so that it doesnt look too stiff and feel more interactive.

One of the biggest limitation is that I cannot really position the elements freely. I wanted to decorate my page with scattered strawberries, but since all of my elements follow the structure of their respective containers, it would be really hard to put an element that intersects the container. 

I would love to be able to place elements in the middle of other elements so it can allow me create more interesting visuals rather than having every element follow a fixed layout.

4. AI Disclosure: I used AI (ChatGPT) when I had an idea but did not know how to implement it. I would ask how to add a hover animation, how to change the cursor, how to modify certain elements. However, I do not just copy paste whatever code it gave me. I would take the suggestion and modify it based on what I actually want and needed for my website.

The code that AI gave me is more of a suggestion and I still had to figure out whether it actually works with my existing code. I had to test and change it many times before getting the result that I actually wanted.

I also noticed that noy every problem can be solved by asking AI. I was trying to commit and push to github and PWS, however, it took me quite amoung of time because the issues I have received were unsolveable with AI, which led to researches on Google & consultations with an upperclassmen to guide me.

Also encountered problems when trying to modify my custom cursor. The code had no issues, after some manual troubleshooting, I was able to customize my cursor, which was unsolvable with AI.

Overall, AI is useful to give suggestions on how to implement, but it does not replace the process of actually understanding and testing every step of work. 

AI Prompting Log : https://chatgpt.com/share/6a9d8c8a-e0ec-83ec-863c-30d88a0abc1d

### Assignment 2
Clarification: 
a. Projects == Volunteering Projects 
b. Experience == Organizational Experience
c. Contact == Contact Me

1. When the user open the page of the Projects page, for example by going to /projects/, the browser first sends a request to the django project. The projects urls.py receive the request and direct it to the URL configuration of the main application. Then, main/urls.py checks the URL and match /projects/ with show_projects, which is connected to the shows_projects

The view gets the data that is needed for the page. So show_projects retrieves all the Project objets from the database by using the Project model. The data that was received is being placed into project_list and then passed to the project.html template. The template uses Django Template Language, such as a {% for %} loop, i have also used it to display other things such as project title, description, and year without fully hard coding it.

2. The portfolio data is better to be stores in a model instead of being written directly inside the template because it seperates the data from what the website shows. For example, instead of head coding a project title and description inside projects.html, i can use {{project.title}} and {{project.description}} to it displays information retrieved from then database.

This makes the website much easier to maintain. If I want to change a project description or add a new project, i only need to update the database rather than manually editing the HTML. This makes the data more flexible, organizem and easier to update as the portfolio grows.

3. Makemigration: create a migration file that records the changes made to the model. which basically tells django what changes need to be made to the database structure

Migrate = the one that is applying those changes to the database. Example: if i have a Project model and add a new field to it, I would first run python manage.py makemigrations. then django will create a migration file containing the change, then i will run python manage.py migrate to apply the change to the database.

4. AI Disclosure: I used AI (ChatGPT) as a supporting tool when I needed help with specific parts of the object. The django implementation, including the use of models, views, URLs, and migrations was done following the instructions and concept taught in Tutorial 2.

For assignment 2, I aksed AI for suggestions on what test cases I could & whether or not the test case that i think of can be added to make sure that my Project page is working correctly, and whether the empty state was displayed when there were no projects.

I also used AI when i encoutered error in the terminal. One of the examples: when i try to do >>> python manage.py makemigrations, i received a SyntaxError. I asked AI why this happened because the command itself is correct. 

Turns out, python manage.py makemigrations is not a Python syntax and should be instead be run directly in the terminal.

Since I have moved a section to another page, which made that section empty, I brainstormed on what else can i add in that section, which ended up to be the contact me section. I used AI to guide me making the Contact Me section where the users of the website can enter their information and send me a message. I adapted it to my code and modified the HTML and CSS to fit my liking.

Overall, I use AI mainly as a supporting tool. Most of the Volunteering Project's development follows the materials and instructions provided in Tutorial 2 which then AI helps me when I encouter specific problems or when I am unsure how to approach a particular feature (such as the Contact Me section)

AI Prompting Log: https://chatgpt.com/share/6aa6cfc4-4b74-83ec-8e77-18ddc43a2629

### Assignment 3
1. ModelForm is used because it makes it easier to make forms on a model without having to manually make every HTML form frield. ModelForm automatically input the form fields based on the fields in the model, and it also handle validation and save hte submitted data to the database. This makes the vode very easy to maintain, make the code shorted, and reduce the possibility of errors compared to making the form manually.

We also need to add {% csrf_token %} to forms that use POST requests because Django uses CSRF protection to prevent Cross-Site Request Forgery attacks. THE CSRF token is a secret unique token created by server in purpose to secure application from malicious and unauthorized request.

2. JSON is preffered in modern web application development because it has a simpler and more compact structure than XML. JSON is also easier for humans to read and write, and it is easily processed by programming alnguages, especially JavaScript. 

It is convenient for transferrign structured data between a server and a client because JSON uses a key value paris and arrays. Which makes it common to be used in frontend and backend.

3. When a view function needs to return portfolio data in JSON format, the process start when the client sends a request tot he Django view. The view take the data from the database throught the Django model. However it cannot be directly returned as JSON because the data received from the database is represented as Django model objects

Which is why we need to do serialization which converts the Django model objects and their data into a format that is compatible. After that, DJango can return the serialized data through a HttpResponse with content_type="application/json". The client can then receive and process the data as JSON.

4. AI Disclosure: I did not use any AI tools in this assignment as I have been referring to Tutorial 3.

### Assignment 4

-- Sep 24 - Sep 26, 2026
I worked on Tutorial 4 by implementing the basic authentication features, including registration, login, and logout. I also added the login status and last_login information, and restricted certain Project actions so that only authorized users could access them.

I then added the star feature using ManyToManyField. This allows logged-in users to star or unstar a Project while also keeping track of how many users have starred each Project.


-- Sep 26 - Sep 27, 2026
I continued with Individual Assignment 4 by implementing an Editor role using Django Groups and Permissions. The Editor is allowed to edit existing Project data but doesnt have permission to create or delete Projects.

I also updated the templates so that the available actions depend on the current user's role. For example, the Edit button is available to Editors and the portfolio owner, while Create and Delete are limited to the portfolio owner.

Finally, I tested the authorization system using different types of users, including visitors, regular users, Editors, and the superuser. I checked both the buttons shown on the website and direct access through the URL to make sure unauthorized users receive a 403 Forbidden response.

-- Sep 27 - Sep 28, 2026
I improved the portfolio's visual presentation by adding a horizontal carousel for the Project section. This makes it possible to browse through multiple Projects by scrolling horizontally instead of displaying everything in a long vertical list.

I also adjusted the layout and styling so that the carousel fits better with the existing design of the portfolio.

AI Disclosure: I did not use any AI tools in this assignment as I have been referring to Tutorial 3. 
Reflective Question: This week’s reflective question has been removed


### Assignment 5

-- Sep 28 - Sep 30, 2026

I worked on Tutorial 5 by applying AJAX and JavaScript interactivity to the Education section of my portfolio. I changed the Education page so that the data is loaded through a JSON endpoint uses a Fetch API. I also added loading, empty, and error states so the page can show different conditions when fetching the data.

I then added an AJAX search feature for Education with debouncing. This allows the search results to update without reloading the page, while debouncing prevents a request from being sent every time I type a character.

-- Oct 4 - Oct 5, 2026

I continued Individual Assignment 5 by adding the Add Education feature using a modal and Fetch API. The form uses a ModelForm to validate the submitted data, and the server returns JSON responses with suitable HTTP status codes. I also kept the permissions from Assignment 4, so only authorized users can add and delete Education data.

After successfully adding Education data, the list is refreshed using AJAX without reloading the page. I also added toast notifications for successful actions, errors, and when data is deleted. When the server returns validation errors, the error messages are displayed directly through the toast notification so the user can understand what went wrong.

I also added the delete functionality using AJAX and the existing delete URL. This allows the Education item to be deleted without requiring the whole page to reload, while still checking the user's permissions on the server.

Finally, I added XSS protection to the Education section. Text values returned from the server are escaped before being inserted into HTML, and the ModelForm also cleans text input using strip_tags. This prevents user input containing HTML or JavaScript from being executed when the data is displayed.


1. Debouncing is a technique where we wait for a short amount of time after the user stops typing before sending the AJAX request. This is useful for search because without debouncing, a request would be sent every time the user types a character. For example, if the user types "University", the application could send many requests while the word is being typed. With debouncing, the application waits until the user stops typing and then sends only one request. This makes the search more efficient and reduces unnecessary requests to the server.

2. await is used with fetch() so that the JavaScript code waits for the request to finish before continuing to the next line. For example, when we write const response = await fetch(url), the response is available before we try to process it. If we do not use await, fetch() returns a Promise instead of the actual response. This means the code could try to access the response before the request has finished, which can cause errors or make the program not work as expected. await makes it easier to handle asynchronous operations in a sequential way.

3. Cross-Site Scripting (XSS) is an attack where malicious HTML or JavaScript is inserted into a website and then executed when another user views the data. Data displayed through AJAX and JavaScript can be more vulnerable because we manually insert the returned data into the HTML using JavaScript. If the value is inserted directly without escaping it, the browser may interpret the value as HTML or JavaScript instead of normal text. For example, a value such as <img src="x" onerror="alert('XSS!')"> could execute JavaScript if it is inserted directly into the page. This is why values inserted through JavaScript need to be escaped, such as by using escapeHtml or textContent. Server-side cleaning using strip_tags also provides another layer of protection.

4. AI Disclosure: I used AI (ChatGPT & Claude) as a supporting tool when I needed help a specific parts of the assignment. Most of the implementation was done by following the concepts and instructions provided in Tutorial 5, especially the implementation of AJAX, Fetch API, debouncing, modal forms, toast notifications, and XSS protection.

For Assignment 5, I used AI for the delete functionality for the Education section. I had troubles making the deleteEducation work, so I asked AI for suggestions on how I could modify the existing delete action and connect it with the deleteUrl so that the deletion could be handled without reloading the page. One limitation I encountered was that the AI could not fully determine how my existing Django delete view and HTML structure worked without me checking my own code. AI initially explained different possible ways of providing the deleteUrl, so I had to compare its suggestions with my actual Django URL configuration and dynamically generated Education cards. I also had to make sure that the suggested JavaScript matched the way my project was already structured.

I made sure that the deleteEducation function worked with the existing fetchEducation() function so that the Education list could be refreshed after a successful deletion, and that the toast notification could show whether the deletion was successful or failed.

Overall, I used AI mainly as a supporting tool when I encountered a specific problem or was unsure about how to approach a particular implementation. The majority of the Assignment 5 development was done by following the concepts and examples taught in Tutorial 5 and adapting them to my own Education section.

AI Prompting Log:
    1. https://claude.ai/share/b923ff19-8266-47d3-b314-71b5f92479f7 
    2. https://chatgpt.com/share/6ac3ae7e-2368-83ec-b19a-19a1d29d0c85