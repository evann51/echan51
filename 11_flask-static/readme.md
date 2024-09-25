## K11: Some Things Never Change
### Due: 2024-09-26r before class

Your Trio Mission:

1. In a new directory in your workshop, save a copy of the demo for using flask to serve static files.
1. As a team...
  - Familiarize yourself with the app directory structure and the files' content.
  - Note anything notable.
  - Predict expected behaviors.
  - Spin up your website on localhost and reconcile behavior with prediction.
  - Record your notes in `readme` in app's root directory.
1. Once your team has done this, compose and store another html file named `fixie.html` (containing some html to render your team name and roster) so that flask can serve it staticly.

<br>

DELIVERABLES:
* Save to workshop as indicated.
* Each teammate should submit matching sourcecode.

```
path/to/myworkshop$ tree 11_flask-static
.
├── app.py
├── readme
└── static
    ├── foo
    ├── foo.html
    └── fixie.html
```

<br>

[related](https://ukulelemagazine.com/lessons/uke-lesson-3-chords-and-the-truth-country-songwriting-legend-harlan-howard)  
[related](https://en.wikipedia.org/wiki/Plain_text)  

Notes:
If you add the input to app.route() to the end of the link, you can run the next? function   
This makes me think function definitions in flask have two lines:   
1. The route to the webpage
2. The name of the function (with no arguments?)   

<br>
If you add a route to a file that exists without defining a function at that route, it attempts to open the file:   
<br>
HTML files are opened as HTML   
<br>
Plaintext files are given a download prompt   
