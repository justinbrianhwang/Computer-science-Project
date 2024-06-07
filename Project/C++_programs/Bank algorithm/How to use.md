### **Code Analysis**

This code is a simple banking management program. It stores user information and provides functionalities such as deposit, withdrawal, and balance checking. Below is the explanation of the main class and its methods.

### **Class and Method Descriptions**

### **`class Bank`**

This class stores bank account-related information and handles various banking transactions.

- **Member Variables:**
    - **`std::string name`**: User name
    - **`std::string account`**: Account number
    - **`std::string pwd`**: Password
    - **`int choice`**: Menu choice
    - **`int my_money`**: Account balance
- **Constructor:**
    - **`Bank(std::string n, std::string a, std::string p)`**: Initializes the user name, account number, and password.
- **Private Member Function:**
    - **`void inforepeat()`**: Prompts the user to enter account number and password for authentication.
- **Public Member Functions:**
    - **`int money()`**: Main function to run the program.
    - **`void personPrint()`**: Prints user information.
    - **`void in()`**: Handles deposit transactions.
    - **`void out()`**: Handles withdrawal transactions.
    - **`void remainMoney()`**: Checks and displays the account balance.

### **Main Method Descriptions**

### **`void Bank::inforepeat()`**

This function authenticates the user by prompting for the account number and password. It repeatedly asks for the correct input if incorrect information is provided.

### **`Bank::Bank(std::string n, std::string a, std::string p)`**

Constructor that initializes the user name, account number, and password using an initializer list. The initial balance is set to 0.

### **`void Bank::personPrint()`**

Prints the user name and account number. The password is not printed for security reasons.

### **`void Bank::in()`**

Handles deposit transactions. Calls **`inforepeat()`** to authenticate the user, then prompts for the deposit amount and adds it to the balance.

### **`void Bank::out()`**

Handles withdrawal transactions. Calls **`inforepeat()`** to authenticate the user, then prompts for the withdrawal amount and subtracts it from the balance. If the withdrawal amount is greater than the balance, an error message is shown, and the user is prompted again.

### **`void Bank::remainMoney()`**

Checks and displays the account balance. Calls **`inforepeat()`** to authenticate the user.

### **`int Bank::money()`**

Manages the main program loop. Displays a menu to the user and performs the selected function (view member info, deposit, withdraw, check balance, exit). Repeats until the exit option is selected.

### **`main` Function**

The entry point of the program. Creates a **`Bank`** object and calls the **`money()`** method to run the program.

```cpp
int main() {
	Bank usr1("Kim Yonsei", "1111-1111", "1111");
	usr1.money();
	return 0;
}
```

### **Code Execution Flow Summary**

1. The program starts by creating a **`Bank`** object in the **`main`** function.
2. The **`money()`** method is called to display the menu and wait for the user's choice.
3. The user selects one of the options: view member info, deposit, withdraw, or check balance.
4. The selected function is executed, and the menu is displayed again.
5. The process repeats until the exit option is chosen.

Overall, the code is well-structured, with security measures implemented for password input, such as not displaying the password on the screen. However, there are some aspects that can be improved, like handling invalid inputs more robustly during deposit and withdrawal transactions.

### **Code with English Comments**
#include <iostream>#include <conio.h> // Header file for getch() functionclass Bank {
private:
	std::string name; // Member name
	std::string account; // Account number
	std::string pwd; // Password
	int choice; // Menu choice
	int my_money; // Balance
	void inforepeat(); // Function for user authentication
public:
	Bank(std::string n, std::string a, std::string p); // Constructor with name, account, password
	int money(); // Main function to run the program
	void personPrint(); // Print user information
	void in(); // Handle deposit
	void out(); // Handle withdrawal
	void remainMoney(); // Check and display balance
};

void Bank::inforepeat() {
	do {
		std::cout << "Enter your account number: ";
		std::string tmp;
		std::cin >> tmp;
		if (account == tmp) {
			break;
		}
		std::cout << "The user does not exist. Please enter a valid account number." << std::endl;
	} while (1);

	do {
		std::cout << "Enter your password: ";
		std::string tmp;
		char ch;

		tmp.clear();
		ch = _getch(); // Get character input from user (not visible on screen)
		while (ch != 13) { // Repeat until Enter key is pressed (ASCII code for Enter is 13)
			tmp.push_back(ch); // Add character to password
			if (ch != 8) {
				std::cout << '*'; // Display * on screen, except for backspace
			} else {
				if (!tmp.empty()) {
					tmp.pop_back(); // Remove last character from password
					std::cout << "\b \b"; // Erase last character from screen
				}
			}
			ch = _getch(); // Get next character input
		}
		std::cout << std::endl;
		if (pwd == tmp) {
			std::cout << std::endl;
			break;
		}
		std::cout << "Please enter the correct password." << std::endl;
	} while (1);
}

Bank::Bank(std::string n, std::string a, std::string p) : name{ n }, account{ a }, pwd{ p } {
	// Initialize balance
	my_money = 0;
}

void Bank::personPrint() {
	std::cout << "Member name: " << name << std::endl;
	std::cout << "Account number: " << account << std::endl;
	// The password is suggested to be printed, but it will not be printed for security reasons
}

void Bank::in() {
	int money;
	inforepeat(); // Authenticate user
	do {
		std::cout << "Enter the amount to deposit (only positive amounts): ";
		std::cin >> money;
	} while (money <= 0);
	my_money += money;
	std::cout << "Deposit completed." << std::endl;
	std::cout << name << "'s current balance: " << my_money << std::endl;
}

void Bank::out() {
	inforepeat(); // Authenticate user
	int money;
	do {
		std::cout << "Enter the amount to withdraw (only positive amounts): ";
		std::cin >> money;
		if (money > 0) {
			if (money > my_money) {
				std::cout << "The amount exceeds your current balance. Please enter a smaller amount." << std::endl;
			} else {
				my_money -= money;
				std::cout << "Withdrawal completed." << std::endl;
				std::cout << name << "'s current balance: " << my_money << std::endl;
				break;
			}
		}
	} while (1);
}

void Bank::remainMoney() {
	inforepeat(); // Authenticate user
	std::cout << name << "'s current balance: " << my_money << std::endl;
}

int Bank::money() {
	// Run the program
	do {
		system("cls");
		std::cout << "**************************************************" << std::endl;
		std::cout << "**************** Bank Management Program *********" << std::endl;
		std::cout << "**************************************************" << std::endl;
		std::cout << "1. View member 2. Deposit, 3. Withdraw 4. Balance, 5. Exit" << std::endl;
		std::cout << "Enter your choice >> ";
		std::cin >> choice; // Get input from user
		switch (choice) {
		case 1:
			personPrint();
			break;
		case 2:
			in();
			break;
		case 3:
			out();
			break;
		case 4:
			remainMoney();
			break;
		case 5:
			std::cout << "Exiting the program. Thank you for using." << std::endl;
			break;
		default:
			std::cout << "Please enter a valid number." << std::endl;
		}
		system("pause");
	} while (choice != 5);
	return 0;
}

int main() {
	Bank usr1("Kim Yonsei", "1111-1111", "1111");
	usr1.money();
	return 0;
}
