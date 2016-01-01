from flask import Flask, jsonify, abort, render_template, request, session, escape
import MySQLdb
from flask_limiter import Limiter
import time
import random

app = Flask(__name__)


#####################################
####        MAIN CONFIG          ####
#####################################
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





##############################################################################################################################
#################################### DO NOT EDIT BELOW UNLESS YOU KNOW WHAT YOU ARE DOING ####################################
##############################################################################################################################



#####################################
####           TOOLS             ####
#####################################
def genUrl():
    l = list(letterChoices)
    final = ""
    for x in range(urlLength):
        final += random.choice(l)
    return final






#####################################
####         SETUP URLS          ####
#####################################
if enableHyphenAndUnderscore:
    letterChoices += "-_"
if enableUppercase:
    letterChoices += upperCase
if enableNumbers:
    letterChoices += numbers



#####################################
####         HOME PAGE           ####
#####################################
# The main page
@app.route('/', methods=["GET"])
@app.route('/<path:url>', methods=["GET"])
@limiter.limit("200 per minute")
def home_page(url=None):
    if (not url):
        return render_template('index.html', websiteTitle=websiteTitle)
    else:
        db = MySQLdb.connect(MySQLHost, MySQLUser, MySQLPass, MySQLDB)
        cursor = db.cursor()
        cursor.execute("SELECT longLink FROM short WHERE shortLink='%s'" % (str(escape(url))))
        if cursor.rowcount > 0:
            foundURL = cursor.fetchone()[0]
            db.close()
            if (enableRedirectTimeout):
                return render_template('redirect.html', redirectTimeout=enableRedirectTimeout, url=foundURL)
            else:
                return render_template('redirect.html', redirectTimeout=0, url=foundURL)
        else:
            return render_template('redirect.html', redirectTimeout=0, url="/")


#####################################
####         SAVE PAGE           ####
#####################################
@app.route('/saveURL', methods=["GET", "POST"])
def save_URL():
    if request.method == "POST":
        url = str(escape(request.form["url"]))
        cont = True
        while cont:
            custom = str(genUrl())
            db = MySQLdb.connect(MySQLHost, MySQLUser, MySQLPass, MySQLDB)
            cursor = db.cursor()
            cursor.execute("SELECT shortLink FROM short WHERE shortLink='%s'" % (str(custom)))
            if cursor.rowcount > 0:
                cont = True
            else:
                cont = False
        cursor = db.cursor()
        cursor.execute("INSERT INTO short (id, shortLink, longLink, time, ipAddress) VALUES (DEFAULT, '%s', '%s', '%d','%s')" % (custom, url, time.time(), str(request.remote_addr)))
        db.commit()
        db.close()
        return render_template('redirect.html', redirectTimeout=0, url="/")














        

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=1313)
