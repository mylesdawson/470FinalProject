# Skedge

## Overview

Skedge is an easy to use appointment booking website, that allows customers to find local businesses and set up appointments with them. Businesses can list information about themselves and their various offered services, and customers can book appointments for these services.

## Running

First run:

`docker-compose build && docker-compose up`

Then visit:

`localhost:8000`

To clean up the containers:

`docker-compose down && docker system prune -f`

`docker volume prune`

## Logging In

To log in, either create an account (customer or business) by clicking on "Create An Account" in the top right corner, or log in using one of the existing accounts below.

Customer:

`Username: customer1 Password: secret`

Businesses:

`Username: business1 Password: secret`

`Username: business2 Password: secret`

`Username: business3 Password: secret`

## Customer Features

A customer can filter all businesses by category (fitness, wellness, beauty) by clicking on the corresponding button on the home page. The information for a business can then be viewed by clicking on the View button for that business. When a business is viewed its information is displayed at the top, while the services it offers are in a list at the bottom.

A customer can book a service by clicking the Book button next to their desired service. A calendar then appears showing the options a customer has for booking an appointment.
 - The customer first picks a day
 - Information is then displayed beneath the calendar regarding whether that day is open or closed for appointments
 - If that day is open for appointments, the customer can choose an available timeslot
 - Finally, the customer can click Book Appointment

The timeslots are generated making sure that they do not overlap with any existing appointments for the business, and are strictly within the business hours.

The customer can click on the 'Your Appointments' tab at the top to see a list of all their appointments. They can also cancel appointments, and see a list of appointments that were either cancelled by them or by the business.

## Business Features

A business can click on the Calendar tab in the navbar to look at a calendar containing all of their past and upcoming appointments, as well as their closed and unavailable days. Each day will indicate whether it is in the past, whether the business is closed that day, whether the business is open (and has available appointment slots), whether the business is fully booked (no free appointment slots), or whether that day is unavailable (it is too far in the future for customers to book appointments). Clicking on an individual day will bring up a list of all the appointments made by customers for that day, and also indicate whether any of the appointments were cancelled, either by the customer or by the business.

A business can also click on the Services tab in the navbar to view a list of their offered services. From here they can click on a service and delete it if needed. Another service can be added by clicking the Add Service button on the right, filling in required information describing the service, and clicking Save.

A business can edit the main information (name, contact information, description, etc.), location information, and business hours by clicking on the Business tab in the navbar, then clicking Save. A business has several options to control how appointments are booked by customers. They can set individual opening and closing hours for every day of the week, specify how many days in advance that customers are allowed to book appointments (two weeks by default), and also specify how many hours notice is required for booking an appointment on the current day (default is 1 hour).
