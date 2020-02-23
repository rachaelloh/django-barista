# Rach's Coffee Roasters - Full Stack Django Project 4

### Introduction
The project consists of an ecommerce site for an online coffee shop called Rach’s Coffee Roasters. The inspiration for this website came from my personal love for coffee which also brings my friends and myself closer together.
Visitors will be able to view the shop’s short introduction, contact the shop, view and search for different categories of coffee (ground coffee, instant coffee, coffee beans). They have to create a user account in order to add items to cart and make purchases. The site is designed in a way where it is intuitive for users to use and the deployed link can be found [here](https://.herokuapp.com/).

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

[Wireframes DataCentric](https://drive.google.com/open?id=1UnhRookhnV4_G75Wt2_pGjqgzN7CFKan)

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

Implement sign in feature for users such that only signed in users can share recipes and only delete their own recipes.

The ability to upload images for individual recipes.


## Testing (Manual)

(i) Mobile Responsiveness

The website has been tested on **Macbook Air/iPad Mini/iPad/iPhone XS/iPhone 6/ Sony Xperia** which covers various screen-size. The browsers used for testings are Google Chrome & Apple Safari.

During the testing process, I found out that:

-On devices such as iPhone X or smaller screen sizes, the brand logo 'Recipe Sharing' overspills to the next line. Hence I added media query such that from screen sizes of iPhone X and below, the font size will decrease.

-Search results will not be shown if I did not type in the exact cuisine name. Hence, the regular expression function has been used to make search function dynamic.

-Ordered list was unable to display properly in the view recipe page. Hence, I used split to solve the problem and the steps is now able to be displayed in an ordered list.


(ii) Test Cases

| Test Case(s)      | Test Description   | Outcome | 
| :------------- |:-------------| :-------------| 
| 1    | Users will see all recipes at the landing page. | Pass|
| 2    | If on mobile, users will see a navbar on top with a hamburger on the left and the brand logo 'Recipe Sharing' in the middle. | Pass|
| 3    | When users click on the hamburger, they will see 3 links 'Search by Cuisine', 'All Recipes', and 'Add Recipe', on top of one another| Pass|
| 4    | If on web browser on laptop/desktop, users will see a navbar on top with the brand logo on the left and the other 3 links 'Search by Cuisine', 'All Recipes', and 'Add Recipe' on the right side. | Pass|
| 5    | At the landing page, when users click on the edit button, they will be able to edit and update the recipe that they selected. | Pass|
| 6    | At the landing page, when users click on the delete button, they will be able delete the selected recipe. | Pass|
| 7    | At the landing page, when users click on the view button, they will be able to see the details of the recipe that they have selected where the ingredients appear as an unordered list and the cooking steps appear as an ordered list. | Pass|
| 8    | When users click on the 'Search by Cuisine' button on the navbar, they will be able to see a search bar and the list of recipes below. | Pass|
| 9    | When users search for the cuisine that they want, relevant results will appear below. | Pass|
| 10   | When users click on the 'All Recipes' button and the brand logo 'Recipe Sharing', it will direct them to the main/landing page. | Pass|
| 11   | When users click on the 'Add Recipe' button, they will see a form where they can choose a cuisine category by clicking on the dropdown button, add their recipe name, the ingredients and the cooking steps. After adding, the recipe will be shown in the All Recipes page. | Pass|


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
* [Heroku](https://www.heroku.com/)

## Deployment
### GitHub Deployment

My code was written using AWS Cloud9. AWS Cloud9 serves as the local repository which was then deployed to GitHub. Whenever a new commit is done to the master branch, the deployed site will be updated accordingly. 

This repository can also be deployed locally by cloning the repository. This can be done by going to the main page of the repository to clone/download directly into the editor of choice by pasting git clone into terminal.

### Heroku Deployment

- Project was also deployed and hosted to heroku. Website can be found [here](https://lzq-recipe-share.herokuapp.com/)
- Created Procfile and requirements.txt for dependencies.
- Created new heroku app and set environment variables.
- Linked Github and environment with Heroku.
- Project was pushed to Heroku once in awhile to ensure that update features are working.


## Credits

1) Website design/outlook was inspired by http://recipebook-project.herokuapp.com/

2) Background image was taken from [Pexels](https://www.pexels.com/)

3) [Stack Overflow](https://stackoverflow.com/)

4) [w3schools](www.w3schools.com)

**This is for educational use only.**


