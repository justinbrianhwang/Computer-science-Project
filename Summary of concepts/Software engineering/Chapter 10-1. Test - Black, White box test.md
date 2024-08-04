# English

### Testing

Software development is a human-centered and intellectual activity. Since it is performed by humans, it is prone to errors.

Reducing coupling:
- Prevention: Inspection, static analysis
- Identification and removal: Testing, debugging

Testing:
Executing the software with test cases to verify if the system behaves as expected. Testing consumes more than 50% of time and budget.

### Terminology

1. Bug: A general term used to describe a problem, defect, or difficulty.
2. Error: Mistakes made by developers in design or coding.
3. Fault: The result of errors that cause system failures. Declared errors in code or documentation.
4. Failure: The inability of a system to perform its required functions.

Testing aims to discover errors by executing programs. Perfect testing is impossible. Testing is a creative and challenging task. It prevents error introduction and should be performed by an independent team not involved in implementation.

### Steps

1. Define what to check through testing.
2. Determine the testing methods.
3. Develop test cases.
4. Document the expected correct results.
5. Execute with the test cases.

![stage](https://i.imgur.com/MODpfBu.png)

### Test Cases

The most critical factor for successful testing is identifying test cases. These include inputs that can check for faults, test conditions, test data, expected results, and test case specifications.

## Black-Box Testing

Testing the functionality or performance of the subject without considering the internal paths. Focuses on system input and output. Based on requirements and specifications.

![black Box](https://i.imgur.com/72885a1a-5288-4763-a9be-6197325409b0.png)

**Advantages**

- No technical background needed for testing.
- Testers and developers can work independently.
- Effective for large and complex applications.

**Disadvantages**

- Testing can only start after coding is completed.
- Complete testing is impossible for large and complex subjects.

### Equivalence Partitioning

Equivalence classes: Identify inputs expected to produce similar behavior and select representative values for testing. Consider both normal and abnormal inputs.

### Boundary Value Analysis

Focuses on testing at the boundary values. Boundaries are values near the limits where system behavior changes.

### Cause-Effect Graph

A test technique for systematically selecting input condition combinations. Represented by nodes and symbols. Nodes: causes (input conditions), effects (output conditions). Symbols: ∨(and), ∧(or), ∾(not). Use decision tables to list combinations of conditions for each result.

## White-Box Testing

A method to observe the internal operations of a module in detail. Systematically examines the logical structure of a module - structural testing.

**Testing Process**

1. Understand the application structure through source code - logical flowcharts.
2. Set verification criteria (coverage).
3. Prepare test data to drive each path.

Logical flowcharts: Graphs representing the flow within a module.

### Statement Coverage

Verifies that each line of code is executed at least once.

### Branch Coverage

Each IF statement has two branches, True and False.

### Path Coverage

Tests all execution paths.

### State-Based Testing

Targets systems that exhibit the same behavior and produce the same results for the same inputs. Batch processing systems, computation-centric systems, hardware-based circuits. System behavior is determined by the system state.

State model components:
- State: Indicates the effect of past inputs on the system.
- Transition: Describes how the system changes from one state to another in response to an event.
- Event: Input to the system.
- Action: Output in response to an event.

### Integration Testing

Tests the coupling of module interfaces. Targets unit modules developed by various teams. Tests the integration of module-to-module coupling.

Methods vary by module integration order:
- Big Bang
- Top-Down
- Bottom-Up
- Sandwich

**Integration Testing - Big Bang Integration**

Integrates all modules at once.

Advantages:
- Easy schedule management.
- No need to create stubs for integration.

Disadvantages:
- Difficult to locate and identify errors.
- Requires significant time and effort for unit testing.
- Many drivers/stubs needed.
- Hard to predict development progress.

![Big bang](https://i.imgur.com/7tW2vtV.png)

**Integration Testing - Top-Down Integration**

Starts integration from the topmost module in the system structure.

Advantages:
- Early testing of critical module interfaces.
- Early system implementation with stubs.
- Developer-friendly.

Disadvantages:
- Input/output modules are relatively lower.
- Difficult to write and execute test cases.
- Core functions are implemented last.

![under](https://i.imgur.com/6Sa9FaP.png)

**Integration Testing - Bottom-Up Integration**

Starts integration from the bottommost module in the system structure.

Advantages:
- Incremental integration approach.
- Easy to find errors.
- Distributed hardware usage.
- More tests on lower modules than upper layers.

Disadvantages:
- Initially lacks system skeleton.
- Critical upper-layer interfaces are confirmed last.
- Limited opportunities for clients to test the system.

![down](https://i.imgur.com/kYDi29K.png)

**Integration Testing - Sandwich Integration**

Begins with minimal modules that perform specific functions. Input, output, and basic functionality modules. Develops relatively important modules first.

Advantages:
- Forms system skeleton early.
- Early client feedback.
- Easy to divide and develop the system.



# Korean

### 테스트

소프트웨어 개발은 인간 중심의 활동이며 지적인 활동이다. 사람이 직접하기에 오류가 발생하기 쉬운 활동이다.

결합을 낮추는 방법:
- 방지: 인스펙션, 정적 분석
- 식별하고 제거: 테스트, 디버깅

테스트:
시험할 소프트웨어의 테스트 케이스를 주어 실행시킨 후 시스템의 동작이 예상한 대로 실행되는지 확인하는 것. 테스트는 시간/예산의 50% 이상을 소비한다.

### 용어 정리

1. 버그: 문제, 결함 또는 난이도를 나타내는 데 일반적으로 사용되는 용어
2. 오류: 개발자가 잘못하여 설계나 코딩에 실수한 것
3. 결함: 시스템이 고장을 일으키게 하는 오류의 결과, 코드 또는 문서에 오류가 있다고 선언된 것
4. 고장: 시스템이 원하는 작업을 수행할 수 없는 상황, 현상

테스트는 오류를 발견하려고 프로그램을 실행시키는 것. 완벽한 테스트는 불가능하다. 테스트는 창조적인 일이며 힘든 일이다. 테스트는 오류의 유입을 방지하며, 구현과 관계없는 독립된 팀에 의해 수행되어야 한다.

### 단계

1. 테스트에 의하여 무엇을 점검할 것인지 정한다
2. 테스트 방법을 결정한다
3. 테스트 케이스를 개발한다
4. 테스트의 예상되는 올바른 결과를 작성한다
5. 테스트 케이스로 실행시킨다

![stage](https://i.imgur.com/MODpfBu.png)

### 테스트 케이스

성공적인 테스트를 위해 가장 중요한 것은 테스트 케이스를 찾아내는 것이다. 결함을 검사할 수 있는 입력, 시험조건, 테스트 데이터, 예상 결과, 테스트 케이스 명세서를 포함한다.

## 블랙박스 테스트

내부 경로에 대한 지식을 보지 않고 테스트 대상의 기능이나 성능을 테스트한다. 시스템의 입력 및 출력에 중점을 둔다. 요구 사항 및 사양을 기반으로 한다.

![black Box](https://i.imgur.com/72885a1a-5288-4763-a9be-6197325409b0.png)

**장점**

- 테스트를 하기 위한 기술적 배경이 필요하지 않다.
- 테스터와 개발자가 독립적으로 작업할 수 있다.
- 크고 복잡한 응용 프로그램에 효과적이다.

**단점**

- 코딩이 완료되어야만 테스트를 시작할 수 있다.
- 크고 복잡한 테스트 대상은 완전한 테스트 범위가 불가능하다.

### 동등 분할 기법

동등 클래스: 시스템의 동작이 같을 것으로 예상되는 입력을 찾고 대푯값을 선정하여 테스트. 정상적인 입력 뿐만이 아니라 비정상적인 입력도 고려.

### 경계값 분석

입력 값의 경계선에 중점을 두는 테스트. 경계는 시스템의 동작이 변경되는 한계 근처의 값.

### 원인과 결과 그래프

입력 조건의 조합을 체계적으로 선택하는 테스트 기법. 노드와 기호로 표시. 노드: 원인(입력 조건), 결과(출력 조건). 기호: ∨(and),∧(or), ∾(not). 결정 테이블을 사용하여 각각의 결과들에 대하여 조건의 조합을 나열.

## 화이트 박스 테스트

모듈 안의 작동을 자세히 관찰하는 시험 방법. 모듈의 논리적인 구조를 체계적으로 점검 - 구조적 테스트.

**테스트 과정**

1. 원시 코드를 통해 애플리케이션의 구조를 이해 - 논리 흐름도
2. 검증 기준(커버리지)을 정한다.
3. 각 경로를 구동시키는 테스트 데이터를 준비

논리 흐름도: 모듈 내의 흐름을 간선으로 표시한 그래프

### 문장 커버리지

각 라인이 적어도 한 번 실행되는지를 검증

### 분기 커버리지

IF 문에는 True와 False의 두 가지

### 경로 커버리지

모든 실행 경로를 테스트하는 기준

### 상태 기반 테스팅

같은 입력에 대해 같은 동작을 보이며 동일한 결과를 생성하는 시스템을 대상으로 한다. 배치 처리 시스템, 계산 중심 시스템, 하드웨어로 구성된 회로. 시스템의 동작은 시스템의 상태에 의해 좌우됨.

상태 모델 구성 요소:
- 상태: 시스템의 과거 입력에 대한 영향을 표시
- 트랜지션: 이벤트에 대한 반응으로 시스템이 하나의 상태에서 다른 상태로 어떻게 변해가는지를 나타냄
- 이벤트: 시스템에 대한 입력
- 액션: 이벤트에 대한 출력

### 통합 테스트

모듈의 인터페이스 결합을 테스트. 여러 개발 팀에서 개발한 각각의 단위 모듈을 대상으로 한다. 모듈-모듈 간의 결합을 테스트.

모듈의 결합 순서에 따라 방법이 다르다:
- 빅뱅
- 하향식
- 상향식
- 연쇄

**통합테스트 - 빅뱅통합**

한번에 모든 모듈을 모아 통합.

장점:
- 일정에 대한 관리가 편하다.
- 통합을 위하여 스텁을 구성할 필요가 없다.

단점:
- 오류의 위치와 원인을 찾기 어렵다.
- 단위 테스트에 많은 시간과 노력이 든다.
- 준비해야 할 드라이버/스텁 수가 많다.
- 개발 진도를 예측하기 어렵다.

![Big bang](https://i.imgur.com/7tW2vtV.png)

**통합테스트 - 하향식 통합**

시스템 구조상 최상위에 있는 모듈부터 통합.

장점:
- 중요한 모듈의 인터페이스를 조기에 테스트.
- 스텁을 이용하여 시스템 모습을 일찍 구현 가능.
- 개발자 입장에서 용이하다.

단점:
- 입출력 모듈이 상대적으로 하위에 있음.
- 테스트 케이스 작성 및 실행이 어려움.
- 중요 기능이 마지막에 구현됨.

![under](https://i.imgur.com/6Sa9FaP.png)

**통합테스트 - 상향식 통합**

시스템 구조상 최하위에 있는 모듈부터 통합.

장점:
- 점증적 통합 방식.
- 오류 발견이 쉬움.
- 하드웨어 사용 분산.
- 하위 모듈을 상위층보다 더 많이 테스트.

단점:
- 초기에 시스템의 뼈대가 갖추어지지 않음.
- 상위층의 중요한 인터페이스가 마지막에 가서야 확인 가능.
- 의뢰자에게 시스템을 시험해 볼 기회를 충분히 제공하지 못함.

![down](https://i.imgur.com/kYDi29K.png)

**통합 테스트 - 연쇄식 통합**

특정 기능을 수행하는 모듈의 최소 단위로부터 시작. 입력, 출력. 어느 정도의 기본 기능을 수행하는 모듈. 상대적으로 중요한 모듈부터 개발.

장점:
- 초기에 시스템에 골격이 형성된다.
- 사용자 의견을 빨리 확인 가능.
- 시스템을 나누어 개발하기 쉽다.
