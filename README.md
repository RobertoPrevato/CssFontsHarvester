## Bulk downloader for font files inside CSS source code
Have you ever desired to bulk download font files from css source, to not rely on third parties CDN networks? I did, sometimes. Sometimes I worked for clients that didn't accept to have certain static files downloaded from third party servers; and sometimes while developing a new application, with developer console open and _"Disable Cache"_ option on, I saw that downloading all the time the fonts from remote servers could be slow. In other words, I desired to download fonts as static files and have my development server serve them.

For example, having this CSS source from CDN: __[https://fonts.googleapis.com/css?family=Roboto:300,400,500,700|Material+Icons](https://fonts.googleapis.com/css?family=Roboto:300,400,500,700|Material+Icons)__, in some situations I desire to download the source fonts, to deploy them in my applications. This simple console application does it; it also generates CSS files with URLs pointing to absolute HTTP paths with a relative path: `/fonts/file_name`. Downloaded fonts can then be placed in a folder: `fonts` in the application root folder.

```bash
python fetchfonts.py -s roboto-material-icons.css
```

### Requirements
* Python >= 3.5

### How to use
```bash
python -m venv env

# activate environment (Linux)
source env/bin/activate

# activate environment (Windows)
env\Scripts\activate 

# install dependencies
pip install -r requirements.txt

# download fonts, having a css file locally:
python fetchfonts.py -s roboto-material-icons.css
```