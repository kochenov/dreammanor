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
      <div v-if="current_component == 'all'">
        <ListAdsComponents :items="estateStore.homes" />
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
import ListAdsComponents from "../components/ListAdsComponents.vue";

const estateStore = useEstateStore();
const current_component = ref("all");
const meta_title = ref("");
const component_lists = ref([
  {
    name_component: "all", // Имя файла компонента
    title: "Свежие объявления о продаже домов в деревне", // Заголовок текущего компонента
    //sub_title: "Новости из всех категорий в одном месте",
    text_btn: "Последние", // Имя вкладки
    flag: "box-news",
    to: "/desk/realEstate/all",
  },
  {
    name_component: "popular", // Имя файла компонента
    title: "Опубликованные объявление", // Заголовок текущего компонента
    //sub_title: "Обсуждение новости читателями",
    text_btn: "Популярные", // Имя вкладки
    flag: "box-news",
    to: "/desk/realEstate/popular",
  },
  {
    name_component: "add-new-ads-home", // Имя файла компонента
    title: "Добавить новое объявление", // Заголовок текущего компонента
    //sub_title: "Список всех новостных категорий",
    text_btn: "Добавить объявление", // Имя вкладки
    flag: "box-news",
    to: "/desk/realEstate/links/add-new-ads-home",
  },
]);
const route = useRoute();
const links = ref(null);

onMounted(async () => {
  if (current_component.value == "all") {
    await estateStore.getHomes();
    if (estateStore.homes) {
      links.value = estateStore.links;
      load(current_component.value);
    }
  }
});
watch(current_component, async () => {
  if (current_component.value == "all") {
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
        path: "/lists",
        meta: { title: "Объявления" },
      },
    ],
    title,
    true
  );
};
const load = async (component) => {
  if (component == "all") {
    updateBreadscrumbs("Список ссылок на объявления");
    meta_title.value = "Список ссылок на объявления";
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
