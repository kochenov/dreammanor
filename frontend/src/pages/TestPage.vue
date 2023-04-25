<template>
  <q-page class="">
    <tabs-conteiner
      tabs
      :component_lists="component_lists"
      :current_component="current_component"
      :nav_route="true"
      @setCurrentComponent="
        (c) => {
          current_component = c;
        }
      "
    >
      {{ current_component }}

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
