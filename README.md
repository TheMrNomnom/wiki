# Wiki Encyclopedia

This project is a Python implementation of a web application that simulates a wiki encyclopedia. It allows users to view, create, edit, and search for encyclopedia entries. The application stores the encyclopedia entries as Markdown files and converts them to HTML for display.

## Background

[Wikipedia](https://www.wikipedia.org/) is a popular free online encyclopedia that contains encyclopedia entries on various topics. Each entry can be viewed by visiting its page, which is specified in the route `/wiki/TITLE`. The content of the page is written in HTML, which is rendered by the browser.

To simplify the process of creating and editing encyclopedia entries, this project uses a lighter-weight markup language called Markdown instead of HTML. Markdown is a human-friendly markup language that is converted to HTML when displayed to the user.

## Features

The implemented features of the Wiki Encyclopedia project include:

### Entry Page

Visiting `/wiki/TITLE` displays the contents of the encyclopedia entry with the given title. The content is obtained by calling the appropriate utility function. If the requested entry does not exist, an error page is displayed.

### Index Page

The `index.html` template lists all the encyclopedia entries. Users can click on any entry name to be taken directly to that entry page.

### Search

The sidebar contains a search box where users can enter a query to search for an encyclopedia entry. If the query matches an entry's name, the user is redirected to that entry's page. If the query does not match any entry, a search results page is displayed, listing all entries that have the query as a substring. Clicking on any entry name on the search results page takes the user to that entry's page.

### New Page

Clicking "Create New Page" in the sidebar takes the user to a page where they can create a new encyclopedia entry. Users can enter a title for the page and provide the Markdown content in a textarea. Clicking the save button saves the new page. If an entry with the same title already exists, an error message is displayed. Otherwise, the entry is saved to disk, and the user is taken to the new entry's page.

### Edit Page

On each entry page, the user can click a link to edit the entry's Markdown content. They are taken to a page with a textarea pre-populated with the existing Markdown content. After making the desired changes, the user can click a button to save the changes. Once saved, the user is redirected back to the entry's page.

### Random Page

Clicking "Random Page" in the sidebar takes the user to a random encyclopedia entry.

### Markdown to HTML Conversion

On each entry's page, the Markdown content is converted to HTML before being displayed to the user. The conversion is performed using the `python-markdown2` package, which can be installed via `pip3 install markdown2`. The converted HTML allows rendering headings, bold text, unordered lists, links, and paragraphs.

## Installation and Usage

1. Clone the repository to your local machine.
2. Install the required dependencies by running `pip install -r requirements.txt`.
3. Navigate to the project directory: `cd wiki`.
4. Run the Django development server: `python manage.py runserver`.
5. Open a web browser and visit `http://localhost:8000` to access the application.

## Future Improvements

While the current implementation fulfills the basic requirements, there is always room for improvement. Here are some possible enhancements for future iterations:

- User authentication: Implement user accounts to allow users to have personalized profiles and track their own entries.
- Rich text editor: Replace the plain textarea with a rich text editor to provide a more user-friendly editing experience.
- Categories and tags: Introduce a categorization system for entries and enable searching by categories and tags.
- Media uploads: Allow users to upload and embed media files such as images and videos in their entries.
- Version control: Implement a version control system to track the changes made to each entry and provide revision history.
- Advanced search features: Enhance the search functionality with advanced filters and options to improve search accuracy and relevance.

## Contributing

Contributions are welcome! If you find any issues or want to enhance the application, feel free to submit a pull request.

Please ensure that your code follows the PEP 8 style guide and includes appropriate tests.

## Credits

This project is developed based on the specifications provided by [CS50](https://cs50.harvard.edu/web/2020/projects/1/wiki/) from Harvard University.

## License

This project is licensed under the MIT License. You can find the license information in the [LICENSE](LICENSE) file.
