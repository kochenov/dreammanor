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
            Данная страница является центром активности пользователей на сайте.
            Все действия, производимые пользователями, записываются в базу
            данных и выводятся в ленте событий, которая отображается на этой
            странице. Лента событий представляет собой динамически обновляемую
            таблицу, в которой отображаются различные события, такие как
            комментарии, лайки, репосты, покупки, подписки и другие действия
            пользователей на сайте.
          </p>
          <p>
            Каждое событие содержит информацию о пользователе, который выполнил
            действие, а также об объекте, над которым было произведено действие.
            Например, при добавлении нового комментария к записи в блоге
            отображается имя пользователя, который оставил комментарий, а также
            содержание самого комментария и заголовок записи в блоге.
          </p>
          <p>
            На странице также доступны фильтры, которые позволяют отобразить
            только определенные типы событий или выбрать определенный период
            времени для отображения. Это помогает пользователям находить нужную
            информацию в ленте событий и следить за активностью определенных
            пользователей или объектов на сайте. Страница является важным
            инструментом для анализа поведения пользователей и оценки
            эффективности функционала сайта. Она также может быть использована
            для повышения вовлеченности пользователей и создания более
            персонализированного опыта использования сайта.
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
    title: "Следите за активностью пользователей на нашем сайте", // Заголовок текущего компонента
    //sub_title: "Новости из всех категорий в одном месте",
    text_btn: "Содержимое", // Имя вкладки
    flag: "box-news",
    to: "/news/all-news",
  },
]);

onMounted(async () => {
  meta_title.value =
    "Просмотрите активность пользователей на сайте Усадьба Мечты";
  updateBreadscrumbs("Лента событий");
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
