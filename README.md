# Rach's Coffee Roasters - Full Stack Django Project 4

### Introduction
The project consists of an ecommerce site for an online coffee shop called Rach’s Coffee Roasters. The inspiration for this website came from my personal love for coffee which also brings my friends and myself closer together.
Normal users will be able to view the shop’s short introduction, contact the shop, view and search for different categories of coffee (ground coffee, instant coffee, coffee beans). They have to create a user account in order to add items to cart and make purchases. For logged in superusers, they have the CRUD (Create, Read, Update, Delete) rights. The site is designed in a way where it is intuitive for users to use and the deployed link can be found [here](https://lzq-django-coffee.herokuapp.com/).

Please register as a new user or use the following accounts to navigate the website:

To log in as a user without CRUD rights, please use the following:
````
Username: marygoh
Password: goh12345
````

To log in as a user (superuser) with CRUD rights, please use the following:
````
Username: admin
Password: rachcoffeeroasters
````

### UX
| User Stories        | Description   |  
| :------------- |:-------------| 
| 1    | As someone who loves coffee, I want to be able to make my own quality coffee at the comfort of my home.|
| 2    | As someone who is a friend of a coffee-lover, I want to be able to look at the different types of products and their descriptions which best suit the taste bud of a friend.|
| 3    | As someone who just happen to browse through this page, I want to be able to know about the different categories and the taste notes of individual products.|
| 4    | As someone who is a frequent visitor of the shop, I want to continue enjoying the convenience of ordering my favourite coffee online.|


The website will be designed based on the identified goals and hence allow users to do the following:

-view coffee products available on the website

-add coffee products to shopping cart (only when logged in)

-remove items from shopping cart (only when logged in)

-checkout from shopping cart and make payment through Stripe (only when logged in)

-search coffee products by names

-search products by cost

-register for an account for new users who wish to purchase products

-add new products (only when signed in as superuser)

-update product information (only when signed in as superuser)

-delete product (only when signed in as superuser)


(i) Wireframes

[Wireframes Full Stack](https://drive.google.com/open?id=1UnhRookhnV4_G75Wt2_pGjqgzN7CFKan)

### Project Skeleton - Features

**Existing Features**

-On left hand side of the navigation bar, it shows the name of the coffee shop ‘Rach’s Coffee Roasters’ which links to the homepage of the site. The homepage shows main banner of the page which will appear in every html pages and shows a short introduction to the site. It also shows the 3 main categories of coffee available in the store and users can click on link to start looking at the products.

-The next link on the navigation bar shows **Products** which redirects users to the show_products page when the link is being clicked. Users will be able to see all products with the name, category, description, image, and price. They can click on ‘add to cart’ which will add_to_cart the product selected and will be redirected to the shopping_cart page. When item has been added, a flash message will appear saying ‘Product has been added to your cart’ and users can dismiss message by clicking on the ‘x’.

#### For users who are not logged in
-Following which shows **Register** which redirects users to the register page when the link is clicked. This page allows new users to register for an account to start shopping. The page also shows the link for users to sign in if they already have an account. When account has been registered, a flash message will appear which says ‘You have successfully registered’ and users can dismiss message by clicking on the ‘x’.

-Lastly on the navigation bar shows the **Log In** link which allows users to log in if they have already registered an account previously. Users will log in with their username and password. When user has logged in, there will be a flash message which says ‘Logged in as <username>’ and users can dismiss message by clicking on the ‘x’. There is also a link for new users to the register page to register an account. Users can also click on forget password where they can enter their email address for instructions to be sent to them. This is a Django default password reset page.

#### For users who are logged in
-After the ‘Products’ link, they will see a **My Account** link which will redirect users to the page which shows them what they are logged in as. 

-They will then see the **Log Out** link which logs users out and redirect them back to the show_products/index page. When user has logged out, there will be a flash message which says ‘You have successfully logged out’ and users can dismiss message by clicking on the ‘x’.

-Lastly, they will see the **Cart** link which will display the number of items that has been added to the cart. When clicked, users will be directed to the view_cart page where they will be able to view their cart items where the product image, name, category, description and price will be displayed. Users can also choose to adjust their shopping cart quantity, choose to checkout or continue shopping. 

-When users click on checkout, they will be redirected to the payment page using Stripe Online Payment Platform. The items that they have checked out and the amount that they have to pay will be displayed and they will be able to pay using their credit card. Upon successful payment, users will be directed to a thank you page.

#### For superusers who are logged in
-Before the ‘Products’ link, they will see a **Add Product** link where they will be redirected to the create_product page. They will see a form which allows them to add products by inputting the name, description, category, price, image of the product where all fields are mandatory.

-At the **Products** (show_products) page, they will see the ‘update product’ button. When clicked, they will be redirected to the update_product page where they will be able to make changes to the product such as the name, description, category, price, and image of the particular product that they have selected.

-At the **Products** (show_products) page, they will see the ‘delete product’ button. When clicked, they will be redirected to the confirm_delete_product page where they will be asked to confirm their deletion. If they click ‘yes’, delete_product will be rendered and the product will be deleted. If they click no, they will be redirected back to the show_products page.


**Feature(s) for Future Implementation**

1) To allow users to add ratings and reviews for the coffee products
2) To add a live chat bot to answer user queries in real time
3) To add in the function of stock taking so that staffs do not need to keep track of the products’ stocks level. They will be notified to stock up on items that are low on stock count.
4) When users click on each category in the home page (index.template.html), their results will be filtered according to the category that they have selected.


## Testing (Manual)

(i) Mobile Responsiveness

The website has been tested on **Macbook Air/iPad Mini/iPhone XS/iPhone 6/ Sony Xperia** which covers various screen-size. The browsers used for testings are Google Chrome & Apple Safari.

During the testing process, I found out that:

-Cart number does not increase if same item is added. But quantity will be updated in shopping_cart page.


(ii) Test Cases

| Test Case(s)      | Test Description   | Outcome | 
| :------------- |:-------------| :-------------| 
| 1    | At the landing page, users will be able to see the navbrand, the 'Products' link, the 'Register' link, and the 'Log In' link on the navigation bar. When they scroll, they will see a banner image, a short introduction, another image,followed by the 3 coffee categories. | Pass|
| 2    | When users click on 'Shop Now' under the coffee categories, they will be redirected to the show_products page. | Pass|
| 3    | When users click on the 'Products' link on the navigation bar, they will be redirected to the show products page. | Pass|
| 4    | When users are at the show_products page, they will see the banner image, 'Our Products' title, Search by name bar, min cost bar, max cost bar, followed by the products below. | Pass|
| 5    | For each product, users will see the image, the product name, the product category, the product description, product price in SGD, and the 'Add to Cart' button. | Pass|
| 6    | When users click on 'Add to Cart', they will be redirected to the login page. | Pass|
| 7    | At the login page, users will see the banner image, title, link to register if they do not have an account yet, form to type in username and password, 'Submit' button, and 'Forgot Password' button. | Pass|
| 8    | When users' username and password matches,they will be redirected to the show_products page and a flash message will show 'Successfully logged in as (username)' | Pass|
| 9    | When users are logged in, they will see the 'Products' link, 'My Account' link, 'Logout' link, and 'Cart' link on the navigation bar. | Pass|
| 9    | When users click on 'My Account', they will be redirected to the profile page and will see the banner image, 'My Account' title, welcome message. | Pass|
| 10   | When users click on 'Logout', they will be redirected to landing/index page and see the flash message 'You have successfully logged out'. The links on the navigation bar will be back to showing 'Products', 'Register' and 'Log In'. | Pass|
| 11   | When users' username and password don't match, and error message 'Invalid username or password' will be shown. | Pass|
| 12   | When users click on submit when both the username and password fields are empty, 'This field is required.' will be shown. | Pass|
| 13   | When users click on 'Forgot Password', they will be redirected to a password reset page where they will be asked to enter their email address for password to be sent. Once users click on reet password, they will be redirected to a page which tells them that instructions to reset password has been sent. | Pass|
| 14   | When users click on link to register, they will be redirected to the register page. | Pass|
| 15   | At the register page, users will see the banner image, title, link to sign in if they already have an account, form to type in emai address, username, password, password confirmation, and submit button. | Pass|
| 16   | When users have successfully registered, they will be redirected to landing page/index page and a flash message will show 'You have successfully registered' | Pass|
| 17   | Users will get error messages if email address is not in right format, both passwords don't match, fields are empty. | Pass|
| 18   | When users click on 'Add to Cart' button when they are logged in, they will be redirected to the shopping_cart page where they will be able to see the product that they have just added and the flash message which says 'Product has been added to your cart' | Pass|
| 19   | At the shopping_cart page, users will see banner image, title, product image, product name, quantity with a minus and plus sign, price, total price, dustbin icon, 'Continue shopping' button and 'Proceed to checkout' button. They will also see the number beside the 'Cart' link on the navigation bar. | Pass|
| 20   | When users click on the plus button, the quantity will increase by 1 and the total price will be updated accordingly. | Pass|
| 21   | When users click on the minus button, the quantity will decrease by 1 and the total price will be updated accordingly. | Pass|
| 22   | When users click on 'Continue shopping', they will be redirected to the show_products page. | Pass|
| 23   | When users click on 'Proceed to checkout', they will be redirected to the Stripe Online Payment checkout page. | Pass|
| 24   | At the Stripe page, users will see the product(s) they ordered, the quantity, and the price. They will also be asked to pay with card and will have to input their email, card information, before their ordered gets processed. | Pass|
| 25   | When payment is successful, users will be redirected to a thank you page where they are told that they will contact via email and a button which redirects them to the show_products page. | Pass|
| 26   | When users complete the transaction, the number beside the 'Cart' link resets to 0 | Pass|
| 27   | When users login as superusers (admin), they will see an additional link on the navigation bar 'Add a Product' | Pass|
| 28   | When they click on 'Add a Product', they will see the banner image, 'Add a Product' title, form to type in name, description, price, category, upload image of the product they want to add, and a create product button.  | Pass|
| 29   | When they click on 'Create Product', they will be redirected to the show_products page where they will see the newly added product and see a flash message 'Product[product name] has been added!'  | Pass|
| 30   | At the show_products page, superusers will see 2 additional buttons other than the 'Add to cart' button. They will see 'Update Product' button and 'Delete Product' button.  | Pass|
| 31   | When they click on 'Update Product', they will be redirected to update_product page.  | Pass|
| 32   | At the update_product page, superusers will see the banner image, 'Update Product' title, and the form similar to 'Create Product' page except that they will see the previously input name, description, price, category, and image, and an update button.  | Pass|
| 33   | When superusers edit the name, description, price, category, image, they will have to click on the update button. They will be redirected to the show_products page and see the flash message 'Product[product name] has been updated.'  | Pass|
| 34   | When superusers click on 'Delete Product', they will be redirected to the confirm_delete_product page.  | Pass|
| 35   | At the confirm_delete_product page, superusers will see the banner image, title 'Are you sure you want to delete the product?', product name that they have selected to delete, and 2 buttons 'Yes, delete' and 'No'  | Pass|
| 36   | If superusers click on 'Yes, delete', they will be redirected back to show_products page and will not see the product that they have deleted.  | Pass|
| 37   | If superusers click on 'No', they will be redirected back to show_products page and will still see all the products.  | Pass|


## Technologies Used

* [HTML5](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5)
* [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
* [Javascript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)/[JQuery](https://jquery.com/download/)
* [Python3](https://www.python.org/)
* [Django 2.2.6](https://www.djangoproject.com/)
* [Uploadcare](https://uploadcare.com/)
* [Bootstrap4](https://getbootstrap.com/docs/4.0/getting-started/introduction/)
* [Google Fonts](https://fonts.google.com/)
* [Font Awesome](https://fontawesome.com/) 
* [GitHub]( https://github.com/)
* [Stripe](https://stripe.com/en-sg)
* [Heroku](https://www.heroku.com/)

## Deployment
### GitHub Deployment

My code was written using AWS Cloud9. AWS Cloud9 serves as the local repository which was then deployed to GitHub. Whenever a new commit is done to the master branch, the deployed site will be updated accordingly. 

This repository can also be deployed locally by cloning the repository. This can be done by going to the main page of the repository to clone/download directly into the editor of choice by pasting git clone into terminal.

I deployed the site to Github with the following steps:
1. Go to this repository's github [link](https://github.com/rachaelloh/django-coffee)
2. Click on settings --> Github Pages
3. Select "none" for the Source and then select "master branch"

To deploy the page locally:
1.	Go to the github [link](https://github.com/rachaelloh/django-coffee)
2.	Click on the Clone/download button and copy the URL 
3.	Set up and install your own Stripe and uploadcare accounts, and also install crispy forms
5.	To run the application locally, type `python3 manage.py runserver 8080` in bash

### Heroku Deployment

The website has been deployed to Heroku with reference to our lecturer Mr Paul Chor Kun Xin's notes/document. <br>

- The following steps are instructions for deployment to Heroku in the terminal:

1. Go to [Heroku](https://dashboard.heroku.com/) and register for an account

2. Install Heroku in your system with this command
 `sudo snap install heroku --classic`

3. Install these one by one following using pip3:
````
sudo apt install libpq-dev python3-dev
sudo pip3 install gunicorn 
sudo pip3 install psycopg2
sudo pip3 install Pillow
sudo pip3 install whitenoise 
sudo pip3 install dj_database_url
````

4. In the `settings.py` file, add Whitenoise to the middleware:
````
MIDDLEWARE = [ 
..... 
'whitenoise.middleware.WhiteNoiseMiddleware'
]
````

5. Create a repository in Github

6. Create a hidden file named `.gitignore` and add `.c9` in the file. Also add the following django files to be ignored taken from [here](https://gitignore.io/api/django)

7. In your terminal, type these commands to add the repository origin from Github:
````
git init 
git add . 
git commit -m "Your commit message" 
````

8. Login to Heroku from your terminal by using this command `heroku login -i`

9. Create a new app with a unique name with this command `heroku create <app_name>` replacing the <app_name> with a name of your choice

10. To check if the correct github repository and heroku app are connected to this project, use this command: 
`git remote -v`

11. In your app in Heroku in the settings tab, click on the 'Reveal Config Vars' button. Copy the exported variables from the `.bashrc` in Cloud9 over to Heroku Config Vars (omit quotes)

12. The Procfile contains a command that Heroku will run when the app starts. In the root folder, create a file named Procfile. Open the file and put the following:

```
web: gunicorn coffee.wsgi:application
```

where 'coffee' in my project name in this project.


13. Inside the `settings.py` add the URL of the heroku app into the ALLOWED_HOST section (without the https)

```
ALLOWED_HOSTS = ["lzq-django-coffee.herokuapp.com/", "*"]
```

14. Use this command to create a `requirements.txt` file which lists all the required packages needed for this project:
````
pip3 freeze --local > requirements.txt
````

15. At the project directory level, create a `Static` folder, which should  be on the same level as the `manage.py` file. Place some files inside here like images or text files

16. Add STATIC_ROOT to your settings.py file
We need this for Whitenoise to work (so that it can serve static files properly):

```
coffee/settings.py
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
```

Also make sure when you use static files in your template, you make use of the {% static .... %} helper.

Example
```
{% load static %}
<img src="{% static "images/hi.jpg" %}" alt="Hi!" />
```

17. Commit all files to Heroku with these commands
````
git add . 
git commit -m "deploy to Heroku" 
git push heroku master
````

18. To use the PostgresSQL database, type this to your terminal 
````
heroku addons:create heroku-postgresql
````

19. To check the URL to the database created, run this command
`heroku config` and copy this URL to be used later

20. In the `.bashrc` file, add the following
`export DATABASE_URL="database_url"` and restart the bash terminal

21. In the `settings.py` add `import dj_database_url` after all the other import statements

22. In the `settings.py` file, comment out the `DATABASES` section and add the URL copied from Heroku here
````
DATABASES = {'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))}
````

23. Save and restart the terminal

24. Make migrations with this command
````
python3 manage.py migrate
````

25. Commit all files to Heroku with these commands
````
git add . 
git commit -m "Updated settings.py" 
git push heroku master
````

26. Make a superuser with this command
`python manage.py createsuperuser`

27. At the very top right hand side of the page in Heroku, click "Open App". You will now be able to view the project in Heroku


## Credits

1) Images are taken from [Pexels](https://www.pexels.com/), and a variety of website links as shown below:

-https://www.discountcoffee.co.uk/products/lavazza-ground-coffee-qualita-rossa-250g

-https://www.mycuppa.com.au/brazil-freeze-dried-instant-coffee-500g

-http://www.symmetry.com.sg/for-sale-1/coffeebeans 

-https://www.indiamart.com/proddetail/malnad-coffee-powder-16088014397.html 

-https://www.colourbox.com/image/photo-shot-of-instant-coffee-powder-and-coffee-beans-image-2700463 

-https://club.atlascoffeeclub.com/4-main-types-of-coffee-beans/


2) Product names and descriptions taken from [illy](https://www.illy.com/en-gb/coffee)


3) [Stack Overflow](https://stackoverflow.com/)


4) Social Media Links ideas - Bootstrap Social Icons https://embed.plnkr.co/LpJLnT/


### Special Thanks to:

**Our Lecturer, Mr Paul Chor Kun Xin**

- For guiding us through hands-on learning and consultations to solve project issues.


**This is for educational use only.**


