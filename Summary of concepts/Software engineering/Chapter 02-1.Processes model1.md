# In English

### Types of Process Models 1

**Process Model**

A simplified (abstract) representation of development stages
Abstraction of processes (explaining different approaches to software development)

**Waterfall Model** 

![waterfall model](https://i.imgur.com/xQQY5eV.png)

The oldest and most widely used model
Performed in sequence from planning , operation , to maintenance
Each process is clearly distinguished with deliverables between stages.
No rework going back to previous tasks.
Linear progression like a waterfall
Tasks are arranged in a sequence, enabling function-centered project organization. Suitable for large, complex, and long-term projects.

Advantages: 
1. Simple and easy to understand.
2. Each stage is clear, making it easy to manage the process progress.

Disadvantages:
1. Problems arise if issues in previous stages are not detected.
2. Since tasks are performed sequentially, previous tasks cannot be redone. ⇒ Biggest disadvantage
3. It is difficult to incorporate changes in the process progression.

**V (Verification) Model**

![Verification model](https://i.imgur.com/6yXsLbc.png) 

An extended model of the waterfall model from the perspective of strengthening verification
Verification is performed upwards from the coding stage.
When a small separated module is completed, it is checked through unit testing.
Integration testing is done to verify if modules are well integrated.
System testing is done to verify if the entire system works well.
Acceptance testing is done to verify if all user requirements are met.

**Prototyping Model**

![prototyping model](https://i.imgur.com/DeDNyHM.png)

A method of experimentally creating a system to show and evaluate it with users to get feedback on requirements
By creating prototypes, communication with users can clarify requirements.
Some parts of the final product can be implemented and shown, with the code used for the final implementation.

Advantages: 
1. Problems can be quickly identified.
2. Functional requirements can be accurately determined.
3. Increases customer satisfaction with the product.

Disadvantages:
1. If too much cost is spent on the prototype, disadvantages increase.
2. Excessive demands from customers can arise.

**Spiral Model**

![spiral model](https://i.imgur.com/13ZPP1E.png) 

The system is expanded through iterative cycles of the following four stages:
1. Determine objectives , methods , and constraints
2. Analyze and resolve risks
3. Development and evaluation
4. Plan the next stage
Can analyze risks overlooked in other models.
After planning and requirement analysis for development, there is a stage to review risks and alternatives.
Suitable when it is difficult to understand requirements or architecture.

Advantages: 
1. Can improve the quality of deliverables.
2. Can flexibly handle error correction and changes made in earlier cycles.

Disadvantages: 
1. Poor management of each cycle can affect subsequent cycles. ⇒ Incremental management

**Evolutionary Model**

![evolutionary model](https://i.imgur.com/TZxgJIM.png)

Improves the initial system through iterative processes.
Also called an iterative model as it repeats requirement analysis, design, implementation, and testing during improvements.
Suitable for object-oriented technologies.

Advantages: 
1. Can quickly reflect user requirements.
2. Can pioneer new software markets that didn't exist before. ⇒ Software market pioneering
3. Development teams can focus on different areas in each release.

Disadvantages:
1. Not suitable for small projects (project management is complex).
2. Difficult to obtain a final version of the project. ⇒ Continuous updates

**Unified Process**

![Unified Process](https://i.imgur.com/7g7aHvW.png)

- Inception
Conducted over 1 to 2 iterations
Develop simple use case models, software architecture, and project plans.
- Elaboration
Performed over several iterations
Develop most use cases
Design the architecture
- Construction
Implement and integrate the remaining use cases
Incrementally install the system in the target environment.
- Transition
Deploy the system and train users
Beta testing, defect fixing, and feature enhancement.

Advantages:
1. Well-documented, making it easy to share.

Disadvantages:
1. The process is too complex for non-experts to understand or apply.

**Agile Process**

Development is repeated in short cycles of 2 ~ 6 weeks.
The entire system is gradually completed by developing executable software.
Agile Manifesto:
1. The project moves towards its goals through communication rather than formal documentation.
2. Users confirm requirements through executable software, not documents.
3. User requirements can change during the project due to business environment changes.
4. During short cycles, requirements definition, implementation, and testing are completed, and feedback from each iteration is included in the next plan.
⇒ These 4 points must be considered!




# In korean

### 프로세스 모델의 종류 1

**프로세스 모델**

개발 단계를 단순화(추상화)하여 표현한 것 
프로세스의 추상(소프트웨어 개발에 대한 다양한 접근 방식을 설명)

**폭포수 모델** 

![waterfall model](https://i.imgur.com/xQQY5eV.png)

가장 오래되고 널리 사용되는 모델
계획 , 운영 , 유지보수까지 순서대로 수행
각 프로세스 사이에 결과물이 있어 명확히 구분된다. 
이전 작업으로 돌아가는 재작업이 없다. 
폭포수가 떨어지는 듯한 선형적인 진행
작업이 일렬로 나열되어 있어 직능 중심의 프로젝트 조직이 가능하다. 크고 복잡하고 , 오래 지속되는 프로젝트에 적합

장점) 
1. 단순하여 이해하기 쉽다.
2. 각 단계가 명확하여 프로세스의 진행 상황을 관리하기 쉽다. 

단점)
1. 이전 단계의 문제가 발견되지 않고 넘어가는 경우 문제가 생긴다. 
2. 작업이 순차적으로 이루어지기 때문에 이전 작업을 다시 할 수 없다. ⇒ 가장 큰 단점
3. 프로세스 진행 과정에 대한 변경 사항이 반영되기 어렵다. 

**V(verification) 모델**

![Verification model](https://i.imgur.com/6yXsLbc.png) 

검증을 강화하는 관점에서 폭포수 모델을 확장한 모델 
코딩 단계에서 위로 올라가며 검증한다. 
분리된 작은 모듈이 완성되면 단위 테스트를 통해 확인
모듈이 잘 결합되었는지 통합테스트를 통해 확인
전체 시스템이 잘 동작하는지 시스템 테스트를 통해 확인
사용자의 요구를 모두 반영하였는지 인수 테스팅을 통해 확인 

**프로토타이필 모델**

![prototyping model](https://i.imgur.com/DeDNyHM.png)

요구 사항에 대한 피드백을 받기 위해 시스템을 실험적으로 만들어 사용자에게 보여주고 평가받는 방법
프로토타입을 만들면서 사용자와 소통하여 요구를 명확하게 처리할 수 있다. 
완성품의 일부를 구현하여 보여주는 것으로 완성품 구현에 코드를 활용할 수 있다. 

장점) 
1. 문제점을 빠르게 파악할 수 있다. 
2. 정확하게 기능요구를 확정지을 수 있다. 
3. 고객의 제품에 대한 만족도를 높일 수 있다. 

단점)
1. 포로토타입에 너무 많은 비용을 소모하면 단점이 커진다. 
2. 고객의 과도한 요구가 생길 수 있다. 

**나선형 모델**

![spiral model](https://i.imgur.com/13ZPP1E.png) 

아래 4가지 단계를 반복 순환하며 시스템을 확대시켜 나간다. 
1. 목표 , 방법 , 제약조건 결정
2. 위험 요소 분석 및 해결
3. 개발과 평가
4. 다음 단계의 계획
다른 모델에서 간과하는 위험을 분석할 수 있다. 
개발을 위한 계획 및 요구분석 후에 위험 요소와 차선책에 대하여 검토하는 단계가 있다. 
요구사항이나 아키텍처를 이해하기 어려운 경우에 적합하다. 

장점) 
1. 결과물의 품질을 높일 수 있다. 
2. 오류 수정과 앞 주기에서 이루어지는 변경에 유연하게 대처할 수 있다. 

단점) 
1. 각 싸이클을 잘 관리하지 않으면 이후 싸이클에도 영향을 끼친다. ⇒ 점진적 관리

**진화적 모델**

![evolutionary model](https://i.imgur.com/TZxgJIM.png)

초기 시스템에서 개선과정을 거친다.
개선하는 과정에 요구 분석 , 설계 , 구현 , 테스트를 반복하므로 반복적 모델이라고도 부른다. 
객체지향 기술에 적합하다. 

장점) 
1. 사용자의 요구를 빠르게 반영할 수 있다. 
2. 이전에는 없던 새로운 소프트웨어 시장을 선점할 수 있다. ⇒ 소프트웨어 시장 선점 
3. 개발팀이 릴리스마다 다른 영역에 초점을 둘 수 있다. 

단점)
1. 소규모 프로젝트에는 적합하지 않다. (프로젝트 관리가 복잡하다)
2. 프로젝트의 완성본을 얻기가 어렵다. ⇒ 계속 업데이트 

**Unified process**

![Unified Process](https://i.imgur.com/7g7aHvW.png)

- 도입
1 , 2회 정도 반복으로 도입 단계를 진행
간단한 유스케이스 모델과 소프트웨어 구조 , 프로젝트 계획을 작성
- 정련
여러 번의 반복 과정으로 이루어짐
대부분의 유스케이스를 작성
아키텍처 설계
- 구축
남아 있는 유스케이스에 대하여 구현하고 통합
시스템을 목표 환경에 점증적으로 설치
- 전환
시스템을 배치 , 사용자를 교육
베타 테스팅 , 결함 수정 , 기능 개선 

장점)
1. 문서화가 잘 되어있어 공유가 편하다

단점)
1. 프로세스가 너무 복잡하여 전문가가 아니면 이해하거나 적용하기 어렵다. 

**애자일 프로세스**

2 ~ 6주간의 짧은 주기로 개발을 반복
실행되는 소프트웨어를 개발하여 단계적으로 시스템 전체를 완성
애자일 선언
1) 형식적인 문서보다는 커뮤니케이션을 통하여 프로젝트가 목표를 향하여 나아가게 함 
2) 사용자는 문서가 아니라 실행되는 소프트웨어를 통하여 요구를 확인
3) 사용자의 요구는 비즈니스 환경에 따라 프로젝트 중간에 바뀔 수 있음을 고려
4) 짧은 주기 동안 요구 정의에서 구현 , 테스트까지 이루어지며 각 반복 주기의 반성 의견을 다음 계획에 포함
⇒ 이 4가지는 반드시 고려!
