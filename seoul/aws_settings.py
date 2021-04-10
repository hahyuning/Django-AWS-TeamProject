DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',	# DB 엔진
        'NAME': 'bigseoul',	# DB 이름
        'USER': 'root',	# 사용자 이름
        'PASSWORD': '1q2w3e4r!',	# 사용자 비밀번호
        'HOST': 'bigseoul.ctggx67idgh2.ap-northeast-2.rds.amazonaws.com',	# 인스턴스 주소(IP), RDS에서의 엔드포인트
        'PORT': '3306',	# 포트번호
    }
}