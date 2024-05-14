# Using PyTest to test XVWA web application for reflected XSS vulnerabilities
Explaining XVWA : (https://www.vulnhub.com/entry/xtreme-vulnerable-web-application-xvwa-1,209/) 
Explaining Reflected XSS : (https://www.veracode.com/security/reflected-xss#:~:text=Reflected%20XSS%20is%20a%20kind,the%20website%20they%20are%20visiting.)
## Setup : 
To run this project, ensure the following are installed :  
  1. pip3 install -U selenium  
  2. pip3 install -U pytest  
  3. Mozilla Firefox  
### Additionally :
  1. Move geckodriver to your system path - https://github.com/mozilla/geckodriver/releases  
  2. Download and run XVWA in a docker https://github.com/s4n7h0/xvwa  
  3. Use https://github.com/tuxotron/xvwa_lamp_container (Follow provided instructions)  

## To Run :
Run "pytest ReflectedXSSTest.py"
