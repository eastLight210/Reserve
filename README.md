# Reserve

서울대 풋살장 예약

* git clone 혹은 다운로드 이후 
"pip install -r requirements.txt"
를 이용해 필요한 패키지를 설치해주세요.  

* Account.txt, Member.txt로 계정 정보와 멤버를 작성하여 폴더에 넣어주세요

* 이후 날짜, 시간 등을 수정하여 사용하면 됩니다.

# Account.txt 예시  
myid  
mypasswd  

# Memeber.txt 예시  
이oo,2039-11111,010-1111-1111,공과대학 기계공학부  
김oo,2039-22222,010-2222-2222,공과대학 기계공학부  
박oo,2039-33333,010-3333-3333,공과대학 기계공학부

## 기존 크롬 브라우저에서 실행하기
스크립트가 매번 새로운 브라우저 창을 여는 것이 불편하다면, 크롬을
원격 디버깅 모드로 실행한 뒤 프로그램을 실행합니다. 크롬을 다음과 같이
실행하면 `reserve.py`가 현재 열린 브라우저에서 동작합니다.

```bash
chrome --remote-debugging-port=9222
```

macOS의 경우 예시는 다음과 같습니다.

```bash
/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222
```

이후 `python reserve.py`를 실행하면 새 창을 띄우지 않고 기존 브라우저에
연결하여 작업합니다.
