from django.db import models


class Category(models.Model):
    class Meta:
        verbose_name = "Kategoriya"
        verbose_name_plural = "Kategoriyalar"


    name = models.CharField(max_length=255, verbose_name="Nomi")
    icon = models.ImageField(upload_to="images/", verbose_name="Rasmi")

    def __str__(self):
        return self.name



class SubCategory(models.Model):
    class Meta:
        verbose_name = "Kichik kategoriya"
        verbose_name_plural = "Kichik kategoriyalar"

    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name



class Product(models.Model):
    class Meta:
        verbose_name = "Mahsulot"
        verbose_name_plural = "Mahsulotlar"

    title = models.CharField(max_length=255)
    price = models.FloatField()
    description = models.TextField()
    rating = models.FloatField()
    image = models.ImageField(upload_to="images/")
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)


    # lekin bizda bazada avval bu maydonlar yoqlgi uchun xatolik beradi, shunga hozircha null=True qilib qoymamiz aslida bu qoshilmedi, mahsulotlar ochib ketmasligi uchunn shunaqa qilyapman

    created_at = models.DateTimeField(auto_now_add=True, null=True)
    # auto_now_add -> bu bazaga malumot kiritilgan paytni ozida saqledi

    updated_at = models.DateTimeField(auto_now=True, null=True)
    # auto_now -> bazada shu obyekt ustida bolgan ozgarishni sognisini sanasini vaqtini saqledi


    def __str__(self):
        return f"{self.title} - {self.price}"
    

    def get_rating_percent(self):
        return 100 * (self.rating / 5)

# aytgancha bizda updated_at degan maydon yo'q)))