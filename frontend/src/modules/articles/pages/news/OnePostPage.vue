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
      <div v-if="current_component == 'FullPost'">
        <FullPost v-if="articlesStore.news" />
      </div>
      <div v-if="current_component == 'Comments'">
        <!--  <CommentsComponent v-if="articlesStore.comments" /> -->
      </div>
      <div v-if="current_component == 'Related'">
        <CategoryList />
      </div>
    </tabs-conteiner>
  </q-page>
</template>

<script setup>
import { ref, onMounted } from "vue";
import TabsConteiner from "src/components/blocks/tabs/TabsConteiner.vue";
//import { useArticlesStore } from "src/stores/all";
import CategoryList from "../../components/news/CategoriesComponent.vue";
import FullPost from "../../components/news/PostComponent.vue";
import { useRoute } from "vue-router";
import { setBreadscrumbs, setMetaTitle } from "src/services/Service";
import CommentsComponent from "../../components/CommentsComponent.vue";
const articlesStore = useArticlesStore();
const current_component = ref("FullPost");
const component_lists = ref([
  {
    name_component: "FullPost", // Имя файла компонента
    title: "Содержимое", // Заголовок текущего компонента
    //sub_title: "Новости из всех категорий в одном месте",
    text_btn: "Содержимое", // Имя вкладки
    flag: "box-news",
    to: "/news/all-news",
  },
  {
    name_component: "Comments", // Имя файла компонента
    title: "Коментарии", // Заголовок текущего компонента
    sub_title: "Обсуждение новости читателями",
    text_btn: "Коментарии", // Имя вкладки
    flag: "box-news",
    to: "/news/all-news",
  },
  {
    name_component: "Related", // Имя файла компонента
    title: "Похожие новости", // Заголовок текущего компонента
    sub_title: "Список всех новостных категорий",
    text_btn: "Похожие новости", // Имя вкладки
    flag: "box-news",
    to: "/news/all-news",
  },
]);
const route = useRoute();
onMounted(async () => {
  await articlesStore.getPost(route.params.cat, route.params.num);

  if (articlesStore.news) {
    setBreadscrumbs(
      [
        {
          meta: { title: articlesStore.news.category.name },
          path: "/news/category/" + articlesStore.news.category.id,
        },
      ],
      articlesStore.news.title
    );
    setMetaTitle(articlesStore.news.title);
  }

  component_lists.value[0].title = articlesStore.news.title;
  component_lists.value[0].sub_title = articlesStore.news.category.name;

  /* component_lists.value[1].title =
      component_lists.value[1].title + articlesStore.news[0].category.title;
    component_lists.value[1].sub_title =
      component_lists.value[1].sub_title + articlesStore.news[0].category.title; */
});
</script>

<style lang="scss" scoped>
.my-card {
  width: 100%;
  max-width: 250px;
}
</style>
