# That's a perfect example of how to use a dictionary to select the correct Service object! You've shown how to dynamically pass the right service to webdriver.Chrome().

# Now, let's think about the overall structure. Jamie wants to be able to switch between Chrome, Firefox, and Edge. How could Jamie write a more generalized piece of code that, given a browser_choice variable (e.g., "Chrome", "Firefox", "Edge"), would initialize the correct webdriver object for that choice, perhaps using an if/elif/else structure or another dictionary to map the browser name directly to the webdriver class itself?

# Think about how you'd handle the different webdriver.Chrome, webdriver.Firefox, and webdriver.Edge calls based on the browser_choice.

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

dict = {'Chrome': "chrome_driver_path", 'Edge':'Edge_driver_path', 'Firefox': 'Gecko_driver_path'}
cond= "Firefox"
if cond in dict:
    path, service_class, driver_class = dict[cond]
    driver = driver_class(service=service_class(path))
    print(f"The driver has been selected and it's {cond}'s path: {path}")
else:
    print(f"No driver found for {cond}")


