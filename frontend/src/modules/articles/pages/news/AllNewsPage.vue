<template>
  <q-page class="">
    <tabs-conteiner
      tabs
      :component_lists="component_lists"
      :current_component="current_component"
      :nav_route="false"
      @setCurrentComponent="
        (c) => {
          current_component = c;
        }
      "
    >
      <div v-if="current_component == 'ListPosts'">
        <PostList v-if="articlesStore.news" />
      </div>
      <div v-if="current_component == 'PopularPosts'">
        <PostList v-if="articlesStore.news" :popular="1" />
      </div>
      <div v-if="current_component == 'CategoriesList'">
        <CategoryList />
      </div>
    </tabs-conteiner>
  </q-page>
</template>

<script setup>
import { ref, onMounted, watch } from "vue";
import TabsConteiner from "src/components/blocks/tabs/TabsConteiner.vue";
import PostList from "../../components/news/PostsComponent.vue";
//import { useArticlesStore } from "src/stores/all";
import CategoryList from "../../components/news/CategoriesComponent.vue";
import { setBreadscrumbs, setMetaTitle } from "src/services/Service";

const articlesStore = useArticlesStore();
const current_component = ref("ListPosts");
const component_lists = [
  {
    name_component: "ListPosts", // Имя файла компонента
    title: "Новости", // Заголовок текущего компонента
    sub_title: "Новости из всех категорий в одном месте",
    text_btn: "Последние", // Имя вкладки
    flag: "box-news",
    to: "/news/all-news",
  },
  {
    name_component: "PopularPosts", // Имя файла компонента
    title: "Популярные новости", // Заголовок текущего компонента
    sub_title: "Рейтинг самых популярных новостей",
    text_btn: "Популярные", // Имя вкладки
    flag: "box-news",
    to: "/news/all-news",
  },
  {
    name_component: "CategoriesList", // Имя файла компонента
    title: "Категории новостей", // Заголовок текущего компонента
    sub_title: "Список всех новостных категорий",
    text_btn: "Категории", // Имя вкладки
    flag: "box-news",
    to: "/news/all-news",
  },
];

onMounted(async () => {
  setMetaTitle("Последние новости из всех категорий в одном месте");
  await articlesStore.getAllNews();
  updateBreadscrumbs("Последние новости");
});

watch(current_component, () => {
  if (current_component.value == "ListPosts") {
    setMetaTitle("Последние новости из всех категорий в одном месте");
    updateBreadscrumbs("Последние новости");
  }
  if (current_component.value == "PopularPosts") {
    setMetaTitle("Самые популярные новости");
    updateBreadscrumbs("Популярные новости");
  }
  if (current_component.value == "CategoriesList") {
    setMetaTitle("Список всех категорий новостей");
    updateBreadscrumbs("Список кaтегорий новостей");
  }
});
const updateBreadscrumbs = (title) => {
  setBreadscrumbs(
    [
      {
        path: "/news",
        meta: { title: "Новости" },
      },
    ],
    title,
    true
  );
};
</script>

<style lang="scss" scoped>
.my-card {
  width: 100%;
  max-width: 250px;
}
</style>
