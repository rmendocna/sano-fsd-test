# Sano Genetics Full-stack engineer task

## Comments and Answers

This whole task took me considerable time
1. I am still employed in my current position - this was only possible at later hours
2. I do not use Flask - had to browse some to go through these

In an attempt to deliver this sooner than later I dismissed the Loom presentation and 
merely address the following task in writing, without sample implementation.

It has nonetheless been very entertaining to learn a bit Flask and Tailwind.
Also appreciate your work setup and architecture.


#### Task 6
As suggested below, browser’s localStorage could hold the fragments of data in between page loads.

#### Task 7
The feature would be implemented in a Study ‘detail’ page.

Current posts titles + authors’ names would be listed by date somewhere below the main study contents.

Clicking a given title could bring up a modal/lightbox with the full text of the post,, followed by the full list of comments, stacked up, with the authors’ name next to each corresponding comment. Again, sorted by date.

Sample models:

    class Posts(BaseModel):
       author = ForeignKeyField(Users)
       study = ForeignKeyField(Studies)
       title = CharField(255)
       body = CharField(1500)

    class Comment(BaseModel):
       author = ForeignKeyField(Users)
       others_post = ForeignKeyField(Posts)
       content = CharField(500)
These wouldn't allow to comment on comments.

Authors or `webmasters`/moderators should be allowed to delete their own comments.

Contributed content should be sanitised to prevent both code injection and inappropriate
language.

Additionally could consider whether only users enrolled in said study could be allowed to issue a Post on the given Study.

#### Task 8 - Password security
(On this whole subject maybe best to delegate password storage/validation to social accounts (google, twitter, facebook or any other relevant OAuth2 provider) )

Did google and considered these checks https://www.geeksforgeeks.org/password-validation-in-python/

Aside from these a couple more to take into account that its alphanumerical components is not:

    1. a variation/subset of the corresponding username/email

    2. a common name - although this would be language-dependent and a lot more complex and time-consuming to check against a potentially huge catalog of names

#### Task 9 - Token authentication
Not aware of such schemes. 
An unattended browser session could allow for a human scripter 
to access the auth token by its key in the browsers localStorage and eventually check the Network history and gain access to one's account.
 
But I am sure this is nearly off topic. 