<template>
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

    <div v-if="posts" class="q-mt-xl">
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
import { ref, onUpdated, onMounted, watch } from "vue";
import TabsConteiner from "src/components/blocks/tabs/TabsConteiner.vue";
import { useRoute } from "vue-router";
import PostsComponent from "../components/PostsComponent.vue";
import CategoryList from "../components/CategoriesComponent.vue";
import { useNewsStore } from "../store";
import { setBreadscrumbs } from "src/services/Service";
import { useMeta } from "quasar";

const current_component = ref("all-posts");
const component_lists = ref([
  {
    name_component: "all-posts", // Имя файла компонента
    title: "Последние новости из категории ", // Заголовок текущего компонента
    sub_title: "Свежие новости из выбранной категории",
    text_btn: "Последние", // Имя вкладки
    flag: "box-news",
    to: "",
  },
  {
    name_component: "popular-posts", // Имя файла компонента
    title: "Популярные новости из категории", // Заголовок текущего компонента
    sub_title: "Рейтинг самых популярных новостей из категории",
    text_btn: "Популярные", // Имя вкладки
    flag: "box-news",
    to: "",
  },
  {
    name_component: "news-categories", // Имя файла компонента
    title: "Категории новостей", // Заголовок текущего компонента
    sub_title: "Список всех новостных категорий",
    text_btn: "Категории", // Имя вкладки
    flag: "box-news",
    to: "/news/posts/news-categories",
  },
]);

const route = useRoute();
const newsStore = useNewsStore();

const posts = ref(null);
const count = ref(0);
const current_page = ref(1);
const current_category = ref(0);
const meta_title = ref(null);

onMounted(async () => {
  current_component.value = route.params.id_component;
  current_category.value = route.params.category_id;
  if (route.params.category_id) {
    await loadPosts();
  }

  current_page.value = 1;
});
watch(route, async () => {
  if (route.params.category_id) {
    await loadPosts();
  }

  current_page.value = 1;
});

watch(current_page, async () => {
  if (route.params.category_id) {
    await loadPosts();
  }
});
onUpdated(() => {
  //current_component.value = route.params.id_component;
});

/**
 * Функции
 */
const updateBreadscrumbs = (title) => {
  setBreadscrumbs(
    [
      {
        path: "/news",
        meta: { title: "Новости" },
      },
      {
        path: `/news/category/${newsStore.cur_category.id}/all-posts`,
        meta: { title: newsStore.cur_category.name },
      },
    ],
    title,
    true
  );
};

const loadPosts = async (page = 0) => {
  await newsStore.loadInfoCategory(route.params.category_id);
  if (route.params.id_component == "all-posts") {
    meta_title.value = `Последние новости из категории - ${newsStore.cur_category.name}`;
    let offset = 0;
    if (page != 0) {
      offset = newsStore.limit * (current_page.value - 1);
    }

    await newsStore.loadPosts(route.params.category_id, offset, 0);
  }
  if (route.params.id_component == "popular-posts") {
    meta_title.value = `Популярные новости из категории - ${newsStore.cur_category.name}`;
    let offset = 0;
    if (page != 0) {
      offset = newsStore.limit * (current_page.value - 1);
    }
    await newsStore.loadPosts(route.params.category_id, offset, 1);
  }
  /*  if (route.params.id_component == "news-categories") {
    meta_title.value = `Список категорий новостей`;
    //await newsStore.loadPosts();
  } */
  posts.value = newsStore.posts;
  count.value = newsStore.count_news;

  component_lists.value[0].title = `Последние новости из категории ${newsStore.cur_category.name}`;
  component_lists.value[1].title = `Популярные новости из категории ${newsStore.cur_category.name}`;

  if (route.params.category_id) {
    component_lists.value[0].to = `/news/category/${route.params.category_id}/all-posts`;
    component_lists.value[1].to = `/news/category/${route.params.category_id}/popular-posts`;
    //component_lists.value[2].to = `/news/category/${route.params.category_id}/news-categories`;
  }
  if (meta_title.value) {
    //setMetaTitle(meta_title.value);
    updateBreadscrumbs(meta_title.value);
  }
};

useMeta(() => {
  return {
    title: meta_title.value + " : Усадьба Мечты",
  };
});
</script>

<style lang="scss" scoped></style>
