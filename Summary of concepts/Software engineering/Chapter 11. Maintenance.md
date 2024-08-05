# English

### Maintenance

Maintenance involves making changes to software after development. Software evolves according to changes in the environment and business requirements. The effort required for maintenance is significant.

**Legacy Systems**
Replacing them is costly.
They encapsulate valuable knowledge, experience, and intelligence.
- Bug fixes
- Adaptation to changes in the operating environment
- Compliance with new government policies and regulations
- Updates to business processes
- Changes to prevent future issues

**Types of Maintenance**

1. **Corrective Maintenance**
   - Fixing identified defects.
   
2. **Adaptive Maintenance**
   - Modifying software to continue using it in a new or changed environment.
   
3. **Perfective Maintenance**
   - Improving performance or maintainability.
   
4. **Preventive Maintenance**
   - Preventing potential defects.

## Lehman's Laws

Trends and patterns in software maintenance changes.

Types of systems:
- **E-type** - Systems that evolve continually.
- **S-type** - Systems that cannot be perfectly defined.

### Law of Continuing Change

- After release, systems must be continually modified until they are replaced.
- Software must always evolve as requirements change.

### Law of Increasing Entropy

- Software system structures deteriorate as changes accumulate.
- Reengineering or restructuring is needed to improve system architecture.

### Law of Self-Regulation

- System attributes are interpreted as probabilistic distributions.

### Law of Conservation of Organizational Stability

- The work rate of evolving systems tends to remain constant until system retirement.

### Law of Conservation of Familiarity

- The average growth rate of a system remains consistent until it is retired.

### Law of Continuing Growth

- Functional content must continually grow to satisfy user needs.

### Law of Declining Quality

- Unless adapted to changes in the operating environment, software quality deteriorates.

### Law of Feedback Systems

- The evolution process involves multiple stages of iteration and feedback from stakeholders.

## Types of Maintenance

**Corrective Maintenance**: Planned resolution of identified issues.

**Adaptive Maintenance**: Porting or modifying software to accommodate new data, operating systems, or hardware environments.

**Perfective Maintenance**: Modifications to improve performance or maintainability.

**Emergency Maintenance**: Unplanned maintenance to address urgent issues.

### Maintenance Process

1. **Understanding the Current Program**  
   Trace the program logic or understand the requirements and design.
   
   ↓
   
2. **Change Identification and Analysis**  
   Identify necessary changes, analyze the impact, costs, and risks.

   ↓
   
3. **Impact Assessment**  
   Notify stakeholders and gather feedback.
   
   ↓
   
4. **Implement, Test, and Install Changes**  
   Modify the system, verify the changes, and install the updates.

### Maintenance Process Models

**Immediate Fix Model**

A model for ad-hoc maintenance tasks.
When a problem is identified, it is fixed as quickly as possible.
Long-term effects and potential impacts are not thoroughly analyzed, and documentation updates are minimal.

**Iterative Enhancement Model**

Changes occur repeatedly across the full lifecycle stages, leading to continuous system improvement.

**Reuse-Oriented Model**

Maintenance activities focus on reusing program components.

### Program Understanding

To modify software, you must understand the program.
Extracting design or specifications from the source code and forming a mental model.
This process follows a path opposite to that of development, pursuing abstraction.

### Change Identification and Analysis

Identify what needs to be changed based on change requests.
Explore other possible change methods.

- Change analysis
- Impact analysis
- Estimate the costs and time required for implementing and testing changes
- Identify risks

### Configuration Management

The practice of managing documentation and tracking the state of software systems and components throughout the development lifecycle.

If documentation and deliverables are not well coordinated, inconsistencies arise.
When a class is modified, dependent classes must also be updated.
Traditional principles applied to hardware are also applicable to software development.

### Baselines

A set of software configuration items.

**Purpose**
- Define critical project states.
- Indicate when a product has reached a specific state.
- Serve as the basis for continued development and maintenance.
- Provide a mechanism for controlling changes to configuration items.

**Types**

**Plan Baseline**
- Requirements
- Domain models
- Project plan

**Requirement Baseline**
- Use cases
- Requirements analysis documents
- Draft user manuals

**Design Baseline**
- Class/sequence diagrams
- Integration test plans

**Implementation Baseline**
- Source code
- Unit test cases/results

**Integration Baseline**
- Integration test cases/reports

**Validation Baseline**
- Validation test cases/reports
- Installation manuals
- User manuals

### Need for Configuration Management

Configuration management may not be necessary if a small team of developers is working in a single location.

However, it becomes essential when multiple teams and developers need to collaborate and synchronize their work.

It is also crucial when maintaining multiple versions or products tailored to various customers.

### Configuration Management Procedures

![struct](https://i.imgur.com/IAeFSDG.png)

- Identify software configurations.
- Control configuration changes.
- Audit software configurations.
- Maintain configuration status.

### Configuration Identification

- Unique identifier - ID number.
- Name.
- Document type.
- Document file.
- Author.
- Creation date, target completion date.
- Version number.
- Update history.
- Description.
- SQA Manager - Quality Assurance Lead.
- SCM Manager - Configuration management responsibility.

### Configuration Change Control

Identify the reasons for changes.
- Software defects.
- Hardware changes.
- Changes in operational requirements.
- Requests for enhancements from customers or users.
- Budget, schedule, or duration changes.

- Perform change analysis.
- Prepare change proposals:
  Include descriptions, the organizations or developers involved, the reasons for the change, affected items, the effort required, and the impact on the project schedule.
- Evaluate change proposals.
- Implement changes.

### Configuration Audits

Define mechanisms for establishing baselines.
Manage the construction and approval of future baselines.

**Configuration Item Review**
- Ensure there are no discrepancies after updates.

**Configuration Item Verification**
- Verify that the correct issues have been addressed by checking accuracy.

### Reverse Engineering

**Definition of Reverse Engineering**
The process of analyzing a system to identify its components and their interrelationships, then creating representations of the system at the same or higher levels of abstraction.

Reverse engineering gradually recovers higher levels of abstraction from source code.

**Steps in Reverse Engineering**

Extracting software artifacts from the source code.
Components of reverse engineering tools.

![re](https://i.imgur.com/RfcoQeu.png)

**Uses of Reverse Engineering**

Restored diagrams can be used in several ways:

1. **Program Understanding**
   Helps understand the structure, function, and behavior of the software.
2. **Formal Analysis**
   Detects potential issues within the software.
3. **Test Case Generation**
   Flowchart paths help create path-based test cases.
4. **Reengineering**

**Redocumentation**

Creating representations at the same level of abstraction.

**Purpose**
- Enhance the understanding of the software by providing different perspectives.
- Improve existing documentation.
- Document newly modified programs.

**Design Recovery**

Analyzing source code in detail to discover meaningful higher-level abstractions.

Recovered designs

- Aid in understanding the source code.
- Can serve as a baseline for future maintenance or reengineering.
- May be used to develop similar applications.

**Reengineering**

The process of restructuring systems or components.

**Objectives**
- Improve software architecture.
- Reduce software complexity.
- Enhance adaptability to changes.
- Improve performance, efficiency, and resource utilization.
- Improve software system maintainability.

**Process**

- Identify areas needing improvement.
- Choose an improvement strategy.
- Implement the proposed improvements.
- Evaluate the system against the set objectives.





# Korean

### 유지보수

개발 후에 이루어지는 소프트웨어의 변경 작업
소프트웨어가 유용하게 활용되는 기간
소프트웨어는 환경과 비즈니스 요구에 따라 진화함
유지 보수에 드는 노력

**레거시 시스템**
대체하라면 비용이 많이 든다.
지식, 경험, 지능이 녹아 있다.
- 버그 제거
- 운영 환경의 변화
- 정부 정책, 규례의 변화
- 비즈니스 절차의 변화
- 미래 문제를 배제하기 위하여 변경

**유지보수의 유형**

1. 수정형 유지보수
    
    발견된 결함을 고치기 위하여 소프트웨어 제품을 수정
    
2. 적응형 유지보수 
    
    변경된 환경에서도 계속 사용할 수 있도록 소프트웨어를 이식하거나 변경
    
3. 완전형 유지보수 
    
    성능이나 유지보수성을 개선하기 위하여 실시하는 유형
    
4. 예방형 유지보수 
    
    오류 발생을 방지하기 위해 수행하는 유지보수 

## Lehman의 법칙

유지보수에서의 변경에 대한 추세와 패턴

시스템의 타입
E타입 - 계속 진화하는 타입
S타입 - 완벽히 정의할 수 없는 타입

### 지속적인 변경의 원칙

- 시스템이 릴리스 된 후 변경은 그 시스템이 대체될 때까지 변경된다.
- 시스템의 요구는 항상 변화하기 때문에 소프트웨어는 항상 진화되어야 한다.

### 엔트로피, 복잡도 증가의 법칙

- 소프트웨어 시스템 구조는 변경이 계속되면서 나빠진다.
- 시스템 구조를 개선하는 재구조화/리엔지니어링이 필요하다.

### 자기 통제의 법칙

- 시스템의 속성은 확률분포로 해석된다.

### 안정성 유지의 법칙

- 진화하는 시스템의 유지보수는 시스템이 소멸될 때까지 일정한 평균 작업량을 보인다.

### 친근성 유지의 법칙

- 시스템의 평균 성장률은 소멸될 때까지 일정하다.

### 지속적 성장의 법칙

- 사용자를 만족시키기 위하여 기능적 성장을 계속해야 한다.

### 품질 저하의 법칙

- 운영 환경의 변화에 완전히 적응하지 못하는 한 저하된다.

### 피드백 시스템의 법칙

- 진화 프로세스는 여러 단계의 여러 번 반복, 관련자들의 피드백으로 구성된다.

## 유지보수의 종류

**교정형 유지보수**: 발견된 오류의 원인을 찾아 계획적으로 문제해결

**적응형 유지보수**: 새로운 자료나 운영체제, 하드웨어 환경으로 이식

**완전형 유지보수**: 성능이나 유지보수성을 개선하기 위한 변경

**응급형 유지보수**: 응급처치하기 위한 무계획적 유지보수 

### 유지 보수 작업 과정

1. 현재 프로그램의 이해 
프로그램 로직을 추적하거나 요구, 설계 등에 대한 이해가 필요

      ↓

2. 변경 파악과 분석
필요한 변경을 파악하고 그 영향도와 소요 비용, 변경에 의한 리스크를 분석

      ↓

3. 변경 영향파악
이해당사자들에게 알리고 피드백을 얻음

      ↓

4. 변경 구현, 테스트, 설치
시스템을 수정하고 확인 후 설치 

### 유지 보수 프로세스 모델

**즉시 수정 모델**

임시 방편적인 유지 보수 작업 모델
문제가 확인되면 가능한 한 빨리 문제를 해결한다. 
장기적인 효과나 파급효과를 자세히 분석하지 않고 바로 수정하며 문서 수정은 최소화한다. 

**반복적 개선 모델**

소프트웨어에 대한 변경이 전체 생명주기 단계에 반복적으로 일어나 시스템이 계속 개선된다. 

**재사용 중심 모델**

유지 보수 작업 = 프로그램 컴포넌트의 재사용 

### 프로그램의 이해

소프트웨어를 변경하려면 프로그램을 이해해야 한다. 

원시코드로부터 설계나 명세를 추출하여 멘탈 모델로 표현하는 작업
개발 프로세스와 반대로 추상성을 추구하는 방향

### 변경 파악과 분석

변경 요구를 기초로 어떤 부분을 변경할 지 찾아냄
다른 변경 방법도 찾아냄 

- 변경분석
- 변경 효과 분석
- 변경을 구현하고 테스트하는 데 드는 비용, 시간의 예측
- 리스트 파악 

### 형상 관리

개발 주기 동안 생성된 문서를 관리하고 소프트웨어 시스템과 컴포넌트의 상태를 추적하는 작업

문서와 결과물에 대한 변경이 잘 조정되지 않는다면 불일치 발생
클래스 변경 후 의존 클래스를 업데이트 하여야 한다. 
하드웨어에 적용되었던 전통적 원리를 소프트웨어 개발에 적용 

### 베이스 라인

소프트웨어 형상 항목의 집합

**목적**
- 프로젝트의 중요한 상태 정의
- 프로덕트가 특정 상태에 이르렀는지를 나타냄
- 계속되는 개발, 유지보수 작업의 기준
- 형상 항목에 대한 변경을 제어하는 메커니즘

**종류**

계획 베이스 라인

- 요구
- 도메인 모델
- 계획서

요구 베이스 라인

- 사용사례
- 요구 분석 명세서
- 사용자 메뉴얼 초안

설계 베이스 라인

- 클래스/시퀸스 diagram
- 통합시험 계획

구현 베이스 라인

- 원시코드
- 단위 테스트 케이스/결과

통합 베이스 라인

- 통합 테스트 케이스/결과 보고

검증 베이스 라인

- 검증 테스트 케이스/결과 보고
- 설치 메뉴얼
- 사용자 메뉴얼

### 형상 관리의 필요성

소수의 개발자가 한 장소에서 일한다면 형상 관리는 불필요 

시스템을 개발하는 많은 팀과 개발자들이 협력하고 동기화 할 필요

여러 버전을 유지하여야 할 경우
다양한 고객을 만족시키기 위한 제품을 유지하기 위해 

### 형상 관리 절차

![struct](https://i.imgur.com/IAeFSDG.png)

소프트웨어 형상 파악
형상 변경 제어
소프트웨어 형상 감사
소프트웨어 형상 상태 보관 

### 형상 파악

- 고유 식별자 - 고유 번호
- 이름
- 문서 종류
- 문서 파일
- 저자
- 생성 날짜, 목표 완성일
- 버전 번호
- 업데이트 이력
- 설명
- SQA 담당자 - 품질 보증 책임자
- SCM 담당자 - 항목 체크한 책임자

### 형상 변경 제어

변경의 이유를 파악
소프트웨어의 결함
하드웨어 변경
운영 요구의 변경
고객이나 사용자로부터 개선 요구
예산, 프로젝트 일정, 기간의 변경 

- 변경 분석
- 변경 제안 준비
   변경의 설명, 조직 및 개발자 파악, 변경의 이유, 영향 받는 항목, 소요 노력, 프로젝트 일정에 대한 영향
- 변경 제안의 평가
- 변경을 추가 

### 형상 감사

베이스 라인을 구축하기 위한 메커니즘 정의
향후 구축될 베이스 라인과 승인된 베이스 라인

형상 항목 검토
- 업데이트 되어도 차이가 없음을 보장하여야 한다. 

형상 항목 확인
- 올바른 문제를 해결하였는지 확증하기 위하여 정확성을 체크 

### 역공학

역공학의 정의
대상 시스템을 분석하여 시스템의 컴포넌트와 관계를 찾아내어 같은 수준의 다른 표현이나
더 높은 수준의 표현으로 만드는 작업

프로그램의 추상 수준을 점증적으로 복구해 나가는 과정

**역공학 작업 순서** 

원시코드에서 소프트웨어 결과물들을 추출하는 것 
역공학 도구의 구성

![re](https://i.imgur.com/RfcoQeu.png)

**역공학의 용도**

복원된 다이어그램은 다음 여러 방면에 사용

1. 프로그램 이해
소프트웨어의 구조, 기능, 동작 이해 용이
2. 정형적 분석
소프트웨어에 존재할 수 있는 문제를 감지
3. 테스트 케이스 생성
흐름도의 경로 - 경로 테스트 케이스에 도움
4. 리엔지니어링 

**재문서화**

의미적으로 같은 추상 수준을 가진 표현을 생성하는 작업

목적
- 소프트웨어의 이해를 증진시키기 위하여 시스템의 다른 관점
- 현재 보유한 문서를 개선
- 새로 수정된 프로그램의 문서화

**설계 복구**

원시코드를 자세히 검토하여 의미 있는 추상성 높은 표현을 찾아내고 추출하는 작업 

복구된 설계

원시 코드 이해에 도움이 될 수 있다. 
향후 유지보수 또는 리엔지니어링을 위한 베이스라인으로 사용
유사한 다른 애플리케이션을 위하여 사용될 수도 있음

**리엔지니어링**

시스템 또는 컴포넌트를 재구조화하는 과정
목적
- 소프트웨어 아키텍처 개선
- 소프트웨어의 복잡도 경감
- 변경에 대한 적응성 개선
- 성능, 효율성, 자원 유용성 개선
- 스프트웨어 시스템의 유지보수 개선 

**과정**

- 개선이 필요한 위치파악
- 개선 전략을 선택
- 제안된 개선의 구현
- 목표를 기준으로 시스템 평가
