<template>
  <q-tabs
    v-if="mobile == false"
    align="left"
    inline-label
    shrink
    outside-arrows
    narrow-indicator
    mobile-arrows
    indicatorColor="white"
    active-color="white"
    class="sub-menu bg-primary text-white shadow-2 gt-sm"
  >
    <q-route-tab
      v-for="item in currentMenu[tabName]"
      :key="item.id"
      :name="item.name"
      :label="item.label"
      :to="item.name != 'home' ? '/' + tabName + '/' + item.name : '/'"
      :class="
        $route.matched[$route.matched.length - 1].meta.name == item.name
          ? 'q-tab--active'
          : ''
      "
      exact
    />
  </q-tabs>
  <template v-if="mobile">
    <q-item
      clickable
      v-ripple
      v-for="item in currentMenu[tabName]"
      :key="item.id"
      class="q-pl-lg"
      :active="$route.matched[$route.matched.length - 1].meta.name == item.name"
      active-class="bg-light-blue-2 text-grey-10"
      :to="item.name != 'home' ? '/' + tabName + '/' + item.name : '/'"
      exact
    >
      <q-item-section>{{
        item.label != null ? item.label : "Главная"
      }}</q-item-section>
      <q-item-section avatar>
        <q-icon color="primary" :name="item.icon" />
      </q-item-section>
    </q-item>
  </template>
</template>

<script setup>
const currentMenu = {
  home: [
    {
      id: 1,
      name: "home",
      label: "Главная",
    },
    {
      id: 2,
      name: "topBlogers",
      label: "Топ блогеров",
    },
    {
      id: 3,
      name: "topVideo",
      label: "Топ видео",
    },
    {
      id: 4,
      name: "reitingGroup",
      label: "Рейтинг сообществ",
    },
  ],
  news: [
    {
      id: 1,
      name: "posts/all-posts",
      label: "Все новости",
    },
    {
      id: 2,
      name: "actions",
      label: "События",
    },
    {
      id: 3,
      name: "newUsers",
      label: "Новые пользователи",
    },
    {
      id: 4,
      name: "records",
      label: "Рекорды портала",
    },
  ],
  about: [
    {
      id: 1,
      name: "about",
      label: "О сайте",
    },
    {
      id: 2,
      name: "contacts",
      label: "Контакты",
    },
    {
      id: 3,
      name: "forPartners",
      label: "Партнёрам",
    },
    {
      id: 4,
      name: "forAuthors",
      label: "Авторам",
    },
    {
      id: 5,
      name: "forEditors",
      label: "Стать автором",
    },
    {
      id: 6,
      name: "feedback",
      label: "Обратная связь",
    },
    {
      id: 7,
      name: "rules",
      label: "Правила",
    },
  ],
  desk: [
    {
      id: 1,
      name: "realEstate",
      label: "Недвижимость",
    },
    {
      id: 2,
      name: "products",
      label: "Продукция",
    },
    {
      id: 3,
      name: "animals",
      label: "Животные",
    },
    {
      id: 4,
      name: "addAds",
      label: "Добавить объявление",
    },
  ],
  blogs: [
    {
      id: 1,
      name: "allPosts",
      label: "Все записи",
    },
    {
      id: 2,
      name: "listBlogs",
      label: "Список блогов",
    },
    {
      id: 3,
      name: "blogers",
      label: "Блогеры",
    },
    {
      id: 4,
      name: "addBlog",
      label: "Создать блог",
    },
  ],
  articles: [
    {
      id: 1,
      name: "useful",
      label: "Полезное",
    },
    {
      id: 2,
      name: "vegetableGarden",
      label: "Огород и сад",
    },
    {
      id: 3,
      name: "animalHusbandry",
      label: "Животноводство",
    },
    {
      id: 4,
      name: "addArticle",
      label: "Добавить статью",
    },
  ],
  calculate: [
    {
      id: 1,
      name: "seeding",
      label: "Расчёты посева",
    },
    {
      id: 2,
      name: "feedCalculation",
      label: "Расчёт корма",
    },
    {
      id: 3,
      name: "weightControl",
      label: "Контроль веса",
    },
    {
      id: 4,
      name: "businesPlans",
      label: "Бизнес планы",
    },
    {
      id: 5,
      name: "userCalculations",
      label: "Расчёты пользователей",
    },
  ],
  calendars: [
    {
      id: 1,
      name: "taskList",
      label: "Список задач",
    },
    {
      id: 2,
      name: "recommendations",
      label: "Рекомендации",
    },
    {
      id: 3,
      name: "userTasks",
      label: "Задачи пользователей",
    },
    {
      id: 4,
      name: "addTask",
      label: "Добавить задачу",
    },
  ],
};
defineProps({
  tabName: String,
  mobile: { type: Boolean, default: false },
});
</script>

<style lang="scss">
.sub-menu {
  height: 80px;
  .q-tab__label {
    font-family: "Bitter", sans-serif;
    font-weight: 600;
    font-size: 11px;
  }
  .absolute-bottom {
    bottom: 15px;
  }
  .q-tab__indicator {
    height: 10px;
  }
  .q-tab--active .q-tab__indicator {
    opacity: 0.5;
    transform-origin: left /* rtl:ignore */;
  }

  .q-hoverable:hover {
    .q-tab__indicator {
      opacity: 0.5;
    }
    .q-focus-helper {
      opacity: 0 !important;
    }
  }
}
</style>
