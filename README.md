# gene_search
A Searching Web App 

Install 

To install the web app you will need to be running Python 3 and Django 1.10. I have a requiements.txt file that has all the requirements.
You can use this using "pip install -r requirements.txt" in your terminal in the projects folder.


TEST 

to run my tests in your terminal go into the Gene_Search folder and run python manage.py test

RUNNING THE APPLICATION 

to run the application please download the folder. Make sure that the needed requirements are there. then in the project folder run 
python manage.py runserver then open your browser of choose and go to http://localhost:8000/ .  When doing the auto search sadly I
couldn't get the enter key to work, so you will have to actually hit the magnifying glass to do the search.


COMMENTS

Hey considering this was a challeneg I figured I put down some of the challenges I faced and some of the reasoning of why I did certain things. One of the bigger challenges I faced was getting my Query Set to return json. Originally I tried to use Django REST Framework
but ended up not being able to make it work. After many hours and a lot of failed attempts of trying and many pages of a google search later I got it to work. I have used API and AJAX before but not with Python and Django so it was a lot of fun figuring out how to make it work even if for awhile there was a learning curve. One of the things that was easier then I expected was converting the csv into SQLite and having it import right. I started with trying to import it
into regualr SQL but then it wouldn't import right so I decided to just stick with what I had. It ended up working pretty well but it did take awhile.  Something I had never done was tests and I found it very fun to figure out how it worked and it was so rewarding seeing when a test passed and you can  see your code working on an independent base so it would be easier to debugg if you test every step. So after working on this project with a lot of things I am  unfamilar with I really enjoyed myself and learned a lot on the way. Some things I would improve if I had more time. I would try and be able to press enter
and do the search instead of having to click the magnifying icon. Also trying to make the gene's clickable to show more information. Another thing that looked like a lot of fun was Pagination. So this is what I have and thank you for letting me work on it I really enjoyed myself. 
