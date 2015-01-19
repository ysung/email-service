##Email-service
A service that accepts the necessary information and sends emails. It should provide an abstraction between two different email service providers. If one of the services goes down, your service can quickly failover to a different provider without affecting your customers.

###Whether the solution focuses on back-end, front-end or if it's full stack.
Back-end

###Reasoning behind your technical choices, including architectural.
Because I have used Python in data mining and machine learning, I am more comfortable in this concise programming language.
I separated different senders to different files. New sender can be easliy implemented without influence to the other senders.

###Trade-offs you might have made, anything you left out
The project assumes users provide valid API key and API URL. The system should add a feature to check if the user is authorized to use the API in the future.

###what you might do differently if you were to spend additional time on the project.
I will use Flask in this project. Flask is a microframework and impressive with built-in development server and fast debugger, Jinja2 templating, RESTful request dispatching and integrated support for unit testing. Beside, I will use regular expression to detect the invalid emails.

###Link to other code you're particularly proud of.
I have used R to complete data analysis and statistical visualization on social network.
https://github.com/ysung/R

###Link to your resume or public profile.
* My LinkedIn: www.linkedin.com/in/ycsung
* My AngelList: https://angel.co/yun-chieh-sung
* My Email: Yun-Chieh Sung, s.yunchieh@gmail.com
