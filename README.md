#### PYENV
```
1. pyenv 설치 & 업그레이드 & 삭제
# 설치
$ brew update && brew upgrade pyenv
$ brew install 
```

```
2. 환경설정
~/.zshrc에 추가 및 적용을 한다.

$ echo -e '\nif command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.zshrc
결과적으로 아래 코드가 추가된다.

if command -v pyenv 1>/dev/null 2>&1; then
eval "$(pyenv init -)"
fi
아래 명령어로 설정코드 적용

$ source ~/.zshrc
```

```
3. 필요한 Version 설치
# 설치 가능한 Python 버전 리스트 확인
$ pyenv install --list
$ pyenv install --l
```

```
4. 필요한 버전 설치
$ pyenv install 3.8.12
```

```
5. Version 설정   
# 버전 전역으로 설정
$ pyenv global 3.8.12

# 현재 프로젝트만 적용
$ pyenv local 3.8.12
```

#### ENV 설정
```
$ virtualenv venv --python=python3.8.12
$ source venv/bin/activate
$ pip install --upgrade pip

$ pip install -r ./requirements.txt
$ # pip freeze > requirements.txt
$ # pip freeze > requirements.txt.pytorch_bert
$ # pip freeze | xargs pip uninstall -y
$ # pip uninstall -r requirements.txt -y
```