from django.db import models
from ckeditor.fields import RichTextField
from phonenumber_field.modelfields import PhoneNumberField
from django_jalali.db import models as jmodels



# Create your models here



class Articles(models.Model):
    total_ep = models.PositiveIntegerField(verbose_name="آمار کل مقالات انگلیسی و فارسی")
    number_e = models.PositiveIntegerField(verbose_name="مقالات انگلیسی")
    number_p = models.PositiveIntegerField(verbose_name="مقالات فارسی")
    total_tpm = models.PositiveIntegerField(verbose_name="آمار کل طرح پژوهشی مصوب دانشگاه پایان یافته")
    number_mojri = models.PositiveIntegerField(verbose_name="به عنوان مجری")
    number_hamkar = models.PositiveIntegerField(verbose_name="به عنوان همکار")
    total_gs = models.PositiveIntegerField(verbose_name="آمار گوگل اسکولار")
    number_refgs = models.PositiveIntegerField(verbose_name="تعداد ارجاع به مقاله")
    number_gs_hindex = models.PositiveIntegerField(verbose_name="H-index")
    total_ISI = models.PositiveIntegerField(verbose_name="آمار مقالات ISI")
    number_ISIacc = models.PositiveIntegerField(verbose_name="تعداد مقاله پذیرفته شده")
    number_ISIprinted = models.PositiveIntegerField(verbose_name="تعداد مقاله منتشر شده")
    total_Scopus = models.PositiveIntegerField(verbose_name="آمار مقالات Scopus")
    number_Scopus = models.PositiveIntegerField(verbose_name="تعداد مقالات منتشر شده")
    number_Sc_hindex = models.PositiveIntegerField(verbose_name="H-index")
    total_Orcid = models.PositiveIntegerField(verbose_name="آمار مقالات Orcid")

    def __str__(self):
        return ("آمار مقالات")

    class Meta:
        verbose_name = "آمار مقالات "
        verbose_name_plural = "آمار مقالات "


class Books(models.Model):
    image = models.ImageField(upload_to="BookImages", verbose_name="عکس کتاب")
    header = models.CharField(max_length=100, verbose_name="عنوان کتاب")
    slug = models.SlugField(max_length=150, unique=True, blank=True, null=True, verbose_name="نام آدرس بار")
    body = RichTextField(blank=True, null=True, verbose_name="متن اصلی")

    def __str__(self):
        return self.header

    class Meta:
        verbose_name = "کتاب های منتشر شده  "
        verbose_name_plural = "کتاب ها"


class Research(models.Model):
    image = models.ImageField(upload_to="ResearchImages", verbose_name="عکس مطلب")
    header = models.CharField(max_length=100, verbose_name="عنوان مطلب")
    slug = models.SlugField(max_length=150, unique=True, blank=True, null=True, verbose_name="نام آدرس بار")
    preview = models.CharField(max_length=200, verbose_name="پیش نمایش")
    body = RichTextField(blank=True, null=True, verbose_name="متن اصلی")



    def __str__(self):
        return self.header





    class Meta:
        verbose_name = "مطالب منتشر شده  "
        verbose_name_plural = "مطالب"


class Comment(models.Model):
    post = models.ForeignKey(Books, on_delete=models.CASCADE, verbose_name="مربوط به کتاب")
    name = models.CharField(max_length=50, verbose_name="نام")
    phone = PhoneNumberField(region='IR', verbose_name="موبایل")
    content = models.TextField(max_length=500, verbose_name="دیدگاه")
    timestamp = jmodels.jDateTimeField(auto_now_add=True)
    reply = models.ForeignKey('self', null=True, related_name='replies', on_delete=models.CASCADE)

    def __str__(self):
        return '{}-{}'.format(self.post.header, str(self.name))

    class Meta:
        verbose_name = "دیدگاه های منتشر شده  "
        verbose_name_plural = "دیدگاه های کتاب ها"


class Commenta(models.Model):
    post = models.ForeignKey(Research, on_delete=models.CASCADE, verbose_name="مربوط به مطالب")
    name = models.CharField(max_length=50, verbose_name="نام")
    phone = PhoneNumberField(region='IR', verbose_name="موبایل")
    content = models.TextField(max_length=500, verbose_name="دیدگاه")
    timestamp = jmodels.jDateTimeField(auto_now_add=True)
    reply = models.ForeignKey('self', null=True, related_name='replies', on_delete=models.CASCADE)

    def __str__(self):
        return '{}-{}'.format(self.post.header, str(self.name))

    class Meta:
        verbose_name = "دیدگاه های منتشر شده  "
        verbose_name_plural = "دیدگاه های مطالب"
