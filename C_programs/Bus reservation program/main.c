#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>

void PrintBusTicketStatus(); //버스표 상태 출력함수 원형선언
void PrintBusTicketReservation(); //버스표 예매함수 원형선언
void PrintBusTicketChange(); //버스표 변경함수 원형선언
void PrintBusTicketCancellation(); //버스표 취소함수 원형선언
int PrintScreen(int mode); //화면 출력함수 원형선언
int GetLocationNumber(const char* location); //도시 위치 변환함수 원형선언
void FileWrite(); //파일 쓰기 함수 원형선언

const char* LocationNames[3] = { "", "SEOUL", "BUSAN" }; //도시 이름 문자열
int SeatInfo[3][20] = { 0 }; // 자리번호!

int main() // 메인함수
{
    FILE* fp = fopen("server.txt", "r"); //파일 열기, 읽기

    char temp; // 체크해주는 문자이다. 
    int isLocation = 1;
    char location[10];
    int countChar = 0;
    int newLineCount = 0;

    while ((temp = fgetc(fp)) != EOF) //좌석 정보 읽기
    {
        if (temp == ' ')
        {
            location[countChar] = '\0'; //도시 이름 문자열 종료
            countChar = 0;
            isLocation = 0;
        }
        else if (temp == '\n')
        {
            SeatInfo[GetLocationNumber(location)][countChar] = 1; //좌석 정보 저장
            countChar = 0;
            isLocation = 1;

            if (newLineCount == 1)
                break;
            else
                newLineCount++;
        }
        else
        {
            if (isLocation == 1)
            {
                location[countChar] = temp;// 도시 이름 문자 읽기
                countChar++;
            }
            else
            {
                if (countChar == 0)
                    countChar = temp - 48; // 아스키 -48
                else
                    countChar = countChar * 10 + (temp - 48); // 아스키 -48
            }
            newLineCount = 0;
        }
    }

    fclose(fp); //파일 닫기

    while (1)
    {
        int userChoice;

        printf("<고속버스>\n");
        printf("무엇을 도와드릴까요?\n");
        printf("1. 버스표 상태\n");
        printf("2. 버스표 예매\n");
        printf("3. 버스표 변경\n");
        printf("4. 버스표 취소\n");
        printf("5. 종료\n");

        userChoice = _getch() - '0';
        while (userChoice <= 0 || userChoice >= 6)
        {
            printf("잘못된 입력입니다. 다시 입력해주세요.\n");
            userChoice = _getch() - '0';
        }

        switch (userChoice)
        {
        case 1:
            PrintBusTicketStatus();
            break;
        case 2:
            PrintBusTicketReservation();
            break;
        case 3:
            PrintBusTicketChange();
            break;
        case 4:
            PrintBusTicketCancellation();
            break;
        case 5:
            printf("프로그램을 종료합니다.\n");
            return 0;
        }
    }
}

void PrintBusTicketStatus() //버스 상태 출력
{
    PrintScreen(1);
}

void PrintBusTicketReservation() //버스표 예매함수
{
    int busNumber = PrintScreen(1);

    printf("예매할 좌석을 선택해주세요 (예: 1a): ");
    char seatInput[3];
    scanf("%s", seatInput);

    int row = seatInput[0] - '0';
    char column = seatInput[1];
    int seatIndex = (row - 1) * 4 + (column - 'a');

    if (SeatInfo[busNumber][seatIndex] == 1)
    {
        printf("이미 예매된 좌석입니다.\n");
        return;
    }

    SeatInfo[busNumber][seatIndex] = 1;

    printf("예매가 완료되었습니다!\n");

    FileWrite();
}

void PrintBusTicketChange() //버스표 변경함수
{
    int busNumber = PrintScreen(1);

    printf("현재 예매된 좌석: \n");
    for (int i = 1; i <= 5; i++)
    {
        for (int k = 1; k <= 4; k++)
        {
            int seatIndex = (i - 1) * 4 + (k - 1);
            if (SeatInfo[busNumber][seatIndex] == 1)
                printf("%d%c ", i, 'a' + (k - 1));
        }
    }
    printf("\n");

    // 기존 좌석 취소
    printf("취소할 좌석을 선택해주세요 (예: 1a): ");
    char seatInput[3];
    scanf("%s", seatInput);

    int row = seatInput[0] - '0';
    char column = seatInput[1];
    int seatIndex = (row - 1) * 4 + (column - 'a');

    if (SeatInfo[busNumber][seatIndex] == 0)
    {
        printf("선택한 좌석은 예매되지 않았습니다.\n");
        return;
    }

    SeatInfo[busNumber][seatIndex] = 0;

    // 새로운 좌석 예매
    printf("예매할 좌석을 선택해주세요 (예: 1a): ");
    scanf("%s", seatInput);

    while (1)
    {
        row = seatInput[0] - '0';
        column = seatInput[1];
        seatIndex = (row - 1) * 4 + (column - 'a');

        if (SeatInfo[busNumber][seatIndex] == 1)
        {
            printf("이미 예매된 좌석입니다. 다시 입력해주세요.\n");
            scanf("%s", seatInput);
        }
        else
        {
            SeatInfo[busNumber][seatIndex] = 1;

            printf("변경이 완료되었습니다!\n");
            break;
        }
    }

    FileWrite();
}

void PrintBusTicketCancellation() //버스표 취소함수
{
    int busNumber = PrintScreen(1);

    printf("현재 예매된 좌석: \n");
    for (int i = 1; i <= 5; i++)
    {
        for (int k = 1; k <= 4; k++)
        {
            int seatIndex = (i - 1) * 4 + (k - 1);
            if (SeatInfo[busNumber][seatIndex] == 1)
                printf("%d%c ", i, 'a' + (k - 1));
        }
    }
    printf("\n");

    printf("취소할 좌석을 선택해주세요 (예: 1a): ");
    char seatInput[3];
    scanf("%s", seatInput);

    int row = seatInput[0] - '0';
    char column = seatInput[1];
    int seatIndex = (row - 1) * 4 + (column - 'a');

    if (SeatInfo[busNumber][seatIndex] == 0)
    {
        printf("선택한 좌석은 예매되지 않았습니다.\n");
        return;
    }

    SeatInfo[busNumber][seatIndex] = 0;

    printf("취소가 완료되었습니다!\n");

    FileWrite();
}

int PrintScreen(int mode) //화면 출력함수
{
    printf("\n버스를 선택해주세요\n");
    printf("1. 서울\n");
    printf("2. 부산\n\n");

    int busNumber = _getch() - '0';
    while (busNumber <= 0 || busNumber >= 3)
    {
        printf("잘못된 입력입니다. 다시 입력해주세요.\n");
        busNumber = _getch() - '0';
    }

    printf("도착지: %s\n", LocationNames[busNumber]);
    printf("요금: 20000\n\n");

    printf("<좌석>\n");
    printf("  ab cd\n");
    for (int i = 1; i <= 5; i++)
    {
        printf("%d ", i);
        for (int k = 1; k <= 4; k++)
        {
            if (SeatInfo[busNumber][(i - 1) * 4 + k - 1] == 1)
                printf("■");
            else
                printf("□");

            if (k == 2)
                printf(" ");
        }
        printf("\n");
    }

    return busNumber;
}

int GetLocationNumber(const char* location) //위치 번호 변환 함수
{
    int locationNumber = 0;
    for (int i = 1; i <= 2; i++)
    {
        if (strcmp(location, LocationNames[i]) == 0)
        {
            locationNumber = i;
            break;
        }
    }
    return locationNumber;
}

void FileWrite() //파일 쓰기 함수
{
    char str[100] = "";
    int index = 0;

    for (int i = 1; i < 3; i++)
    {
        for (int j = 0; j < 20; j++)
        {
            if (SeatInfo[i][j] == 1)
            {
                if (i == 1)
                {
                    str[index] = 'S';
                    index++;
                    str[index] = 'E';
                    index++;
                    str[index] = 'O';
                    index++;
                    str[index] = 'U';
                    index++;
                    str[index] = 'L';
                    index++;
                    str[index] = ' ';
                    index++;
                }
                else if (i == 2)
                {
                    str[index] = 'B';
                    index++;
                    str[index] = 'U';
                    index++;
                    str[index] = 'S';
                    index++;
                    str[index] = 'A';
                    index++;
                    str[index] = 'N';
                    index++;
                    str[index] = ' ';
                    index++;
                }
                if (j < 10)
                {
                    str[index] = j + 48;
                    index++;
                }
                else if (j < 100)
                {
                    str[index] = j / 10 + 48;
                    index++;
                    str[index] = j % 10 + 48;
                    index++;
                }
                str[index] = '\n';
                index++;
            }
        }
    }

    FILE* fp = fopen("server.txt", "w");

    fprintf(fp, str);

    fclose(fp);
}
