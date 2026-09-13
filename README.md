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
