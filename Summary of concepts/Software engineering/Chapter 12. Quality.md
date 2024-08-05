# English

### Maintenance

Software maintenance involves modifications after development to ensure software remains useful and meets evolving business and environmental needs.

**Legacy Systems**
Replacing legacy systems can be costly.
These systems contain valuable knowledge, experience, and intelligence.
- Bug fixes
- Changes in the operating environment
- Changes in government policies and regulations
- Changes in business procedures
- Changes to prevent future problems

**Types of Maintenance**

1. **Corrective Maintenance**
    - Fixing discovered defects in software products

2. **Adaptive Maintenance**
    - Adapting software to work in changed environments

3. **Perfective Maintenance**
    - Improving performance or maintainability of software

4. **Preventive Maintenance**
    - Preventing potential issues in the future

## Lehman's Laws

Trends and patterns in maintenance changes

System Types:
E-type - Systems that evolve continuously
S-type - Systems that can be fully defined

### Law of Continuing Change

- Systems must continually adapt to changing environments to remain useful.
- Software requirements are always changing, so software must continually evolve.

### Law of Increasing Complexity

- Software systems become more complex over time unless efforts are made to reduce complexity.
- Restructuring/reengineering is necessary to improve system structure.

### Law of Self-Regulation

- System attributes follow a probabilistic distribution.

### Law of Conservation of Organizational Stability

- The average work rate for an evolving system remains constant until the system becomes obsolete.

### Law of Conservation of Familiarity

- The rate of functional growth in a system remains constant until the system becomes obsolete.

### Law of Continuing Growth

- Systems must continue to grow in functionality to satisfy users.

### Law of Declining Quality

- Software quality will decline unless it adapts fully to the operating environment.

### Law of Feedback Systems

- Evolution processes consist of multiple iterations and feedback from stakeholders.

## Types of Maintenance

**Corrective Maintenance**: Planned problem-solving based on discovered errors

**Adaptive Maintenance**: Porting to new data, operating systems, or hardware environments

**Perfective Maintenance**: Changes to improve performance or maintainability

**Emergency Maintenance**: Unplanned maintenance for emergency fixes

### Maintenance Process

1. Understanding the Current Program
   - Trace program logic or understand requirements, design, etc.
   
      ↓
      
2. Identifying and Analyzing Changes
   - Identify necessary changes, analyze impact, costs, and risks
   
      ↓
      
3. Assessing Change Impact
   - Communicate with stakeholders and gather feedback
   
      ↓
      
4. Implementing, Testing, and Installing Changes
   - Modify the system, verify the changes, and install updates

### Maintenance Process Models

**Quick Fix Model**

An ad-hoc maintenance model to resolve issues as quickly as possible without extensive analysis. Documentation is minimized.

**Iterative Enhancement Model**

Continuous system improvements through iterative changes across the system lifecycle.

**Reuse-Oriented Model**

Maintenance tasks revolve around reusing program components.

### Understanding Programs

To modify software, one must understand the program.

Abstracting designs or specifications from source code into mental models
The reverse of the development process aiming for higher abstraction

### Identifying and Analyzing Changes

Identify which parts need modification based on change requests and explore alternative solutions.

- Change analysis
- Impact analysis
- Estimating time and cost for implementing and testing changes
- Risk assessment

### Configuration Management

Tracks the status of documents and software system components throughout the development cycle.

Prevent inconsistencies when documents and deliverables change.
Class changes must be updated in dependent classes.
Apply traditional principles used in hardware to software development.

### Baseline

A collection of software configuration items.

**Purpose**
- Define critical project states
- Indicate when a product reaches a particular state
- Serve as a reference for ongoing development and maintenance
- Control changes to configuration items

**Types**

- Plan Baseline: Requirements, domain model, plans
- Requirements Baseline: Use cases, requirement specs, user manual drafts
- Design Baseline: Class/sequence diagrams, integration test plans
- Implementation Baseline: Source code, unit test cases/results
- Integration Baseline: Integration test cases/results reports
- Verification Baseline: Verification test cases/results reports, installation manual, user manual

### Necessity of Configuration Management

Unnecessary if a small number of developers work in one location.

Necessary for coordinating and synchronizing work among many teams and developers.
Essential for maintaining various versions to satisfy different customers.

### Configuration Management Procedure

![struct](https://i.imgur.com/IAeFSDG.png)

- Software configuration identification
- Configuration change control
- Software configuration auditing
- Software configuration status accounting

### Configuration Identification

- Unique identifier - unique number
- Name
- Document type
- Document file
- Author
- Creation date, target completion date
- Version number
- Update history
- Description
- SQA Manager - Quality Assurance Manager
- SCM Manager - Configuration item checker

### Configuration Change Control

Determine the reason for changes:
- Software defects
- Hardware changes
- Changes in operational requirements
- Customer or user improvement requests
- Changes in budget, project schedules, or durations

- Change analysis
- Prepare change proposals
   - Description, identifying organizations and developers, reasons, affected items, effort estimation, impact on project schedules
- Evaluate change proposals
- Implement changes

### Configuration Auditing

Define mechanisms to establish baselines and subsequent approved baselines.

Review configuration items to ensure no discrepancies.
Verify the correctness of configuration items to confirm proper problem resolution.

### Reverse Engineering

Analyzing a system to identify its components and their relationships, creating representations at the same or higher levels of abstraction.

Incrementally recover the abstraction level of the program.

**Reverse Engineering Process**

Extract software deliverables from source code.
Components of reverse engineering tools.

![re](https://i.imgur.com/RfcoQeu.png)

**Uses of Reverse Engineering**

Reconstructed diagrams can be used in various ways:

1. Program Understanding
   - Easier comprehension of software structure, functionality, and behavior
2. Formal Analysis
   - Detect potential issues in software
3. Test Case Generation
   - Flow paths in flowcharts aid in path test case generation
4. Reengineering

**Redocumentation**

Generating representations at the same level of abstraction with semantic equivalence.

Purpose
- Enhance understanding of software by presenting different system perspectives
- Improve existing documentation
- Document newly modified programs

**Design Recovery**

Analyzing source code to extract meaningful high-abstraction representations.

Recovered designs aid in source code understanding, serve as baselines for future maintenance or reengineering, and can be used for similar applications.

**Reengineering**

Restructuring systems or components.
Purpose:
- Improve software architecture
- Reduce software complexity
- Enhance adaptability to changes
- Improve performance, efficiency, and resource utilization
- Improve software system maintainability

**Process**

- Identify areas needing improvement
- Select improvement strategies
- Implement proposed improvements
- Evaluate the system based on objectives




# Korean


### 품질

좋은 품질의 SW를 개발하는 것이 쉽지 않으나 품질 관리의 필요성은 있다.

**품질 높이는 활동**

1. **테스트**
    - 제품 주기에서 테스트가 너무 늦게 수행된다.
    - 테스트는 좁은 차원만 다룬다.
    - 테스트는 코드 품질만 향상시킨다.

2. **리뷰**
    - 테스트를 보완, 개발 초기에 검토할 수 있어 오류가 조기에 발견된다.

3. **품질 보증**
    - 개발자와 협력하여 소프트웨어 개발의 적절한 표준과 절차를 수립한다.
    - 검토 및 감사를 통해 업무를 모니터링하여 확인한다.
    - 품질 목표를 향한 진행 상황에 대해 상급 관리자 및 기타 이해 관계자에게 피드백을 제공한다.

**품질 관리**

품질 계획, 품질 관리, 품질 보증, 검증 및 여러 가지 품질 관련 프로세스
품질 목표를 설정하고 목표 달성을 위한 프로젝트 실행을 관리 및 통제하기 위한 모든 활동
- 측정
- 프로세스 평가 및 개선

**품질 개선**

품질에 대한 다양한 관점
관점에 따라 다른 정의
품질에 대한 정의에 따라 품질 관리 활동이 달라짐
- 고객 만족
- 요구 적합성
- 제품 품질

**품질 개념**

품질에 대한 다양한 관점
관점에 따라 다른 정의
품질에 대한 정의에 따라 품질 관리 활동이 달라짐

- **고객만족**
    
    사용자 만족도는 제품의 전반적 요소를 기반으로 하여 품질은 그 중 하나
    
- **요구 적합성**
    
    모호하지 않음
    지정된 요구 사항과 디자인을 준수하는 제품이 높은 품질의 제품
    일정 수준 이상의 고급이라는 의미가 없음
    
- **제품 품질**
    
    여러 속성의 집합이며 이들이 품질을 결정
    디지털 카메라의 품질을 결정하는 세 가지 속성

**소프트웨어 품질**

시스템, 구성 요소, 프로세스가 지정된 요구 사항을 충족 시키는 정도
시스템, 구성 요소, 프로세스가 고객 또는 사용자 요구나 기대를 충족시키는 정도

→ 소프트웨어에 대한 작업 관점이 있느냐에 따라 품질 속성의 관심이 달라짐

![qu](blob:https://imgur.com/686a64e8-4ce6-45f1-893f-a834581541e5)

**소프트웨어 품질 특성**

소프트웨어의 품질의 특성은 세 가지 차원이 존재
- 품질 요소: 사용자에 의한 외부 관점
- 품질 기준: 개발자 측면의 내부 관점
- 메트릭 차원: 품질을 제어

**품질 속성**

1. **신뢰성**: 소프트웨어에 요구된 기능을 명시된 조건 하에 실행하여 정확하고 일관성 있는 결과를 생성하는 능력
2. **강인성**: 소프트웨어에 요구된 기능을 어렵거나 예외적인 환경에서 수행할 능력
3. **효율성**: 소프트웨어에 요구된 기능을 최소의 시간과 자원을 사용하여 원하는 결과를 생성하는 능력
4. **상호운용성**: 소프트웨어가 다른 소프트웨어와 정보를 교환하는 능력
5. **유지보수성**: 소프트웨어가 수리 및 진화될 수 있는 성질
6. **테스트 가능성**: 소프트웨어에 요구된 또는 적용될 수 있는 모든 형식의 평가, 인스펙션, 동료검토, 화이트 박스 테스팅, 블랙박스 테스팅 등
7. **이식성**: 소프트웨어가 여러 운영 환경 및 플랫폼에서 실행될 수 있도록 변형이 가능한 성질
8. **재사용성**: 소프트웨어가 확장이나 커스텀화 없이 유사한 또는 다른 배경에서 사용될 수 있는 성질
9. **모듈성**: 소프트웨어가 모듈 컴포넌트의 통합이나 조정을 쉽게 만드는 성질

**품질 관리**

소프트웨어 제품이나 아이템이 정해진 요구에 적합하다는 것을 보장하는 데 필요한 계획적이고 체계적인 활동
다양한 작업이며 미치는 영향이 크다

- 품질 관리 기능
- 프로세스와 표준의 정의
- 품질 보증
- 프로세스 개선

**품질 보증 조직**

관리적 활동
- 개발 조직의 표준화 방법론을 잘 따르도록 하는 것

기술적 활동
- 방법론을 잘 정의하는 것

**품질 계획**

- 각 프로젝트 초기에 이루어짐
- 목적
- 관리
- 표준과 관례
- 리뷰와 감리
- 형상 관리
- 프로세스, 방법론, 도구, 기술
- 메트릭, 지표

**품질 보증 제어**

계획이 정확하게 실행되고 있는지 확인하는 것
개발자가 품질 보증 활동을 수행하도록 도와주는 것
품질 관련 데이터를 모아 데이터베이스 사용하여 관리
관리자에게 프로세스 개선을 위한 제안을 하고
수용된 제안이 적절히 실현되고 프로세스에 녹아 들었는지 확인
