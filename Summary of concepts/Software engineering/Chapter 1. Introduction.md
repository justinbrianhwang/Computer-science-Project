# In English
### What is Software Engineering?

Computers [CPU, input/output devices, memory] are everywhere. Even in a simple restaurant, there are kiosks, and simple appliances like washing machines and air conditioners at home can be considered computers.

Software is the program that operates a computer and is composed of numerous commands that control the operation of the hardware.

Software engineering is about producing high-quality software within a given cost and resources within the specified time. In other words, it is about planning. The larger the scale of the software, the more the development plan influences the quality rather than the programming itself. Planning is crucial as multiple people are involved in the work.

In the actual work environment, there are two types of people: those who plan and those who code. The planners can code but focus on detailed planning on how to implement the software, while the coders focus solely on coding.

The following diagram makes it easier to understand.

![SoftwareEngineering](https://i.imgur.com/CBhDzv9.png)

### Characteristics of Software

1. Complexity: The automation target is complex, and numerous internal elements interact.
2. Conformity: It can be modified according to requirements or environment → The algorithm is similar, but the details differ.
3. Changeability: Programs are composed of text, making them modifiable and improvable.
4. Invisibility: The structure is hidden within the code and not apparent → It is hard to see how the code is constructed.

### Types of Software

1. Custom Software: Software designed to meet specific needs of a particular customer.
   → Commissioned by a specific customer
2. Packaged Software: Software that is commercially sold as a package
   → Typically purchased by users, e.g., OS
3. Embedded Software: Software for hardware devices sold in the market
   → Air conditioners, washing machines, etc.

### Systems

Software does not exist independently. It interacts with various systems based on computers.

The following diagram makes it easier to understand.

![Software Engineering2](https://i.imgur.com/ZnpyeFc.png)

### Basic Activities for Software Development

1. Specification: Agreement between the customer and the contractor on how the product will operate and its performance requirements
2. Implementation: Translating the specification (documented) into a programming language
3. Validation: Ensuring the software meets the customer's requirements
4. Maintenance: Fixing defects found during the usage phase

The following diagram makes it easier to understand.

![Software Engineering3](https://i.imgur.com/bHdSwSa.png)

### Characteristics of Development Work

Increasing the number of people does not proportionally increase productivity.

The quality of developed software depends on the abilities of the individuals involved.

1. Difficulty in Specification
2. Difficulty in Reusability
3. Difficulty in Prediction
4. Difficulty in Maintenance
5. Difficulty in High Quality

→ These are the characteristics.

Spontaneous software development involves repeated coding → modification. This method is suitable for learning but causes issues in the development process.

[Problems]

1. Delays and budget overruns
2. Low quality
3. Maintenance difficulties
4. Rework

The concept of approaching software development systematically was introduced at the NATO conference in Germany in 1968
→ Need for systematization

Software engineering systematically approaches and applies principles to develop software.

### Objectives of Software Engineering

1. Reduce complexity → Organic connection
2. Minimize cost → Calculating costs is also part of software engineering.
3. Shorten development time → Reducing the time is essential due to the existence of release schedules.
4. Manage large-scale projects → Managing personnel is also important.
5. High-quality software
6. Efficiency

⇒ The ultimate goal is to develop high-quality software within the planned schedule at the lowest cost.

Software engineering can be divided into three major tasks.

1. Step-by-step Process

   Focus on coding only, but follow established procedures such as requirement analysis, design, coding, and testing.

   1. Requirement Analysis → Requirement Analysis Specification
   2. Design → Design Specification
   3. Coding → New System/Maintenance Plan ⇒ Should not be changed arbitrarily.
      → Even if the code seems inefficient, the programmer may think so because they are only in charge of a part of the work. Still, the designer considers the entire code and instructs it accordingly. Therefore, the programmer should not change it arbitrarily.
   4. Testing → Testing Result Report
      → Identify any defects in the program.

2. Quality Assurance
   1. Review: Check if each phase is performed according to the presented procedures and methods.
   2. Verification: Inspect if the developed product is produced according to the quality level.
   3. Testing: Execute the implemented software to check
      (Maintainability/Reliability/Efficiency/Usability) ⇒ Testing is the process of verifying these properties.
3. Project Management

   Maintaining quality while satisfying time/cost/scope.

   1. Project Planning
   2. Resource Management
   3. Risk Management
   4. Project Execution and Monitoring

   The following diagram makes it easier to understand the relationship between the three elements of project management.

   ![Software Engineering4](https://i.imgur.com/H4K5UNv.png)



# In korean 
### 소프트웨어공학이란?

컴퓨터[CPU, 입출력장치, 메모리]가 없는 곳은 없다. 단순하게 음식점만 가도 키오스크가 있고, 집에 단순한 세탁기, 에어컨들도 컴퓨터라 할 수 있다.

소프트웨어란 컴퓨터를 작동시키는 프로그램이며, 하드웨어의 동작을 제어하는 수많은 명령어로 구성되어 있다.

소프트웨어공학이란 주어진 비용과 자원 안에서 품질 좋은 소프트웨어를 기간 내에 생산하기 위한 것이다. 즉, 계획하는 것이다. 소프트웨어의 규모가 클수록 프로그래밍 자체보다는 개발 계획이 품질에 더 큰 영향을 끼친다. 여러 명의 사람이 작업하기에 계획이 중요하다.

실제 작업 현장에 가보면 두 종류로 나뉜다. 계획하는 사람과 코딩하는 사람. 이 두 부류를 보면 계획하는 사람은 코딩 자체도 할 수 있지만, 어떻게 구현할지 세세하게 계획하고, 코딩하는 사람에게 해당 작업을 맡기면 코딩하는 사람은 코딩만 한다.

아래 그림을 보면 이해가 쉬울 것이다.

![SoftwareEngineering](https://i.imgur.com/CBhDzv9.png)

### 소프트웨어의 특징

1. 복잡성: 자동화하려는 대상이 복잡하고 수많은 내부 요소들이 상호작용한다.
2. 순응성: 요구나 환경에 따라 변형된다. → 알고리즘은 유사한데, 세세한 내용이 다른 경우
3. 변경성: 문자로 구성된 프로그램이기에 수정 및 보완이 가능하다.
4. 비가시성: 구조가 코드 안에 숨어 있어 드러나지 않는다. → 코드가 어떻게 짜였는지 알 수 없다.

### 소프트웨어 종류

1. 주문형 소프트웨어: 특정 고객의 특정 수요를 만족시키기 위한 소프트웨어
   → 특정 고객에게 의뢰를 받은 경우
2. 패키지형 소프트웨어: 패키지화하여 상업적으로 판매하는 소프트웨어
   → 주로 사용자가 구매하는 것. ex) OS
3. 임베디드형 소프트웨어: 시장에서 판매되는 하드웨어 장치를 위한 소프트웨어
   → 에어컨, 세탁기 등등

### 시스템

소프트웨어는 독립적으로 존재하지 않는다. 컴퓨터를 기반으로 하는 여러 시스템과 관계를 맺는다.

아래 그림을 보면 더 이해가 쉬울 것이다.

![Software Engineering2](https://i.imgur.com/ZnpyeFc.png)

### 소프트웨어 개발을 위한 기본 활동

1. 명세화: 고객과 계약자 간에 제품 작동 방식, 성능 요구 등을 합의
2. 구현: 프로그래밍 언어로 명세화(≒문서화)된 것을 변환하는 것
3. 검증: 소프트웨어가 고객의 요구와 일치하는지 확인
4. 유지보수: 사용 단계에서 확인되는 결함 수정

아래의 그림을 보면 이해가 쉬울 것이다.

![Software Engineering3](https://i.imgur.com/bHdSwSa.png)

### 개발 작업의 특징

인원이 늘어난 만큼 생산성이 늘어나는 것이 아니다.

개발한 소프트웨어의 질이 참여한 개인의 능력에 따라 좌우되는 것이다.

1. 명세화의 어려움
2. 재사용의 어려움
3. 예측의 어려움
4. 유지보수의 어려움
5. 고품질의 어려움

→ 이러한 특징들이 있다.

즉흥적인 소프트웨어 개발은 코딩→수정 작업의 반복이다. ⇒ 공부를 하는 과정에서는 이 방법이 맞지만, 개발하는 과정에서는 이 과정이 문제를 일으킨다.

[문제점]

1. 개발 지연과 예산 초과
2. 낮은 품질
3. 유지 보수 곤란
4. 재작업

소프트웨어 개발을 공학적으로 접근하려는 개념은 1968년 독일의 NATO 회의에서 도입됨
→ 체계화의 필요성

소프트웨어 공학이란, 소프트웨어를 개발하기 위하여 체계적으로 접근하고 원리를 적용하는 것이다.

### 소프트웨어 공학의 목표

1. 복잡도 낮춤 → 유기적 연결
2. 비용 최소화 → 비용을 계산하는 과정도 소프트웨어 공학의 일부이다.
3. 개발 기간 단축 → 출시 기간은 존재하므로 기간을 단축시키는 과정도 중요하다.
4. 대규모 프로젝트 관리 → 인원 관리도 중요
5. 고품질의 소프트웨어
6. 효율성

⇒ 품질 좋은 소프트웨어를 최소의 비용으로 계획된 일정에 맞추어 개발하는 것 → 궁극적인 목표이다.

소프트웨어 공학은 크게 세 가지 작업으로 나눌 수 있다.

1. 단계적 프로세스

   개발할 때 코딩에 치중하지 않고, 요구분석, 설계, 코딩, 테스팅 등 정해진 절차에 따라 작업하는 것.

   1. 요구분석 → 요구분석 명세서
   2. 설계 → 설계 명세서
   3. 코딩 → 새 시스템/유지보수 계획 ⇒ 임의로 바꾸면 안 된다.
      → 비효율적으로 보이는 코드여도, 프로그래머는 일부분만 맡은 일이기에 그렇게 생각할 수는 있겠지만, 설계자는 전체적인 코드를 생각해야 하므로 그렇게 하라고 한 것이다. 즉, 프로그래머가 임의로 바꾸면 안 된다.
   4. 테스팅 → 테스팅 결과 보고서
      → 해당 프로그래밍에 어떤 결함이 있는지 확인할 것.

2. 품질보증
   1. 검토: 각 단계의 작업이 제시된 절차와 방법에 맞게 진행되었는지 체크
   2. 확인: 개발 완료된 결과물이 품질 수준에 맞게 생산되었는지 검사
   3. 테스팅: 구현된 소프트웨어를 실행하여 확인하는 작업
      (유지보수성/신뢰성/효율성/유용성) ⇒ 이 성질을 확인하는 과정이 테스팅이다.
3. 프로젝트 관리

   시간/비용/범위를 만족시키며 품질을 지키는 것.

   1. 프로젝트 계획
   2. 자원관리
   3. 리스크 관리
   4. 프로젝트 수행과 모니터링이다.

   아래의 그림을 보면 프로젝트 관리의 3요소의 관계를 알 수 있다.

   ![Software Engineering4](https://i.imgur.com/H4K5UNv.png)
