<template>
  <q-page class="">
    <tabs-conteiner
      :nav_route="false"
      :tabs="false"
      :component_lists="component_lists"
      :current_component="current_component"
    >
      <div class="text-body1 q-px-lg column items-center">
        <div style="max-width: 1200px">
          <q-banner inline-actions class="text-white q-my-md bg-red">
            Cтраница находится на стадии разработки. Ниже описан будущий
            функционал.
          </q-banner>
          <p>
            Данная страница представляет собой список вновь зарегистрированных
            пользователей на сайте. Она отображает информацию о каждом новом
            пользователе, включая его имя, фотографию (если она была загружена),
            дату регистрации и другие дополнительные данные, такие как
            местоположение или интересы (если они были указаны при регистрации).
          </p>
          <p></p>
          Страница может быть полезна как для администраторов сайта, так и для
          других пользователей, которые хотят найти новых друзей или коллег на
          сайте. Для администраторов страница является важным инструментом для
          отслеживания активности регистрации пользователей на сайте и
          определения эффективности маркетинговых кампаний. Для новых
          пользователей страница может быть полезна для знакомства с другими
          пользователями сайта и создания социальных связей.
          <p>
            Страница также может содержать некоторые дополнительные функции,
            такие как поиск по списку пользователей или фильтры, которые
            позволяют пользователю отобразить только определенные типы
            пользователей (например, только пользователей из определенного
            города или с определенными интересами).
          </p>
          <p>
            В целом, страница вновь зарегистрированных пользователей на сайте
            является важным инструментом для создания социальной сети и
            повышения вовлеченности пользователей в жизнь сайта. Она также может
            помочь улучшить пользовательский опыт и увеличить количество
            регистраций на сайте.
          </p>
        </div>
      </div>
    </tabs-conteiner>
  </q-page>
</template>

<script setup>
import { useMeta } from "quasar";
import { setBreadscrumbs } from "src/services/Service";
import { ref, onMounted } from "vue";
import TabsConteiner from "src/components/blocks/tabs/TabsConteiner.vue";

const current_component = ref("show");
const meta_title = ref("");
const component_lists = ref([
  {
    name_component: "show", // Имя файла компонента
    title: "Список новых пользователей на сайте", // Заголовок текущего компонента
    //sub_title: "Новости из всех категорий в одном месте",
    text_btn: "Содержимое", // Имя вкладки
    flag: "box-news",
    to: "/news/all-news",
  },
]);

onMounted(async () => {
  meta_title.value = "Недавно зарегистрированные пользователи сайта";
  updateBreadscrumbs("Новые пользователи");
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
