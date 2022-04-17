export default [
  {
    path: "/",
    name: "home",
    meta: {
      layout: "index",
      parent: "home",
    },
    component: () => import("../views/HomePage.vue"),
  },
  {
    path: "/blogers/top",
    name: "BlogersTop",
    meta: {
      layout: "index",
      parent: "home",
      breadcrumbs: [
        {
          name: "Блогеры",
          url: "/blogers",
        },
        {
          name: "Топ деревенских блогеров",
          url: "/blogers/top",
        },
      ],
    },
    component: () => import("../views/HomePage.vue"),
  },
  {
    path: "/video/top",
    name: "VideoTop",
    meta: {
      layout: "index",
      parent: "home",
      breadcrumbs: [
        {
          name: "Видеоролики",
          url: "/video",
        },
        {
          name: "Топ деревенских блогеров",
          url: "/video/top",
        },
      ],
    },
    component: () => import("../views/HomePage.vue"),
  },
  {
    path: "/communities",
    name: "Communities",
    meta: {
      layout: "index",
      parent: "home",
      breadcrumbs: [
        {
          name: "Список сообществ",
          url: "/сommunities",
        },
      ],
    },
    component: () => import("../views/HomePage.vue"),
  },
  {
    path: "/authors/register",
    name: "AuthorRegister",
    meta: {
      layout: "index",
      parent: "home",
      breadcrumbs: [
        {
          name: "Список авторов",
          url: "/authors",
        },
        {
          name: "Регистранция нового автора / Заявка ",
          url: "/authors/register",
        },
      ],
    },
    component: () => import("../views/HomePage.vue"),
  },
  {
    path: "/news",
    name: "news",
    meta: {
      layout: "index",
      parent: "news",
      breadcrumbs: [
        {
          name: "Новости",
          url: "/news",
        },
        {
          name: "Все новости",
          url: "/news/action",
        },
      ],
    },
    component: () => import("../views/NewsPage.vue"),
  },
  {
    path: "/news/action",
    name: "newsAction",
    meta: {
      layout: "index",
      parent: "news",
      breadcrumbs: [
        {
          name: "Новости",
          url: "/news",
        },
        {
          name: "События",
          url: "/news/action",
        },
      ],
    },
    component: () => import("../views/NewsPage.vue"),
  },
  {
    name: "newUsers",
    path: "/users/new",
    meta: {
      layout: "index",
      parent: "news",
      breadcrumbs: [
        {
          name: "Новости",
          url: "/news",
        },
        {
          name: "События",
          url: "/news/action",
        },
      ],
    },
    component: () => import("../views/NewsPage.vue"),
  },
  {
    path: "/records",
    name: "AuthorRecords",
    meta: {
      layout: "index",
      parent: "news",
      breadcrumbs: [
        {
          name: "Рекорды сайта",
          url: "/authors/records",
        },
      ],
    },
    component: () => import("../views/HomePage.vue"),
  },
  {
    path: "/about",
    name: "about",
    meta: {
      layout: "index",
    },
    component: () => import("../views/DefaultPage.vue"),
  },
  {
    path: "/bulletin-board",
    name: "bulletinBoard",
    meta: {
      layout: "index",
    },
    component: () => import("../views/DefaultPage.vue"),
  },
  {
    path: "/blogs",
    name: "blogs",
    meta: {
      layout: "index",
    },
    component: () => import("../views/DefaultPage.vue"),
  },
  {
    path: "/articles",
    name: "articles",
    meta: {
      layout: "index",
    },
    component: () => import("../views/DefaultPage.vue"),
  },
  {
    path: "/seeding",
    name: "seeding",
    meta: {
      layout: "index",
      parent: "seeding",
      breadcrumbs: [
        {
          name: "Расчёты",
          url: "/seeding",
        },
        {
          name: "Калькулятор посева томатов / выращивание томатов по технологии",
          url: "/seeding",
        },
      ],
    },
    component: () => import("../views/SeedingPage.vue"),
  },
  {
    path: "/сalendars",
    name: "calendars",
    meta: {
      layout: "index",
    },
    component: () => import("../views/DefaultPage.vue"),
  },
  {
    path: "/account",
    name: "account",
    meta: {
      layout: "index",
    },
    component: () => import("../views/DefaultPage.vue"),
  },
  {
    path: "/:pathMatch(.*)*",
    name: "NotFound",
    meta: {
      layout: "index",
    },
    component: () => import("../views/NotFound.vue"),
  },
];
