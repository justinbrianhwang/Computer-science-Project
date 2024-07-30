# English

### Design Principles

Requirements analysis deals with 'what to create,' while design specifies 'how to implement it.' The focus of the design phase is on creating a solution to fulfill the requirements.

1) Basic Structure Design - Architecture design defines the roles and interfaces of each module.
2) Detailed Design - Specifies the algorithms and data within the modules.

**Design** deals with the concrete subject of programs but is a conceptual activity.

Design involves a series of high-level decision-making processes, making design principles crucial. Traditional design methods apply principles such as divide and conquer, abstraction, and synthesis. Recently, architecture-based design methods have become more prevalent.

Understanding architecture involves grasping the concepts of subsystems and modules and understanding the perspective and process of design work.

**Architecture** is a set of components and their interactions that make up a system. It is an independently treatable unit.

**Subsystems** are collections of classes (packages) divided to reduce the complexity of the system. Dividing complex systems into subsystems reduces the burden on developers.

Design specifies the services provided by each subsystem and the constraints under which they operate.

### Design Perspectives

Software is represented in the design phase as a structure of subsystems.

- Module Perspective: Modules as units of code implementing certain responsibilities and their relationships
- Component Perspective: Elements that operate and interact when executed
- Allocation Perspective: Perspectives on software installation on hardware, task allocation, implementation, and data storage

### Design Process

The design process is a decision-making process and a process of understanding the system. The type of system to be developed is crucial as it greatly influences the choice of architecture style. Design objectives significantly impact the design results.

![architecture](https://i.imgur.com/rOB7IXO.png)

### Quality Goals

Quality constraints can become design goals. Non-functional requirements are specified as design goals, leading to the creation of design plans, from which the optimal plan is selected.

![goal](https://i.imgur.com/s8yPKy8.png)

### Traditional Design Principles

- Efficiency: Processing time and memory space
- Simplicity: The most important characteristic affecting maintainability
- Abstraction: Focus on information relevant to a particular purpose, ignoring the rest
- Encapsulation: Makes the services provided by the abstracted entity easily accessible
- Modularity: Divides problems into components that can become software elements

Abstraction focuses on the key characteristics of the system to divide a large system, while encapsulation exposes only the core information of the divided parts.

![system](https://i.imgur.com/5B4QVHE.png)

### Coupling

Indicates the degree to which modules depend on each other.

1. Content Coupling: One module directly references the content of another
2. Common Coupling: One module writes or changes the value of a global variable read by another module
3. Control Coupling: One module determines the control flow path of another module
4. Stamp Coupling: A composite data structure is passed to a module, but the module only uses part of it
5. Data Coupling: Modules exchange simple data types or fields within a record

### Cohesion

Indicates the degree to which tasks performed within a module are related. High cohesion makes modules easier to reuse, understand, and less affected by modifications.

1. Accidental Cohesion: Elements within a unit are unrelated semantically
2. Logical Cohesion: Elements perform similar functions and are logically categorized
3. Temporal Cohesion: Elements are grouped because they are processed at the same time in the program's execution
4. Procedural Cohesion: Operations within a module are related to the program's execution order
5. Communicational Cohesion: Internal elements of a module manipulate the same data
6. Functional Cohesion: Elements contribute to a single function and are closely related



# korean

### 설계 원리

요구 분석은 ‘무엇을 만들 것인가’를 다루는 작업이며, 설계는 ‘어떻게 실현할 것인가’를 구체적으로 결정하는 활동입니다. 설계 단계의 중심은 요구를 실현하는 솔루션입니다.

1) 기본 구조 설계 - 아키텍처(큰 덩어리) 설계로 각 모듈의 역할과 인터페이스를 정의합니다.
2) 상세 설계 - 모듈 내부의 알고리즘과 데이터를 명세화합니다.

**설계**는 프로그램이라는 구체적인 대상을 다루지만, 개념적인 작업입니다.

설계는 높은 수준의 의사 결정 과정의 연속이며, 설계 원리가 중요합니다. 전통적 설계 방법: 분할정복, 추상화, 합성 등의 원리를 적용합니다. 최근에는 아키텍처 기반의 설계 방법이 많이 사용됩니다.

아키텍처 이해는 서브시스템, 모듈의 개념과 설계 작업의 관점, 설계 작업 과정을 숙지해야 합니다.

**아키텍처**는 시스템을 구성하는 컴포넌트와 컴포넌트 상호작용의 집합입니다. 독립적으로 취급될 수 있는 단위입니다.

**서브시스템**은 클래스를 모아놓은 패키지로, 시스템의 복잡도를 줄이기 위하여 분할된 것입니다. 복잡한 시스템을 서브시스템으로 분할하면 개발자의 부담이 줄어듭니다.

설계는 각 서브시스템이 제공하는 서비스의 명세와 작동되는 제약 조건을 제공합니다.

### 설계 관점

소프트웨어는 설계 단계에서 서브시스템의 구조로 표현됩니다.

- 모듈 관점: 일정한 책임을 구현한 코드 단위인 모듈과 그 관계
- 컴포넌트 관점: 실행될 때 동작하는 요소와 상호작용
- 할당 관점: 소프트웨어의 하드웨어 설치, 작업 할당, 구현, 데이터 저장에 대한 관점

### 설계 작업 과정

의사 결정 과정이면서 동시에 시스템을 알아가는 과정입니다. 개발될 시스템의 유형이 중요하며, 설계 목적은 설계 결과에 많은 영향을 줍니다.

![architecture](https://i.imgur.com/rOB7IXO.png)

### 품질 목표

품질 제약사항은 설계에 대한 목표가 될 수 있습니다. 비기능적인 요구를 설계 목표로 구체적으로 명시합니다. 이를 만족시키기 위하여 설계안을 만들고 그 중에 최적안을 골라내는 작업입니다.

![goal](https://i.imgur.com/s8yPKy8.png)

### 전통적인 설계 원리

- 효율성: 처리 시간과 기억 공간
- 단순성: 유지보수성에 영향을 주는 가장 중요한 특성
- 추상화: 대상에 대하여 특정한 목적에 관련된 정보에 집중하고 나머지 정보는 무시하는 관점
- 캡슐화: 추상화된 대상이 제공하는 서비스를 쉽게 접근하게 하는 개념
- 모듈화: 문제를 소프트웨어의 구성요소가 될 만한 수준으로 분할하는 과정

추상화는 시스템의 핵심 특성에 초점을 두어 하나의 큰 시스템을 분할하는 원리이며, 캡슐화는 분할된 핵심 정보만을 노출합니다. 

![system](https://i.imgur.com/5B4QVHE.png)

### 결합

모듈 간에 서로 의존하는 정도를 나타냅니다.

1. 내용 결합: 한 모듈이 다른 모듈의 내용을 직접 참조
2. 공통 결합: 한 모듈이 다른 모듈이 읽은 전역 변수 값을 쓰거나 변경
3. 제어 결합: 한 모듈이 다른 모듈의 제어 흐름 경로를 결정
4. 스탬프 결합: 복합 데이터 구조의 일부만 사용하는 모듈에 복합 데이터 구조 전달
5. 데이터 결합: 모듈들이 주고받는 매개변수가 간단한 타입이거나 레코드 안의 필드인 경우

### 응집

하나의 모듈 안에서 수행되는 작업들이 서로 관련된 정도를 나타냅니다. 높은 응집은 재사용하기 쉽고, 이해하기 좋으며, 수정에 의한 영향을 적게 받습니다.

1. 우연적 응집: 단위 안의 요소들이 의미적으로 아무 관계가 없음
2. 논리적 응집: 본질적으로 다르더라도 같은 범주의 기능을 수행
3. 시간적 응집: 프로그램 실행의 특정한 시간에 처리
4. 절차적 응집: 모듈 안에서 수행되는 연산이 프로그램에서 수행되는 순서와 관련
5. 교환적 응집: 모듈의 내부 요소들이 동일한 데이터를 조작하기 때문에 그룹화
6. 기능적 응집: 하나의 기능에 모두 기여하고 밀접하게 관련
