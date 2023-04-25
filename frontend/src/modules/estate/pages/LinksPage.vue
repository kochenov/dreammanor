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
      <div v-if="current_component == 'list'">
        <div v-if="estateStore.links" class="q-pa-md">
          <q-markup-table dense :key="estateStore.links">
            <thead>
              <tr>
                <th class="text-left">Номер</th>
                <th class="text-right">Ссылка на объявление</th>
                <th class="text-right">Цена</th>
                <th class="text-right">Дата</th>
                <th class="text-right">Архив</th>
                <th class="text-right">Действия</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="i in estateStore.links" :key="i.id">
                <td class="text-left">{{ i.id }}</td>
                <td class="text-right">
                  <a target="_blank" :href="`${i.link}`">Перейти</a>
                </td>
                <td class="text-right">
                  {{i.price}}
                </td>
                <td class="text-right">
                  {{ date.formatDate(i.created_ad, "DD MMM YYYY HH:mm:ss") }}
                </td>
                <td class="text-right">
                  <q-btn dense size="sm" icon="delete" color="red"  @click="editItem(i.id, 5)"
                    >В архив</q-btn
                  >
                </td>
                <td class="text-right">
                  <q-btn-dropdown
                    dense
                    size="sm"
                    icon="settings"
                    color="primary"
                  >
                    <q-list
                      v-for="status in estateStore.status_list"
                      :key="status.id"
                      dense
                    >
                      <q-item
                        clickable
                        v-close-popup
                        @click="editItem(i.id, status.id)"
                      >
                        <q-item-section>
                          <q-item-label>{{ status.label }}</q-item-label>
                        </q-item-section>
                      </q-item>
                    </q-list>
                  </q-btn-dropdown>
                </td>
              </tr>
            </tbody>
          </q-markup-table>
        </div>
        <div v-else>
          <div v-if="estateStore.error">
            <span v-for="i in estateStore.error" :key="i">
              <q-banner class="bg-grey-3 q-ma-sm">
                <template v-slot:avatar>
                  <q-icon name="signal_wifi_off" color="primary" />
                </template>
                {{ i }}
              </q-banner>
            </span>
          </div>
        </div>
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
import { date } from "quasar";
import { ref, onMounted, watch } from "vue";
import TabsConteiner from "src/components/blocks/tabs/TabsConteiner.vue";
import { useRoute } from "vue-router";
import { useEstateStore } from "../store";
import NeWHomeAdaComponent from "../components/NewHomeAdaComponent.vue";
import { setBreadscrumbs } from "src/services/Service";
import { useMeta } from "quasar";

const estateStore = useEstateStore();
const current_component = ref("list");
const meta_title = ref("");
const component_lists = ref([
  {
    name_component: "list", // Имя файла компонента
    title: "Список ссылок на объявление", // Заголовок текущего компонента
    //sub_title: "Новости из всех категорий в одном месте",
    text_btn: "Список ссылок", // Имя вкладки
    flag: "box-news",
    to: "/desk/realEstate/links/list",
  },
  {
    name_component: "published", // Имя файла компонента
    title: "Опубликованные объявление", // Заголовок текущего компонента
    //sub_title: "Обсуждение новости читателями",
    text_btn: "Опубликованные", // Имя вкладки
    flag: "box-news",
    to: "/news/all-news",
    to: "/desk/realEstate/links/published",
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
  if (current_component.value == "list") {
    await estateStore.getLinks();
    if (estateStore.links) {
      links.value = estateStore.links;
      load(current_component.value);
    }
  }
});
watch(current_component, async () => {
  if (current_component.value == "list") {
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
  if (component == "list") {
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
