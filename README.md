# Python URL Shortner
A simple Public URL shortner written in Python + Flask with MySQL backend for storage

## Features
- Built on Flask
- Built in rate limiter
- MySQL database storage
- user IP tracking enable/disable
- custom URL length
- Uppercase URL's enable/disable
- Add hyphen and underscore to short URL? (Enable/Disable)
- Add numbers to short URL? (Enable/Disable)
- Create a redirect timeout if needed (Can put ads or more on a redirect loading page)

## Screenshots
Home page screenshot:
![Home Page Python URL Shortner screenshot](/screenshots/home.png?raw=true "Home Page Python URL Shortner")



## Installation
### Setting up packages/modules:
```
pip install MySQL-python
pip install Flask
pip install flask-limiter
```

### Setup app.py file
Setup only this section below
```py
numbers = "0123456789"
lowerCase = "abcdefghijklmnopqrstuvwxyz"
upperCase = lowerCase.upper()           # Will take the lowercase variable
                                        # and turn it into uppercase
letterChoices = lowerCase

# Set website limits
limiter = Limiter(app, global_limits=["2 per second"])

websiteTitle = "Python"                 # Website Title

MySQLHost = "localhost"                 # MySQL hostname
MySQLUser = "root"                      # MySQL username
MySQLPass = ""                          # MySQL pass
MySQLDB = "pythonurlshortner"           # Database name

storeIP = True                          # Store IP Address of user?
urlLength = 6                           # The length of your short URLS
enableHyphenAndUnderscore = True        # Have a "-" and "_"
                                        # (Hyphen/Dash and Underscore) in URLs?

enableNumbers = True                    # Have numbers in the short URL?

enableUppercase = True                  # Have upper case along with lowercase

enableRedirectTimeout = False           # Have a redirect page time out
                                        # To use this give it a seconds timeout
                                        # To disable, set to "False"
```

### Setting up port
Setting up the port is optional, by default the port is set to 1313.
So enter your machine's IP address and add 1313 as the port number,
example url to type into browser:
```
http://192.168.2.13:1313
```
Local host can be used as well:
```
http://localhost:1313
```
