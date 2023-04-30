### Организация структуры URL модуля
---


`https://dreammanor.ru/<module>/<page>/<component>/<slug>`


```
module_mame - news
```
## Ноды
---

- `id` - уникальный номер ноды
- `url` - адрес
- `module` - название модуля
- `page` - название шаблона страницы
- `component` - название текущего компонента
- `slug` - id, alias, short_name
- `title` - Заголовок Node
- `description`- мета описание страницы
- `keywords` - мета ключевые слова
- `robots` - доступ к индексации
- `canonical_full_url` - полный адрес к страницы для ПСЯ
- `user_role_id` - null - публичный, если есть id (Только для этой роли)
- `user_auth` - false для всех, true - только для авторизированных
- `name_menu` - короткое название для меню
- `icon` - иконка, которая отображает смысл содержимого (для меню)


### Меню

- id
- url
- name
- icon
- parent_id
- priority
- role_id
  - null - гость (доступно всем)
  - 1 - пользователь ( 1 <= 1)
  - 2 - публицист ( 1 <= 2)
  - 3 - менеджер ( 1 <= 3)
  - 4 - админ ( 1 <= 4)
  - 5 - супер админ
- status
#### Страницы
---
- postPage.vue
- postsPage.vue


- Список всех новостей в порядке убывания даты `postsPage.vue`
  - все новости `/<module=news>/<page=posts>/<component=last>/<slug=slug_default=null>`
  - по категориям `/<module=news>/<page=posts>/<component=category>/<slug=name_category>`
  - по популярности `/<module=news>/<page=posts>/<component=popular>/<slug=slug_default=null>`
  - список категорий `/<module=news>/<page=posts>/<component=categoryes>/<slug=null>`
- Текст полной новости  `postPage.vue`
  - `/<module=news>/<page=post>/<component=cat_name>/<slug=post_id>`
