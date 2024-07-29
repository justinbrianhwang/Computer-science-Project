# English

### Requirement Modeling

This is arguably the most important chapter. Requirement modeling is the method used in the following process.

![require modeling](https://i.imgur.com/mKaPvxm.png)

Requirement analysis concludes with the creation of a specification for the system requirements.

Requirement modeling aims to create a requirement specification where both the customer and developer agree on what is being developed.

Requirement analysis defines what elements from the problem domain will be implemented in the target system.
Requirement modeling expresses the requirements from the perspective of the solution domain that developers understand.

The result of the requirement modeling work is the interface where the problem/solution domains meet.

![interface](https://i.imgur.com/C9sH8FO.png)

How to deal with complex systems:
Simplify or abstract a subject that is too complex to handle entirely.

Reasons for modeling:
(1) To manage complexity effectively.
(2) To visualize the structure of intangible software.
(3) To communicate with others.
(4) To understand the problem domain and product requirements.
(5) To understand the system being developed.
(6) To experiment with potential solutions before implementation.
(7) To document existing systems.

⇒ In other words, it's a method that allows both developers and customers to communicate easily.

A software model is a visual diagram composed of graphic symbols and annotations.
The result of modeling work influences other modeling tasks.

### UML

The standard graphical language for modeling object-oriented software.
Models various aspects of the system through diagrams.
Equivalent to circuit diagrams in hardware.
→ Just as hardware has circuit diagrams, software has UML.

UML is a common language for software modeling.
System modeling consists of functional, structural, and dynamic perspectives.

**UML Modeling Process**
(1) Organize requirements into use cases and create use case diagrams.
(2) Identify class candidates and create a conceptual object model.
(3) Create sequence diagrams based on use cases.
(4) Find attributes, operations, and relationships between classes to complete the object model.
(5) Add other diagrams like state diagrams or activity diagrams to complete the UML model.
(6) Identify subsystems and design the overall system structure.
(7) Find or customize appropriate objects or design new objects.

### Static Modeling

Static model:
Abstraction of common structures and behaviors of objects.

Understanding basic concepts of object-orientation is necessary.
Objects and attributes, associations, aggregations, inheritance, polymorphism.

Class diagrams, which represent classes and relationships between classes, are typical for representing domain concepts and attributes.

### Object-Oriented Concepts (UML originates from object-orientation)

**Objects and Classes**

![object class](https://i.imgur.com/DxPWC80.png)

Simplified UML representation of the above diagram:

![UML2](https://i.imgur.com/L07iOQ1.png)

**Encapsulation**
Grouping attributes and operations of an object into a single unit.
Information hiding.

**Association**
The relationship where an object providing a service interacts with an object requesting a service.

![asso](https://i.imgur.com/9kqlkuB.png)

**Inheritance**
A specialized class inherits attributes and operations from a generalized class.

![extends](https://i.imgur.com/7vipWup.png)

**Polymorphism**
The ability to call the same message by different objects or subclasses.

![poly](https://i.imgur.com/ohYLemS.png)

### Class Diagram

Class symbols are divided into three parts:
Class name at the top, attributes in the middle, and operations at the bottom.
Abstract classes are italicized, and interface classes are marked with <<interface>>.

Attributes: Include all fields an object possesses.

Operations/Methods:
Very common methods (getters/setters) are omitted.

**Relationships**
(1) Association: Links between related objects (structurally related to reference information).
(2) Inheritance: In object orientation, it refers to inheritance.
(3) Dependency: A dependency where changes in one class may require changes in another class.
(4) Implementation: Indicates that a class implements an interface.

Example:

![exam](https://i.imgur.com/sDyBmqb.png)

Modeling actual code:

Example: Course registration program

![diagram](https://i.imgur.com/KZ7jskK.png)




# korean

### 요구 모델링

사실상 제일 중요한 단원이다. 요구 모델링은 다음과 같은 과정에서 사용되는 방법이다. 

![require modeling](https://i.imgur.com/mKaPvxm.png)

요구 분석은 구축될 시스템에 요구사항에 대한 명세서를 작성하는 작업으로 마무리

요구 모델링은 고객과 개발자가 무엇이 개발되고 있는 지에 동의하는 것을 주된 목적으로 하는 요구 명세 생성 방법

요구 분석은 다루는 문제 영역에 있는 것들 중 대상 시스템에 구현할 것들을 요구로 정의
요구 모델링은 개발자가 이해하는 솔루션 영역의 관점으로 요구를 표현하는 방식

요구 모델링 작업에 의한 결과는 문제/솔루션 영역이 만나는 인터페이스이다. 

![interface](https://i.imgur.com/C9sH8FO.png)

복잡한 시스템을 다루는 방법
전체를 다루기에는 너무 복잡한 대상을 추상화 또는 단순화

모델링을 하는 이유
(1) 복잡함을 잘 관리하기 위하여
(2) 형체가 없는 소프트웨어의 구조를 시각화 하기 위하여
(3) 다른 사람과 커뮤니케이션 하기 위하여
(4) 문제 도메인 및 제품 요구 사항을 이해하기 위하여 
(5) 개발 중인 시스템을 이해하기 위하여
(6) 구현하기 전에 잠재적 솔루션을 실험해보기 위하여
(7) 기존 시스템의 문서화

⇒ 즉, 개발하는 사람이나 고객들도 쉽게 커뮤니케이션할 수 있는 방법이다. 

소프트웨어 모델은 그래픽 기호와 주석으로 구성된 시각적 다이어그램
모델링 작업의 결과물은 다른 모델링 작업에 영향을 준다. 

### UML

객체지향 소프트웨어를 모델링 하는 표준 그래픽 언어
시스템의 여러 측면을 그림으로 모델링
하드웨어의 회로도 같은 의미 
→ 하드웨어에서 회로도가 있다면 소프트웨어에는 UML이 있다고 생각하면 쉽다. 

UML은 소프트웨어 모델링의 공통 언어 
시스템의 모델링은 기능적 관점, 구조적 관점, 동적 관점으로 구성 

**UML 모델링 과정**
(1) 요구를 사용 사례로 정리하고 사용 사례 다이어그램을 작성
(2) 클래스 후보를 찾아내고 개념적인 객체 모형을 작성
(3) 사용 사례를 기초하여 순서 다이어그램을 작성
(4) 클래스의 속성, 오퍼레이션 및 클래스 사이의 관계를 찾아 객체 모형을 완성 
(5) 상태 다이어 그램이나 액티비트 다이어그램 등 다른 다이어그램을 추가하여 UML 모델을 완성
(6) 서브 시스템을 파악하고 전체 시스템 구조를 설계
(7) 적당한 객체를 찾아내거나 커스텀화 또는 객체를 새로 설계 

### 정적 모델링

정적 모델
객체들의 공통 구조와 동작들을 추상화 시킨 것

객체지향 기본 개념의 이해가 필요
객체와 속성, 연관, 집합, 상속, 다형성 

클래스 다이어그램(클래스와 클래스 사이의 관계를 나타내는 핵심 다이어그램)이 대표적 클래스 및 클래스 사이의 관계를 표현
도메인 개념과 속성

### 객체지향 개념(UML은 객체지향에서 출발)

**객체와 클래스**

![object class](https://i.imgur.com/DxPWC80.png)

위의 그림을 단순하게 UML로 표현한 것이 아래의 그림이다. 

![UML2](https://i.imgur.com/L07iOQ1.png)

**캡슐화**
객체의 속성 부분과 오퍼레이션 부분을 하나로 모아서 단위화
정보 은닉 

**연관**
서비스를 제공하는 객체와 서비스를 요청하는 객체가 상호작용하는 관계

![asso](https://i.imgur.com/9kqlkuB.png)

**상속**
일반화된 클래스가 갖는 속성과 연산을 하위 개념의 구체화된 클래스가 그대로 물려 받는 것 

![extends](https://i.imgur.com/7vipWup.png)

**다형성**
같은 이름의 메시지를 다른 객체 또는 서브 클래스에 호출할 수 있는 특징 

![poly](https://i.imgur.com/ohYLemS.png)

### 클래스 다이어그램

클래스 심볼
세 개의 부분으로 나누고
클래스의 이름, 중간에는 클래스의 속성, 아래 부분은 오퍼레이션을 적음
추상 클래스는 이탤릭체, 인터페이스 클래스는 <<interface>>추가

속성: 객체가 가지는 모든 필드를 포함

오퍼레이션/메소드
아주 흔한 메소드(getter/setter)는 생략 

**관계**
(1) 연관: 객체 사이에 관련되어 링크되어 있음(구조적으로 연관을 맺고 있어 정보를 참조하는 관계)
(2) 상속: 객체 지향에서는 상속
(3) 의존: 한 클래스의 변경으로 다른 클래스의 변경이 필요할 수 있는 의존성
(4) 구현: 클래스가 인터페이스를 구현한다는 것 

예)

![exam](https://i.imgur.com/sDyBmqb.png)

실제 코드를 모델링하기 

예) 수강신청 프로그램

![diagram](https://i.imgur.com/KZ7jskK.png)



