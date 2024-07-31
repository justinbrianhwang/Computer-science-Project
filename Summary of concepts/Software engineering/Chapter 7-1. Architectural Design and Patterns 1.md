# English

### Architectural Design and Patterns

Grouping procedures and treating the unit group as a single entity allows for design at the subsystem level. This focuses on the roles of components and their relationships at various levels.

![relation](https://i.imgur.com/6RwOy3M.png)

Example: Web-based system architecture
The architecture is client/server-based.

### Role of Architecture

The architecture establishes the structure of the system, serving as the backbone throughout software development, including design, implementation, integration, and testing. It embodies critical early decisions that affect all stages, reflecting non-functional requirements.

### Architectural Styles

Defining a general shape and harmony through style is essential. This includes system partitioning, overall control flow, error handling, and communication protocols among subsystems.

**Major Styles**

**I. Client-Server Style**

- **Server**: Manages resources with powerful performance, providing requested functions or resources to clients.
- **Client**: Connects to the server to use resources.

**Advantages**
1. Data centralization - All data is centralized in the server, simplifying configuration and management.
2. Security - Keeps records of client requests.

**Disadvantages**
1. Bottleneck - Increased load with more clients.
2. Cost - Generally high installation and maintenance costs.
3. Single point of failure - If the server fails, the entire system is unusable.

![client](https://i.imgur.com/IcwlZwX.png)

**II. Layered Style**

Software functions are divided into multiple layers that interact vertically, exchanging messages.

**Advantages**
1. Abstraction - Understand roles and relationships of each layer.
2. Encapsulation.
3. High cohesion - High cohesion within layers, low coupling between layers.
4. Reusability - Easily replaceable modules.

**Disadvantages**
1. Restricted communication with adjacent layers.

![hierarchy](https://i.imgur.com/F7fdptv.png)

**III. Event-Based Architecture**

Consists of event producers generating event streams and event consumers waiting to receive these events. Events are delivered in real-time, allowing consumers to respond immediately.

**Advantages**
1. Encapsulation.
2. High cohesion - Separates event producers and consumers.
3. Scalability - Easily add new consumers.

**Disadvantages**
1. Complexity - Requires sophisticated control.
2. Testing - Handling unauthorized events is challenging.

![event](https://i.imgur.com/uTKgDCQ.png)

**IV. MVC (Model-View-Controller)**

Separates the user interface from business logic and data.

- **Controller**: Sends commands to the model to change its state.
- **Model**: Notifies the controller and view of state changes.
- **View**: Generates the user interface based on the model's data.

**Advantages**
1. Loose coupling and scalability - Weak coupling among components.
2. Multiple views - Separates data and business logic.
3. Asynchronous - Utilizes asynchronous techniques for faster application loading.

**Disadvantages**
1. Complexity - Increased complexity due to component separation.
2. Inefficiency - Inefficiency in accessing data from the view.

![MVC](https://i.imgur.com/lcs5I0X.png)

**V. Pipe and Filter**

Processes data step-by-step by passing it through filters, each performing a transformation.

**Advantages**
1. Simplicity - Structured as input-processing-output transformations.
2. Reusability - Filters can be reused in different programs.
3. Parallelism - Filters can operate in parallel.

**Disadvantages**
1. Resource waste - Potentially unnecessary transformations.

![pipe](https://i.imgur.com/XBPtDfE.png)

**VI. Data-Centered Architecture**

Composed of a shared data repository and data accessors who add, delete, and modify the shared data.

- **Blackboard**: Includes control threads, uses the observer design pattern.
- **Repository**: Queries shared data to find changes.

**Advantages**
1. Low coupling - Loose coupling between accessors.
2. Scalability - Modifiable and extensible accessors.

**Disadvantages**
1. Single point of failure - Failure of the shared data affects the entire system.

![data](https://i.imgur.com/dgXqqvs.png)

**VII. Peer-to-Peer Style**

Each component is equal, acting as both a client requesting services and a server providing services. The system is symmetric, with equal data transmission and reception.

**Advantages**
1. No dedicated server - Distributes the load evenly.
2. Improved scalability and reliability - System remains operational even if some components fail.

**Disadvantages**
1. Security vulnerabilities - Difficult to secure.
2. Lack of centralized control - Challenging to manage.

![ptp](https://i.imgur.com/ig4KRF9.png)



# Korean

### 아키텍처 설계와 패턴

프로시저를 그룹화하고 단위 그룹을 한 덩어리로 취급하여 그룹 수준에서 설계합니다. 서브 시스템 수준의 덩어리화 작업으로 다양한 수준에서 구성 요소의 역할과 구성 요소 간의 관계에 집중합니다.

![relation](https://i.imgur.com/6RwOy3M.png)

예: 웹 기반 시스템
아키텍처는 클라이언트/서버 구조입니다.

### 아키텍처의 역할

시스템의 구조를 확립하는 소프트웨어 개발의 중심축으로서, 설계, 구현과 통합, 테스팅까지 통합하는 뼈대 역할을 합니다. 모든 단계에 영향을 줄 만한 초기 의사 결정의 핵심이며 비기능적 요구는 아키텍처를 구축하면서 반영됩니다.

### 아키텍처 스타일

일반적인 모양과 조화를 위한 스타일을 정하는 작업으로 시스템 분할, 전체 제어 흐름, 오류 처리 방침, 서브 시스템 간의 통신 프로토콜 등을 포함합니다.

**주요 스타일**

**I. 클라이언트 서버형**

- **서버**: 강력한 성능으로 자원을 관리하며 클라이언트가 요청하는 기능이나 자원을 제공합니다.
- **클라이언트**: 자원의 사용을 위해 서버에 접속합니다.

**장점**
1. 데이터 집중화 - 모든 데이터를 서버에 모아서 구성과 관리를 단순화합니다.
2. 보안 - 클라이언트의 요청 기록을 남길 수 있습니다.

**단점**
1. 병목 현상 - 클라이언트가 증가하면 부하가 증가합니다.
2. 비용 - 설치 및 관리 비용이 일반적으로 높습니다.
3. 단일 장애 지점 - 서버가 고장 나면 전체 시스템을 사용할 수 없습니다.

![client](https://i.imgur.com/IcwlZwX.png)

**II. 계층형**

소프트웨어의 기능을 수직으로 상호 작용하는 여러 층으로 분할하며 각 층 사이에 메시지를 교환합니다.

**장점**
1. 추상화 - 각 층의 역할과 관계를 잘 이해할 수 있습니다.
2. 캡슐화
3. 높은 응집도 - 각 층의 응집도가 높고 층 사이의 결합이 적습니다.
4. 재사용 가능 - 다른 모듈로 쉽게 교체할 수 있습니다.

**단점**
1. 이웃 층과의 커뮤니케이션이 제한적입니다.

![hierarchy](https://i.imgur.com/F7fdptv.png)

**III. 이벤트 기반 아키텍처**

이벤트 스트림을 생성하는 이벤트 생산자와 이벤트 수신을 대기하는 이벤트 소비자로 구성됩니다. 이벤트는 실시간으로 전달되어 발생 즉시 소비자가 이벤트에 응답할 수 있어야 합니다.

**장점**
1. 캡슐화
2. 높은 응집도 - 이벤트 생산자와 소비자가 분리됩니다.
3. 확장성 - 새로운 소비자를 쉽게 추가할 수 있습니다.

**단점**
1. 복잡성 - 정교한 제어가 필요합니다.
2. 테스팅 - 허용되지 않은 이벤트에 대한 처리가 필요합니다.

![event](https://i.imgur.com/uTKgDCQ.png)

**IV. MVC (Model-View-Controller)**

사용자 인터페이스로부터 비즈니스 로직과 데이터를 분리합니다.

- **컨트롤러**: 모델에 명령을 보내어 상태를 변경합니다.
- **모델**: 데이터의 상태 변화를 컨트롤러와 뷰에 통보합니다.
- **뷰**: 사용자가 볼 결과물을 생성하기 위해 모델로부터 정보를 가져옵니다.

**장점**
1. 느슨한 결합과 확장성 - 각 컴포넌트의 결합이 약합니다.
2. 다수의 다른 뷰 - 데이터와 비즈니스 로직이 분리됩니다.
3. 비동기 - 비동기 기술을 이용하여 애플리케이션을 빠르게 로딩할 수 있습니다.

**단점**
1. 복잡성 - 컴포넌트의 분리로 인해 메커니즘 이해가 어려워집니다.
2. 비효율성 - 뷰에서 데이터를 접근해야 하는 비효율성이 존재합니다.

![MVC](https://i.imgur.com/lcs5I0X.png)

**V. 파이프 필터**

필터 사이에 데이터를 이동시키며 단계적으로 처리합니다. 데이터의 변환을 수행하는 필터 구성 요소로 구성됩니다. 예를 들어 컴파일러가 있습니다.

**장점**
1. 단순성 - 입력-출력-변환 형태로 이루어집니다.
2. 재사용 - 다른 프로그램에서 필터를 재사용할 수 있습니다.
3. 병렬성 - 필터를 병렬로 사용할 수 있습니다.

**단점**
1. 자원의 낭비 - 불필요한 변환으로 자원이 낭비될 수 있습니다.

![pipe](https://i.imgur.com/XBPtDfE.png)

**VI. 데이터 중심 아키텍처**

공유 데이터 저장소와 데이터 접근자로 구성됩니다. 접근자는 공유 데이터를 추가, 삭제 및 수정합니다.

- **블랙보드**: 제어 스레드를 포함하며 옵서버 디자인 패턴을 사용합니다.
- **리포지토리**: 공유 데이터를 질의하여 변경 사항을 발견합니다.

**장점**
1. 낮은 결합 - 접근자 사이의 결합이 느슨합니다.
2. 확장성 - 각 접근자를 수정하고 확장할 수 있습니다.

**단점**
1. 단일 장애 지점 - 공유 데이터의 장애는 전체 시스템에 영향을 미칩니다.

![data](https://i.imgur.com/dgXqqvs.png)

**VII. Peer-to-Peer 스타일**

각 컴포넌트는 동등하여 서비스를 요청하는 클라이언트인 동시에 서비스를 제공하는 역할을 합니다. 동일한 수신, 전송 데이터 양을 가지므로 대칭적인 시스템입니다.

**장점**
1. 전담하는 서버가 없습니다.
2. 규모 확장성과 신뢰성 개선 - 일부 컴포넌트에 고장이 있더라도 전체 시스템은 가동할 수 있습니다.

**단점**
1. 보안에 취약합니다.
2. 중앙에서 제어가 불가능합니다.

![ptp](https://i.imgur.com/ig4KRF9.png)


