# Low Level Design - Parking Lot

## Requirements -
1. One entry point
2. One exit point
3. Vehicle comes in through the entry point, a ticket is generated
4. Vehicle exits from the exit point, amount is calculated, paid, ticket is closed
5. A vehicle cannot enter twice, no two open tickets for same vehicle
6. Entry point cannot close a ticket
7. Exit point cannot create a ticket

## Test cases -
1. Create a ticket for a new vehicle
2. Create a ticket for a vehicle which already has an open ticket
   1. Raise ExistingOpenTicketException
3. Close an open ticket
4. Close an already closed ticket
   1. Raise ClosedTicketException
5. Close a non-existing ticket
   1. Raise TicketNotFoundException