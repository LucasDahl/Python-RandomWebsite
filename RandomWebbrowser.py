#Import libraries
import wbbrowser
import time
import random

# Setup the while loop
while True:
    # Choose the sites
    sites = random.choice(["google.com", "github.com", "youtube.com", "weather.gov"])
    # Setup the first part fpr tje webbrowser to search
    visit = "http://{}".fromat(sites)
    # Have the webbrowser open the random site to visit
    webbrowser.open(visit)
    # Pick a random number betweem 5 and 20 which will then open a site
    seconds = random.randrang(5, 20)
    # Wait x(seconds variable).
    time.sleep(seconds)
    
