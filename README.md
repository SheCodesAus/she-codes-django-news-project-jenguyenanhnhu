TITLE: She Codes News

Heroku: https://jn-she-codes-news.herokuapp.com/news/
Last I checked, Heroku was serving up error 500 so I screenshot everything. Not sure how to add screenshots into README for a Mac device but so all screenshots are in 'Screenshots folder'.

SCREENSHOTS:
1. 'index.html' shows index or home page.
2. 'myAccount.html' shows user's account information if they are logged in, displaying their username as well as stories they have edited which I achieved by filtering stories by author.
3. 'Authored_Story' shows a story I can select 'Edit' because I am the author. 
4. Notice that with 'Another_Story' authored by a different user, I cannot edit. 

Issue: 
- getting image submitted in 'Publish Your Thoughts' form to load for article and on index page. 
- formatting forms. I tried using widgets and bootstrap 'class': 'form-control' but it didn't change them. 
- Every time I click on a story, it always shows screenshot 'error1' because it has issues with the url having an <int:pk> in it. Then when I click to edit, 'error2' shows to now add <int:pk>. Not sure how to not get any errors.  
