API Endpoints:
--------------------------------
Note: Please look through the steps below to know how following API endpoints are working:

For registering: http://127.0.0.1:8000/api/register/


For login: http://127.0.0.1:8000/api/login/


For sending paragraphs: http://127.0.0.1:8000/api/insertparagraphs/


For finding the paragraphs having target word: http://127.0.0.1:8000/api/findparagraphs/



To execute the code, follow given steps:
------------------------------------------
1.pip install -r requirements.txt


2.Setup your database credentials in settings.py

Example:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'para',
        'USER':'postgres',
        'PASSWORD':'devansh'
    }
}


3.python manage.py migrate


4.python manage.py runserver




To have a look on the backend panel:
------------------------------------------
1.python manage.py createsuperuser (NOTE: Write DOB in YYYY-MM-DD format)


2.python manage.py runserver


3.Go to url: http://127.0.0.1:8000/admin




To use API:
-----------------------------------

Use Postman(Recommended) or Thunder Client for easy use

POST the data in form of JSON


![json](https://user-images.githubusercontent.com/62210359/233691951-1917161d-baf3-4f8e-9063-e61be0dc0861.png)




(A)Register in the API by following simple steps:
-----------------------------------------------------
1.After selecting the POST method, go to url: http://127.0.0.1:8000/api/register/

2.Send a POST request in form of JSON data


Example:


{
  "username":"devanshjha",
  "email":"devanshjha@gmail.com",
  "dob":"2002-09-08",
  "password":"Devansh@#123"
}


![one](https://user-images.githubusercontent.com/62210359/233692756-eaa6885e-f5d3-4c05-91a8-0096bac8dbd1.png)

You will receive data like this.


![image](https://user-images.githubusercontent.com/62210359/233694326-b8a91017-d973-422b-8dc3-9e3f143e6295.png)



(B)Login in the API by following simple steps:
-----------------------------------------------------
1.After selecting the POST method, go to url: http://127.0.0.1:8000/api/login/

2.Send a POST request in form of JSON data

Example:

{
  "username":"devanshjha",
  "password":"Devansh@#123"
}

![two](https://user-images.githubusercontent.com/62210359/233695088-6154fee2-9430-4ae4-9a03-b76c537546a3.png)


You will receive data like this.

![image](https://user-images.githubusercontent.com/62210359/233695182-8ad39459-7986-45f4-88dc-4e3c1b2c32f9.png)

Note:
------------------------
Take this token to fetch remaining API urls


(C)Send paragraphs to the API by following simple steps:
-----------------------------------------------------------

1.After selecting the POST method, go to url: http://127.0.0.1:8000/api/insertparagraphs/

2.Take the auth token and put in the header section like this:

![auth](https://user-images.githubusercontent.com/62210359/233696218-58b44b5f-b4a1-4dc2-958a-6bd718eaa37f.png)


3.Send a POST request in form of JSON data


Note: Don't forget to put "\n\n" to distiguish multiple paragraphs in a string.

Example:

{
  "paragraphs":"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Magna ac placerat vestibulum lectus. Elit duis tristique sollicitudin nibh sit amet commodo. Senectus et netus et malesuada fames. Fermentum iaculis eu non diam phasellus vestibulum lorem sed. Dictumst quisque sagittis purus sit amet volutpat consequat mauris. Aliquam ut porttitor leo a diam sollicitudin tempor. Consectetur a erat nam atlectus urna duis convallis. Sed viverra ipsum nunc aliquet bibendum enim facilisis gravida neque.\n\nMaecenas volutpat blandit aliquam etiam erat velit scelerisque. Lectus sit amet est placerat in egestas erat imperdiet. Ante in nibh mauris cursus mattis. Tellus rutrum tellus pellentesque eu tincidunt. Euismod quis viverra nibh cras pulvinar mattis. Proin nibh nisl condimentum id venenatis a. Quam elementum pulvinar etiam non quam. Arcu dictum varius duis at consectetur lorem donec. Aliquet porttitor lacus luctus accumsan tortor. Duis ut diam quam nulla porttitor massa id."
}

![three](https://user-images.githubusercontent.com/62210359/233695963-3b788783-2a7a-49da-a7a5-0e33bbddf5ac.png)


You will receive data like this.

![image](https://user-images.githubusercontent.com/62210359/233696594-ebf509a9-c800-4929-a768-0adf3df97fdb.png)



(D)Search the target word by following simple steps:
---------------------------------------------------------------

1.After selecting the POST method, go to url: http://127.0.0.1:8000/api/findparagraphs/

2.Take the auth token and put in the header section like this:

![auth2](https://user-images.githubusercontent.com/62210359/233697097-0e74dd18-de9e-42e4-bf14-1d2ff9b34c15.png)

3.Send a POST request in form of JSON data

Example:

{
   "word":"lorem"
}


![four](https://user-images.githubusercontent.com/62210359/233699121-9cf4b61c-8196-44bb-9d16-d8902f79e12c.png)


You will receive data like this.


![image](https://user-images.githubusercontent.com/62210359/233697507-ba812c87-6a47-42a7-96b5-e95b732e5c86.png)




API Designing Details
----------------------------------

Techstack Used: Django Rest Framework

Database used: Postgresql

Steps:

1.Firstly I just had to create a custom user using AbstractBaseClass. So I created a managers.py file in which I defined a class called CustomUserManager which was derived from BaseUserManager.


2.Then , I handled the user registration view through GenericAPIView and CreateModelMixin. Also I handled whether the data sent by user was valid or not.


3.For login purpose, I authenticated the user and provided a unique token by using rest_framework.authtoken.


4.For paragraphs, I created a model called ParagraphItem to store the paragraph and the words.


5.Then, I created views to manage functionality to store the paragraphs.I distiguised paragraphs from a group of paragraph. I tokenize the paragraph into words and store the words along with that parent paragraph.


6.Finally, to fetch top 10 paragraphs having the target word, I looked through all the paragraphs objects in the database and looked into the words array and sorted the resultant paragraphs on the basis of target count. Then I returned top 10 paragraphs with maximum instances of the target word.


7.I also used serializers where it was necessary.


8.User could push paragraphs or search paragraphs only if he/she has authentication token.





