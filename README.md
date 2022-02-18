# Selenium Classic Hello World in Google

In this repository, you can find a simple exercise with  Selenium, in where I build a simple automatization over Firefox Browser. 

The flow is:
- Open a Firefox browser in the Google's URL.
- Write "Hello World in Google with Selenium"
- Take screenshot of the open session and saved this in img folder.
- Close the session and generate report in Folder reports.

For run this example, you need:

- Clone this repository. 
- In your local space, create a virtual envioronment.
- Activate the envioronment and install package so:
        
        pip3 install selenium webdriver-manager pyunitreport


Notes: 
- If you used a local browser different to Mozilla, you can make some modifications in hello_world script using [this documentation](https://pypi.org/project/webdriver-manager/) 

- Remember that We used Python for this example and this is at least in a version 3.6

- The class @classmethod permit that each method or test it could be execute in tyhe same firefox's window. If you want run each method for separete should be replace cls for self, delete @classmethod and change methods setUpClass and tearDownClass for setUp and tearDown respectively. 