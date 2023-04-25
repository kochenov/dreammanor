<template>
  <tabs-conteiner
    :key="newsStore.count_news"
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
    <div
      v-if="
        current_component == 'all-posts' || current_component == 'popular-posts'
      "
    >
      <PostsComponent :posts="posts" :load="newsStore.loading" />
    </div>
    <div v-if="current_component == 'news-categories'">
      <CategoryList />
    </div>

    <div
      v-if="
        current_component == 'all-posts' || current_component == 'popular-posts'
      "
      class="q-mt-xl"
    >
      <div class="flex flex-center">
        <q-pagination
          v-if="Math.ceil(newsStore.count_news / newsStore.limit) >= 2"
          v-model="current_page"
          :max="Math.ceil(newsStore.count_news / newsStore.limit)"
          :max-pages="Math.ceil(newsStore.count_news / newsStore.limit)"
          boundary-numbers
          direction-links
          color="black"
          active-color="yellow"
          active-text-color="black"
        />
      </div>
    </div>
  </tabs-conteiner>
</template>

<script setup>
import { ref, onMounted, watch, onUpdated } from "vue";
import TabsConteiner from "src/components/blocks/tabs/TabsConteiner.vue";
import { useRoute } from "vue-router";
import PostsComponent from "../components/PostsComponent.vue";
import CategoryList from "../components/CategoriesComponent.vue";
import { setBreadscrumbs, setMetaTitle } from "src/services/Service";
import { useNewsStore } from "../store";
import { useMeta } from "quasar";

const current_component = ref("all-posts");
const component_lists = [
  {
    name_component: "all-posts", // Имя файла компонента
    title: "Последние новости", // Заголовок текущего компонента
    sub_title: "Свежие новости из всех категорий в одном месте",
    text_btn: "Последние", // Имя вкладки
    flag: "box-news",
    to: "/news/posts/all-posts",
  },
  {
    name_component: "popular-posts", // Имя файла компонента
    title: "Популярные новости", // Заголовок текущего компонента
    sub_title: "Рейтинг самых популярных новостей",
    text_btn: "Популярные", // Имя вкладки
    flag: "box-news",
    to: "/news/posts/popular-posts",
  },
  {
    name_component: "news-categories", // Имя файла компонента
    title: "Категории новостей", // Заголовок текущего компонента
    sub_title: "Список всех новостных категорий",
    text_btn: "Категории", // Имя вкладки
    flag: "box-news",
    to: "/news/posts/news-categories",
  },
];

const route = useRoute();
const newsStore = useNewsStore();

const posts = ref(null);
const count = ref(0);
const current_page = ref(1);
const meta_title = ref(null);
onMounted(async () => {
  await loadPosts();

  current_component.value = route.params.id_component;
  current_page.value = 1;
});
watch(route, async () => {
  await loadPosts();
  current_page.value = 1;
});

watch(current_page, async () => {
  await loadPosts(current_page);
});

onUpdated(() => {
  console.log("//", newsStore.count_news);
  loadPosts();
  posts.value = newsStore.posts;
});

/**
 * Функции
 */

const loadPosts = async (page = 0) => {
  if (route.params.id_component == "all-posts") {
    meta_title.value = "Самые свежие новости из всех категорий";
    let offset = 0;
    if (page != 0) {
      offset = newsStore.limit * (current_page.value - 1);
    }

    await newsStore.loadPosts(0, offset, 0);
  }
  if (route.params.id_component == "popular-posts") {
    meta_title.value = "Популярные новости из всех категорий";
    let offset = 0;
    if (page != 0) {
      offset = newsStore.limit * (current_page.value - 1);
    }
    await newsStore.loadPosts(0, offset, 1);
  }
  if (route.params.id_component == "news-categories") {
    meta_title.value = "Список категорий новостей";
    //await newsStore.loadPosts();
  }
  posts.value = newsStore.posts;
  count.value = newsStore.count_news;

  if (meta_title.value) {
    // setMetaTitle(meta_title.value);
    updateBreadscrumbs(meta_title.value);
  }
};

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
useMeta(() => {
  return {
    title: meta_title.value + " : Усадьба Мечты",
  };
});
</script>

<style lang="scss" scoped></style>
