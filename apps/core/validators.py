from django.core.validators import RegexValidator


cyrillic = RegexValidator(r'[а-яА-ЯёЁіІїЇєЄґҐ]', 'Только символы кириллицы')

right_tel_num = r'[+][3][8][0][(]\d{2}[)]\d{3}([-]\d\d){2}'
tel_number = RegexValidator(right_tel_num,
                            'Телефон должен быть формата +380(ХХ)ХХХ-ХХ-ХХ')
