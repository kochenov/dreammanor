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
        <CategoryList v-if="articlesStore.news" @type="switchCat()" />
      </div>
    </tabs-conteiner>
  </q-page>
</template>

<script setup>
import { ref, onMounted, watch, onUpdated } from "vue";
import TabsConteiner from "src/components/blocks/tabs/TabsConteiner.vue";
import PostList from "../../components/news/PostsComponent.vue";
import { useRoute, useRouter } from "vue-router";
//import { useArticlesStore } from "src/stores/all";
import CategoryList from "../../components/news/CategoriesComponent.vue";
import { setBreadscrumbs, setMetaTitle } from "src/services/Service";

const articlesStore = useArticlesStore();
const route = useRoute();
const router = useRouter();

const current_component = ref("ListPosts");
const component_lists = ref([
  {
    name_component: "ListPosts", // Имя файла компонента
    title: "Новости из категории ", // Заголовок текущего компонента
    sub_title: "Список всех новостей из категории ",
    text_btn: "Последние", // Имя вкладки
    flag: "box-news",
    to: "/news/all-news",
  },
  {
    name_component: "PopularPosts", // Имя файла компонента
    title: "Популярное в категории: ", // Заголовок текущего компонента
    sub_title: "Рейтинг самых популярных новостей в категории: ",
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
]);

const switchCat = async () => {
  await articlesStore.loadInfoCategory(route.params.cat);
  current_component.value = "ListPosts";
};

onMounted(async () => {
  await articlesStore.getAllNews(route.params.cat);
  //await articlesStore.loadInfoCategory(route.params.cat);
  component_lists.value[0].title += `[${articlesStore.cur_cat_news.name}]`;
  component_lists.value[0].sub_title += `${articlesStore.cur_cat_news.name}`;
  component_lists.value[1].title += `[${articlesStore.cur_cat_news.name}]`;
  component_lists.value[1].sub_title += `${articlesStore.cur_cat_news.name}`;

  if (articlesStore.news) {
    if (articlesStore.cur_cat_news) {
      updateBreadscrumbs(
        "Список всех новостей в категории: " + articlesStore.cur_cat_news.name
      );
    }
  }
});
onUpdated(async () => {
  await articlesStore.getAllNews(route.params.cat);
});

watch(current_component, async () => {
  if (current_component.value == "ListPosts") {
    // setMetaTitle("Последние новости из всех категорий в одном месте");
    await articlesStore.getAllNews(route.params.cat);
    updateBreadscrumbs(
      "Последние новости в категории " + articlesStore.cur_cat_news.name
    );
  }
  if (current_component.value == "PopularPosts") {
    await articlesStore.getAllNews(route.params.cat);
    setMetaTitle(
      "Самые популярные новости в категории " + articlesStore.cur_cat_news.name
    );
    updateBreadscrumbs(
      "Популярные новости в категории " + articlesStore.cur_cat_news.name
    );
  }
  if (current_component.value == "CategoriesList") {
    // setMetaTitle("Список всех категорий новостей");
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

<style lang="scss" scoped></style>
