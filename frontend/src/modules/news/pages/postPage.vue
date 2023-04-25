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
      <div v-if="current_component == 'show'">
        <FullPost :post="post" v-if="post" />
      </div>
      <div v-if="current_component == 'comments'">
        <!--  <CommentsComponent v-if="articlesStore.comments" /> -->
      </div>
      <div v-if="current_component == 'related'">
        <!-- <CategoryList /> -->
      </div>
    </tabs-conteiner>
  </q-page>
</template>

<script setup>
import { ref, onMounted, onActivated } from "vue";
import TabsConteiner from "src/components/blocks/tabs/TabsConteiner.vue";
//import CategoryList from "../components/CategoriesComponent.vue";
import FullPost from "../components/PostComponent.vue";
import { useRoute } from "vue-router";
import { useNewsStore } from "../store";

import { setBreadscrumbs, setMetaTitle } from "src/services/Service";
import { useMeta } from "quasar";

const newsStore = useNewsStore();
const current_component = ref("show");
const meta_title = ref("");
const component_lists = ref([
  {
    name_component: "show", // Имя файла компонента
    title: "Содержимое", // Заголовок текущего компонента
    //sub_title: "Новости из всех категорий в одном месте",
    text_btn: "Содержимое", // Имя вкладки
    flag: "box-news",
    to: "/news/all-news",
  },
  {
    name_component: "comments", // Имя файла компонента
    title: "Коментарии", // Заголовок текущего компонента
    sub_title: "Обсуждение новости читателями",
    text_btn: "Коментарии", // Имя вкладки
    flag: "box-news",
    to: "/news/all-news",
  },
  {
    name_component: "related", // Имя файла компонента
    title: "Похожие новости", // Заголовок текущего компонента
    sub_title: "Список всех новостных категорий",
    text_btn: "Похожие новости", // Имя вкладки
    flag: "box-news",
    to: "/news/all-news",
  },
]);
const route = useRoute();
const post = ref(null);
onMounted(async () => {
  await newsStore.getPost(route.params.category_id, route.params.post_id);
  if (newsStore.posts) {
    post.value = newsStore.posts;
    load();
    //setMetaTitle(post.value.title);
    meta_title.value = post.value.title;
  }
});

onActivated(async () => {
  console.log("activate");
  await newsStore.getPost(route.params.category_id, route.params.post_id);
  if (newsStore.posts) {
    post.value = newsStore.posts;
  }
});
const updateBreadscrumbs = (title) => {
  setBreadscrumbs(
    [
      {
        path: "/news",
        meta: { title: "Новости" },
      },
      {
        meta: { title: post.value.category.name },
        path: "/news/category/" + post.value.category.id + "/all-posts",
      },
    ],
    title,
    true
  );
};
const load = () => {
  if (post.value) {
    updateBreadscrumbs(post.value.title);

    component_lists.value[0].title = post.value.title;
    component_lists.value[0].sub_title = post.value.category.name;
  }
};

useMeta(() => {
  return {
    title: meta_title.value + " : Усадьба Мечты",
  };
});
</script>

<style lang="scss" scoped>
.my-card {
  width: 100%;
  max-width: 250px;
}
</style>
