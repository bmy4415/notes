## 자료구조
- 각 자료구조를 비교할 때에는 다음의 4가지 기준에 따라 비교하자
    - search 시간복잡도
    - insert/delete 시간복잡도
    - memory 공간복잡도
    - 기타 특성


### Array vs LinkedList
- search
    - Array: O(n)
    - LinkedList: O(n)
- insert/delete
    - Array: O(n) -> 삽입이나 삭제 후 shift 해야함
    - LinkedList: 지울 node를 알 경우 O(1), 일반적인 경우 O(n) -> 일반적인 경우 지울 노드를 찾아야함
- memory 공간복잡도
    - Array: O(n)
    - LinkedList: O(cn) -> 다음 node를 가르키는 포인터만큼 추가공간 필요
- 기타 특성
    - array는 random access 가능(물리적으로 연속해서 할당되므로)
    - linked list는 random access 불가능(link를 쭉 따라가야함)
    - array는 fixed size, linked list는 dynamic size
    - array가 fixed size 이므로 약간의 공간비효율이 있을 수 있음(예를 들어 size 100인 array를 할당 후 element를 3개만 쓰는 경우)

### IP address
- key word
    - 내부IP vs 외부IP, 사설IP vs 공인IP
    - 고정IP vs 유동IP
    - 공유기에 접속할 때 일어나는 일
    - NAT vs PAT

- IP address
    - IP(Internet Protocol)을 사용하기 위해 각 장치에 부여되는 고유 주소
    - IPv4(32bit 주소), IPv6(64bit 주소) 등이 있음
    - 세계 IPv4주소는 ICANN에서 관리하고 한국의 IPv4주소는 KISA에서 관리
    - A class대역(최상위 1Btye 이용) -> 3Byte(2^24)개의 IP를 가질 수 있음
    - B class대역(최상위 2Byte 이용) -> 2Byte(2^16)개의 IP를 가질 수 있음
    - C class대역(최상위 3Byte 이용) -> 1Btye(2^8)개의 IP를 가질 수 있음


- 내부IP vs 외부IP, 사설IP vs 공인IP
    - 전체 IP는 공인IP(= 외부IP)와 사설IP(= 내부IP)로 나뉜다
    - 공인 IP: 실제 IP주소이며 unique 함
    - 사설 IP: 특수목적을 위해 배정된 IP들이며(192.168.0.0 등) 사용자가 임의로 지정할 수 있지만 사설 IP간에는 네트워크상에서 연결되지 않음
    - 보통 하나의 Router가 공인IP를 배정받고, 그 안에 연결된 기기들은 사설IP를 배정 받는다
    - 예를들어 공유기의 IP주소를 111.111.111.111 이라고 할 때, 공유기에 연결된 컴퓨터 C1, C2, C3는 각각 192.168.0.2 ~ 192.168.0.4 등의 IP를 받으며 이 IP주소는 사설 IP주소이다. 즉 외부에서 192.168.0.2라는 IP주소를 입력하여 접근할 때 C1에 접근할 수 없다(사설 IP간에는 네트워크상에서 연결되지 않으므로). 마치 111.111.111.111을 중심으로 자체 네트워크를 형성하는 것으로 볼 수 있다. 이때 이 네트워크 안에서 35.123.123.123(예를들어 google.com의 IP주소) 이라는 공인IP를 C4에 마음대로 설정을 하면, C1~C3에서는 35.123.123.123이라는 IP로 C4에는 접속할 수 있지만 실제 35.123.123.123이라는 공인 IP를 가지고 있는 google.com에는 접속할 수 없다

- 고정IP vs 유동IP
    - 고정IP: 특정 기기에 고정 IP를 부여
    - 유동IP: 특정 IP를 기기에 부여하지 않고 선점한 기기에 부여
    - 만약 IP를 10개 가지고 있는데 기기가 20개라면, 고정 IP사용시, 10개의 기기만 IP를 얻고 나머지 10개의 기기는 IP를 얻지 못해 인터넷을 사용할 수 없다. 이때, 유동 IP를 사용하면 20개의 기기가 각각 10개의 IP중 남아있는 IP를 이용하여 인터넷에 접속할 수 있다.

- 참고
    - http://gotocloud.co.kr/?p=320

### VPN
- (주로 보안등의 목적을 위해) 인터넷 망을 이용하여 사설망의 효과를 내는 네트워크(사설망 같은 illusion을 줌)
- A와 B 사이에 사설망을 구축하고 싶은데, 가장 확실하고 안전한 방법은 직접 cable을 연결하는 것이지만 이는 매우 비싸므로 인터넷 망을 이용하여 사설망과 같은 효과를 내기위해 사용한다. 이를 위해 A와 B 사이에 VPN 터널을 만드는 방법을 이용할 수 있다.
- VPN 터널링 프로토콜은 대표적으로 PPTP, L2TP 등이 있으며 PPTP는 windows, Android 등에서 기본으로 제공한다.
- 참고: http://gotocloud.co.kr/?p=1280

### NAT vs PAT
- NAT(Network Address Translation)는 Network Address, 즉 IP address를 바꾸는 기술을 말한다. 특히 내부 IP를 외부 IP로 바꿔주는 역할을 하는데 이로써 외부에서 사용하는 IP와 내부에서 사용하는 IP를 분리할 수 있다.

- PAT(Port Address Translation)는 NAT의 extension으로 port mapping을 통해 내부 IP와 외부IP를 mapping한다. 특히 하나의 (외부IP, port)에 여러개의 (내부IP, port)를 mapping하므로 global ip address를 늘리는 효과가 있다.


### 객체지향 프로그래밍(Opject Oriented Programming)
- 절차지향 프로그래밍(procedural programming)
    - 프로그램의 흐름과 순서를 먼저 정하고 그에 필요한 함수나 자료구조 등을 정하여 프로그래밍 하는 방식
    - procedure(함수, 메소드 등)를 이용한 프로그래밍
    - ex) C언어에서의 프로그래밍
- 객체지향 프로그래밍
    - 절차지향 프로그래밍과 반대로 자료구조와 해당 자료구조에 필요한 모듈을 먼저 정하고 그 후 프로그램의 흐름과 순서를 정하여 프로그래밍 하는 방식
    - 프로그램을 객체들의 모임으로 보고 각 객체들은 데이터를 주고 받고 처리할 수 있다고 보는 방식
    - 자료구조는 함수와 묶여서 하나의 객체로 사용됨, 주로 class 형태로 구성
    - ex) JAVA에서 class를 이용한 프로그래밍

- OOP의 4대 기본 원칙
    - Abstraction(추상화): 사물의 구체적인 공통적인 특성을 뽑아내서 이를 하나의 개념으로 다룸, **어떤 영역에서 필요한 속성이나 행동을 추출함**, ex) 자동차는 사람을 태운다 / 차가 이동한다 / 사람을 내린다 등의 행동으로 추상화 가능
    - Encapsulation(캡슐화)
        - 데이터와 메소드를 한개의 유닛에서 처리, ex) class 등
        - 내부 구현을 외부에서 알지 못하도록 hiding함, 주로 method call을 통해서 내부 state를 바꿈, 사용자는 내부 구현에 대해서 몰라도 method를 통해 내부 state를 바꿀 수 있으며 이로써 프로그래밍 복잡도가 감소함
    - Inheritance(상속): 객체간의 관계를 구축하는 방법의 하나로써 하나의 객체가 다른 하나의 객체를 포함하는 관계를 구성하며 포함 하는 객체를 자식객체, 포함 당하는 객체를 부모 객체라고 한다. 즉 자식객체는 부모객체를 포함하며 나아가 (extends) 다른 더 세부적인 특성을 갖는다.
    - Polymorphism(다형성): In computer science, it describes the concept that objects of different types can be accessed through the same interface.(서로 다른 type이 똑같은 interface를 통해서 접근할 수 있는 개념)
        - overloading: 똑같은 function name을 갖지만 parameter의 갯수나 type이 달라서 서로 다른 함수가 call되는 것
        - overriding: 부모 class를 상속한 자식 class에서 부모 class내의 함수와 똑같은 이름의 함수를 재정의 하는 것

- OOP의 5대 설계 원칙(SOLID)
    - SRP(Single Responsibility Principle): **THERE SHOULD NEVER BE MORE THAN ONE REASON FOR A CLASS TO CHANGE.** 클래스는 하나의 책임만 가져야하며 클래스가 변경된다면 그 이유는 가지고 있는 하나의 책임에 대한 변경 때문이어야 한다. 즉 시스템에 변경사항이 생길 경우 해당 변경사항에 대한 책임을 갖는 최소한의 내용만 변경할 수 있도록 해줌, class를 최대한 겹치는 기능이 없도록 분리해야함

    - OCP(Open-Closed Principle): **YOU SHOULD BE ABLE TO EXTEND A CLASSES BEHAVIOR, WITHOUT MODIFYING IT.** 어떤 기능을 확장하려고 할 때 기존의 코드를 수정하지 않고 확장할 수 있어야 한다. 이를 위해 변경 및 확장될 것과 그렇지 않은 것을 명확히 구분할 수 있어야 한다. 변하는 것은 쉽게 변할 수 있도록 설계하고 변하지 않는 것은 변하는 것이 생길 때에도 변하지 않도록 설계해야 한다. **OOP의 가장 중요한 Design 원칙**

    - LSP(Liskov Substitution Principle): **FUNCTIONS THAT USE POINTERS OR REFERENCES TO BASE CLASSES MUST BE ABLE TO USE OBJECTS OF DERIVED CLASSES WITHOUT KNOWING IT.** 자식 클래스와 부모 클래스 사이에 일관성이 있어야 한다. 즉 부모 클래스의 인스턴스 대신에 자식 클래스의 인스턴스를 사용해도 프로그램이 변화되지 않아야 한다, 자식 클래스는 최소한 부모 클래스의 모든 행위를 수행할 수 있어야 한다. 이를 위해서는 자식 클래스에서 부모 클래스의 메소드를 재정의 하지 않아야 한다. 즉 **자식 클래스는 부모 클래스의 책임을 무시하거나 재정의하지 않고 확장만 수행한다.**
        - 2개의 객체에 대하여
            - 똑같은 일을 수행함 => 하나의 클래스로 만들고 둘을 구분할 수 있는 field 이용
            - 똑같진 않지만 비슷한 일을 수행함 => 하나의 interface를 만들고 interface를 구현
            - 비슷한 점이 전혀 없음 => 서로 다른 2개의 class 구성
            - 2개의 객체가 하는 일에 세밀한 추가 구현을 한다면(superset-subset 관계) => class 상속

    - ISP(Interface Segregation Principle): **CLIENTS SHOULD NOT BE FORCED TO DEPEND UPON INTERFACES THAT THEY DO NOT USE.** 클라이언트는 자신이 사용하지 않는 인터페이스의 변화에 의해 영향을 받으면 안된다. 즉 클라이언트 별로 필요한 인터페이스만 사용할 수 있게 분리할 수 있어야 한다. 예를들어 복합기가 있는데 이 복사기는 copy, fax, print의 기능을 할 수 있다고 할 때 print의 기능 변화로 인해 copy가 영향을 받으면 안된다. 이를 위해 복합기는 copy, fax, print의 각 기능마다 따로 인터페이스를 두면 해당 인터페이스만을 상속하여 각 기능이 서로 영향받지 않도록 할 수 있다. 또한 여러 기능을 하는 하나의 class(복합기 class)를 이용할 경우 class가 너무 방대해지며 이는 SRP(Single Responsibility Principle)에도 위배된다.

    - DIP(Dependency Inversion): **A: HIGH LEVEL MODULES SHOULD NOT DEPEND UPON LOW LEVEL MODULES. BOTH SHOULD DEPEND UPON ABSTRACTIONS. B: ABSTRACTIONS SHOULD NOT DEPEND UPON DETAILS. DETAILS SHOULD DEPEND UPON ABSTRACTIONS.** 상위레벨 모듈은 하위레벨 모듈에 의존해서는 안되고 모든 것은 abstraction에 의존해야 한다. 즉 상대적으로 변화가 적은 것에 의존해야하며 이는 추상클래스, 인터페이스 등으로 표현할 수 있다.


### RESTful API
- REST의 기본 원칙을 지키는 것을 RESTful 하다고 함
- REST의 기본 원칙 6가지
    - Uniform interface: URI를 통해 자원의 위치를 표현하고 http method를 통해 행동을 정의하는 등 같은 interface를 사용
    - Stateless: state를 저장하지 않음으로써 구현이 단순함
    - Cache: http 표준을 준수함으로써 caching 사용 가능
    - Client-Server: 서버는 api를 통해 요청에 대한 처리를 하고 session 등은 client에서 관리(server와 client의 분리)
    - Layerd System: client는 server에 직접 연결되어 있는지 중간에 다른 server가 있는지 알 지 못한다. 중간 server에서 로드밸런싱 등을 통해 성능 향상이 가능하다.
- 가장 중요한 특성을 한마디로 표현하면 **URI를 통해 자원의 위치를 나타내고 http method를 통해 자원에 대한 행동을 표현한다.**

### 정규 표현식
- meta 문자를 이용하여 문자열에 대한 pattern을 다룰 수 있게 해주는 식
- https://www.tuwlab.com/ece/25809 튜토리얼
- http://zvon.org/comp/r/tut-Regexp.html 튜토리얼
- https://regexper.com/ 도식화

### python range vs xrange
- http://bluese05.tistory.com/57 참고
- range()의 return type은 list, xrange()의 return type은 xrange
    - range()의 경우 list의 내장함수를 사용할 수 있지만 큰 범위에 대해서 memory를 크게 씀
    - xrange()의 경우 list의 내장함수를 사용할 수 없지만 큰 범위에 대해서도 항상 일정 memory를 사용(generator와 비슷하게 동작)
    - 결론: 단순히 for문을 돌릴 용도라면 xrange가 메모리 측면에서 효율적이다