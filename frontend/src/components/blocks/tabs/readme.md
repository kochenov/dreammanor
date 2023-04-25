# Оформление страницы стандарт

## Страница с заголовком (стандарт)

```
<template>
  <q-page class="">
    <tabs-conteiner
      :component_lists="component_lists" // список компонентов (один по умолчанию)
      :current_component="current_component" // Имя текущего компанента (у нас имя единственного)
      :nav_route="false" // Указывает на отключение навигации по ссылкам внутри компонента
      >

      // Содержимое страницы

    </tabs-conteiner>
  </q-page>
</template>

<script setup>
import { ref } from "vue";
import TabsConteiner from "src/components/blocks/tabs/TabsConteiner.vue";

const current_component = ref("formFind"); // Текущий компонент
const component_lists = [
  {
    name_component: "formFind", // Имя файла компонента
    title: "Поиск дома но номеру", // Заголовок текущего компонента
    sub_title: "Поиск по номеру объяета",
    text_btn: "", // Имя вкладки
    flag: "box-news",
    to: "/desk/realEstate/formFind",
  },
];
</script>
```

## Страница с вкладками, каждая вкладка новая страница (Роуты)

```

<template>
  <q-page class="">
    <tabs-conteiner
      tabs // Табы включены
      :component_lists="component_lists" // список компанентов (столько будет вкладок)
      :current_component="current_component"
      :nav_route="true" // Навигация по роутам включена
      @setCurrentComponent="
        (c) => {
          current_component = c;
        }
      "
    >
     // динамический доступ к компанентам
      <component :is="tabs[current_component]"></component>
    </tabs-conteiner>
  </q-page>
</template>

<script setup>
import { ref } from "vue";
import TabsConteiner from "../components/blocks/tabs/TabsConteiner.vue";
import Toms from "src/components/test1Component.vue";
import News from "src/components/test2Component.vue";
import Popular from "src/components/test3Component.vue";
const tabs = {
  Toms,
  News,
  Popular,
};
const current_component = ref("Toms");
const component_lists = [
  {
    name_component: "Toms", // Имя файла компонента
    title: "Заголовок страницы", // Заголовок текущего компонента
    sub_title: "Подзаголовок",
    text_btn: "Расчёт", // Имя вкладки
    flag: "box-news",
    to: "/desk/realEstate/toms",
  },
  {
    name_component: "News", // Имя файла компонента
    title: "Новости", // Заголовок текущего компонента
    text_btn: "Новость", // Имя вкладки
    flag: "box-news",
    to: "/desk/realEstate/news",
  },
  {
    name_component: "Popular", // Имя файла компонента
    title: "Популярное", // Заголовок текущего компонента
    text_btn: "Популярное", // Имя вкладки
    flag: "box-news",
    to: "/desk/realEstate/popular",
  },
];
</script>

```
