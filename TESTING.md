# BookWorm -  Testing

![Bookworm](documentation/bookworm.png)

Visit the deployed site: [Bookworm](https://bookworm2022.herokuapp.com/)

- - -

## CONTENTS

* [AUTOMATED TESTING](#AUTOMATED-TESTING)
  * [W3C Validator](#W3C-Validator)
  * [JavaScript Validator](#JavaScript-Validator)
  * [Python Validator](#Python-Validator)
  * [Lighthouse](#Lighthouse)
  * [WAVE Testing](#WAVE-Testing)
* [MANUAL TESTING](#MANUAL-TESTING)
  * [Testing User Stories](#Testing-User-Stories)
  * [Full Testing](#Full-Testing)
* [BUGS](#BUGS)
  * [Solved Bugs](#Solved-Bugs)
  * [Known Bugs](#Known-Bugs)

Testing was ongoing throughout the entire build. During development I made use of Google Chrome Developer Tools to ensure everything was working correctly and to assist with troubleshooting when things were not working as expected.

I have gone through each page using Google Chrome Developer Tools to ensure that each page is responsive on a variety of different screen sizes and devices.

- - -

## AUTOMATED TESTING

### W3C Validator

[W3C](https://validator.w3.org/) was used to validate the HTML on all pages of the website. It was also used to validate the CSS.

* [Index Page](https://validator.w3.org/nu/?doc=https%3A%2F%2Fbookworm2022.herokuapp.com%2F)
* [Add Bookshelf Page](https://validator.w3.org/nu/?doc=https%3A%2F%2Fbookworm2022.herokuapp.com%2Fadd_bookshelf)
* [Add Review Page](https://validator.w3.org/nu/?doc=https%3A%2F%2Fbookworm2022.herokuapp.com%2Fpopulate_review%3Fgbook_id%3DM4-jzgEACAAJ)
* [Books Page]()
* [Bookshelves Page]()
* [Edit Bookshelf Page]()
* [Edit Review Page]()
* [Error Page](https://validator.w3.org/nu/?doc=https%3A%2F%2Fbookworm2022.herokuapp.com%2Fedit_bookshelf%2Ferror)
* [Login Page](https://validator.w3.org/nu/?doc=https%3A%2F%2Fbookworm2022.herokuapp.com%2Flogin)
* [Profile Page](https://validator.w3.org/nu/?doc=https%3A%2F%2Fbookworm2022.herokuapp.com%2Fprofile%3Fusername%3Dadmin)
* [Register Page](https://validator.w3.org/nu/?doc=https%3A%2F%2Fbookworm2022.herokuapp.com%2Fregister)
* [Search Page](https://validator.w3.org/nu/?doc=https%3A%2F%2Fbookworm2022.herokuapp.com%2Fsearch)

The validator has returned warnings for the use of aria-labels on all pages using the bootstrap icons. I am happy to leave these warnings as I have followed the instructions on the bootstrap site regarding the use of aria labels with icons, and the use of the aria labels is important for accessibility.

- - -

### JavaScript Validator

[jshint](https://jshint.com/) was used to validate the JavaScript.

* [script.js](documentation/testing/validation/jshint-script.png)

- - -

### Python Validator

[PEP8](http://pep8online.com/) was used to validate the python files.

* app.py - No Errors

- - -

### Lighthouse

I used Lighthouse within the Chrome Developer Tools to test the performance, accessibility, best practices and SEO of the website. These scores are somewhat lower than what I would like them to be so this is something that I would prioritise improving in the next implementation.

### Desktop Results

* [Index Page](documentation/testing/validation/lh-index-desk.png)
* [Add Bookshelf Page](documentation/testing/validation/lh-add-bookshelf-desk.png)
* [Add Review Page](documentation/testing/validation/lh-add-review-desk.png)
* [Books Page](documentation/testing/validation/lh-books-desk.png)
* [Bookshelves Page](documentation/testing/validation/lh-bookshelves-desk.png)
* [Edit Bookshelf Page](documentation/testing/validation/lh-edit-bookshelf-desk.png)
* [Edit Review Page](documentation/testing/validation/lh-edit-review-desk.png)
* [Error Page](documentation/testing/validation/lh-error-desk.png)
* [Login Page](documentation/testing/validation/lh-login-desk.png)
* [Profile Page](documentation/testing/validation/lh-profile-desk.png)
* [Register Page](documentation/testing/validation/lh-register-desk.png)
* [Search Page](documentation/testing/validation/lh-search-desk.png)

- - -

### WAVE Testing

[WAVE](http://wave.webaim.org/) (Web Accessibility Evaluation Tool) allows developers to create content that is more accessible to users with disabilities. It does this by identifying accessibility and WGAC errors.

I have used the WAVE testing tool to try and ensure there are no accessibility issues with my site.

- - -

## MANUAL TESTING

### Testing User Stories

| Goals | How are they achieved? | Image |
| :--- | :--- | :--- |
| `First Time Visitors` |
|  |  |  |
| Understand what the site is for and how to navigate the site. | A description of what the site is is included on the home page. | :--- |
| Register for an account. | The description on the home page encourages new users to register for an account. A register link is displayed on the navbar if a user is not logged in. | :--- |
| Search for books | Users are always shown the search link on the navbar regardless of their login status. | :--- |
|`Returning Visitors`|
|  |  |  |
| Log in to my account | If a user is not logged into an account, a login link is provided on the navbar. | :--- |
| Create a bookshelf | The create a bookshelf button is displayed prominently at the top of the bookshelves page. | :--- |
| Edit a bookshelf | When a user views their bookshelves on the bookshelves page, they are given the option to edit their bookshelf. | :--- |
| Delete a bookshelf | When a user views their bookshelves on the bookshelves page, they are given the option to delete their bookshelf. When the user selects delete, a modal will pop up to confirm deletion and to let the user know that all books shelved on that bookshelf will also be deleted. | :--- |
| Create a book review | When a user searches for a book, they are shown the results of the search and each result has a shelve this book button. When the user clicks on this they are redirected to the review page. | :--- |
| Edit a book review | When a user views their books, each book has an edit button, which will take the user to the edit review page with the books information pre-populated. | :--- |
| Delete a book review | When a user views their books, each book has a delete button, when the user clicks this a modal will pop up to confirm the user wishes to delete the book. | :--- |
|`Admin User` |
|  |  |  |
| Remove any reviews that are offensive | Due to time constraints, I have had to place this item in the future implementations list. |  |

- - -

### Full Testing

Full testing was performed on the following devices:

* Laptop:
  * Macbook Pro 2021 14 inch screen
* Mobile Devices:
  * iPhone 13 pro.
  * iPhone 11 pro.
  * Phone X.

Each device tested the site using the following browsers:

* Google Chrome
* Safari
* Firefox

Additional testing was taken by friends and family on a variety of devices and screen sizes. A Big thank you to [Megan](https://github.com/Medusas71) for taking the time to thoroughly test the site for me.

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| `Navbar` |
|  |  |  |  |  |
| Bookworm Logo & Title | When clicked the user will be redirected to the home page. | Clicked Logo and title | Redirected to the home page. | Pass |
| Home Page Link | When clicked the user will be redirected to the home page.| Clicked link | Redirected to the home page. | Pass |
| Search Link | When clicked the user will be redirected to the search page. | Clicked link | Redirected to the search page. | Pass |
| Bookshelves Link (Logged in users only) | When clicked the user will be redirected to the bookshelves page. | Clicked link | Redirected to the bookshelves page | Pass |
| Books Link (Logged in users only) | When clicked the user will be redirected to the books page. | Clicked link | Redirected to the books page | Pass |
| Profile Link (Logged in users only) | When clicked the user will be redirected to the profile page. | Clicked link | Redirected to the profile page | Pass |
| Log in Link (Only shown if user not in session) | When clicked the user will be redirected to the log in page. | Clicked link | Redirected to the log in page | Pass |
| Register Link (Only shown if user not in session) | When clicked the user will be redirected to the register page. | Clicked link | Redirected to the register page  | Pass |
| Log out Link (Logged in users only) | When clicked the user will be redirected to the home page and a flash message displayed to let the user know they have been logged out successfully. | Clicked link |Redirected to the home page and a flash message displayed to let me know I have been logged out | Pass |
| `Footer` |
|  |  |  |  |  |
| Bookworm Title | When clicked the user will be redirected to the home page. | Clicked Logo and title | Redirected to the home page. | Pass |
| Copyright year | The copyright should display the correct year - this is a javascript function that checks what the current year is and injects it into the footer | Checked the year | Displaying the correct year | Pass |
| `Home Page` |
|   |   |   |   |
| Register link in the blurb | When clicked the user will be redirected to the register page. | Clicked link  | Redirected to the register page | Pass |
| Search link in the blurb | When clicked the user will be redirected to the search page. | Clicked link | Redirected to search page | Pass |
| `Log in Page` |
| Username input - empty | This is a required field so the form should not submit if empty | Tried to submit the form with this field empty | Tooltip tells me this field is required | Pass |
| Password input empty | This is a required field so the form should not submit if empty | Tried to submit the form with this field empty | tooltip tells me this field is required |  Pass |
| log in button | Saves the user to session and redirects to the profile page. Flash message shown welcoming the user | Submitted form | Redirected to the profile page and flash message shown | Pass |
| Incorrect username or password used | A flash message should display saying username/password incorrect - this is defensive programming - not letting user know which input is incorrect | Incorrect username/password entered | Message flashes to let the user know they have entered an incorrect username/password | Pass |
| Link to register page |  This should redirect the user to the register page | Clicked link | Redirected to the register page | Pass |
| `Register Page` |
| | | | | | |
| Username input | The username should be 5 characters minimum | Entered username less than 5 characters long | tooltip lets the user know they have not entered enough characters | Pass |
| Username input - empty | The username is a required field, so should not submit with no value | Tried to submit form with no value entered | Tooltip lets user know this value is required | Pass |
| Username input | If username is in use, message should flash to user | entered an in use username | Message flashed to say username already in use | Pass|
| Email input | The email input should include an email address  | Entered plain text | Tooltip tells user to use an email address here | Pass |
| Email input - empty | The email is a required field, so should not submit with no value | Tried to submit form with no value entered | Tooltip lets user know this value is required | Pass |
| Password input | This field should be at least 5 characters long | Entered password less than 5 characters long | Tooltip tells user the password should be at least 5 characters long | Pass |
| Password input - empty | The password is a required field, so should not submit with no value | Tried to submit form with no value entered | Tooltip lets user know this value is required | Pass |
| Register button | Should redirect user to the log in page and a registration successful message flashed | Created new user and submitted form | Redirected to the log in page and message flashed | Pass |
| `Search Page` |
|   |   |   |   |  |
| Search feature | A search is performed when the user enters a search term | Searched for rabbits | The search returns book results | Pass |
| Search feature. - Error | If there is an error with the search, a flash message is displayed to let the user know there was a problem and directs them to try again. | Searched for bulldogs | The search doesn't return a result (please see known bugs No 2), and a flash message is displayed to the user | Pass |
| Shelve this book button on search result book (user signed in) | When the user clicks the shelve this book button they should be redirected to the add review page | Clicked button while signed in | Redirected to the add review page and book information pre-populated | Pass |
| Shelve this book button on search result book (user not signed in) | When the user clicks the shelve this book button they should be flashed a message to let them know they need to be logged in to shelve a book and be redirected to the log in page | Clicked button while not signed in | Redirected to the log in page and flash message displayed | Pass |
| `Bookshelves Page` |
|   |   |   |   |  |
| Add a bookshelf button | When the user clicks this button they should be taken to the add a bookshelf page | Clicked button | Redirected to the add a bookshelf page | Pass |
| Bookshelf accordion | When the user selects a bookshelf, the accordion opens to display the edit and delete bookshelf buttons | Clicked shelf | Accordion opened to display edit and delete buttons | Pass |
| Edit bookshelf button on bookshelf accordion | The user should be taken to the edit bookshelf page with the selected bookshelf pre-populated in the input | Clicked button | Taken to the edit bookshelf page. Input pre-populated with the current bookshelf name | Pass |
| Delete button on bookshelf accordion | When the user clicks the delete button a modal should pop up asking the user to confirm they wish to delete the bookshelf and that by deleting the bookshelf all books associated with the shelf will be deleted too | Clicked button | Modal popped up and displayed the confirm deletion message | Pass |
| Delete Button on Deletion modal| When the user clicks the delete button the bookshelf should be deleted along with any books that were associated with the shelf. A flash message will confirm deletion and the user is redirected to the bookshelves page | Clicked button | Bookshelf deleted together with associated books and a flash message displayed success. Redirected to the bookshelves page | Pass |
| Cancel button on deletion modal | When the user clicks the cancel button the modal should close | Clicked button | Modal closed | Pass |
| `Books Page` |
|   |   |   |   |  |
| Accordion button | Open/close the accordion | Click button | Accordion opens and closes | Pass |
| Edit button on book | When the edit button is clicked the user should be taken to the edit review page with the inputs pre-populated with the values stored in the database for that book | Clicked button | Redirected to the edit review page. Books details filled in with previously saved information | Pass |
| Delete button on book | When the user clicks this button a modal should pop up asking the user to confirm they wish to delete this book | Clicked button | Modal popped up to confirm if I wanted to delete the book | Pass |
| Delete button on modal | When clicked the book should be deleted | Clicked button | Book Deleted from books page | Pass |
| Cancel button on modal | When clicked the modal should close | Clicked button | Modal closed | Pass |
| `Add Bookshelf Page` |
| Bookshelf input | Should prompt the user to enter a shelf name if left blank | Left blank and clicked add bookshelf button | Tooltip tells you this field needs to be filled in | Pass |
| Add Bookshelf button | Saves the new bookshelf to the database, redirects the user to the bookshelves page and flashes messgage to let the user know successful | Clicked button | Bookshelf saved to the database, redirected to the bookshelves page and flash message to save bookshelf created successfully | Pass |
| `Edit Bookshelf Page` |
| Input | This should be pre-populated with the bookshelf selected | Checked input against the bookshelf selected |Input pre-populated with the bookshelf selected | Pass |
| Input - no value entered | The form requires this field be filled in before submission | Left input blank | Tooltip lets me know this field is required | Pass |
| Edit bookshelf button | When clicked the updated shelf name should be saved to the database, the user redirected to the bookshelves page and a message flashed to let them know updated successfully | clicked button | Updated bookshelf name added to the database, redirected to bookshelf page and flash message shows update has been successful | Pass |
| `Add Review Page` |
|   |   |   |   |   |
| Title input | This is a required field so should ask for a value to be entered if empty. This field should be pre-populated with the book information selected in the search | Input was pre-populated. Cleared the input | Tooltip told me it is a required field | Pass |
| Author input | This is a required field so should ask for a value to be entered if empty. This field should be pre-populated with the book information selected in the search | Input was pre-populated. Cleared the input | Tooltip told me it is a required field | Pass |
| Bookshelf dropdown | This should be populated with all the bookshelves associated with the user | Checked to see if all my created bookshelves were displated | Only my bookshelves are displayed | Pass |
| Star Ratings | These should be able to be selected to choose your rating | clicked random ratings | The rating was saved to the database | Pass |
| Review Field | This is an optional field. Any information entered should be saved to the database | Text entered | Text saved to the database | Pass |
| Notes Field | This is an optional field. Any information entered should be saved to the database | Text entered | Text saved to the database | Pass |
| Add Review Button | This should add the review to the database and redirect the user to the books page and flash a message to let the user know the book was saved successfully | Clicked button | Review saved to database and redirected to books page, message flashed to let me know book saved successfully | Pass |
| `Edit Review Page` |
| Title input | This is a required field so should ask for a value to be entered if empty. This field should be pre-populated with the book information saved to the database | Input was pre-populated. Cleared the input | Tooltip told me it is a required field | Pass |
| Author input | This is a required field so should ask for a value to be entered if empty. This field should be pre-populated with the book information saved to the database | Input was pre-populated. Cleared the input | Tooltip told me it is a required field | Pass |
| Bookshelf dropdown | This should be populated with all the bookshelves associated with the user | Checked to see if all my created bookshelves were displated | Only my bookshelves are displayed | Pass |
| Star Ratings | These should be able to be selected to choose your rating. Rating saved to the database should be displayed | Rating saved to the database displayed. Clicked random rating to change the rating | The rating was saved to the database | Pass |
| Review Field | This is an optional field. Previously saved review should display here. Any information entered should be saved to the database | Saved review text displayed. Text Changed | Text saved to the database | Pass |
| Notes Field | This is an optional field. Previous saved notes should display here. Any information entered should be saved to the database | Notes previously saved to the database displayed, text changed | Text saved to the database | Pass |
| Edit Review Button | This should add the updated review to the database and redirect the user to the books page and flash a message to let the user know the book was saved successfully | Clicked button | Review saved to database and redirected to books page, message flashed to let me know book saved successfully | Pass |
| `Error Page` |
|   |   |   |   |   |
| Home page link | Redirects the user to the home page | Clicked link | Redirected to home page | Pass |

 - - -

## BUGS

### Solved Bugs

| No | Bug | How I solved the issue |
| :--- | :--- | :--- |
| 1 | When I added the accordion to the book search results, the accordion would open and close on all books together when triggered due to the accordion being created in the for loop, the id was identical for all results. | To enable each accordion to open and close indivually I needed to find a way to create a unique ID on every iteration of the for loop. Initally I considered taking the title and using the python method replace to remove any spaces in the title. However this would have been a problem if there were two books with identical names. I posed my question on slack and Daisy suggested using a loop.counter. On researching this I discovered it is only applicable to Django, however something very similar exists in Jinja - a loop.index. By using the loop.index in the id attribute I was able to create a unique ID for each book and this allowed the accordion to be opened and closed on each book individually.  |
| 2 | The bootstrap modal for deleting a bookshelf was displaying but was hidden under the backdrop, making it impossible to use the modal buttons or to exit out of the modal. ![Modal Bug](documentation/testing/modal-bug.png) | I initially tried moving the modal code within the file but this made no difference. Upon searching google for bootstrap modal greyed out I found the following [article](https://weblog.west-wind.com/posts/2016/Sep/14/Bootstrap-Modal-Dialog-showing-under-Modal-Background?utm_source=feedburner&utm_medium=feed&utm_campaign=Feed%3A+RickStrahl+%28Rick+Strahl%27s+WebLog%29). I tried a few of the fixes, which didn't work before finding that the fix to remove the backdrop did work. This is not an ideal fix, but works for the moment until I can research this issue further and find a more elegant solution. |

- - -

### Known Bugs

| No | Bug |
| :--- | :--- |
| 1 | When performing searches using the google books API, sometimes it is not returning a result, which results in a flash message being shown. I have noted that during development the API was returning results for certain terms, but when deployed these search terms would not return a result. I plan to look further into this issue as to why it is not returning a result and see if there is a way to filter out book results that are missing attributes. |
| 2 | Some books when shelved are pulling in a different book than the one selected. I have taken the unique volume ID and performed a check on the google books page and the ID is correct for the book selected, so there would appear to be an issue with the request to the API. This is something that I will need to look into further to discover why it is returning the wrong information.|
| 3 | During development I used many search terms to test the search function of the site. However I have found that on deployment some of the search terms that returned a result in development are not returning a result and so are showing the flash message to the user. This is something that I will need to look into further as I know that the search returns a result. I feel that perhaps it may be because some books may be missing parameters. |
| 3 | The star ratings seem to be misaligned since the app has been deployed. Ideally I would like to look into a better way of doing this myself, and will add this to the future implementations list of things to update. |