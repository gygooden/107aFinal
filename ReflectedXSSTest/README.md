# Using PyTest program to test a XVWA web application 
([[Common web](https://www.vulnhub.com/entry/xtreme-vulnerable-web-application-xvwa-1,209/](https://www.vulnhub.com/entry/xtreme-vulnerable-web-application-xvwa-1,209/)) for reflected XSS vulnerabilities.
## Setup : 
To run this project, ensure the following are installed :
  pip3 install -U selenium
  pip3 install -U pytest
  Mozilla Firefox
#### Additionally :
  Have geckodriver in your system path https://github.com/mozilla/geckodriver/releases
  Download and run XVWA in a docker https://github.com/s4n7h0/xvwa ---> https://github.com/tuxotron/xvwa_lamp_container (follow instructions)

Run "pytest ReflectedXSSTest.py"
