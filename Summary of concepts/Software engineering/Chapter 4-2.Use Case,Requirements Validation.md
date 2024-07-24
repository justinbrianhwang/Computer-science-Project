# In English

### Types of Information Sources

Customer → Requestor (the one who requests the program to be made)

Domain Expert - A person needed to build a system that supports the business domain (e.g., an accountant for building an accounting system).

Stakeholder - A person affected by the operation of the system → Broad scope.

User - The person who directly uses the system.
Reverse Engineering - The system or current documents.

**Three Stages of Extraction**
- Identify information sources about the application.
- Collect information about the application.
- Define requirements and constraints.

**Information Collection Methods**
- Customer presentations → Should be done initially.
- Literature and form surveys → Refer to existing programs or laws/regulations.
- Interviews → Primarily with appropriate individuals!
- Surveys
- Brainstorming meetings
- Observation and task analysis
- Prototyping → Making prototypes.

⇒ There can be many more methods.

Analyzing and deciding on requirement candidates and finalizing them as requirements.

**Quality of Requirements**
- Atomicity: Single purpose.
- Completeness: Includes all information.
- Unambiguity and Consistency: Does not mention the same content differently.
- Traceability: Unique number for each requirement.
- Prioritization: Identify importance.
- Testability: Describe to be verifiable ⇒ Final version.

**What is a Domain?**

Background of requirements (Where is the problem located?)
Identify various concepts and business rules necessary for design modeling.
Well-define and analyze concepts in the application field to establish them as concepts in the system.

**Methods**
1) Finding Domain Concepts: Define terms ⇒ Even if it's an easy term we know, we must define it clearly. Different people can interpret it differently.
2) Writing a Domain Dictionary: Organize domain concepts.
3) Summarizing Business Rules: Rules to be followed in business.

Various people participate, conveying various terms and concepts to derive requirements.
It serves to overcome communication barriers.
Scenario-based (5W1H).

**User Story**
<WHO - User/Role>
<WHY - Goal/Benefit>
<WHAT - Action/Task>

### Use Case

A gateway between domain analysis and modeling.
Mapping the results of domain analysis into system specifications consisting of actors, use cases, and relationships.

**Use Case Elements**
Actors, System Scope, Use Cases, Relationships.

**Use Case Analysis Process**
1) Finding Actors.
2) Finding Use Cases.
3) Finding Relationships between Use Cases.

**Use Case Specification**
Describing the services the system should provide, arranged in the order of time elapsed.

### Use Case Diagram

Used to extract and analyze user requirements to show system functions.

**Components**
Use Case: System functions.
Actor: Interacts with the system (user, system).

Let's look at the example diagram below.

![diagram](https://i.imgur.com/a6WXgBi.png)

**Actor**
External entities that interact with the system.
Needs a distinct name and description.

Possible Actors:
- User roles.
- Other systems.

**Questions to Identify Actors**
- Which user groups receive system support to perform tasks?
- Which user groups use the system's main functions?
- Which user groups use ancillary functions like maintenance and management?
- Does the system operate with other external hardware or software systems?

**Finding Use Cases**

A collection of multiple individual scenarios:
- Normal flow.
- Error, exception cases.

Forming use cases from scenarios.

Written together by developers and users.
Using various documents describing the current application domain (guidelines, procedural manuals, etc.).

**Questions to Identify Use Cases**
- What tasks does the actor want the system to perform?
- What information does the actor want?
- Who generates the data? Can data be manipulated or deleted?
- Who performs these tasks?
- What does the actor need to notify the system of information?
- How often and when do these tasks occur?
- What events prompt the actor to retrieve information from the system?
- How frequent are these events?

### Finding Use Case Relationships

Using relationships to reduce model complexity and improve understanding.

**Types of Relationships**

1. Alternate Flow: Slight modifications, choices, or exceptions in the event flow of the basic use case.
    
    ![SELex](https://i.imgur.com/b6PkpTE.png)
    
2. Include Relationship: Encapsulate for reuse in other use cases.
Eliminates redundancy between use cases.
A relationship where one use case includes another.
Common actions can be separated.
![include](https://i.imgur.com/hVINBh9.png)
3. Extend Relationship: When the basic event flow of the primary use case is extended under certain conditions.
    
    If a use case includes extended actions under certain conditions, it is in an extending relationship with another use case.
    
    ![Ex](https://i.imgur.com/HNvBFD8.png)

**Requirement Verification**
1. Understandability
2. Redundancy
3. Consistency
4. Ambiguity
5. Verifiability
6. Traceability



# In Korean

### 정보 출처 유형

고객 → 주어(프로그램을 만들어 달라는 요구자)

도메인 전문가 - 비즈니스 도메인을 지원하는 시스템을 구축하기 위하여 필요한 사람(예, 회계 시스템을 구축하기 위하여 회계사가 필요)

이해 당사자 - 시스템 운용으로 인하여 영향을 받는 사람 → 범위가 넓음

사용자 - 시스템을 직접 사용하는 사람
역공학 - 시스템이나 현재 문서 

**추출의 세 가지 단계**
- 응용에 대한 정보 출처 파악
- 응용에 대한 정보 취합
- 요구와 제한 사항의 정의

**정보 수집 방법**
- 고객의 발표 → 초기에 할 것
- 문헌, 양식 조사 → 참고할만한 프로그램/기존에 만든 프로그램+법규를 따지기
- 인터뷰 → 주로 적합한 사람들로!
- 설문조사
- 브레인스토밍 회의
- 관찰과 작업 분석
- 프로토 타이핑 → 시제품 만들기 

⇒ 이 외에도 정말 많은 방법이 있을 수 있다. 

요구 후보를 분석하고 결정하여 요구로 확정하는 것. 

**요구 품질**
- 원자적: 단일 목적
- 완전성: 정보의 모든 것을 포함
- 비모호성과 통일성: 같은 내용을 다르게 언급하지 않음
- 추적성: 요구사항에 대한 고유 번호
- 우선순위화: 중요도 파악
- 테스트 가능성: 검증 가능하도록 기술 ⇒ 최종본 

**도메인이란?**

요구의 배경(문제가 어디에 놓여있는가?)
설계 모델링에 필요한 여러 개념과 비즈니스 룰을 파악
응용 분야에 존재하는 개념을 잘 정의하고 분석하여 시스템에 존재하는 개념으로 정립하는 단계

**방법**
1) 도메인 개념 찾기: 용어 정의 ⇒ 우리가 아는 쉬운 용어라고 하더라도, 용어를 명확히 정의해야 한다. 사람마다 다른 의미로 받아들일 수 있기 때문이다. 
2) 도메인 사전 작성: 도메인 개념 조직화
3) 비즈니스 규칙 정리: 업무에서 지키기로 한 규정

다양한 사람들이 참여하여 다양한 용어와 개념을 전달하여 요구를 도출
커뮤니케이션의 장벽을 해소하는 역할이다. 
시나리오 기반(5H1W)

**사용자 스토리**
<사용자/역할(WHO)>는
<목표/혜택/이익(WHY)>를 얻기 위해
<행위/작업(WHAT)>을 원한다. 

### 유스 케이스

도메인 분석과 도델링 사이의 관문
도메인 분석의 결과를 액터, 사용사례, 관계들로 구성된 시스템 명세로 매핑하는 작업 

**유스케이스 요소**
액터, 시스템 범위, 유스케이스, 관계

**유스케이스 분석 과정**
1) 액터 찾기
2) 유스케이스 찾기
3) 유스케이스 사이의 관계 찾기

**유스케이스 명세**
시스템이 제공하여야 할 서비스를 시간이 경과되는 순서로 정렬하여 기술한 것 

### 유스케이스 다이어그램

시스템의 기능을 나타내기 위하여 사용자의 요구를 추출하고 분석하는데 사용 

**구성**
사용 사례: 시스템 기능
액터: 시스템과 상호작용 하는 것(사용자, 시스템) 

아래의 예시 다이어 그램을 보자. 

![diagram](https://i.imgur.com/a6WXgBi.png)

**액터**
시스템과 상호작용 하는 외부 엔티티
구별되는 이름과 설명이 필요

액터가 될 수 있는 것
- 사용자가 맡은 일
- 다른 시스템

**액터를 찾기 위한 질문**
- 어떤 사용자 그룹이 작업을 수행하기 위하여 시스템의 지원을 받는가?
- 어떤 사용자 그룹이 시스템의 주요기능을 사용하는가?
- 어떤 사용자 그룹이 유지 보수와 관리 등의 부수적 기능을 사용하는가?
- 시스템이 다른 외부 하드웨어나 소프트웨어 시스템과 동작하는가? 

**유스케이스 찾기**

여러 개별 시나리오를 묶은 것
- 정상적인 흐름
- 오류, 예외 케이스

시나리오로부터 유스케이스 형성 

개발자와 사용자가 함께 작성
현재의 응용  도메인에 대하여 기술한 여러 문서를 이용(지침서, 절차 메뉴얼 등)

**필요한 질문**
- 시스템이 어떤 작업을 수행하기를 액터가 원하는가?
- 액터가 원하는 정보는 무엇인가?
- 누가 데이터를 생성하는가? 데이터는 조작, 삭제될 수 있는가?
- 이런 작업이 누구에 의하여 행해지는가?
- 액터가 시스템에 정보를 알리는데 필요한 것은?
- 얼마나 자주 또 언제 이런 작업이 일어나는가?
- 액터가 시스템으로부터 정보를 알아내는데 필요한 이벤트는?
- 이런 사건의 빈도는?

### 유스케이스 관계 찾기

관계를 이용하여 모형의 복잡도를 줄이고 이해도를 높인가. 

**관계종류**

1. 대안 흐름: 기본 유스케이스에서 이벤트의 흐름이 약간 변형되거나 선택, 예외인 경우
    
    ![SELex](https://i.imgur.com/b6PkpTE.png)
    
2. 포함 관계: 다른 유스케이스에서 재사용 할 수 있도록 캡슐화하려는 경우
유스케이스 사이의 중복을 제거함
어떤 유스케이스가 다른 유스케이스를 포함하는 관계
공통된 동작을 떼어낼 수 있다. 
![include](https://i.imgur.com/hVINBh9.png)
3. 확장 관계: 기본 유스케이스의 기본 이벤트 흐름이 특정 조건에 만족되었을 때 분리 확장된 것. 
    
    유스케이스가 일정한 조건 아래 확장된 동작을 포함한다면 다른 유스케이스를 확장하는 관계에 있다. 
    
    ![Ex](https://i.imgur.com/HNvBFD8.png)
    

**요구 검증**
1. 이해 용이성
2. 중복
3. 일관성
4. 모호성
5. 검증 가능성
6. 추적 가능성

