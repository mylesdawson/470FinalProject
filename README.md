# Skedge

## Running

First run:

`docker-compose build && docker-compose up`

Then visit:

`localhost:8000`

## Logging In

To log in, either create an account (customer or business) by clicking on "Create An Account" in the top right corner, or log in using one of the existing accounts below.

Customer:

`Username: customer1 Password: secret`

Businesses:

`Username: business1 Password: secret`

`Username: business2 Password: secret`

`Username: business3 Password: secret`

## Customer Features

A customer can filter all businesses by category (fitness, wellness, etc.) by clicking on the corresponding button on the home page. The information for a business can thenbe viewed by clicking on the View button for that business. When a business is viewed its information is displayed at the top while the services it offers are in a list at the bottom.

A customer can book a service by clicking the Book button next to their desired service. A calendar then appears showing the options a customer has for booking an appointment.
 - The customer first picks a day
 - Information is then displayed beneath the calendar regarding whether that day is open or closed for appointments
 - If that day is open for appointments, the customer can choose a timeslot
 - Finally, the customer can click Book Appointment

## Business Features

A business can click on the Calendar tab in the navbar to look at a calendar containing all of their past and open appointments, as well as their closed and unavailable days.

A business can also click on the Services tab in the navbar to view a list of their services. From here they can click on a service and delete it if needed. Another service can be added by clicking the Add Service button on the right, filling in required information, and clicking Save.

A business can edit the main information (name, contact information, description, etc.), location information, and business hours by clicking on the Business tab in the navbar, then clicking Save at the bottom.
