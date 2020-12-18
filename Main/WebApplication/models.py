from django.db import models
from django.db import models as m


class Occupation(models.Model):
    occ_name = m.CharField(max_length=50, verbose_name="Назва посади", null=False)
    occ_salary = m.PositiveIntegerField(default=1, verbose_name="Зарплата", null=True )
    occ_responsibilities = m.CharField(max_length=255, verbose_name="Обов'язки", null=True)
    occ_requirements = m.CharField(max_length=255, verbose_name="Вимоги", null=True)

    def __str__(self):
        return self.occ_name


class Employees(models.Model):
    employee_name = m.CharField(max_length=50, verbose_name="Ім'я", null=False)
    employee_surname = models.CharField(max_length=50, verbose_name="Прізвище", null=False)
    employee_age = models.PositiveIntegerField(default=1, verbose_name="Вік", null=True)
    employee_address = models.CharField(max_length=1024, verbose_name="Адреса", null=True)
    employee_telephone = models.CharField(max_length=13, verbose_name="Номер телефону", null=True)
    employee_passport_data = models.CharField(max_length=9, verbose_name="Паспортні дані", null=False)

    def __str__(self):
        return self.employee_name


class Genres(models.Model):
    genre_name = m.CharField(max_length=50, verbose_name="Назва жанру", null=False)
    genre_description = m.TextField(default="Опис жанру відсутній.",verbose_name="Опис жанру", null=True)
    genre_slug = m.SlugField(unique=True)

    def __str__(self):
        return self.genre_name


class MovieUnit(models.Model):
    movie_name = m.CharField(max_length=80, verbose_name="Назва фільму", null=False)
    movie_duration = m.PositiveIntegerField(default=1, verbose_name="Тривалість фільму(у хвилинах)", null=True)
    movie_producer = m.TextField(verbose_name="Продюсер", null=False)
    movie_country = m.CharField(max_length=80, verbose_name="Країна фільму", null=True)
    movie_age_restrictions = m.PositiveIntegerField(default=1, verbose_name="Вікові обмеження", null=True)
    movie_actors = m.TextField(verbose_name="Актори", null=True)
    movie_description = m.TextField(default="Опис фільму відсутній.",verbose_name="Опис", null=True)
    movie_thumbnail = m.ImageField(verbose_name="Постер фільму")
    movie_slug = m.SlugField(unique=True)

    def __str__(self):
        return self.movie_name


class Session(models.Model):
    session_date = m.DateTimeField(verbose_name="Дата", null=False)
    session_price = m.PositiveIntegerField(default=1, verbose_name="Ціна квитка", null=False)
    session_movie = m.ForeignKey(MovieUnit, on_delete=models.CASCADE, verbose_name="Код Фільму", null=False)
    session_slug = m.SlugField(unique=True)


class Seats(models.Model):

    seat_number = m.PositiveIntegerField(default=1, verbose_name="Номер місця", null=False)


class Workers(models.Model):
    worker_info = m.ForeignKey(Employees, verbose_name="Код працівника", on_delete=models.CASCADE)
    worker_Occupation = models.ForeignKey(Occupation, on_delete=models.CASCADE, verbose_name="Код посади", null=True)


class Movies(models.Model):
    movie_info = m.ForeignKey(MovieUnit, on_delete=models.CASCADE, verbose_name="Код Фільму", null=False)
    movie_genre = m.ForeignKey(Genres, on_delete=models.CASCADE, verbose_name="Код Жанру", null=False)


class Ticket(models.Model):
    ticket_session = m.ForeignKey(Session, on_delete=models.CASCADE, verbose_name="Код Сеансу", null=False)
    ticket_worker = m.ForeignKey(Workers, verbose_name="Код працівника", on_delete=models.CASCADE)
    ticket_seat = m.ForeignKey(Seats, verbose_name="Код Місця", on_delete=models.CASCADE)

