# toinen
Just a little python training.

Eats list of urls and keywords from csv format text file and polling time in seconds. Starts simpleHTTPServer and
creates index.html for the script root directory: http://127.0.0.1:8000 from with you see that status of the http
page, http-request time and has the page wanted keyword.

./toinen.py -i example_input.csv -p 60

Ugly hack: You can monitor 6 http addresses with basic setup. If you want more, edit findex.html and add more entries

<p><iframe src="6" seamless></iframe>
<iframe src="7" seamless></iframe></p>

etc.

jenkins test



