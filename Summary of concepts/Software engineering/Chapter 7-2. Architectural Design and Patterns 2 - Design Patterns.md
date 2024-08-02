# English

### Design Patterns

Design occurs at various levels, with each level addressing different design problems and objectives. Solutions suitable for one level might not be appropriate for another. Design patterns offer reusable solutions for problems at levels below architectural design.

![design](https://i.imgur.com/LLzTb2r.png)

1. Reusability: Reuse well-tested and proven solutions.
2. Simplified Design Work: Specialized design patterns for specific situations.
3. Organized Design Knowledge: Systematically documented design solutions.
4. Communication: Facilitates discussions using common vocabulary.
5. Adherence to Object-Oriented Principles: Encourages use of best practices.

### Types of Patterns

**I. Singleton Pattern**

Ensures a class has only one instance and provides a global point of access to it. 
Example: Interface for DB connection.

Method:
- Declare the class itself as a static variable.
- Declare the constructor as private.
- Provide a static method to access the unique instance.

**II. Iterator Pattern**

Allows access to elements of an aggregate object sequentially without exposing its underlying representation. Suitable for traversing collections.

Example: Using getFirst() and getNext() methods in a Vector, you can access each element without knowing the internal details.

**III. Adapter Pattern**

Adjusts the interface of an existing class to another interface expected by clients. The adapter allows incompatible interfaces to work together.

Example: Convert an Enumerator interface to an Iterator interface using the Adapter Pattern.

**IV. Decorator Pattern**

Extends the functionality of an object dynamically by wrapping it with additional behavior. Uses composition and delegation to add responsibilities to objects.

Adding new functionality through inheritance can violate the Open-Closed Principle (OCP).

Example: Adding features to a graphical window class by wrapping it with decorators that add border, scrollbars, etc.

**V. Factory Method Pattern**

Separates the instantiation process from the client to allow for flexible and interchangeable object creation. Defines an interface for creating an object but allows subclasses to alter the type of objects that will be created.

**VI. Abstract Factory Pattern**

Provides an interface for creating families of related or dependent objects without specifying their concrete classes. It separates the client from the actual creation process, making the system more modular.

**VII. State Pattern**

Allows an object to alter its behavior when its internal state changes. The object will appear to change its class. Achieves flexibility by implementing state-specific behavior in separate state classes and delegating state-dependent behavior to the current state object.

**VIII. Observer Pattern**

Defines a one-to-many dependency between objects so that when one object changes state, all its dependents are notified and updated automatically. Used to implement distributed event handling systems.

**Subject Class** - Maintains a list of observers, notifies them of changes.
**Observer Class** - Receives the update and handles the change.

### Evaluating Architecture and Design Patterns

Ensure the chosen architecture meets both functional and non-functional requirements. Evaluate using specific methods:

**SAAM** (Scenario-based Architecture Analysis Method): Determines if the architecture can execute scenarios. If not, modify the architecture to support them. Involves multiple stakeholders to derive scenarios.

- **Direct Scenario**: Does not require system changes.
- **Indirect Scenario**: Requires system changes, such as adding new features or removing unwanted ones.

**ATAM** (Architecture Tradeoff Analysis Method): Focuses on evaluating multiple quality attributes, identifying trade-offs and compromises in the design.

![ATAM](https://i.imgur.com/1z5plO2.png)


# Korean

### 디자인 패턴

디자인은 여러 수준에서 이루어진다. 설계 문제와 목표는 설계 추상 수준마다 다르기 때문에 한 수준에 적합한 패턴이 다른 레벨의 문제에는 적합하지 않을 수 있다. 아키텍처 설계 수준보다 낮은 수준의 설계 문제에 재사용 가능한 솔루션을 제공 

![design](https://i.imgur.com/LLzTb2r.png)

1. 쉽게 재사용 가능 - 개발 검증된 것을 재사용
2. 설계 작업이 쉬워짐 - 특정 상황에 대하여 디자인 패턴을 특수화
3. 설계 관련 지식이 정리됨
4. 디자인을 논의하기 위한 의사소통이 쉬워짐 - 공통의 어휘를 사용
5. 객체지향 설계 원리를 잘 따르게 됨 - 모범 사례 사용

### 패턴의 종류

**I. 싱글톤 패턴**

객체를 강제적으로 하나만 생성하려는 목적(단일 객체)
하나의 클래스 인스턴스만 원하고 모든 클라이언트가 동일한 인스턴스를 공유
예) DB 커넥션을 위한 인터페이스 

방법
클래스 자체를 정적 변수로 
생성자는 private으로 선언
유일한 객체를 접근하는 정적 메서드 

**II. 반복자 패턴**

집합 클래스의 자료구조와 상관없이 집합에 소속된 요소들을 쉽게 접근하기 위하여 
반복자를 두어 접근하고 검색
클라이언트가 특정 집합의 유형과 유형별로 접근하고 집계하는 방법을 신경 쓰지 않아도 됨 

예) Vector에서 getFirst(), getNext() 메서드를 이용하는 경우
각 요소에 접근하기 위한 자세한 방법은 몰라도 된다. 

**III. 어댑터 패턴**

사용 가능한 서비스의 인터페이스를 클라이언트가 예상하는 인터페이스에 맞게 조정
어뎁터 - 서비스가 제공하는 인터페이스를 클라이언트가 기대하는 인터페이스로 변환

예) 어댑터 패턴을 이용하여 Enumerator 타입의 인터페이스를 Iteratir 인터페이스로 전환 

**IV. 데코레이터 패턴**

합 관계와 위임을 사용하여 기존 클래스의 동작을 가볍고 유연하게 확장

새로운 동작을 포함하도록 클래스를 수정한다면 OCP 원리에 위배

→ 상속에 의한 추가
기능의 조합 수 만큼의 서브클래스가 필요
추가되는 기능과 확장되는 클래스 사이에 컴파일 타임 의존 관계가 생성됨 

**V. 팩토리 메소드 패턴**

클라이언트에서 사용할 클래스의 객체를 생성하는 책임을 분리하여 객체 생성에 변화를 대비 

객체를 생성하기 위한 팩토리 메소드를 포함하는 추상 클래스를 정의 

**VI. 추상 팩토리 패턴**

객체를 사용할 클라이언트에서 구체적인 객체 생성을 지정하는 책임을 분리하기 위하여 추상 인터페이스를 이용하여 관련 객체 패밀리를 생성 

**VII. 상태 패턴**

상태에 따라 객체의 동작을 변경해야 하는 경우 
맥락과 상태를 별도로 구현하여 융통성을 달성하기 위한 체계적이고 느슨한 결합 방식 

**VIII. 옵서버 패턴**

데이터를 보관하고 있는 subject가 그 데이터를 이용하는 옵서버와 효과적으로 통신하면서 느슨하게 결합 
**Subject 클래스** - 옵서버 목록을 유지, 변경을 고지
**Observer 클래스** - 변경을 통지 받고 접근을 요청 

### 아키텍처나 디자인 패턴의 속성, 강점 및 약점을 결정하는 방법

개발자가 선택한 아키텍처가 기능적 및 비기능적 품질 요구 사항을 모두 충족시킬 수 있음을 보증 

방법

SAAM: 시나리오 기반 평가 방법
ATAM: 여러가지 품질 속성에 초점을 맞추어 평가 

### SAAM

아키텍처가 시나리오를 실행할 수 있는지 여부를 결정 
실행하지 못하는 경우, 시나리오를 지원하도록 아키텍처를 변경 
여러 이해 당사자를 통하여 시나리오 도출 

시나리오
직접: 시스템의 변경이 요구되지 않는 시나리오 
간접: 시스템의 변경이 요구되는 시나리오. 새로운 기능을 추가하거나 원하지 않는 기능을 삭제 

### ATAM

여러 가지 품질 속성에 초점을 맞추어 평가하여 아키텍처의 Trade-off, 설계 타협점을 찾아냄 

![ATAM](https://i.imgur.com/1z5plO2.png)

