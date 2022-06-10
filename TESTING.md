<h1 align="center">Meg's Italian Kitchen - Testing Details</h1>

[View the main README.md document](README.md)

[View the deployed Meg's Italian Kitchen]()

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

One warning displayed as per the below screenshot.

![W3C HTML Validation Results](/static/images/testing-images/w3c-html-validator-results.jpg)

I spoke to Tutor Support regarding this error and they advised that I can ignore this error, as the error is referring to the "section" that is used for flash messages and will not contain any "heading" elements. 

No other errors or warnings displayed.  

Tutor Support also showed me the best way to validate html, which is to right click on the web page and select "view page source" and copy the code from there and paste into the direct input section of the html checker. This way the jinja code is ignored by the html checker.

* [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/#validate_by_input) was used to ensure that there were no errors or warnings in my CSS document and was validated by direct input. I had no errors or warnings display.

![W3C CSS Validation Results](/static/images/testing-images/w3c-css-validator-results.jpg)

* [Autoprefixer CSS Online](https://autoprefixer.github.io/) was used to ensure that all vendor prefixes 
were included in CSS. the results were copied into the style.css file.

* [Pep8](http://pep8online.com/) was used to check the app.py file. No errors or warnings displayed.

![pep8](/static/images/testing-images/pep8.jpg)

<a id="lighthouse"></a>
## Lighthouse  

Lighthouse was used to check for any problems on all pages.

Below is the lighthouse score for each page on mobile and desktop:

<summary><b>(click to expand or hide)</b></summary>

<a id="wave"></a>
## Wave Report  

<a id="user-stories"></a>
## User Stories 

<a id="manual-testing"></a>
## Manual testing of all elements and functionality on every page  

### Browsers tested:

### Devices tested:

| Page      | Section       | Action        | Expected Behaviour     | Result   |  
| --------- | ------------- | ------------- | ---------------------- | -------- |


</details> 

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