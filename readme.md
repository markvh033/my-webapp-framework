#### uvicorn backend.app.main:app --reload

npx tailwindcss -i ./frontend/static/css/input.css -o ./frontend/static/css/output.css --watch



notes

* create a collection for notes
* add notes to sidenav
* Note object in pydantic
  * id
  * owner
  * list
  * tags
  * color
  * priority
  * title
  * note
  * duedate
  * created
  * updated
  * status

    \
* create routes for notes
  * create a note
  * mark as done
  * delete note
  * update note

    \
* Logic
  * Deleteting notes doesnt actually deletes them but marks them as deleted. 
  * \
    \
* Notes design
  * notes show as cards that follow left to right order, when no more notes fit on one line it goes to the next line
  * you can order notes by name, priority of created date
  * you first see all notes that are not marked as done
  * there is a button called ‘create note’ on the top left of the page above the notes
    * when creating a new note, it uses the first row to display the create-note sectio there the notes would show and temporarly moves all the notes up of there are any. the text box for the content of the note can increase in height moving the rest of the create note card and the notes below it down.
    * there is a button in the create-note section called ‘create’ and saves the note, shrinking the size of the notes to the rest of the notes.
    * use greys, whites, and google style blue for the buttons.
* **Notes**
  * Notes should have a title field (limited to 50 characters)
  * Notes should have a content/body field that can be multi-line and unlimited length
  * Notes should display the created date/time
  * Notes should have a priority field (low, medium, high)
  * Notes should allow toggling between marking as done/undone
  * Notes should be draggable to allow reordering

  **Create Note Section**
  * The create note section slides down from the top when "Create Note" button is clicked
  * There should be a close/cancel button to dismiss creating a new note
    * User can also press escape to cancel
  * Title and content fields are required to save a new note
  * After saving, the create note section slides back up
* Editing Notes
  * Clicking on a note with automatically open the note in the create-note section but will all the info available about the note prepopulated. This allows for easy editing and saving. The text box for the content of the note is automatically selected.
* **Filtering/Sorting/Search**
  * There is a search bar where the user can search for notes. Pressing searches and only filters for relevant results
  * Allow filtering to show all notes, or just notes marked as done/undone
  * Sorting options should be: priority, created date (newest first or oldest first), alphabetical by title

  **Visual Design**
  * Use colors like #ffffff (white), #f1f3f4 (light gray) for backgrounds
  * Use Google's brand blue #4285f4 for primary buttons like Create, Save, sorting options
  * Notes could use material card style with drop shadows
  * Subtle transition animations for creating, dismissing the create form

  **Other**
  * Responsive design for different screen sizes
  * Confirmation for deleting notes


next up:


Send transactional emails

Allow users to signup with custom links

* generate a uuid that is linked allows the user to signup and link themselves to a user group as defined in mongodb (may need to be defined still

Create mongodb script to create collections

Create


