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
            Страница "Как стать автором" предназначена для тех пользователей,
            которые хотят делиться своим опытом и знаниями о деревенской жизни с
            другими участниками сообщества. Для того чтобы стать автором, нужно
            зарегистрироваться на нашем сайте и создать свой профиль.
          </p>
          <p>
            После регистрации вам будет доступен личный кабинет, где вы сможете
            написать статью и опубликовать ее на сайте. Кроме того, вы сможете
            управлять своими опубликованными статьями, редактировать их,
            добавлять новые и удалять старые.
          </p>
          <p>
            Мы приглашаем всех любителей деревенской жизни присоединиться к
            нашему сообществу и поделиться своими знаниями и опытом с другими
            участниками. Будем рады видеть вас в качестве автора на нашем сайте!
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
    title: "Как стать успешным автором", // Заголовок текущего компонента
    //sub_title: "Новости из всех категорий в одном месте",
    text_btn: "Содержимое", // Имя вкладки
    flag: "box-news",
    to: "/news/all-news",
  },
]);

onMounted(async () => {
  meta_title.value = "Стать автором содержимого на сайте";
  updateBreadscrumbs("Стать автором");
});

const updateBreadscrumbs = (title) => {
  setBreadscrumbs(
    [
      {
        path: "/about",
        meta: { title: "О нас" },
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
