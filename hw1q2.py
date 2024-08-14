#Assignment:  Python Dictionaries
'''
2. Python Programming Challenges for Customer Service Data Handling

Task 1: Customer Service Ticket Tracker Demonstrate your ability to use nested collections and loops 
by creating a system to track customer service tickets.

Problem Statement: Develop a program that:

Tracks customer service tickets, each with a unique ID, customer name, issue description, and status (open/closed).
Implement functions to:
Open a new service ticket.
Update the status of an existing ticket.
Display all tickets or filter by status.
Initialize with some sample tickets and include functionality for additional ticket entry.
Example ticket structure:

service_tickets = {
    "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}

'''
service_tickets = {}
ticket = "Ticket"
count = 1
s = 0

service_tickets = {
    "Ticket0": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
}


def open():
    service_tickets = {
    "Ticket0": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"}, 
}  
    print("A new service ticket has been made.")

def update(x, y, z, count):
    new_ticket = ticket + str(count)
    service_tickets.update({new_ticket: {"Customer": x, "Issue": y, "Status": z}})
    print("The service ticket has been updated.")

def updatee(x, y, z, ticketn):
    service_tickets[ticketn].update({"Customer": x, "Issue": y, "Status": z})
    print("The service ticket has been updated.")

def display():
    print("The service ticket is on display below.")
    print(service_tickets)

def quit():
     print("Thank You for using this Customer Service Ticket Tracker application. GoodBye!")


print("Welcome to the Customer Service Ticket Tracker!")
print("Menu:")
print("1. Open a new service ticket.")
print("2. Update the status of a ticket.")
print("3. Update the status of an existing ticket.")
print("4. Display all tickets")
print("5. To Quit")

#User Interaction
try:
      x = ""
      y = ""
      z = ""
      ticketn = ""
      while(s != 5):
        s = int(input("Please enter a number (1-5) of what you want to do by looking at the Menu: "))
        if(s == 1):
             open()
             display()
        elif(s == 2):
             x = str(input("Please enter the Customer's Name: "))
             y = str(input("Please enter the Customer's Issue: "))
             z = str(input("Please enter the Customer's Status: "))
             update(x, y, z, count)
             count = count + 1
        elif(s == 3):
             ticketn = str(input("Please enter the Customer's Ticket with number (example: Ticket1): "))
             x = str(input("Please enter the new Customer's Name: "))
             y = str(input("Please enter the new Customer's Issue: "))
             z = str(input("Please enter the new Customer's Status: "))
             updatee(x, y, z, ticketn)
        elif(s == 4):
             display()
        elif(s == 5):
             quit()
             break
        else:
             print("Please enter a number 1 - 5. Please Try Again")
             break                           
      
except ValueError:
      #Code to handle incorrect input type
      print("Please enter a valid integer.")
except Exception as e:
      #Code to handle an unexpected exception
      print(f"An unexpected error occured: {e}")
else:
      pass
finally:
        print("Thank you for your response.")
