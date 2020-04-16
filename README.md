SMSbot
======
SMSbot implements a auto-responder ("bot") for SMS messages.  It is intended to be deployed as a turn-key application for the AT&T API Marketplace.  The app starts with a default set of responses, but it is expected to be customized by the deployer.

### Pre-requisites
1. AT&T Marketplace Account, with a purchased Local Number.
2. A host to run this application with a "publicly routable FQDN"

NOTE: Item 2 can be satisfied by running this application on a laptop behind a NAT/firewall, and installing a tunnelling utility such as ngrok.  This utility registers a temporary FQDN on their public server, and routes traffic via a secure tunnel to your app running on localhost.  See https://ngrok.com

### Deployment Instructions
1. Clone this repo
2. Run the application  (e.g. python3 SMSbot).  
NOTE: By default, Flask http server listens on port 5000.
3. Verify the application is running by attempting to access it using a browser.  e.g. URL is http://localhost:5000/
4. If using a utility like ngrok, start it now.  Make a note of the public https endpoint it reports.

### Configuration

#### App Setup

Ideally, this step should only need to be done once, and may need to be repeated if the server or app needs to be restarted.

Using a browser, navigate to the SMSbot Home screen http://localhost:5000/
Select App Setup from the navigation menu.
Fill in the SMSbot Configuration form:
- Private Project Key is the value from your AT&T API Marketplace Account.
- Private Project Secret is the value from your AT&T API Marketplace Account.
- Projet TN is a Telephone Number resource you have reserved in the AT&T API Marketplace Account and assigned to the Project.
- APIM URL is the URL of the AT&T API Marketplace server.  (generally, keep the default value)
- Public URL is the URL that APIM server will use to call the webhook in this application.  When using ngrok, this is the value produced in Step 4 of Deployment Instructions above. 

#### Customize SMS Menu
The app is deployed with a starter SMS menu which will need to be edited.
Using a browser, navigate to the SMSbot Home screen http://localhost:5000
Select the Customize SMS Menu from the navigation menu.

The form presents the set of *requests* and *replys* that make up the bot logic.
Use this form to:
- modify the request value
- modify the response to any request value
- activate or deactivate a particular menu item
- add a new menu item 

Remember to click on Submit to make your changes take effect.
### Usage Examples

In these examples, the Project TN is the Destination TN.  i.e. it is the TN that some user will send a query to.  We'll call that user the Sender.

1. Out of the box

| Sender TN | Response from Destination TN |
|----|----|
| hours | M-F 9-5, Sat 8-noon, Sun closed |
| location | 123 Main St, Middletown, NJ |
| phone | 88-555-1212 |
| special | Half off with code SMS |
| soup | Kale with Portuguese Sausage |
| foo | I can reply to hours, location, special, soup, phone |

2. Modify the soup of the day to be Split Pea using the Customize SMS Menu

| Sender TN | Response from Destination TN |
|----|----|
| hours | M-F 9-5, Sat 8-noon, Sun closed |
| location | 123 Main St, Middletown, NJ |
| phone | 88-555-1212 |
| special | Half off with code SMS |
| soup | Split Pea |
| foo | I can reply to hours, location, special, soup, phone |
   
3.  Deactivate the special using the Customize SMS Menu

| Sender TN | Response from Destination TN |
|----|----|
| hours | M-F 9-5, Sat 8-noon, Sun closed |
| location | 123 Main St, Middletown, NJ |
| phone | 88-555-1212 |
| soup | Split Pea |
| foo | I can reply to hours, location, soup, phone |

4. Add a *covid* specific item using the Customize SMS Meny

| Sender TN | Response from Destination TN |
|----|----|
| hours | M-F 9-5, Sat 8-noon, Sun closed |
| location | 123 Main St, Middletown, NJ |
| phone | 88-555-1212 |
| soup | Split Pea |
| covid | We have curbside pickup and limited occupancy restrictions |
| foo | I can reply to hours, location, soup, phone, covid |