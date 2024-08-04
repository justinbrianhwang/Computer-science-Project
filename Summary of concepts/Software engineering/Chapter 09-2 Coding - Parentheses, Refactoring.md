# English

### Coding

Programming that meets the requirements specified in the design specifications
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

### Indentation and Braces

Used to clarify the program structure.
Part of a statement and declarations are indented.

If the intent is that both statements are included in the if control structure, it is wrong.
Leave a space between the keyword and the next parenthesis to distinguish between control structures and method calls.

Statements or expressions are packaged into methods and classes.

Block Statements
     Can reduce confusion when control structures are nested.
Expressions
      Use parentheses to clarify the order of operations.

**How to Handle Invalid Data**

- Parameter errors
- Input error prevention
- List boxes
- Default values

**Comments**

Helpful during debugging.

Make it easier for others to understand the program.

Commenting Rules
- Omit unnecessary words.
- Avoid excessive comments.
- Document class invariants.
- Document the meaning and constraints of class attributes.

**Method Comments**

Use javadoc specifications to describe what the method does, along with preconditions.
Write sentences that perform something and mention all relevant parameters.

**Class/Statement Comments**

The file's beginning should include comments explaining the class's purpose.
Statement comments
Group into logical units.

**Association Implementation**

If class A and class B have an n-to-n association:

- 1-to-1 Association
If A needs to call B’s functions, implement A to have a reference to B.
If B needs to call A’s functions, implement B to have a reference to A.

- 1-to-Many
If class A needs to call instance B’s methods, implement class A to have a collection of references to class B.

- Many-to-Many
An association class may be introduced to convert to 1-to-many relationships.

**Implementing Sequence Diagrams**

If a message from object A to object B is shown, define the method in class B.

### Refactoring

Reorganizing the structure of code without changing its results.
A technique to safely improve the design of existing code.
Enhances readability and ease of maintenance.

**Code Smell**

Anything that makes working with the program difficult.
Programs that are hard to read.
Programs with duplicate logic.
Programs requiring special actions to change running code.
Programs with complex conditional statements.

Refactor to make software easier to understand and cheaper to modify.
Change the internal structure without altering the external behavior.

**Goals of Refactoring**

Improve software design.
Make the software easier to understand.
Help in finding bugs.
Aid in faster program writing.

**Refactoring Process**

Small changes - single refactorings.
Test if all code works properly.
Move to the next refactoring step if everything works.
If not, resolve issues and undo refactoring to maintain system operation.

Methods like method extraction/class extraction.

**Improving Code Quality**

Code Inspection
- Reviewing and checking the program by reading it.

Static Analysis
- Checking for dead code, undeclared variables, etc.

Pair Programming
- Two people share a machine to code and test in agile methods.

Code Inspection

Occurs after successful compilation and static analysis.
Identify hidden defects in the code.
Check efficiency and adherence to coding standards.

Severity
- Indicates the priority of the defect.

Types of Defects
- Logic issues.
- Computing issues.
- Interface/timing issues.
- Data processing.

**Static Analysis**

Systematically analyzing the program text to find defects.
Automated using software tools.

Two methods to find defects:
1) Detect abnormal patterns or unwanted patterns in the code.
2) Directly find defects that may cause runtime failures.

Data Anomalies
- Redundant code.

**Test-Driven Development**

Writing code for tests first, then implementing functionality.
Primarily tests methods within classes.
Development process.


# Korean

### 코딩

설계 명세에 나타낸 대로 요구를 만족할 수 있는 프로그래밍
오류가 적은 품질 좋은 프로그램

→ 설계 명세만 제대로 작성해도 이미 작업은 끝난 것이다.

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
이미 프리로 선언된 자원을 또 다시 프리로 선언하는 경우 오류

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
컴파일러나 테스트 도구에 의하여 검출되지 않는 경우가 많음

**사용자 정의 자료형 오류**

오버 플로우나 언더 플로 오류가 쉽게 발생
사용자 정의 자료형의 값을 다룰 때는 특별한 주의

**스트링 처리 오류**

strcpy(), sprintf 등 많은 string 처리 함수가 있다.
매개변수가 NULL
스트링이 NULL로 끝나지 않았을 경우
source 매개변수의 크기가 destination 매개변수보다 크지 않을 경우

**버퍼 오류**

프로그램이 버퍼에 복사하여 입력 받으려 할 때
입력 값을 고의로 아주 크게 주면 스택의 버퍼에 오버플로 발생

버퍼 오버플로를 이용하여 해커들이 자신의 코드를 실행시킬 수 있음

**동기화 오류**

공통 자원을 접근하려는 다수의 스레드가 있는 병렬 프로그램에서 흔히 발생함

데드락 - 다수의 스레드가 서로 자원을 점유하고 릴리스 하지 않는 상태

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

### 들여쓰기와 괄호

프로그램 구조를 명확하게 하기 위해 사용
문장의 일부와 선언문은 들여쓰기

의도가 두 개의 문장이 모두 if 제어 구조에 포함된 문장이라면 잘못
키워드와 다음 괄호 사이에 공백을 두어 제어 구조와 메서드 호출과 구별하게

문장이나 수식은 메소드 클래스로 패키지화

문장블록
     제어구조가 중첩되었을 때 생기는 혼란은 줄일 수 있음
수식
      괄호를 이용하여 오퍼레이션의 순서를 명확히

**잘못된 데이터는 어떻게 다룰 것인가?**
- 매개변수 오류
- 입력 오류 방지
- 리스트 박스
- 디폴트 값을 지정

**주석**
디버깅하는 동안 얻을 수 있는 도움

다른 사람들이 프로그램을 이해하기 쉽도록 함

주석다는법
- 불필요한 단어는 생략
- 과도한 주석은 피함
- 클래스 불변조건
- 클래스의 속성에 대한 의미와 제약 기술

**메서드 주석**

메서드가 하는 일을 설명하는 javadoc 스펙을 선행 조건과 함께 쓴다
무언가를 수행한다는 문장으로 작성하여 관련된 모든 매개변수를 언급

**클래스/문장 주석**

파일의 시작 부분에는 클래스의 용도를 설명하는 주석이 포함되어야
문장주석
논리적 단위로 그룹화

**연관 구현**

클래스 A와 B사이에 n 대 n 연관 관계가 있다.

- 1 대 1연관
A에서 B의 함수를 호출할 필요가 있다면 A가 B에 대한 참조를 갖도록 구현
반대로 B에서 A의 함수를 호출할 필요가 있다면 B가 A에 대한 참조를 갖도록 구현
- 1 대 다
클래스 A에서 인스턴스 B의 메소드를 호출할 것이 있다면
클래스 A가 클래스 B의 참조를 모음으로 가지고 있도록 구현
- 다 대 다
중간에 연관 클래스 도입하여 1대 다의 관계로 바꾸어 설계하기도 한다

**시퀸스 다이어그램의 구현**

A 객체에서 B 객체로 나가는 메시지가 표시되어 있다면 메소드는 B 클래스에 정의

### 리펙토링

결과의 변경 없이 코드의 구조를 재조정
이미 존재하는 코드의 디자인을 안전하게 향상시키는 기술
가독성을 높이고 유지보수를 편하게 하기 위한 것

**코드 스멜**

프로그램에 대한 작업을 어렵게 만드는 것
읽기 어려운 프로그램
중복된 로직을 가진 프로그램
실행 중인 코드를 변경해야 하는 특별한 동작을 요구하는 프로그램
복잡한 조건문이 포함된 프로그램

소프트웨어를 보다 쉽게 이해할 수 있고 적은 비용으로 수정할 수 있도록
겉으로 보이는 동작의 변화 없이 내부구조를 변경하는 것

**리펙토링의 목적**

소프트웨어의 디자인을 개선시킨다
소프트웨어를 이해하기 쉽게 만든다
버그를 찾는데 도움을 준다
프로그램을 빨리 작성할 수 있게 도와준다

**리펙토링의 과정**

소규모의 변경 - 단일 리펙토링
코드가 전부 잘 작동되는지 테스트
전체가 잘 작동하면 다음 리팩토링 단계로 전진
작동하지 않으면 문제를 해결하고 리팩토링 한 것을 undo 하여 시스템이 작동되도록 유지

메서드 추출/클래스 추출 등

**코드 품질 향상**

코드 인스팩션
- 프로그램을 읽어보고 눈으로 확인하는 방법

정적 분석
- 수행되지 않는 데드 코드가 없는지, 선언이 되지 않고 사용한 변수가 없는지 등을 검사

페어 프로그래밍
- 애자일 방법에서 프로그래밍과 테스팅을 담당하는 두 사람이 머신을 공유하며 코딩

코드 인스펙션

프로그램이 성공적으로 컴파일 되고 정적 분석 도구에 의하여 검사된 후에 이루어짐
코드에 묻혀있는 결함을 찾아내는 것
효율성, 코딩 표준의 준수 여부 등

심각도
- 결함의 우선순위를 나타냄

결함의 타입
- 로직 문제
- 컴퓨팅 문제
- 인터페이스/타이밍 문제
- 데이터 처리

**정적분석**

프로그램 텍스트를 조직적으로 분석하여 결함을 찾아내는 것

소프트웨어 도구를 이용하여 자동으로 가능

결함을 찾는데 두 가지 방법 사용
1) 코드에 존재하는 결함으로 나타날 비정상적인 패턴이나 원하지 않는 패턴을 찾는 방법
2) 실행할 때 프로그램의 고장을 일으킬 코드 상에 존재하는 결함을 직접 찾는 방법

자료변칙
사족

**테스트 중심 개발**

테스트를 위한 코드를 작성한 후 기능을 구현
주로 클래스 안에 있는 메서드를 시험
개발 과정
