This C code represents a console application for managing bus ticket reservations. The program reads bus seat information from a file, allows the user to check the status of bus tickets, make new reservations, change existing reservations, and cancel reservations. Here's an overview of its functionality:

Overview of Functions
PrintBusTicketStatus():

Prints the current status of bus tickets.
PrintBusTicketReservation():

Allows the user to reserve a bus ticket.
PrintBusTicketChange():

Allows the user to change an existing bus ticket reservation.
PrintBusTicketCancellation():

Allows the user to cancel an existing bus ticket reservation.
PrintScreen(int mode):

Displays the bus selection screen and seat arrangement. Returns the selected bus number.
*GetLocationNumber(const char location)**:

Converts a location name to its corresponding index number.
FileWrite():

Writes the current seat reservation information to a file.
Main Function
The main() function is the entry point of the program. It performs the following tasks:

Read Initial Seat Information:

Opens the file server.txt and reads the seat information, storing it in the SeatInfo array.
The seat information is parsed from the file based on the location and seat number.
User Interaction Loop:

Continuously presents the user with a menu to choose from the following options:
Check bus ticket status.
Reserve a bus ticket.
Change a bus ticket.
Cancel a bus ticket.
Exit the program.
The user's choice is read and validated, and the corresponding function is called.
PrintBusTicketStatus
This function calls PrintScreen(1) to display the current status of bus tickets for the selected bus.

PrintBusTicketReservation
This function:

Calls PrintScreen(1) to display the bus seat status.
Prompts the user to enter the seat they wish to reserve.
Checks if the seat is already reserved and updates the SeatInfo array if the seat is available.
Calls FileWrite() to update the seat information in the file.
PrintBusTicketChange
This function:

Calls PrintScreen(1) to display the bus seat status.
Displays currently reserved seats and prompts the user to select a seat to cancel.
Updates the SeatInfo array to mark the seat as available.
Prompts the user to select a new seat and updates the SeatInfo array if the new seat is available.
Calls FileWrite() to update the seat information in the file.
PrintBusTicketCancellation
This function:

Calls PrintScreen(1) to display the bus seat status.
Displays currently reserved seats and prompts the user to select a seat to cancel.
Updates the SeatInfo array to mark the seat as available.
Calls FileWrite() to update the seat information in the file.
PrintScreen
This function:

Displays the bus selection screen.
Prompts the user to select a bus (either Seoul or Busan).
Displays the seat arrangement of the selected bus, indicating reserved (■) and available (□) seats.
Returns the selected bus number.
GetLocationNumber
This function takes a location name as input and returns its corresponding index in the LocationNames array (1 for Seoul, 2 for Busan).

FileWrite
This function:

Creates a string representing the current seat reservations.
Writes this string to the server.txt file.
Summary
This program provides a simple interface for managing bus ticket reservations, including viewing, reserving, changing, and canceling tickets. It reads initial seat information from a file and updates the file with changes made by the user.
