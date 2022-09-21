배포 준비

1. uvicorn host 0.0.0.0으로 변경, reload=False, port=80
2. main.py jinja2에서 파일 경로 str 타입으로 변경
3. requirements.txt 패키지 체크 (aiohttp 누락되어 있는거 추가)
4. github에 코드 올리기

https://github.com/settings/tokens/new 토큰 발급

토큰 복사 해두기 

VPS : 가상 사설 서버 구축

1. AWS Lightsail 사용
2. 인스턴스 생성
3. ssh를 사용하여 연결 (브라우저에서 접속)
4. sudo apt-get update
5. sudo apt-get -y upgrade
6. sudo apt-get install build-essential
7. sudo apt-get install curl git vim python3 python3-pip
8. touch .gitconfig
9. git config --global user.name amamov
10. git config --global user.email amamov@kakao.com
11. git config --global --list
12. git clone <프로젝트>
13. cd <프로젝트>
14. vi secrets.json
15. sudo pip install -r requirements.txt
16. sudo python3 server.py
17. ip 접속
<br>
배포 성공!!
