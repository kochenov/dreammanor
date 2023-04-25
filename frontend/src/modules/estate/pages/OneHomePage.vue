<template>
  <q-page class="" v-if="!estateStore.loading && home">
    <tabs-conteiner
      tabs
      :component_lists="component_lists"
      :current_component="current_component"
      :nav_route="false"
      @setCurrentComponent="(c) => (current_component = c)"
    >
      <div v-if="current_component == 'post'">
        <OneHomeInfoComponent :key="home.id" :item="home" />
      </div>
      <div v-if="current_component == 'related'">
        <!-- <CategoryList /> -->
      </div>
      <div v-if="current_component == 'add-new-ads-home'">
        <NeWHomeAdaComponent />
      </div>
    </tabs-conteiner>
  </q-page>
</template>

<script setup>
import { ref, onMounted, watch } from "vue";
import TabsConteiner from "src/components/blocks/tabs/TabsConteiner.vue";
import { useRoute } from "vue-router";
import { useEstateStore } from "../store";
import NeWHomeAdaComponent from "../components/NewHomeAdaComponent.vue";
import { setBreadscrumbs } from "src/services/Service";
import { useMeta } from "quasar";
import OneHomeInfoComponent from "../components/OneHomeInfoComponent.vue";

const estateStore = useEstateStore();
const current_component = ref("post");
const meta_title = ref("");
const component_lists = ref([
  {
    name_component: "post", // Имя файла компонента
    title: "", // Заголовок текущего компонента
    //sub_title: "Новости из всех категорий в одном месте",
    text_btn: "Описание", // Имя вкладки
  },
  {
    name_component: "reputation", // Имя файла компонента
    title: "Отзовы и коментарии", // Заголовок текущего компонента
    //sub_title: "Обсуждение новости читателями",
    text_btn: "Отзовы", // Имя вкладки
  },
  {
    name_component: "Похожие", // Имя файла компонента
    title: "Похожие объявления", // Заголовок текущего компонента
    //sub_title: "Список всех новостных категорий",
    text_btn: "Добавить объявление", // Имя вкладки
  },
]);
const route = useRoute();
const home = ref(null);

onMounted(async () => {
  if (current_component.value == "post") {
    await estateStore.getHome(route.params.id);
    if (estateStore.home_item) {
      home.value = estateStore.home_item;
      load(current_component.value);
    }
  }
});
watch(current_component, async () => {
  if (current_component.value == "post") {
    await estateStore.getLinks();
    if (estateStore.links) {
      links.value = estateStore.links;
    }
  }
  load(current_component.value);
});

const updateBreadscrumbs = (title) => {
  setBreadscrumbs(
    [
      {
        path: "/desk/realEstate",
        meta: { title: "Объявления" },
      },
    ],
    title,
    true
  );
};
const load = async (component) => {
  if (component == "post") {
    let title = home.value.title;
    updateBreadscrumbs(title);
    meta_title.value = title;
    component_lists.value[0].title = title;
  } else if (component == "add-new-ads-home") {
    updateBreadscrumbs("Создать новое объявление");
    meta_title.value = "Создать новое объявление";
  }

  /* component_lists.value[0].title = post.value.title;
    component_lists.value[0].sub_title = post.value.category.name; */
};

const editItem = async (link_id, status_id) => {
  await estateStore.editLinks(link_id, status_id);
  await estateStore.getLinks();
  if (estateStore.links) {
    links.value = estateStore.links;
  }
};

useMeta(() => {
  return {
    title: meta_title.value + " : Усадьба Мечты",
  };
});
</script>

<style lang="scss" scoped></style>
