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
            На нашем сайте для любителей деревенской жизни любой
            зарегистрированный пользователь, кто хочет поделиться своими
            историями, знаниями и опытом в области сельского хозяйства,
            садоводства, животноводства, ремесел и прочих аспектов деревенской
            жизни, может стать автором.
          </p>
          <p>
            Как автор на нашем сайте, вы можете публиковать статьи, рассказы,
            рецепты, фотографии и видео о своей жизни в деревне, о том, как вы
            выращиваете овощи и фрукты, как содержите скот, как занимаетесь
            рукоделием и многом другом. Вы можете делиться своими знаниями и
            опытом, а также учиться у других авторов и получать отзывы и
            комментарии от наших читателей.
          </p>
          <p>Мы приглашаем всех любителей деревенской жизни стать авторами.</p>
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
    title: "Информация для будующих авторов", // Заголовок текущего компонента
    //sub_title: "Новости из всех категорий в одном месте",
    text_btn: "Содержимое", // Имя вкладки
    flag: "box-news",
    to: "/news/all-news",
  },
]);

onMounted(async () => {
  meta_title.value = "Авторам";
  updateBreadscrumbs("Авторам");
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
