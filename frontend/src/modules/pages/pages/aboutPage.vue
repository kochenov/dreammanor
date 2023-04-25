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
            На странице "О нашей команде и нашем сайте о жизни в деревне" вы
            можете познакомиться с людьми, которые стоят за созданием и
            поддержкой нашего сайта. Мы представляемся вам, рассказываем о нашем
            опыте и профессиональных навыках, которые мы используем, чтобы
            сделать наш сайт лучше для наших пользователей.
          </p>
          <p>
            Мы также подробно рассказываем о целях нашего сайта, которые
            заключаются в том, чтобы предоставить информацию, связанную с жизнью
            в деревне. Мы уделяем особое внимание здоровью, благополучию и
            комфорту жителей деревенских местностей. Наши статьи и ресурсы
            помогают нашим пользователям узнать больше о жизни в деревне и
            наслаждаться ею.
          </p>
          <p>
            Кроме того, мы рассказываем о нашем функционале сайта, о том, какие
            инструменты мы предоставляем нашим пользователям и как они могут
            использовать их для своих целей. Мы также описываем, как мы собираем
            информацию и обрабатываем ее на нашем сайте, чтобы обеспечить нашим
            пользователям наилучший опыт использования сайта.
          </p>

          <p>
            Наша страница "О нашей команде и нашем сайте о жизни в деревне" -
            это ваше окно в мир нашего сайта. Мы надеемся, что вы найдете здесь
            полезную информацию и узнаете больше о том, как мы работаем для вас.
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
    title:
      "Узнайте больше о нашей команде разработчиков и целях нашего сайта о жизни в деревне", // Заголовок текущего компонента
    //sub_title: "Новости из всех категорий в одном месте",
    text_btn: "Содержимое", // Имя вкладки
    flag: "box-news",
    to: "/news/all-news",
  },
]);

onMounted(async () => {
  meta_title.value =
    "Наша команда разработчиков, функционал и цели сайта о жизни в деревне ";
  updateBreadscrumbs("О нас и нашем сайте о жизни в деревне");
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
