### Организация структуры URL модуля
---


`https://dreammanor.ru/<module>/<page>/<component>/<slug>`


```
module_mame - news
```
#### Страницы
- Список всех новостей в порядке убывания даты `postsPage.vue`
  - все новости `/<module=news>/<page=posts>/<component=last>/<slug=slug_default=null>`
  - по категориям `/<module=news>/<page=posts>/<component=category>/<slug=name_category>`
  - по популярности `/<module=news>/<page=posts>/<component=popular>/<slug=slug_default=null>`
- Текст полной новости  `postPage.vue`
  - `/<module=news>/<page=post>/<component=cat_name>/<slug=post_id>`
