# twitterclone

What we're going to do is build a small clone of Twitter. It will feature logged in users, a customized homepage, a tweet composing page, the ability to follow other users, and more. We'll be using every single concept from the previous applications plus a few more; don't worry though, we've got plenty of time. The video from the demo I gave on my site is / will be linked at the bottom of this assignment.

This project is divided into two parts. Part 1 is all about the folder structure. Part 2 is going to be implementing the logic and front end, and there's lots of resources available to help. 

Your Task
Part 1

There will be four pieces to this application, each with their own app:

twitterclone <-- This is your project folder
twitteruser <-- This is a custom user app!
tweet
authentication
notification
Note: Please follow PEP8's guidelines on naming conventions for your packages and modules (https://www.python.org/dev/peps/pep-0008/#package-and-module-namesLinks to an external site.). Mainly, just name them exactly how they are listed above.

Each app will (potentially) need its own:

models.py
views.py
urls.py
forms.py
__init__.py
Set up the initial folder structure and create all the files you'll need -- get the settings.py file configured and the django server ready to go. In Part 2, we'll start filling in the files with logic.

Please make sure you create a .gitignore file in your project directory, and use the following  (Links to an external site.)Links to an external site.text from .gitignore.io for Django projects (Links to an external site.)Links to an external site.. 

Part 2

Though this assignment requires some new knowledge, everything I used is either on stackoverflow or in the Django documentation. Some pieces that might help you:

https://stackoverflow.com/a/16614136 (Links to an external site.)Links to an external site.
https://docs.djangoproject.com/en/3.0/topics/db/examples/many_to_many/ (Links to an external site.)Links to an external site.
https://stackoverflow.com/questions/9410647/how-to-filter-model-results-for-multiple-values-for-a-many-to-many-field-in-djan (Links to an external site.)Links to an external site.
https://docs.djangoproject.com/en/3.0/howto/static-files/ (Links to an external site.)Links to an external site. <-- only if you want to deliver custom CSS
https://stackoverflow.com/questions/18622007/runtimewarning-datetimefield-received-a-naive-datetime (Links to an external site.)Links to an external site.
https://docs.djangoproject.com/en/3.0/ref/templates/builtins/#include (Links to an external site.)Links to an external site.
The demo video covers only the front end, and things like pretty CSS and formatting are completely optional. What matters is that the backend performs the work and it can deliver the user experience. It's up to you to design the backend and make it functional. You may have to do it more than once as your application gains complexity, but hopefully you don't!

Whatever you can write that delivers the pages and functionality shown in the video is good enough. Some suggestions:

Segment each major section of your app into its own folder, then put another copy of the appropriate files under it. For example, `from tweet.models import Tweet`.
Use the `include` keyword I linked above; it will make your templating so much easier.
Create a single function that organizes all the data most of your templates need; then you only have to import that helper function into each view that performs a large render and you know the information will already be there.
Take a look at the rubric for more specific requirements.

Submission
Submit a link to your repo

https://github.com/<github_username>/twitterclone
Rubric
Attack of the Twitterclones
Attack of the Twitterclones
Criteria	Ratings	Pts
This criterion is linked to a Learning OutcomeUsers can access specific tweets by URL without being logged in
1.0 pts
Full Marks
0.0 pts
No Marks
1.0 pts
This criterion is linked to a Learning OutcomeUsers can access specific users by URL without being logged in
1.0 pts
Full Marks
0.0 pts
No Marks
1.0 pts
This criterion is linked to a Learning OutcomeUsers cannot access '/' without being logged in
2.0 pts
Full Marks
0.0 pts
No Marks
2.0 pts
This criterion is linked to a Learning OutcomeUsers can sign up on their own
1.0 pts
Full Marks
0.0 pts
No Marks
1.0 pts
This criterion is linked to a Learning OutcomeUsers get redirected to /login/ when attempting to load the homepage without being logged in
1.0 pts
Full Marks
0.0 pts
No Marks
1.0 pts
This criterion is linked to a Learning OutcomeUsers have a page that they can write a 140 character tweet on
1.0 pts
Full Marks
0.0 pts
No Marks
1.0 pts
This criterion is linked to a Learning OutcomeAfter writing a tweet, that tweet appears (after a page refresh) for all accounts that follow the user (including the user).
3.0 pts
Full Marks
0.0 pts
No Marks
3.0 pts
This criterion is linked to a Learning OutcomeUsers can follow other users.
4.0 pts
Full Marks
0.0 pts
No Marks
4.0 pts
This criterion is linked to a Learning OutcomeUsers can unfollow other users.
2.0 pts
Full Marks
0.0 pts
No Marks
2.0 pts
This criterion is linked to a Learning OutcomeEvery tweet has a link to the author's profile page and a direct link to that specific tweet.
1.0 pts
Full Marks
0.0 pts
No Marks
1.0 pts
This criterion is linked to a Learning OutcomeIf a user mentions another through the @ syntax, that user receives a notification (after page refresh).
5.0 pts
Full Marks
0.0 pts
No Marks
5.0 pts
This criterion is linked to a Learning OutcomeViewing notifications makes new notifications go away.
2.0 pts
Full Marks
0.0 pts
No Marks
2.0 pts
This criterion is linked to a Learning OutcomeThe user profile section has a count of how many tweets that user has written.
1.0 pts
Full Marks
0.0 pts
No Marks
1.0 pts
This criterion is linked to a Learning OutcomeThe user profile section has a count of how many accounts that user is following.
1.0 pts
Full Marks
0.0 pts
No Marks
1.0 pts
This criterion is linked to a Learning OutcomeThere is a working button that sends the logged-in user to their profile.
1.0 pts
Full Marks
0.0 pts
No Marks
1.0 pts
This criterion is linked to a Learning OutcomeNo logic contained in models, forms, or urls files
1.0 pts
Full Marks
0.0 pts
No Marks
1.0 pts
This criterion is linked to a Learning OutcomeUses only three custom models: TwitterUser (custom user model, inherits from AbstractUser), Tweet, and Notification.
4.0 pts
Full Marks
0.0 pts
No Marks
4.0 pts
This criterion is linked to a Learning OutcomeRepo contains pyproject.toml that includes all necessary dependencies to run application
3.0 pts
Full Marks
0.0 pts
No Marks
3.0 pts
Total Points: 35.0
