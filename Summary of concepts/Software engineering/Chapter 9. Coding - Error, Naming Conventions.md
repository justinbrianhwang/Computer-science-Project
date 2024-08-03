# English

### Coding

Programming that satisfies the requirements as specified in the design specifications
A high-quality program with few errors

→ Simply writing proper design specifications means the work is already done.

Errors are numerous, but the types of errors are generally fixed.
- Memory leak
- Duplicate free declarations
- Use of NULL
- Misuse of aliases
- Array index errors
- Arithmetic exceptions
- Off-by-one errors
- User-defined data type errors
- String handling errors
- Buffer errors
- Synchronization errors

**Memory Leak**

Memory is continuously allocated to the program without being freed (beware during dynamic allocation).
This can have severe effects on long-running systems.

**Duplicate Free Declarations**

Resources used in the program should be allocated first and freed after use.
Declaring a resource free again after it has already been freed causes an error.

**Use of NULL**

Accessing the contents of a location pointing to NULL causes an error.
These errors can crash the system.

**Misuse of Aliases**

Aliases can cause many problems.
An error occurs when two variables expected to have different addresses end up with the same value due to aliasing.

**Array Index Errors**

An out-of-bounds array index causes an exception error.
An array index with a negative value causes an error.

**Arithmetic Exception Errors**

Errors such as division by zero and floating-point exceptions.

**Off-by-one Errors**

Starting with 1 instead of 0, or using < N instead of <= N.
These errors are often not detected by compilers or testing tools.

**User-defined Data Type Errors**

Overflow or underflow errors are common.
Special caution is needed when dealing with values of user-defined data types.

**String Handling Errors**

Functions like strcpy() and sprintf() have numerous string handling functions.
Errors occur if a parameter is NULL, the string is not NULL-terminated, or the source parameter size exceeds the destination size.

**Buffer Errors**

When a program tries to copy into a buffer, giving a deliberately large input can cause a buffer overflow in the stack.

Hackers can exploit buffer overflow to execute their code.

**Synchronization Errors**

Common in parallel programs with multiple threads accessing shared resources.

Deadlock - Multiple threads hold resources and do not release them.
Race condition - The outcome depends on the execution order of threads accessing the same resource.
Inconsistent synchronization - Errors occur when locking and unlocking shared variables are alternated.

The main criteria are simplicity and readability.

Simplicity: Clear and uncomplicated, easy to understand.
Readability: Easy to scan and comprehend the program.

Achieving modularization goals, high cohesion, and low coupling in the design simplifies the modules.

### Naming Conventions

**Camel Case**
Class, field, method, and variable names use camel case, with each word's first letter capitalized.

Constants are written in all uppercase.

Class and Interface Names
Use nouns or noun phrases starting with an uppercase letter.

**Method Names**

Usually start with a lowercase verb phrase.

Function names generally describe the value using a noun phrase.

Functions that access and return a field's value use get.

Boolean function names asking a condition usually start with is.

**Variable Names**

Generally start with a lowercase letter.

Provide hints about the usage.

Avoid ambiguous names.

Length of variable names 

Consider the context of use.
Parameters: Keep as short as possible.
Field variables: Should be as long and meaningful as necessary.

**Package Names**

Generally lowercase and use nouns.

**Type Distinctions in Variable Names**

Provide hints about the purpose or nature of the variable.






# Korean

### 코딩

설계 명세에 나타낸 대로 요구를 만족할 수 있는 프로그래밍
오류가 적은 품질 좋은 프로그램

→  설계 명세만 제대로 작성해도 이미 작업은 끝난 것이다. 

오류는 수만 가지가 있지만 대체적인 오류는 그 유형이 정해져 있다. 
- 메모리 누수
- 중복된 프리 선언
- NULL의 사용
- 별칭의 남용
- 배열 인덱스 오류
- 수식 예외 오류
- 하나 차이에 의한 오류
- 사용자 정의 자료형 오류
- 스트링 처리 오류
- 버퍼 오류
- 동기화 오류 

**메모리 누수**

메모리가 프리되지 않고 프로그램에 계속 할당되는 현상(동적 할당 시 주의)
장기로 수행되는 시스템에는 치명적인 영향을 줄 수 있다. 

**중복된 프리선언**

프로그램 안에서 사용하는 자원은 먼저 할당되고 사용 후에는 프리로 선언
이미 프리로 선언된 자원을 또다시 프리로 선언하는 경우 오류 

**NULL의 선언**

NULL을 포인트하고 있는 곳의 콘텐츠를 접근하려고 하면 오류 
이러한 오류는 시스템을 다운시킴 

**별칭의 남용**

별칭은 많은 문제를 야기
서로 다른 주소 값을 예상하고 사용한 두 개의 변수의 값이 
별칭 선언으로 인하여 같은 값이 되었을 때 오류 발생 

**배열 인덱스 오류**

배열 인덱스가 한도를 벗어나면 예외 오류 발생
배열 인덱스가 음수 값을 갖는 경우 오류 발생 

**수식 예외 오류** 

0으로 나누는 오류 
변동 소수점 예외 오류 

**하나 차이에 의한 오류** 

0으로 시작해야 할 것을 1로 시작
<=N으로 써야 할 곳에 < N을 쓴 경우 
컴파일러나 테스트 도구에 의해 검출되지 않는 경우가 많음

**사용자 정의 자료형 오류**

오버 플로우나 언더 플로 오류가 쉽게 발생
사용자 정의 자료형의 값을 다룰 때는 특별한 주의 

**스트링 처리 오류** 

strcpy(), sprint 등 많은  string 처리 함수가 있다. 
매개변수가 NULL
스트링이 NULL로 끝나지 않았을 경우
source 매개변수의 크기가 destination 매개변수보다 크지 않을 경우 

**버퍼오류**

프로그램이 버퍼에 복사하여 입력받으려 할 때 
입력 값을 고의로 아주 크게 주면 스택의 버퍼에 오버플로 발생 

버퍼 오버플로를 이용하여 해커들이 자신의 코드를 실행시킬 수 있음 

**동기화 오류**

공통 자원을 접근하려는 다수의 스레드가 있는 병렬 프로그램에서 흔히 발생함 

데드락 - 다수의 스레드가 서로 자원을 점유하고 릴리스하지 않는 상태

레이스 컨디션 - 두 개의 스레드가 같은 자원을 접근하려 하여 수행 결과가 스레드들의 실행순서에 따라 다르게 되는 경우 

모순이 있는 동기화 - 공유하는 변수를 접근할 때 로킹과 언로킹을 번갈아 하는 상황에서 오류가 발생 

대표적인 기준은 간결하고 읽기 쉬운 것 

간결함: 복잡하지 않고 명확하여 이해하기 쉬운 것 
읽기 쉽다: 프로그램을 대충 훑어보거나 이해하기 쉬운 것 

설계에서 모듈화의 목표, 높은 응집력, 낮은 결합도를 달성하였다면 모듈은 간단해짐 

### 명명 규칙

**카멜 케이스** 
클래스, 필드, 메소드 및 변수 이름
여러 단어를 함께 붙여 쓰되 각 단어의 첫 글자는 대문자

상수는 모두 대문자로 

클래스와 인터페이스 이름
명사 또는 명사구이며 대문자로 시작 

**메서드 이름**

일반적으로 소문자로 시작하는 동사구 

함수 이름은 일반적으로 값을 설명하는 명사구로 

필드의 값을 접근하여 리턴하는 함수는 get

조건을 묻는 부울 함수의 이름은 대개 is로 시작

**변수 이름**

일반적으로 소문자로 시작

용도에 대한 힌트를 제공

모호한 이름을 사용하지 않음

변수 이름의 길이 

대상이 사용된 위치를 고려
매개변수: 되도록 짧게
필드변수: 가능한 길고 의미가 담겨 있어야 함 

**패키지 이름**

일반적으로 모두 소문자이며 명사로

**변수 이름 앞에 타입 구별**

변수의 목적 또는 변수가 무엇인지에 대한 힌트를 줌


