# Django Todo List

Django + MySQL 기반 Todo List 웹 애플리케이션입니다.

## 기능
- Todo 등록 / 목록 / 수정 / 삭제 (CRUD)
- 체크박스로 완료 여부(is_completed) 토글
- 완료된 항목은 취소선과 초록 배경으로 표시
- 등록·수정 시 유효성 검사 및 에러 메시지 출력
- Admin 페이지에서 Todo 관리

## 모델 (Todo)
| 필드 | 타입 | 설명 |
|---|---|---|
| title | CharField(200) | 할 일 제목 (필수) |
| content | TextField | 세부 내용 (선택) |
| is_completed | BooleanField | 완료 여부 (기본값 False) |
| created_at | DateTimeField | 생성 일시 (자동 입력) |

## 실행 방법
```bash
# 1. 가상환경 및 패키지 설치
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt

# 2. MySQL에 DB 생성
mysql -u root -p -e "CREATE DATABASE todo_db DEFAULT CHARACTER SET utf8mb4;"

# 3. config/settings.py 의 DATABASES 비밀번호 수정 (또는 환경변수 DB_PASSWORD 설정)

# 4. 마이그레이션 & 관리자 계정 생성
python manage.py migrate
python manage.py createsuperuser

# 5. 서버 실행
python manage.py runserver
```
- 목록: http://127.0.0.1:8000/
- 관리자: http://127.0.0.1:8000/admin/

## DDL
`schema.sql` 참고.
