# Сервис YamDB
![yatube](https://github.com/1kovalevskiy/yamdb/actions/workflows/main.yml/badge.svg)
![coverage](https://github.com/1kovalevskiy/yamdb/blob/master/coverage.svg)

## Учебный сервис "YamDB" 
Проект YaMDb собирает отзывы пользователей на произведения.

Произведения делятся на категории: «Книги», «Фильмы», «Музыка».
Сами произведения в YaMDb не хранятся, здесь нельзя посмотреть фильм или послушать музыку.
В каждой категории есть произведения: книги, фильмы или музыка. Например, в категории «Книги» могут быть произведения «Винни-Пух и все-все-все» и «Марсианские хроники», а в категории «Музыка» — песня «Давеча» группы «Насекомые» и вторая сюита Баха.
Произведению может быть присвоен жанр из списка предустановленных
Благодарные или возмущённые пользователи оставляют к произведениям текстовые отзывы и ставят произведению оценку в диапазоне от одного до десяти.
Из пользовательских оценок формируется усреднённая оценка произведения — рейтинг.
На одно произведение пользователь может оставить только один отзыв.


## Deploy
В корневой папке 
- Создать файл `.env` по примеру файла `.env.sample`
- Запустить `docker-compose up -d`

## Тестовый сервер
[Тестовый сервер (не работает)](http://yamdb.kovalevskiy.xyz)http://yamdb.kovalevskiy.xyz

## Технологии
- API на "Django + DRF"
- Тестирование на "Pytest"
- БД PostgreSQL
- Proxy Nginx
- Контейнеризация с помощью Docker
