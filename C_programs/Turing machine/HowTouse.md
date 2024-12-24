This C program simulates a simple Turing Machine. It reads input from a file, processes it according to predefined state transition rules, and writes the result to an output file. Below is a detailed explanation of the program:

### **State Definition**

The **`State`** enum defines three states for the Turing Machine: **`A`**, **`B`**, and **`C`**.

```c
typedef enum { A, B, C } State;
```

### **Function Declaration**

The **`runTuringMachine`** function is declared to take two parameters: **`inputFile`** and **`outputFile`**.

```c
void runTuringMachine(const char* inputFile, const char* outputFile);
```

### **Main Function**

The **`main`** function calls **`runTuringMachine`** with **`"input.txt"`** as the input file and **`"output.txt"`** as the output file.

```c
int main() {
    runTuringMachine("input.txt", "output.txt");
    return 0;
}
```

### **runTuringMachine Function**

The **`runTuringMachine`** function is where the Turing Machine logic is implemented:

1. **File Operations**:
    - Open the input file for reading.
    - Open the output file for writing.
    - If either file cannot be opened, print an error message and exit.

```c
void runTuringMachine(const char* inputFile, const char* outputFile) {
    FILE* in = fopen(inputFile, "r");
    FILE* out = fopen(outputFile, "w");

    if (!in || !out) {
        fprintf(stderr, "파일을 열 수 없습니다.\n");
        exit(1);
    }
```

1. **Initialize Tape**:
    - Initialize a tape array to store the input symbols, assuming a maximum length of 1000.
    - Read symbols from the input file into the tape.

```c
    char tape[1000];
    int tapeLen = 0;

    while (fscanf(in, " %c", &tape[tapeLen]) == 1) {
        tapeLen++;
    }
```

1. **Set Initial State and Head Position**:
    - Set the initial state to **`A`**.
    - Set the head position to the beginning of the tape.

```c
    State state = A;
    int head = 0;
```

1. **Turing Machine Operation**:
    - Run the Turing Machine while the head is within the bounds of the tape.
    - Print the current state, head position, and tape contents for debugging.
    - Implement the state transition rules using a switch statement:
        - For state **`A`**, **`B`**, and **`C`**, check the current symbol under the head and decide the next state, symbol to write, and head movement.
    - If the head moves out of the tape bounds, break the loop.

```c
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
    
```

1. **Write Tape to Output File**:
    - Write the contents of the tape to the output file, separating symbols with spaces.

```c
   for (int i = 0; i < tapeLen; i++) {
        fprintf(out, "%c", tape[i]);
        if (i < tapeLen - 1) {
            fprintf(out, " ");
        }
    }

    fclose(in);
    fclose(out);
}

```

The program ends by closing the input and output files.
