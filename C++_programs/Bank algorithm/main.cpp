#include <iostream>
#include <conio.h> // getch() 함수를 사용하기 위한 헤더 파일입니다. 

class Bank {
private:
	std::string name; // 회원명
	std::string account; // 계좌번호
	std::string pwd; // 비밀번호
	int choice; // 항목 선택
	int my_money; // 잔고
	void inforepeat();
public:
	Bank(std::string n, std::string a, std::string p); //회원명, 계좌번호, 비밀번호
	int money(); // 입/출금 프로그램 구동
	void personPrint(); // 사용자 출력
	void in(); // 입금 구동
	void out(); // 출금 구동
	void remainMoney();
};
void Bank::inforepeat() {

	do {
		std::cout << "사용자의 계좌번호를 입력하시오 : ";
		std::string tmp;
		std::cin >> tmp;
		if (account == tmp) {
			break;
		}
		std::cout << "해당 사용자는 존재하지 않습니다. 올바른 계좌번호를 입력하시오." << std::endl;
	} while (1);

	do {
		std::cout << "비밀번호를 입력하시오 : ";
		std::string tmp;
		char ch;

		tmp.clear();
		ch = _getch(); // 사용자로부터 문자를 입력받음 (화면에는 보이지 않음)
		while (ch != 13) { // Enter 키가 입력될 때까지 반복 (Enter의 ASCII 코드는 13)
			tmp.push_back(ch); // 입력된 문자를 password에 추가
			if (ch != 8) {
				std::cout << '*'; // 화면에 * 출력 -> backspace 제외
			}
			else {
				if (!tmp.empty()) {
					tmp.pop_back(); // 마지막 문자를 password에서 제거
					std::cout << "\b \b"; // 화면에서 마지막 문자 지우기
				}
			}
			ch = _getch(); // 다음 문자를 입력받음
		}
		std::cout << std::endl;
		if (pwd == tmp) {
			std::cout << std::endl;
			break;
		}
		std::cout << "올바른 비밀번호를 입력하시오." << std::endl;
	} while (1);
}
Bank::Bank(std::string n, std::string a, std::string p) : name{ n }, account{ a }, pwd{ p } {
	// 초기화
	my_money = 0;
}
void Bank::personPrint() {
	std::cout << "회원 이름 : " << name << std::endl;
	std::cout << "계좌 번호 : " << account << std::endl; 
	//비밀번호도 출력하라고 제시되어있지만, 저는 비밀번호는 출력하진 않겠습니다
}
void Bank::in() {
	int money;
	inforepeat();
	do {
		std::cout << "입금하실 금액을 입력하시오(양수만 입력 가능합니다.) : ";
		std::cin >> money;
	} while (money <= 0);
	my_money += money;
	std::cout << "입금을 완료하였습니다." << std::endl;
	std::cout << name <<"의 현재 금액" << my_money << std::endl;
}
void Bank::out() {
	inforepeat();
	int money;
	do {
		std::cout << "출금하실 금액을 입력하시오(양수만 입력 가능합니다.) : ";
		std::cin >> money;
		if (money > 0) {
			if (money > my_money) {
				std::cout << "현재 가진 금액보다 큽니다. 더 적은 금액을 입력하시오." << std::endl;
			}
			else {
				my_money -= money;
				std::cout << "출금을 완료하였습니다." << std::endl;
				std::cout << name << "의 현재 금액" << my_money << std::endl;
				break;
			}
		}
	} while (1);
	

}
void Bank::remainMoney() {
	inforepeat();
	std::cout << name << "의 현재 금액" << my_money << std::endl;
}
int Bank::money() {
	// 프로그램 구동
	do {
		system("cls");
		std::cout << "**************************************************" << std::endl;
		std::cout << "*************** 은행 관리 프로그램 ***************" << std::endl;
		std::cout << "**************************************************" << std::endl;
		std::cout << "1. 회원 보기 2. 입금, 3. 출금 4. 잔액, 5. 나가기  " << std::endl;
		std::cout << "번호 입력 >> ";
		std::cin >> choice; // 사용자에게 입력을 받아옴. 
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
			std::cout << "프로그램을 종료합니다. 이용해주셔서 감사합니다." << std::endl;
			break;
		default:
			std::cout << "올바른 숫자를 입력하시오." << std::endl;
		}
		system("pause");
	} while (choice != 5);
	return 0;
}

int main() {
	Bank usr1("김연세", "1111-1111", "1111");
	usr1.money();
	return 0;
}
