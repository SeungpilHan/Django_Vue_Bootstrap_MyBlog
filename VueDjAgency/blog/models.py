from django.db import models


class Post(models.Model):
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, blank=True, null=True) #1대1 관계이기 때문에 ForeignKey로 지정
    tags = models.ManyToManyField('Tag', blank=True)
    title = models.CharField('TITLE', max_length=50) #제목
    description = models.CharField('DESCRIPTION', max_length=100, blank=True, help_text='simple one-line text.') #한줄 요약설명
    image = models.ImageField('IMAGE', upload_to='blog/%Y/%m/', blank=True, null=True) #대표 이미지
    content = models.TextField('CONTENT') #포스트 글 내용
    create_dt = models.DateTimeField('CREATE DT', auto_now_add=True) #포스트 생성한 날짜와 시간
    update_dt = models.DateTimeField('UPDATE DT', auto_now=True) #포스트를 수정한 날짜와 시간
    like = models.PositiveSmallIntegerField('LIKE', default=0) #좋아요 개수를 포함한 내용

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.CharField('DESCRIPTION', max_length=100, blank=True, help_text='simple one-line text.')

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, blank=True, null=True)
    content = models.TextField('CONTENT')
    create_dt = models.DateTimeField('CREATE DT', auto_now_add=True)
    update_dt = models.DateTimeField('UPDATE DT', auto_now=True)

    #네임, 타이틀 컬럼이 없기때문에 코멘트 생성
    @property
    def short_content(self):
        return self.content[:10]

    def __str__(self):
        return self.short_content