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