# In English

### Agile Process (Extreme Programming)

An agile method suitable for small development teams facing uncertain and frequently changing requirements.
1. User Stories - Write simple user stories instead of long requirement documents.
2. Daily Builds and Integration - Build and integrate the developed code daily.
3. Test-Driven Development - Write test scenarios to verify requirements before coding. 
Create the minimal code to pass the test scenarios. 
Refactor the code to meet standards.
4. Pair Programming - Two programmers share one computer; one codes while the other reviews. They switch roles and continue development.
Continuously review to improve quality.
Share knowledge to reduce problem-solving time.

### Agile Process (Scrum)

A method that helps the development team work together.
All team members communicate and collaborate to develop software in short cycles.
A collection of tasks, roles, and deliverables for developing software.
Set priorities for tasks (backlog) even if the whole project is not known.
Repeat short cycles (sprints) to shorten release cycles.

### Agile Process

Advantages:
1. Can deploy software faster than other process models.
2. Less resource waste as the latest work is always being done.
3. Can detect and fix defects faster.
4. Spend less time on documentation.

Disadvantages:
1. Poor documentation makes it hard for new developers to catch up.
2. Continuous interaction between developers and customers is required.
3. The project can end ambiguously without a clear finish.

### Support Processes
- Processes of different nature that need to be performed at each stage, not centered on development.

- Contract Perspective - Acquisition process, supply process
- Operational Perspective - Operational process
- Engineering Perspective - Development process, maintenance process
- Management Perspective - Management process, improvement process
- Support Perspective - Documentation process, configuration management process, quality assurance process, problem resolution process

### Support Processes (Management Process)
Proper management ensures well-integrated software development.
All tasks necessary for managing projects to achieve cost and quality goals.
**Planning** - Cost, schedule prediction/decisions on interim checks
**Monitoring** - Ensure development aligns with objectives and progresses as planned.
**Control and Analysis** - Analyze and adjust based on findings from monitoring.

Project monitoring and control span all development process stages, thus taking the longest duration.

### Support Processes (Quality Assurance Process)
Manage and improve the quality of processes and deliverables.

### Inspection Process
Efforts to find or prevent defects in development results.
A peer group inspects work results according to a defined process.

### Process Management Process
Ensure and improve the correctness of the software development process.

### Methodology
= Development methods
Without a clear definition, methodology can be confused with the process.
Defines how to perform each task in the software process.
The process indicates what tasks need to be done but not how to do them.

### Structured Methodology
Principle of divide and conquer.
Handles complex problems by breaking them down.
Uses data flow diagrams.
Converts data flow diagrams into structure charts.

![data flow chart](https://i.imgur.com/KbTSpEj.png)

### Information Engineering Methodology
- Enterprise-centered
- Focus on strategic system planning
- Data-centered
- Divide and conquer
- Engineering approach
- Active user participation

![Information Engineering Methodology](https://i.imgur.com/hErLXkC.png)

### Object-Oriented Methodology
- Define data and functions closely together as objects.
- Use messages between objects to handle desired functions.
- Modularize and encapsulate large systems into classes.

### Methodology Comparison

- Features:
    - Structured Methodology: Program logic-centered, use diagrams to analyze and systematize requirements.
    - Information Engineering Methodology: Enterprise information-centered, data-centered, engineering approach using CASE tools.
    - Object-Oriented Methodology: Analyze with business use cases, identify classes that group data and functions.
- Design Concerns:
    - Structured Methodology: Function-oriented.
    - Information Engineering Methodology: Data-oriented.
    - Object-Oriented Methodology: Class-oriented.
- Design Focus:
    - Structured Methodology: Modules.
    - Information Engineering Methodology: Entities.
    - Object-Oriented Methodology: Objects.
- Core Methods:
    - Structured Methodology: Programming techniques.
    - Information Engineering Methodology: Enterprise strategy and deliverables.
    - Object-Oriented Methodology: Design representation.
- Advantages:
    - Structured Methodology: Relatively easy project planning and monitoring. Easy to understand the method for requirement analysis.
    - Information Engineering Methodology: Flexible to business procedure and environment changes due to data-centered approach. Suitable approach for enterprises.
    - Object-Oriented Methodology: Close modeling to real-world, easy maintenance, easy transition to coding, reusable code.
- Disadvantages:
    - Structured Methodology: Difficult transition from analysis to design process.
    - Information Engineering Methodology: Time-consuming for small-scale automation business areas, not suitable for independent system development from specific business areas.
    - Object-Oriented Methodology: Lack of adequately trained programmers.



# In korean

### 애자일 프로세스(익스트림 프로그래밍)

소규모 개발 조직이 불확실하고 변경이 많은 요구일 때 적절한 애자일 방법이다.
1. 사용자 스토리 - 긴 요구사항 문서가 아닌 간단한 사용자 스토리 작성
2. 매일 빌드와 통합 - 개발한 것을 매일 빌드하고 통합
3. 테스트 주도 개발 - 코딩에 앞서 요구사항을 검증하는 테스트 시나리오를 작성. 
테스트 시나리오를 통과하기 위한 최소한의 코드를 생성. 
작성한 코드를 표준에 맞도록 리팩토링
4. 짝 프로그래밍 - 두 명의 프로그래머가 하나의 컴퓨터를 공유하여 한 사람은 코딩하고 한 사람은 확인하며 개발. 둘이 역할을 바꾸면서 구현해나간다.
수시로 검토하며 품질을 높인다.
지식을 공유하여 문제 해결 시간을 단축한다.

### 애자일 프로세스(스크럼)

개발 팀이 함께 일하는 데 도움이 되는 방법
개발 팀원 모두가 함께 소통하고 협력하여 짧은 주기를 반복하며
소프트웨어를 개발하는 작업, 역할, 결과물의 집합체
전체를 모르지만 할 일(백로그)을 정하고 여기에 우선순위를 부여
짧은 주기(스프린트)를 반복하여 출시 주기를 단축

### 애자일 프로세스

장점)
1. 다른 프로세스 모델보다 소프트웨어를 빠르게 배포할 수 있다.
2. 항상 최신 작업을 수행하기 때문에 자원의 낭비가 적다.
3. 문제의 결함을 더 빨리 감지하고 수정할 수 있다.
4. 문서화에 시간을 조금 쓴다.

단점)
1. 문서화가 잘 안되어서 새로 들어온 개발자가 속도를 높이기 어렵다.
2. 개발자와 고객이 지속적으로 상호작용 해야만 한다.
3. 명확한 끝이 흐지부지해지는 경우가 있다.

### 지원 프로세스
- 개발 중심이 아닌, 각 단계 별로 수행되어야 하는 다른 성격의 프로세스

- 계약 시각 - 획득 프로세스, 공급 프로세스
- 운영 시각 - 운영 프로세스
- 엔지니어링 시각 - 개발 프로세스, 유지보수 프로세스
- 관리 시각 - 관리 프로세스, 개선 프로세스
- 지원 시각 - 문서화 프로세스, 형상관리 프로세스, 품질보증 프로세스, 문제해결 프로세스

### 지원프로세스(관리 프로세스)
적절한 관리는 소프트웨어 개발을 잘 통합하게 한다.
비용과 품질 목표를 달성하기 위하여 프로젝트 관리하는 데 필요한 모든 작업
**계획** - 비용, 일정 예측/중간 점검에 대한 결정
**모니터링** - 개발하는 동안에 목적에 부합하는지 개발이 계획대로 진척되는지 확인
**제어, 분석** - 모니터링에 의해 확인된 사실을 분석하고 조정/조처

프로젝트 모니터링과 제어는 개발 프로세스의 모든 단계를 포함하므로 가장 긴 기간 동안 이루어짐

### 지원프로세스(품질보증 프로세스)
프로세스와 결과물에 대한 품질을 관리하고 향상시킨다.

### 인스팩션 프로세스
개발 결과에서 결함을 찾거나 방지하기 위한 노력
정의된 프로세스에 따라 동료 그룹이 작업 결과를 검사하는 것

### 프로세스 관리 프로세스
소프트웨어 개발 과정이 올바로 되어 있는지 확인하고 개선하는 작업

### 방법론
= 개발 방법
방법론을 정확히 정의하지 않으면 프로세스와 혼동한다.
소프트웨어 프로세스의 각 작업을 어떻게 수행하느냐를 정의
프로세스는 개발할 때 해야 하는 작업만을 어떤 방법으로 하는지는 나타내지 않는다.

### 구조적 방법론
분할과 정복 원리
복잡한 문제를 나누어서 다룬다.
자료 흐름도 사용
자료흐름도를 구조도로 변경하여 사용한다.

![data flow chart](https://i.imgur.com/KbTSpEj.png)

### 정보공학 방법론
- 기업 중심
- 전략적 시스템 계획 중심
- 데이터 중심
- 분할과 정복
- 공학적 접근
- 사용자의 적극적 참여

![Information Engineering Methodology](https://i.imgur.com/hErLXkC.png)

### 객체지향 방법론
- 자료와 함수를 가까운 곳에 정의하여 객체로 묶어두고
- 객체 사이에 메시지를 호출하여 원하는 기능을 담당하게 하는 것
- 대규모 시스템을 클래스로 모듈화하고 캡슐화할 수 있는 방법

### 방법론 비교

- 특징)
    - 구조적 방법론: 프로그램 로직 중심, 그림을 그려 요구사항을 분석하고 체계화
    - 정보공학 방법론: 기업정보 중심, 데이터 중심으로 CASE 도구를 사용하여 공학적인 접근
    - 객체지향 방법론: 비즈니스 유스케이스로 분석, 자료와 함수를 묶은 클래스를 파악
- 설계 관심사)
    - 구조적 방법론: 함수 위주
    - 정보공학 방법론: 자료 위주
    - 객체지향 방법론: 클래스 위주
- 설계 핵심)
    - 구조적 방법론: 모듈
    - 정보공학 방법론: 엔티티
    - 객체지향 방법론: 객체
- 중심방법)
    - 구조적 방법론: 프로그래밍 기법
    - 정보공학 방법론: 기업의 전략 및 산출물
    - 객체지향 방법론: 설계의 표현
- 장점)
    - 구조적 방법론: 프로젝트 계획과 모니터링이 비교적 쉬움. 요구분석에 대한 방법 이해가 쉬움
    - 정보공학 방법론: 데이터 중심으로 업무 절차 및 환경 변화에 유연함. 기업에 맞는 접근법
    - 객체지향 방법론: 실세계와 밀접한 모델링, 유지보수 쉬움, 코딩으로의 전환이 쉬움. 코드 재사용 가능
- 단점)
    - 구조적 방법론: 분석에서 설계 과정에 대한 전환이 쉽지 않음
    - 정보공학 방법론: 소규모 자동화 사업 영역에는 시간이 오래 걸림, 특정 사업 영역으로부터 독립된 시스템 개발에는 부적합
    - 객체지향 방법론: 충분히 훈련된 프로그래머 부족

