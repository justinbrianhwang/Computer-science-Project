# In English

### Project Management Goals

Effectively utilize various resources , manpower , costs , materials , and technologies needed for task execution to achieve project goals.

### Challenges of Project Management

- Development targets are invisible. ⇒ This is a feature of software. (Progress relies on documents written by developers / indirect measurement methods)
- Technological advancement in the software field is very rapid (problems that arise depending on the project are hard to predict)
⇒ It is difficult to bring existing experience to new fields.
- The software field has different processes for each organization (difficult to rely on standardized procedures and methods)
⇒ Software creates intangible assets and the characteristics pursued by each organization are different.

### Starting a Project

**Factors Determining Project Initiation**
- Value Provided by the Project: Direct and indirect value created by the project , sustainability of the project deliverables
- Risks Associated with the Project: Availability of resources , timing , technical difficulties , etc.

**Methods to Evaluate Value**
1) Payback Period: The time it takes to recover the amount of the investment.
2) ROI (Return on Investment): Annual average return on total cost.
3) Net Present Value: Comparing current investment and future income in present value.
4) Scorecard: Scoring non-monetary elements (technology , quality , time flexibility , personnel).
5) SWOT: Understanding strengths , weaknesses , opportunities , and threats of the project to understand feasibility ⇒ Often used in general decision making.

**Project Risks**
- Resources , current usage and availability , expected usage and availability
- Priority and importance of the project
- Time
- Technical difficulties

**Project Planning and Scheduling**
The success or failure of a project depends on the thoroughness of the planning.

Initial Planning

- Setting Goals: What are the characteristics of the project / Who provides the resources / Who uses them
- Defining Schedule: Progress schedule/ allocated resources?
- Cost Estimation: Estimating the required costs

![schedule](https://i.imgur.com/H38Jf6e.png)

**Project Scope**
The scope should be written from the user's perspective.

![Scope](https://i.imgur.com/HEJpKa4.png)

**WBS (Work Breakdown Structure)**

Understand the project's goals from a scheduling perspective.
Hierarchically divide the tasks that the development team must perform to achieve the project goals and produce deliverables.
The purpose of writing WBS is to identify all tasks that occur during the project.

![WBS](https://i.imgur.com/KDoDQm9.png)

### Scheduling

Scheduling is defined based on WBS.
1) Identify dependencies between tasks
- List what tasks exist → Analyze preceding tasks and identify dependencies!
2) Calculate float time using CPM method
- Start with tasks that do not require preceding tasks ⇒ The key is to draw the graph data structure and find the shortest time.
3) Allocate required resources

### Cost Estimation Techniques

Relationship between effort , resources , and duration

$D = E/M$

Important variables in cost estimation are the number of engineers input and the duration of the work.

- Cost Estimation Techniques (COCOMO-81)
    - Use mathematical formulas based on size
    - Consider factors affecting the type of software being developed , the team , project process , and product.
    - Effort = $A \times (\text{Size})^B \times M$
    - $A$ is a constant depending on the characteristics of the development institution and the type of software being developed.
    - Disadvantages)
        - It is difficult to predict the Size value in the early stages of the project.
        - The factors affecting the values of $B$ and $M$ in the basic estimation model are subjective.
- Cost Estimation Techniques (COCOMO 2)
    - Proposes three different models depending on the progress of the software development project.
        1. Prototype creation stage
        Calculate application scores by counting the number of third-generation language components , screens , and outputs (user interfaces).
        2. Early setting stage
        Explore detailed structure and functions.
        3. Post-architecture stage
        Detailed understanding of the system.
    - Estimation Process
        - Count the number of screens , reports , and third-generation language components that make up the application.
        - Determine the complexity level of screens and reports.
        - Find complexity weights for screens , reports , and third-generation language components.
        - Multiply the number of screens , reports , and third-generation language components by the weights to calculate Object Points.
        - Predict the reuse rate and apply it to the formula to calculate NOP (New Object Point).
        - Determine object point productivity.
        - Apply object point productivity to the formula PM = NOP/PROD to calculate the final PM (Person Month) value.
- Expert Judgment
- PERT (Program Evaluation and Review Technique)
- Algorithmic Methods

### Project Team Organization

Organizational Structure → How to organize??
Greatly affects software development productivity.
Communication between team members and characteristics of tasks.

**Definition of Project Team Organization**

Where are roles and responsibilities?
Through what channels is information transmitted and decided?
How to resolve conflicts?

### Project Team Organization

Assigning Team Roles

Project Manager (project manager),
System Administrator (system administrator)
System Analyst (system analyst),
Software Engineer (software engineer),
Database Engineer (database engineer),
QA Manager (QA manager),
Technical Support (technical support),
Hardware Engineer (hardware engineer),
Web Developer and Designer

1. Organization by Function
Different departments enter and perform different stages of a project.
Team members belong to one department , project cooperation is by department.

![Organization by function](https://i.imgur.com/179Uaqm.png)

2. Organization by Project
Functional developers are assigned to projects.
Communication paths are short , making project management such as personnel and progress easy.

![project meeting](https://i.imgur.com/1ecmwVZ.png)

3. Matrix Organization (Functional + Project)
A manager of a functional organization is responsible for the project.
Developers belonging to functional organization departments participate in the project.

### Execution and Monitoring

Monitor and reflect the current situation while the project is being executed.

**Execution**
- Job start meeting
- Collecting work results
**Monitoring**
- Identifying from perspectives such as scope , schedule , cost , quality
**Risk Management**
- Purpose of reducing the impact when a risk occurs
Risk Factors

![Riskfactor](https://i.imgur.com/mZP97gW.png)

**Identifying Risks**
- Meetings
- Document Analysis
- Risk Breakdown Structure , Checklists
- Analogy

**Managing Risks**
Devise ways to mitigate risk factors and apply them while executing the project.

Methods)
1. Change the plan to avoid risks
2. Delegate responsibility to another agency
3. Prototyping
4. Employ competent personnel
5. Collaborate with third parties

### Project Plan
1. Overview
  1.1 Project Overview
  1.2 Project Deliverables
  1.3 Definitions , Acronyms
2. Resource and Schedule Estimation
  2.1 Resources
    a. Personnel
    b. Costs
  2.2 Schedule
3. Organizational Structure and Staffing
  3.1 Organizational Structure
  3.2 Job Descriptions
4. WBS
5. Technical Management Methods
  5.1 Change Management
  5.2 Risk Management
  5.3 Cost and Progress Management
  5.4 Problem Resolution
6. Standards and Development Procedures
  6.1 Development Methodology
7. Review Meetings
  7.1 Review Meeting Schedule
  7.2 Review Meeting Process
  7.3 Follow-up Actions after Review Meetings
8. Development Environment
9. Performance Testing Methods
10. Documentation
11. Maintenance
12. Installation and Acceptance
13. References and Appendices


# In korean

### 프로젝트 관리의 목적

작업 수행에 필요한 여러 가지 자원 , 인력 , 비용 , 재료 , 기술 등을 가장 효과적으로 사용하여 프로젝트의 목표를 달성하는 것.

### 프로젝트 관리의 어려움

- 개발 대상이 눈에 보이지 않는다. ⇒ 소프트웨어의 특징이다. (진척 상황을 개발자들이 작성한 문서 / 간접적인 측정방법에 의존)
- 소프트웨어 분야의 기술 발전은 매우 빠르다(프로젝트에 따라 발생하는 문제예측이 어렵다)
⇒ 기존 경험을 새로운 분야에 가져오기 힘들다.
- 소프트웨어 분야는 조직마다 프로세스가 다르다(표준화된 절차와 방법에 기대기 어렵다)
⇒ 소프트웨어는 무형물을 만들고 조직마다 추구하는 성격이 다르기 때문이다.

### 프로젝트 시작

**프로젝트 시작을 결정하는 요인**
- 프로젝트가 제공할 가치: 프로젝트에 의해 창출되는 직간접적인 가치 , 프로젝트 결과물의 지속 가능성
- 프로젝트와 관련된 리스크: 자원의 가용성 , 타이밍 , 기술적 어려움 등

**가치를 평가하는 방법**
1) 투자 회수 기간: 투자금과 같은 금액을 벌어들이는 데 걸리는 시간
2) ROI(Return of Investment): 총 비용에 대한 연간 평균 이익률
3) 순수 현재 가치: 현재 투자금과 미래 수익금을 현재 가치로 비교
4) 평가표: 금액적인 요소 이외(기술 , 품질 , 시간 여유 , 인력)를 점수화
5) SWOT: 프로젝트의 강점/약점/기회요인/위험요인을 파악하여 타당성을 이해 ⇒ 일반 의사결정에도 많이 사용하는 방법

**프로젝트 리스크**
- 자원 , 현재 사용량과 가용성 , 예상 사용량과 가용성
- 프로젝트의 우선 순위 및 중요도
- 시간
- 기술적 어려움

**프로젝트 계획과 스케쥴링**
프로젝트의 성패는 계획의 치밀함에 달려있다.

초기계획

- 목표설정: 프로젝트의 특성은 무엇인가 / 누가 자원을 제공하는가 / 누가 사용하는가
- 일정 정의: 진행 스케줄/ 할당할 자원은?
- 비용 추정: 필요한 비용 추정

![schedule](https://i.imgur.com/H38Jf6e.png)

**프로젝트 범위**
사용자의 입장에서 범위를 작성해야 한다.

![Scope](https://i.imgur.com/HEJpKa4.png)

**WBS(Work Breakdown Structure)**

프로젝트의 목표를 스케쥴 관점으로 이해
개발 팀이 프로젝트 목표를 달성하고 결과물을 산출하기 위하여 수행해여야 할 작업을 계층적으로 분할
WBS 작성 목적은 프로젝트 진행에서 일어나는 모든 작업을 찾아내기 위한 것

![WBS](https://i.imgur.com/KDoDQm9.png)

### 스케쥴링

WBS를 기초로 하여 일정을 정의하는 것이다.
1) 작업 사이의 의존 관계 파악
- 어떤 작업이 있는 지 나열 → 선행 작업 분석 후 의존 관계 파악!
2) CPM 방법을 이용한 여유 시간 계산
- 선행작업이 필요 없는 작업부터 ⇒ 그래프 자료구조를 그리며 최단 시간을 찾아내는 것이 관건이다.
3) 소요 자원의 할당

### 비용 예측 기법

노력과 자원과 기간의 관계

$D = E/M$

비용 예측의 중요한 변수는 투입되는 엔지니어의 인원수와 작업기간

- 비용 예측 기법(COCOMO-81)
    - 규모를 기반으로 하는 수학적 공식 사용
    - 개발 소프트웨어의 유형이나 팀 , 프로젝트 프로세스 , 등 프로덕트에 영향을 주는 요인을 고려
    - 노력 = $A \times (\text{Size})B \times M$
    - $A$는 개발 기관의 특징과 개발 소프트웨어의 유형에 좌우되는 상수
    - 단점)
        - 프로젝트의 초기 단계에서 Size 값을 예측하는 것이 어려움
        - 기본 예측 모델에서 $B$와 $M$의 값에 영향을 주는 요소들이 주관적이다.
- 비용 예측 기법(COCOMO 2)
    - 소프트웨어 개발 프로젝트가 진행된 정도에 따라 세가지 다른 모델을 제시
        1. 프로토타입 만드는 단계
        화면이나 출력 등 사용자 인터페이스. 3세대 언어 컴포넌트 개수를 세어 응용 점수를 계산
        2. 초기 설정 단계
        자세한 구조와 기능을 탐구
        3. 구조 설계 이후 단계
        시스템에 대한 자세한 이해
    - 추정 과정
        - 애플리케이션을 구성하는 화면 , 보고서 , 3 세대 언어 컴포넌트의 숫자를 카운트
        - 화면과 보고서의 복잡도 수준을 결정
        - 화면과 보고서 , 3 세대 언어 컴포넌트를 위한 복잡도 가중치를 찾음
        - 화면 , 보고서 , 3 세대 언어 컴포넌트의 개수에 가중치를 곱하여 객체 점수 (Object 점수)를 계산
        - 재사용률을 예측하여 공식에 대입하여 NOP(New Object Point)를 구함
        - 객체 점수 생산성을 결정
        - 객체 점수 생산성을 식 PM = NOP/PROD 에 대입하여 최종 PM(Person Month) 값을 구함
- 전문가 판단
- PRET(Program Evaluation and Review Technique)
- 알고리즘식 방법

### 프로젝트 팀 조직
조직의 구성 → 어떻게 조직??
소프트웨어 개발 생산성에 큰 영향
작업의 특성과 팀 구성원 사이의 의사교류

**프로젝트팀 조직의 정의**

역할과 책임이 어디에 있는가?
어떤 통로로 정보가 전달되고 결정되는가?
어떻게 갈등을 해소할 것인가?

### 프로젝트 팀 조직

팀역할 나누기

프로젝트 관리자 (project manager),
시스템 운영자 (system administrator)
시스템 분석가 (system analyst),
시스템 개발자 (software engineer),
데이터베이스 엔지니어 (database engineer),
QA 관리자 (QA manager),
기술 지원 (technical support),
하드웨어 엔지니어 (hardware engineer),
웹 개발자 및 디자이너

1. 직능별 조직
서로 다른 부서가 한 프로젝트의 다른 단계에 들어와 작업을 수행
팀원은 한 부서에 소속 , 프로젝트의 협력은 부서별로

![Organization by function](https://i.imgur.com/179Uaqm.png)

2. 프로젝트별 조직
직능별 개발자들이 프로젝트에 배정
의사 전달 경로가 짧으며 인력 , 진도 등 프로젝트 관리가 수월

![project meeting](https://i.imgur.com/1ecmwVZ.png)

3. 매트릭스 조직(직능별+프로젝트별)
직능별 조직의 관리자가 프로젝트 책임을 맡고
직능별 조직 부서에 소속된 개발자가 프로젝트에 참여

### 실행과 모니터링

프로젝트가 실행되는 동안 모니터링하고 현재 상황을 반영

**실행**
- 직업 시작 미팅
- 작업 결과 수집
**모니터링**
- 범위 , 일정 , 비용 , 품질 등의 관점으로 파악
**리스크 관리**
- 위험이 발생되었을 때의 영향을 줄이기 위한 목적
리스크 요소

![Riskfactor](https://i.imgur.com/mZP97gW.png)

**리스크 찾기**
- 회의
- 문서 분석
- 리스크 분할 구조 , 체크리스트
- 유추

**리스크 관리**
위험 요소를 해소하기 위한 방법을 강구하고 프로젝트 실행하는 동안 이를 적용

방법)
1. 리스크를 피하기 위하여 계획을 변경
2. 책임을 다른 기관에 맡김
3. 프로토 타이핑
4. 유능한 인재를 등용
5. 3자와 협업

### 프로젝트 계획서
1. 개 요
  1.1 프로젝트 개요
  1.2 프로젝트의 산출물
  1.3 정의 , 약어
2. 자원 및 일정 예측
  2.1 자원
    가. 인력
    나. 비용
  2.2 일정
3. 조직 구성 및 인력 배치
  3.1 조직 구성
  3.2 직무 기술
4. WBS
5. 기술관리 방법
  5.1 변경 관리
  5.2 위험 관리
  5.3 비용 및 진도 관리
  5.4 문제점 해결 방안
6. 표준 및 개발 절차
  6.1 개발 방법론
7. 검토 회의
  7.1 검토회 일정
  7.2 검토회 진행 방법
  7.3 검토회 후속 조치
8. 개발 환경
9. 성능 시험 방법
10. 문서화
11. 유지보수
12. 설치 , 인수
13. 참고문헌 및 부록

