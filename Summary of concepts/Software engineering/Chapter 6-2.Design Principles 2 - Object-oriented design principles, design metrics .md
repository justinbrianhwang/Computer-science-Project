# Egnlish

**I. Single Responsibility Principle**

A class should have only one reason to change, meaning it should have only one job or responsibility.

**II. Open-Closed Principle**

Software entities (classes, modules, functions, etc.) should be open for extension but closed for modification.
- Inheritance
- Polymorphism allowing for interchangeable implementations

**III. Liskov Substitution Principle**

Subtypes must be substitutable for their base types without altering the correctness of the program.
- Subclasses should replace their parent classes without affecting the functionality from the client's perspective.

**IV. Interface Segregation Principle**

Clients should not be forced to implement interfaces they do not use.
- No dummy methods: Methods that are not necessary should not be included.
- No fat interfaces
- No polluted interfaces

**V. Dependency Inversion Principle**

High-level modules should not depend on low-level modules. Both should depend on abstractions.
- Concrete modules should depend on abstract modules to invert the dependency.

### Design Metrics

**Traditional Metrics**

- Size
- Complexity
- Coupling
- Cohesion
- Information Flow

**Object-Oriented Metrics**

- Weighted Methods per Class (WMC): Measures the complexity of a class.
- Depth of Inheritance Tree (DIT): Measures the inheritance depth.
- Number of Children (NOC): Measures the inheritance breadth.
- Coupling Between Object Classes (CBO): Measures the coupling between classes.
- Response For a Class (RFC): Measures the size of a class.
- Lack of Cohesion in Methods (LCOM): Measures the cohesion among methods.




# Korean

**I. 단일 책임 원리 (Single Responsibility Principle)**

클래스의 역할과 책임을 단일화하여 클래스를 변경해야 할 이유를 하나로 제한합니다.
⇒ 즉, 하나의 역할만 수행해야 합니다.

**II. 개방 폐쇄 원리 (Open-Closed Principle)**

소프트웨어 개체(클래스, 모듈, 기능 등)가 확장을 위해 열려 있어야 하지만 수정을 위해 닫혀 있어야 합니다.
- 상속
- 다형성이 적용되어 서로 대체할 수 있는 인터페이스를 구현합니다.

**III. 리스코프 치환 원리 (Liskov Substitution Principle)**

클래스 B가 클래스 A에서 상속받은 하위 유형이라면 프로그램의 동작을 방해하지 않고 A를 B로 대체할 수 있어야 합니다.
- 하위 클래스는 클라이언트의 관점에서 기능을 손상시키지 않는 방식으로 상위 클래스 메소드를 대체해야 합니다.

**IV. 인터페이스 분리 원리 (Interface Segregation Principle)**

클라이언트가 사용하지 않는 인터페이스를 강제로 구현해서는 안 됩니다.
- 더미 메서드: 필요하지 않은 메서드를 포함하지 말아야 합니다.
- 비만 인터페이스
- 오염된 인터페이스

**V. 의존 역전 원리 (Dependency Inversion Principle)**

높은 수준의 모듈은 재사용이 가능하고 낮은 수준의 모듈 변경에 의해 쉽게 영향을 받지 않아야 합니다.
- 구체화된 모듈이 추상화된 모듈에게 의존이 역전되도록 설계해야 합니다.

### 설계 메트릭

**전통적인 메트릭**

- 크기
- 복잡도
- 결합도
- 응집도
- 정보 흐름

**객체지향 메트릭**

- 클래스 당 가중 메서드 (Weighted Methods per Class, WMC): 클래스의 복잡도 측정
- 상속 트리의 깊이 (Depth of Inheritance Tree, DIT): 상속의 깊이를 측정
- 자식 노드의 개수 (Number of Children, NOC): 상속의 너비를 측정
- 클래스 사이의 결합 (Coupling Between Object Classes, CBO): 결합도를 측정
- 클래스의 책임 (Response For a Class, RFC): 클래스의 크기를 측정
- 메소드의 응집 결핍 (Lack of Cohesion in Methods, LCOM): 메소드 간 응집도를 측정



