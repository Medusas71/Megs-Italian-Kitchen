<h1 align="center">Meg's Italian Kitchen - Testing Details</h1>

[View the main README.md document](README.md)

[View the deployed Meg's Italian Kitchen](https://megs-italian-kitchen.herokuapp.com)

**Please note: To open any links in this document in a new browser tab, press 'CTRL + click'.**

<a id=#table-of-contents></a>
# Table of Contents
<details open>
<summary><b>(click to expand or hide)</b></summary>
<!-- MarkdownTOC -->

[Testing](#testing)
* [Validators](#validators)
* [Lighthouse](#lighthouse)
* [Wave Report](#wave)
* [User Stories](#user-stories)
* [Manual Testing](#manual-testing)
* [Bugs/Fixes](#bugs-fixes)

<!-- /MarkdownTOC -->
</details>

<a id="testing"></a>
# Testing

Testing was conducted manually and through different validator services on each page of the website.

<a id="validators"></a>
## Validators

* [W3C Markup Validation Service](https://validator.w3.org/#validate_by_uri) was used on each page to 
ensure that there were no errors or warnings in my HTML document. I originally used the Direct Input, 
however I was getting jinja errors, as the HTML didn't like the Jinja code in Direct Input. So I used 
the Validate by URI, which ignored the jinja code and gave me a true indication of any errors or warnings.

  * One warning displayed as per the below screenshot.

![W3C HTML Validation Results](/static/images/testing-images/w3c/w3c-html-validator-results.jpg)

   * I spoke to Tutor Support regarding this error and they advised that I can ignore this error, as the error is referring to the "section" that is used for flash messages and will not contain any "heading" elements. 

  * No other errors or warnings displayed.  

  * Tutor Support also showed me the best way to validate html, which is to right click on the web page and select "view page source" and copy the code from there and paste into the direct input section of the html checker. This way the jinja code is ignored by the html checker.

* [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/#validate_by_input) was used to ensure that there were no errors or warnings in my CSS document and was validated by direct input. I had no errors or warnings display.

![W3C CSS Validation Results](/static/images/testing-images/w3c//w3c-css-validator-results.jpg)

* [Autoprefixer CSS Online](https://autoprefixer.github.io/) was used to ensure that all vendor prefixes 
were included in CSS. the results were copied into the style.css file.

* [Pep8](http://pep8online.com/) was used to check the app.py file. No errors or warnings displayed.

![pep8](/static/images/testing-images/pep8/pep8.jpg)

[Back to Table of Contents](#table-of-contents)

<a id="lighthouse"></a>
## Lighthouse  

Lighthouse was used to check for any problems on all pages. Unfortunately the scores were not as high as I would have liked. My heart sunk, especially as due to time restraints I haven't been able to look into these issues. It is something that will be addressed once the course is finished and I have more time to spend on each issue. 

I did try to rectify one of the issues regarding image aspect ratio, where I installed "npm i --save-dev css-aspect-ratio" and imported the plain css using a cdn however that did not rectify the issue. I realise there is more that needs to be done and this will be addressed once the course is finished.

Below is the lighthouse score for each page on mobile and desktop:

<details open>
<summary><b>(click to expand or hide)</b></summary>

### index.html - mobile

![index-mobile-lh](/static/images/testing-images/lighthouse/index-mobile-lh.jpg)

### index.html - desktop

![index-desktop-lh](/static/images/testing-images/lighthouse/index-desktop-lh.jpg)

### recipes.html - mobile

![recipes-mobile-lh](/static/images/testing-images/lighthouse/recipes-mobile-lh.jpg)

### recipes.html - desktop

![recipes-desktop-lh](/static/images/testing-images/lighthouse/recipes-desktop-lh.jpg)

### full_recipe.html - mobile

![full-recipe-mobile-lh](/static/images/testing-images/lighthouse/full-recipe-mobile-lh.jpg)

### full_recipe.html - desktop

![full-recipe-desktop-lh](/static/images/testing-images/lighthouse/full-recipe-desktop-lh.jpg)

### login.html - mobile

![login-mobile-lh](/static/images/testing-images/lighthouse/login-mobile-lh.jpg)

### login.html - desktop

![login-desktop-lh](/static/images/testing-images/lighthouse/login-desktop-lh.jpg)

### register.html - mobile

![register-mobile-lh](/static/images/testing-images/lighthouse/register-mobile-lh.jpg)

### register.html - desktop

![register-desktop-lh](/static/images/testing-images/lighthouse/register-desktop-lh.jpg)

### add_recipe.html - mobile

![add-recipe-mobile-lh](/static/images/testing-images/lighthouse/add-recipe-mobile-lh.jpg)

### add_recipe.html - desktop

![add-recipe-desktop-lh](/static/images/testing-images/lighthouse/add-recipe-desktop-lh.jpg)

### my_recipes.html - mobile

![my-recipes-mobile-lh](/static/images/testing-images/lighthouse/my-recipes-mobile-lh.jpg)

### my_recipes.html - desktop

![my-recipes-desktop-lh](/static/images/testing-images/lighthouse/my-recipes-desktop-lh.jpg)

### edit_recipe.html - mobile

![edit-recipe-mobile-lh](/static/images/testing-images/lighthouse/edit-recipe-mobile-lh.jpg)

### edit_recipe.html - desktop

![edit-recipe-desktop-lh](/static/images/testing-images/lighthouse/edit-recipe-desktop-lh.jpg)

</details>

[Back to Table of Contents](#table-of-contents)

<a id="wave"></a>
## Wave Report  

* [Wave](https://wave.webaim.org/) was used to check for accessibility issues on all pages. Some errors have displayed such as empty links and contrast errors. The empty link is not an issue as it is to do with the mobile side nav. The contrast errors will be fixed after I finish the course due to time restraints.

Below is the wave report for each page:

<details open>
<summary><b>(click to expand or hide)</b></summary>

### index.html

![index-summary](/static/images/testing-images/wave/index-summary-wave.jpg)
![index-details](static/images/testing-images/wave/index-details-wave.jpg)

### recipes.html

![recipes-summary](/static/images/testing-images/wave/recipes-summary-wave.jpg)
![recipes-details](/static/images/testing-images/wave/recipes-details-wave.jpg)

### full_recipe.html

![full-recipe-summary](/static/images/testing-images/wave/full-recipe-summary-wave.jpg)
![full-recipe-details](/static/images/testing-images/wave/full-recipe-details-wave.jpg)

### login.html

![login-summary](/static/images/testing-images/wave/login-summary-wave.jpg)
![login-details](/static/images/testing-images/wave/login-details-wave.jpg)

### register.html

![register-summary](/static/images/testing-images/wave/register-summary-wave.jpg)
![register-details](/static/images/testing-images/wave/register-details-wave.jpg)

### add_recipe.html

![add-recipe-summary](/static/images/testing-images/wave/add-recipe-summary-wave.jpg)
![add-recipe-details](/static/images/testing-images/wave/add-recipe-details-wave.jpg)

### my_recipes.html

* Unfortunately Wave wouldn't accept a users own recipes. A Key Error displayed. This may have something to do with having to be logged in to view the page. Due to time restraints, this will be looked into once I have finished the course.

![my-recipe-error](/static/images/testing-images/wave/my-recipe-key-error-wave.jpg)

### edit_recipe.html

![edit-recipe-summary](/static/images/testing-images/wave/edit-recipe-summary-wave.jpg)
![edit-recipe-details](/static/images/testing-images/wave/edit-recipe-details-wave.jpg)

</details>

[Back to Table of Contents](#table-of-contents)

<a id="user-stories"></a>
## User Stories 

### Testing User Stories from the UX section of [the main README.md document](README.md)

<details open>
<summary><b>(click to expand or hide)</b></summary>

Each screenshot displays a red square around each item that is needed to achieve the testing criteria.

### First Time Visitor Goals

* As a first time visitor to the website, I would like to search for Italian recipes.
  * This is achieved by clicking the Browse link on the home page or the Recipes link in the nav bar. Once you are on the All Recipes page you can search by recipe title, course and ingredients.

![1-browse-recipes](/static/images/testing-images/user-stories/1-browse-recipes-links.jpg)

![2-search-links](/static/images/testing-images/user-stories/2-search-links.jpg)

* As a first time visitor to the website, I would like to view various Italian recipes.
  * This is achieved by clicking the Recipes link in the nav bar and scrolling through the recipes. The visitor has an option to view the full recipe details.

![3-view-full-recipe](/static/images/testing-images/user-stories/3-view-full-recipe-link.jpg)

![4-full-recipe](/static/images/testing-images/user-stories/4-full-recipe.jpg)

* As a first time visitor to the website, I would like to be able to have the opportunity to register so I can add new recipes to the database.
  * This is achieved by having a Register link on the home page and in the nav bar that allows the user to Register.

![5-register](/static/images/testing-images/user-stories/5-register-links.jpg)

![6-register](/static/images/testing-images/user-stories/6-register.jpg)

### Returning Visitor Goals

* As a returning user to the website, I would like to have the ability to log in so I can view my recipes.
  * This is achieved by clicking the Log In link on the nav bar, logging in and clicking My Recipes.

![7-login](/static/images/testing-images/user-stories/7-login.jpg)

![8-my-recipes](/static/images/testing-images/user-stories/8-my-recipes.jpg)

* As a returning visitor to the website, I would like to have the ability to search for recipes whilst logged in.
  * This is achieved by clicking the Recipes link in the nav bar. Once you are on the All Recipes page you can search by recipe title, course and ingredients.

![9-search](/static/images/testing-images/user-stories/9-search-recipes.jpg)

* As a returning visitor to the website, I would like to have the ability to add a recipe.
  * This is achieved by clicking the Add Recipes link on the nav bar and adding details about the recipe.

![10-add-recipe](/static/images/testing-images/user-stories/10-add-recipe.jpg)

* As a returning visitor to the website, I would like to have the ability to amend the recipe as required.
  * This is achieved by clicking the My Recipes link in the nav bar and clicking Edit on your recipe, making the necessary changes and saving the recipe.

![11-edit-recipe](/static/images/testing-images/user-stories/11-edit-recipe-links.jpg)

![12-edit-recipe](/static/images/testing-images/user-stories/12-edit-recipe.jpg)

![13-save-recipe](/static/images/testing-images/user-stories/13-save-recipe.jpg)

* As a returning visitor to the website, I would like to have the ability to delete my own recipes.
  * This is achieved by clicking the My Recipes link in the nav bar and clicking Delete on your recipe.

![14-delete-recipe](/static/images/testing-images/user-stories/14-delete-recipe.jpg)

</details>

[Back to Table of Contents](#table-of-contents)

<a id="manual-testing"></a>
## Manual testing of all elements and functionality on every page 

### Browsers tested:

* Google Chrome
* Mozilla Firefox
* Microsoft Edge
* Opera
* Safari

No errors were found on the above browsers.

### Devices tested:

* iPhone 12
* iPhone 11
* iPhone XR
* iPhone 7
* Samsung Tablet S6
* Samsung S20 Plus
* Samsung Galaxy S10
* Samsung A3
* Motorola G9 Plus

No errors were found when testing on the above devices.

<details open>
<summary><b>(click to expand or hide)</b></summary>

| Page      | Section       | Action        | Expected Behaviour     | Result   |  
| --------- | ------------- | ------------- | ---------------------- | -------- |
| Home Page | Tab at top of page | On a desktop go to https://megs-italian-kitchen.herokuapp.com/index | The Home Page displays; there is a MIK favicon displaying in the tab; the tab is named Meg's Italian Kitchen | Pass |
|           | Navigation Bar | The name "Meg's Italian Kitchen" with "Meg's" being in green, "Italian" being in red, "Kitchen" being in Green displays on the left hand side | The name "Meg's Italian Kitchen in the correct colours displays | Pass |
|           |               | Confirm 4 navigation links display, which include: Home (which is in green), Recipes (which is in red), Log In (which is in green) and Register (which is in red) | 4 navigation links display | Pass |
|           |               | Click each navigation link | The correct corresponding page displays | Pass |
|           | Main  | Confirm the hero image of cheese on a cheese board, tomatoes and pasta display | The hero image displays | Pass |
|           |       | Confirm the home page text displays | The home page text displays with links to Browse and Register | Pass |
|           | Footer | Confirm the "copyright" information and the "developed by" information display in the middle of the footer | Copyright and developed by information displays in the middle of the footer | Pass |
|           | Responsiveness | Go to Dev Tools and confirm the page displays correctly when you reduce and expand the margins | The correct page displays | Pass |
|           |           | Change the pixels to 992px | The hamburger menu displays | Pass |
|           |           | Click the hamburger menu | The Name of the website and 4 links display being Home (which is in green), Recipes (which is in red), Log In (which is in green), Register (which is in red) | Pass |
| Recipes Page | Main | On a desktop go to https://megs-italian-kitchen.herokuapp.com/get_recipes | The All Recipes Page displays with a search bar and a reset and search links | Pass |
|           |           | Type in Spaghetti in the search bar | The recipe spaghetti bolognese displays | Pass |
|           |           | Confirm the recipes display on the page | The recipe displays with a photo of the recipe, the name of the recipe, who created the recipe, the course, the prep time, the cook time, servings and a link to View full recipe display | Pass |
|           |           | Click View Full Recipe | The image of the recipe, the name of the recipe, the ingredients and steps display | Pass |
| Log In Page | Main | On a desktop go to https://megs-italian-kitchen.herokuapp.com/login | The Log In Page displays | Pass |
|           |       | There is a prompt for Username and Password | The prompts display | Pass |
|           |       | Click the Log In link | A prompt displays on the Username to ask you to complete the field | Pass |
|           |       | Type a Username and click Log In | A prompt displays on the Password to ask you to complete the field | Pass |
|           |       | There is a link underneath the Log In button to Register Account | The Register Account link displays | Pass |
|           |       | Click the Register Account link | The Register page displays | Pass |
|           |       | The title Register displays | The title displays | Pass |
|           |       | There is a prompt for Username and Password | The prompts display | Pass |
|           |       | Click the Register button | A prompt displays on the Username to ask you to complete the field | Pass |
|           |       | Type a Username and click Log In | A prompt displays on the Password asking you to complete the field | Pass |
|           |       | There is a link underneath the Register button to Log In | Clicking the link displays the Log In Page | Pass |
| Register Page | Main | Enter a Username and Password and click Register | You are taken to the My Recipes page and a Registration Successful displays | Pass |
|           |       | Click the Log Out button | You have been logged out displays | Pass |
| Log In Page | Main | Enter the Username and Password that you registered with | You are taken to the My Recipes page | Pass |
| Add Recipe Page | Main | Click the Add Recipes link | The Add Recipe Page displays | Pass |
|           | Main | The Add Recipe form displays | The sections to complete are Recipe Name, Select Category (which is either entree, main or dessert), Preparation time, Cooking Time, Servings (which is numbers only), Ingredients, Recipe Method and there is a part to Add an Image URL that isn't mandatory | Pass |
|           |       | Click Add Recipe | The All Recipes page displays with a prompt stating the Recipe Successfully Added | Pass |
| My Recipes Page | Main | Click the My Recipes link | The users name displays at the top of the page, the recipe that was added displays with an edit and delete button | Pass |
|           |       | Click the Edit button | The Edit Recipe page displays with all the fields populated | Pass |
|           |       | Go to the bottom of the page and click Cancel | The All Recipes page displays | Pass |
|           |       | Go back to the My Recipes page | The username's Recipe page displays | Pass |
|           |       | Click the Edit button | The Edit Recipe page displays with all the fields populated | Pass |
|           |       | Make a change to the recipe and click Save Recipe | The All Recipes page displays and the change has been saved, you may have to click View Full Recipe to see some changes, all depends on where you made the change, A flash message stating the Recipe has been Successfully Updated displays | Pass |
|           |       | Click My Recipes and delete the recipe that you created | The All Recipes page displays with a message stating the Recipe has been Successfully Deleted | Pass |
|           |       | Click My Recipes | The recipe has been deleted | Pass |

</details> 

[Back to Table of Contents](#table-of-contents)

<a id="bugs-fixes"></a>
## Bugs/Fixes  

**Font colour**

**1. Issue**:
I was wanting to change the font colour on the navbar and Flash Messages and was having problems in overriding the default settings in Materialize.
* **FIX**:
The only way I could rectify this was use the !important rule in my CSS. There may be another way to rectify this, but I found this worked.

**Home Page**

**1. Issue**:
I was having issues with my footer where the footer wouldn't stay at the bottom of the page.
* **Fix**:
I found a fix for this on [Stack Overflow](https://stackoverflow.com/questions/55541850/how-to-make-footer-stay-at-bottom-of-the-page-with-flex-box) where I changed the html and body height to 100%, display of flex and flex-direction of column.

**2. Issue**:
As I was using Materialize in my project, the class of container had its own style. I originally had the class of container in my base.html, so it could update every page. However, this was affecting my home page image and it wouldn't cover the whole page. I changed the container width to 100%, but then that affected every other page and I didn't want the recipe cards to have 100% width.
* **Fix**:
I removed the class of container from the base.html page and added it directly to the pages that I wanted to use that styling on. Then I could make my home page have a width of 100%.

**Full Recipes Page**

**1. Issue**:
I was having issues with the ingredients and steps displaying on one line each. All of my ingredients and steps were next to each other in a big row.
* **FIX**:
I searched Slack for other peoples recipe cookbooks and found [My Ruby's Kitchen](http://ms3-recipe.herokuapp.com/home) who had the ingredients and steps in the same way that I wanted the page to be laid out. I followed her code to organise my ingredients and steps on the page by using splitlines.

**Outstanding bugs**
On a mobile phone I have an extra [dropdown menu displayed in blue carots ^](./static/images/testing-images/edit-recipe-bug.jpg) on the Add Recipe and Edit Recipe pages. I am yet to find a way to remove these extra characters off the screen. As it doesn't affect the ability to complete the form, this bug will be further looked into at a later stage.