#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>

// 상태 정의
typedef enum { A, B, C } State;

// 함수 선언
void runTuringMachine(const char* inputFile, const char* outputFile);

int main() {
    runTuringMachine("input.txt", "output.txt");
    return 0;
}

void runTuringMachine(const char* inputFile, const char* outputFile) {
    FILE* in = fopen(inputFile, "r");
    FILE* out = fopen(outputFile, "w");

    if (!in || !out) {
        fprintf(stderr, "파일을 열 수 없습니다.\n");
        exit(1);
    }

    // 테이프 초기화 (최대 길이 1000으로 가정)
    char tape[1000];
    int tapeLen = 0;

    // 입력 파일에서 테이프 읽기
    while (fscanf(in, " %c", &tape[tapeLen]) == 1) {
        tapeLen++;
    }

    // 초기 상태와 헤드 위치 설정
    State state = A;
    int head = 0;

    // 튜링 머신 동작
    while (head >= 0 && head < tapeLen) {
        printf("State: %d, Head: %d, Tape: ", state, head);  // 디버그 출력
        for (int i = 0; i < tapeLen; i++) {
            printf("%c", tape[i]);
        }
        printf("\n");

        switch (state) {
        case A:
            if (tape[head] == '1') {
                tape[head] = 'C';
                head++;
                state = B;
            }
            else if (tape[head] == '2') {
                tape[head] = 'B';
                head--;
                state = C;
            }
            else if (tape[head] == '3') {
                tape[head] = 'B';
                head--;
                state = C;
            }
            else {
                head++;
            }
            break;
        case B:
            if (tape[head] == '2') {
                tape[head] = 'A';
                head++;
                state = A;
            }
            else if (tape[head] == '3') {
                tape[head] = 'A';
                head--;
                state = A;
            }
            else if (tape[head] == '1') {
                tape[head] = 'A';
                head--;
                state = A;
            }
            else {
                head++;
            }
            break;
        case C:
            if (tape[head] == '1') {
                tape[head] = 'A';
                head++;
                state = A;
            }
            else if (tape[head] == '3') {
                tape[head] = 'A';
                head++;
                state = A;
            }
            else if (tape[head] == '2') {
                tape[head] = 'B';
                head--;
                state = B;
            }
            else {
                head--;
            }
            break;
        }

        // 테이프의 범위를 벗어나지 않도록 합니다.
        if (head < 0 || head >= tapeLen) {
            break;
        }
    }

    // 출력 파일에 테이프 내용 쓰기
    for (int i = 0; i < tapeLen; i++) {
        fprintf(out, "%c", tape[i]);
        if (i < tapeLen - 1) {
            fprintf(out, " ");
        }
    }

    fclose(in);
    fclose(out);
}
