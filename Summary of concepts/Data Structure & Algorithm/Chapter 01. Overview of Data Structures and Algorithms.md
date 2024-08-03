# English

### Data Structures Concept

Why do we need data structures? When we create software, we rarely start from scratch. After analyzing customer requirements, we go through the process of drawing up design plans, and data structures are often used in this stage.

Why do we organize and structure data in daily life?
- To use things conveniently and efficiently. Without organization, finding or searching becomes inconvenient.

Data structures refer to various structures for organizing and arranging data in a computer.

Characteristics:
- Efficient data storage methods in a computer
- Memory conservation
- Reduced program execution time

The design of data structures, considering the execution time or storage space of a program, depends on how the program is used.

Programs consist of data and commands, and data structures are necessary for processing these appropriately.

### Types of Data Structures

![data structure](https://i.imgur.com/DJduUWD.png)

**Evolution of Data Structures**

1. Simple Structures
- Basic structures provided by programming languages
- Data types
- Examples: integers, floats, characters, strings

2. Linear Structures
- Data elements have a one-to-one relationship
- Examples: lists, stacks, queues, deques

3. Non-Linear Structures
- Data elements have hierarchical or network relationships
- Examples: trees, graphs

4. File Structures
- Data structures for files stored in secondary storage devices

### Abstract Data Types (ADT)

Overview of Abstract Data Types:
- A key method for describing data structures
- Information hiding
- Shows only essential information and hides irrelevant details

**Types**

1. Integer: data + operators
2. Command: calculate distance between positions, equal()

### Concept of Algorithms

An algorithm is a set of computer instructions. Broadly, it is one component that makes up a computer program along with data structures. In a narrow sense, it is a procedure to solve a specific problem.

Characteristics of Algorithms:
- Input: Must have zero or more external inputs
- Output: Must produce at least one result
- Definiteness: Each instruction must be clear and unambiguous
- Finiteness: Must terminate after a finite number of steps
- Effectiveness: All operations must be feasible

### Relationship Between Algorithms and Data Structures

The performance of an algorithm depends on the data structure:
- Different representations and storage methods for the same data can result in different algorithms.
Algorithms are used to implement basic operations of data structures:
- Algorithms for arithmetic operations, etc.

### Algorithm Representation

**Natural Language**: Expressed in general human language
- Not suitable for algorithm representation due to lack of consistency and clarity.

**Flowcharts**: Graphical representation of algorithms

**Pseudocode**:
- Expressed in a fictitious language, not a specific programming language
- Less strict grammar than programming languages but more structured than natural language
- Syntax may vary between data structure/algorithm books
- Also called pseudo-code or pseudo-language in different books

**Programming Language**:
- Expressed in languages like C
- Advantages: No additional implementation steps required
- Disadvantages: May be too strictly written, causing inefficiencies

### Algorithm Performance Analysis Criteria

Space Complexity

**Time Complexity**:
- Measure actual elapsed time
- Count the number of executed instructions
- Time complexity function
- Frequency of operations based on input values

Time Complexity = Big-O Notation

# Big-O Notation Overview

Big-O Notation is a mathematical notation used to describe the performance of algorithms, mainly in terms of time complexity and space complexity. It shows how the performance changes as the input size n increases. It represents the worst-case performance and plays a crucial role in evaluating algorithm efficiency.

## Time Complexity

Time complexity represents the time taken by an algorithm to run as a function of the size of the input. Major time complexity types include:

- **O(1)**: Constant time complexity - Takes a constant amount of time regardless of input size.
- **O(log n)**: Logarithmic time complexity - Increases proportionally with the logarithm of the input size.
- **O(n)**: Linear time complexity - Increases linearly with the input size.
- **O(n log n)**: Linearithmic time complexity - Increases with the input size times the logarithm of the input size.
- **O(n^2)**: Quadratic time complexity - Increases with the square of the input size.
- **O(2^n)**: Exponential time complexity - Increases exponentially with the input size.
- **O(n!)**: Factorial time complexity - Increases with the factorial of the input size.

## Space Complexity

Space complexity represents the memory space required by an algorithm as a function of the input size. Similar to time complexity, it is expressed using Big-O Notation.

- **O(1)**: Constant space complexity - Requires a constant amount of memory regardless of input size.
- **O(n)**: Linear space complexity - Requires memory proportional to the input size.
- **O(n^2)**: Quadratic space complexity - Requires memory proportional to the square of the input size.

## Examples

Here are some examples of time complexities for different algorithms:

1. **Element Search in Array**: Searching for a specific element in an array has a constant time complexity O(1).
2. **Sorting Algorithms**: Quick sort and merge sort have an average time complexity of O(n log n).
3. **Nested Loops**: An algorithm with nested loops has a quadratic time complexity O(n^2).

## Conclusion

Big-O Notation is an essential tool for evaluating and comparing algorithm performance. Considering time complexity and space complexity when designing or selecting algorithms can lead to more efficient programs.


# Korean

### 자료구조의 개념

자료구조가 필요한 이유는 무엇일까? 우리가 소프트웨어를 만들 때 처음부터 만드는 경우는 잘 없다. 고객의 요구를 분석한 후 설계도를 그리는 과정을 거치게 되는데 이때 주로 사용되는 것이 바로 자료구조이다.

일상 생활에서 자료를 정리하고 조직화하는 이유는 무엇일까?
- 사물을 편리하고 효율적으로 사용하기 위함이다. 체계 없이 정리할 경우, 찾기 또는 검색이 불편해진다.

그렇다면, 자료구조는, 컴퓨터에서 자료를 정리하고 조직화하는 다양한 구조를 의미한다.

특징은 다음과 같다

- 컴퓨터에서 자료를 효율적으로 저장하는 방식
- 메모리 절약
- 프로그램 수행 시간 단축

프로그램의 수행 시간 혹은 저장 공간을 고려한 자료구조의 설계 → 프로그램이 어떻게 사용되는지에 따라 결정

프로그램은 자료와 명령어로 구성되어있다. 이들을 적절히 처리하는 과정에서 자료구조가 필요한 것이다.

### 자료구조의 종류

![data structure](https://i.imgur.com/DJduUWD.png)

**자료구조의 발전**

1. 단순구조
    - 프로그래밍 언어에서 기본으로 제공
    - 데이터 타입
    - 예) 정수, 실수, 문자, 문자열 
2. 선형구조
    - 자료들 사이의 앞뒤 관계가 일대일인 경우
    - 예) 리스트, 스택, 큐와 덱 등 
3. 비선형구조
    - 자료들 사이의 앞 뒤 관계가 계층 구조 혹은 망 구조
    - 예) 트리, 그래프 등 
4. 파일 구조
    - 보조 기억 장치에 저장되는 파일에 대한 자료 구조 

### 추상 자료형

추상자료형의 개요
- 자료구조를 기술하는 가장 대표적인 방법 중 하나 
- 정보 은닉
- 중요한 정보만을 나타내고, 중요하지 않은 정보는 숨기는 것 

**종류**

1. 정수형 → 자료 + 연산자
2. 명령
    - 위치 사이의 거리 계산
    - equal() 

### 알고리즘 개념

컴퓨터 명령어들의 집합을 알고리즘이라 한다. 넓은 의미로 자료구조와 함께 컴퓨터 프로그램을 구성하는 한가지 요소이다. 좁은 의미로는 어떠한 문제를 해결하기 위한 절차이다.

알고리즘의 특성
입력
- 외부에서 제공되는 자료가 0개 이상 있어야 함 
출력
- 적어도 1개 이상의 결과를 만들어야 함 
명백성
- 각 명령어는 의미가 모호하지 않고 명확해야 함 
유한성
- 한정된 수의 단계 뒤에는 반드시 종료
유효성
- 모든 명령은 실행 가능한 연산이어야 함 

### 알고리즘과 자료구조와의 관계

알고리즘의 성능은 자료구조에 종속됨
- 같은 자료라 하더라도 어떻게 표현되고 저장되느냐에 따라 사용 가능한 알고리즘이 달라지기 때문 
자료구조의 기본적인 연산을 구현하기 위해서는 알고리즘이 사용
- 사칙 연산등을 위한 알고리즘 사용 

### 알고리즘 표현

**자연어** - 사람이 사용하는 일반적인 언어로 표현
→ 알고리즘 표현으로는 부적절하다. 기술하는 사람에 따라 일관성과 명확성이 달라지기 때문.

**순서도** - 알고리즘을 도식화해서 표현 

**의사코드** 
- 특정 프로그래밍 언어가 아닌 가상의 언어로 표현
- 프로그래밍 언어보다는 덜 엄격한 문법이나, 자연어보다는 더 체계적으로 기술이 가능
- 자료구조/알고리즘 책마다 약간씩 구문의 차이가 존재
- 책에 따라 가상코드, 유사코드, 또는 슈도 코드라 불림 

**프로그래밍언어**
- C와 같은 프로그래밍 언어로 표현
- 장점: 추가 구현 단계가 필요 없음
- 알고리즘을 구현 소스를 통해 나타내기 때문 
- 단점: 너무 엄격하게 기술하여 비효율적인 경우가 있음 

### 알고리즘 성능 분석 기준

**공간 복잡도**

**시간 복잡도**
- 실제 걸리는 시간을 측정
- 실행되는 명령문의 개수를 계산
- 시간 복잡도 함수
- 입력 값에 따른 실행 연산의 빈도수 

시간 복잡도 = 빅-오 개념

# 빅오(Big-O) 표기법 개요

빅오 표기법(Big-O Notation)은 알고리즘의 성능을 나타내기 위한 수학적 표기법으로, 주로 알고리즘의 시간 복잡도(Time Complexity)와 공간 복잡도(Space Complexity)를 나타내는 데 사용된다. 빅오 표기법은 입력 크기 n이 증가할 때 알고리즘의 성능이 어떻게 변화하는지를 나타낸다. 이는 최악의 경우 성능을 나타내며, 알고리즘의 효율성을 평가하는 데 중요한 역할을 한다.

## 시간 복잡도(Time Complexity)

시간 복잡도는 알고리즘이 입력 크기 n에 따라 실행되는 데 걸리는 시간을 나타낸다. 주요 시간 복잡도 유형은 다음과 같다:

- **O(1)**: 상수 시간 복잡도 - 입력 크기에 상관없이 일정한 시간이 소요된다.
- **O(log n)**: 로그 시간 복잡도 - 입력 크기가 커질수록 실행 시간이 로그 함수에 비례하여 증가한다.
- **O(n)**: 선형 시간 복잡도 - 입력 크기에 비례하여 실행 시간이 증가한다.
- **O(n log n)**: 선형 로그 시간 복잡도 - 입력 크기와 로그 함수의 곱에 비례하여 실행 시간이 증가한다.
- **O(n^2)**: 이차 시간 복잡도 - 입력 크기의 제곱에 비례하여 실행 시간이 증가한다.
- **O(2^n)**: 지수 시간 복잡도 - 입력 크기가 증가할수록 실행 시간이 지수 함수에 비례하여 급격히 증가한다.
- **O(n!)**: 팩토리얼 시간 복잡도 - 입력 크기의 팩토리얼에 비례하여 실행 시간이 증가한다.

## 공간 복잡도(Space Complexity)

공간 복잡도는 알고리즘이 입력 크기 n에 따라 필요한 메모리 공간을 나타낸다. 시간 복잡도와 유사하게, 공간 복잡도도 빅오 표기법을 사용하여 표현된다.

- **O(1)**: 상수 공간 복잡도 - 입력 크기에 상관없이 일정한 메모리 공간이 필요하다.
- **O(n)**: 선형 공간 복잡도 - 입력 크기에 비례하여 메모리 공간이 필요하다.
- **O(n^2)**: 이차 공간 복잡도 - 입력 크기의 제곱에 비례하여 메모리 공간이 필요하다.

## 예시

다음은 몇 가지 알고리즘의 시간 복잡도 예시이다:

1. **배열의 요소 검색**: 배열에서 특정 요소를 찾는 연산은 상수 시간 복잡도 O(1)이다.
2. **정렬 알고리즘**: 퀵 정렬과 병합 정렬의 평균 시간 복잡도는 O(n log n)이다.
3. **이중 루프**: 이중 루프를 사용한 알고리즘의 시간 복잡도는 O(n^2)이다.

## 결론

빅오 표기법은 알고리즘의 성능을 평가하고 비교하는 데 중요한 도구이다. 알고리즘을 설계하거나 선택할 때 시간 복잡도와 공간 복잡도를 고려하면 더 효율적인 프로그램을 작성할 수 있다.


