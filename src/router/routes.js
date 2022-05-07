export default [
  {
    path: "/",
    name: "home",
    meta: {
      title: "Социальная сеть фермеров, сельских жителей и дачников",
      layout: "index",
      parent: "home",
    },
    component: () => import("../views/DefaultPage.vue"),
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
    component: () => import("../views/DefaultPage.vue"),
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
    component: () => import("../views/DefaultPage.vue"),
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
    component: () => import("../views/DefaultPage.vue"),
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
    component: () => import("../views/DefaultPage.vue"),
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
    component: () => import("../views/DefaultPage.vue"),
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
    component: () => import("../views/DefaultPage.vue"),
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
    component: () => import("../views/DefaultPage.vue"),
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
    component: () => import("../views/DefaultPage.vue"),
  },
  {
    path: "/about",
    name: "about",
    meta: {
      parent: "about",
      layout: "index",
    },
    component: () => import("../views/DefaultPage.vue"),
  },
  {
    path: "/contacts",
    name: "contacts",
    meta: {
      parent: "about",
      layout: "index",
    },
    component: () => import("../views/DefaultPage.vue"),
  },
  {
    path: "/for-partners",
    name: "for-partners",
    meta: {
      parent: "about",
      layout: "index",
    },
    component: () => import("../views/DefaultPage.vue"),
  },
  {
    path: "/for-authors",
    name: "for-authors",
    meta: {
      parent: "about",
      layout: "index",
    },
    component: () => import("../views/DefaultPage.vue"),
  },
  {
    path: "/author/new",
    name: "author-new",
    meta: {
      parent: "about",
      layout: "index",
    },
    component: () => import("../views/DefaultPage.vue"),
  },
  {
    path: "/feedback",
    name: "feedback",
    meta: {
      parent: "about",
      layout: "index",
    },
    component: () => import("../views/DefaultPage.vue"),
  },
  {
    path: "/rules",
    name: "rules",
    meta: {
      parent: "about",
      layout: "index",
    },
    component: () => import("../views/DefaultPage.vue"),
  },
  {
    path: "/bulletin-board",
    name: "bulletinBoard",
    meta: {
      parent: "bulletinBoard",
      layout: "index",
    },
    component: () => import("../views/DefaultPage.vue"),
  },
  {
    path: "/real-estate",
    name: "real-estate",
    meta: {
      parent: "bulletinBoard",
      layout: "index",
    },
    component: () => import("../views/DefaultPage.vue"),
  },
  {
    path: "/production",
    name: "production",
    meta: {
      parent: "bulletinBoard",
      layout: "index",
    },
    component: () => import("../views/DefaultPage.vue"),
  },
  {
    path: "/animals",
    name: "animals",
    meta: {
      parent: "bulletinBoard",
      layout: "index",
    },
    component: () => import("../views/DefaultPage.vue"),
  },
  {
    path: "/board-add",
    name: "board-add",
    meta: {
      parent: "bulletinBoard",
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
    path: "/posts",
    name: "posts",
    meta: {
      layout: "index",
      parent: "blogs",
    },
    component: () => import("../views/DefaultPage.vue"),
  },
  {
    path: "/blogers-list",
    name: "blogersList",
    meta: {
      layout: "index",
      parent: "blogs",
    },
    component: () => import("../views/DefaultPage.vue"),
  },
  {
    path: "/blogers",
    name: "blogers",
    meta: {
      layout: "index",
      parent: "blogs",
    },
    component: () => import("../views/DefaultPage.vue"),
  },
  {
    path: "/create-add-blog",
    name: "createAddBlog",
    meta: {
      layout: "index",
      parent: "blogs",
    },
    component: () => import("../views/DefaultPage.vue"),
  },
  {
    path: "/articles",
    name: "articles",
    meta: {
      parent: "articles",
      layout: "index",
    },
    component: () => import("../views/DefaultPage.vue"),
  },
  {
    path: "/articles/useful",
    name: "articlesUseful",
    meta: {
      parent: "articles",
      layout: "index",
    },
    component: () => import("../views/DefaultPage.vue"),
  },
  {
    path: "/articles/vegetable-garden-and-garden",
    name: "articlesVegetableGardenAndGarden",
    meta: {
      parent: "articles",
      layout: "index",
    },
    component: () => import("../views/DefaultPage.vue"),
  },
  {
    path: "/articles/animal-husbandry",
    name: "AnimalHusbandry",
    meta: {
      parent: "articles",
      layout: "index",
    },
    component: () => import("../views/DefaultPage.vue"),
  },
  {
    path: "/articles/create",
    name: "articlesCreate",
    meta: {
      parent: "articles",
      layout: "index",
    },
    component: () => import("../views/DefaultPage.vue"),
  },
  {
    path: "/calculation/seeding",
    name: "seeding",
    meta: {
      title: "Калькулятор расчёта размера грядок овощей",
      layout: "index",
      parent: "seeding",
      breadcrumbs: [
        {
          name: "Расчёты",
          url: "/calculation",
        },
        {
          name: "Калькулятор расчёта грядок овощей",
          url: "/seeding",
        },
      ],
    },
    component: () => import("../views/SeedingPage.vue"),
  },
  {
    path: "/calculation/feed",
    name: "calculationFeed",
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
    path: "/calculation/weight-control",
    name: "calculationWeightControl",
    meta: {
      layout: "index",
      parent: "seeding",
      breadcrumbs: [
        {
          name: "Расчёты",
          url: "/seeding",
        },
        {
          name: "Контроль веса",
          url: "/seeding",
        },
      ],
    },
    component: () => import("../views/SeedingPage.vue"),
  },
  {
    path: "/calculation/bisnes-plans",
    name: "calculationBisnesPlans",
    meta: {
      layout: "index",
      parent: "seeding",
      breadcrumbs: [
        {
          name: "Расчёты",
          url: "/seeding",
        },
        {
          name: "Контроль веса",
          url: "/seeding",
        },
      ],
    },
    component: () => import("../views/SeedingPage.vue"),
  },
  {
    path: "/calculation/all-users",
    name: "calculationAllUsers",
    meta: {
      title: "Последние расчёты посльзователей социальной сети",
      layout: "index",
      parent: "seeding",
      breadcrumbs: [
        {
          name: "Расчёты",
          url: "/seeding",
        },
        {
          name: "Контроль веса",
          url: "/seeding",
        },
      ],
    },
    component: () => import("../views/SeedingPage.vue"),
  },
  {
    path: "/сalendars",
    name: "сalendars",
    meta: {
      layout: "index",
    },
    component: () => import("../views/DefaultPage.vue"),
  },
  {
    path: "/task-list",
    name: "taskList",
    meta: {
      parent: "сalendars",
      layout: "index",
    },
    component: () => import("../views/DefaultPage.vue"),
  },
  {
    path: "/recomendations",
    name: "recomendations",
    meta: {
      parent: "сalendars",
      layout: "index",
    },
    component: () => import("../views/DefaultPage.vue"),
  },
  {
    path: "/user-tasks",
    name: "userTasks",
    meta: {
      parent: "сalendars",
      layout: "index",
    },
    component: () => import("../views/DefaultPage.vue"),
  },
  {
    path: "/add-task",
    name: "addTask",
    meta: {
      parent: "сalendars",
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
    path: "/login",
    name: "login",
    meta: {
      parent: "account",
      layout: "index",
    },
    component: () => import("../views/LoginPage.vue"),
  },
  {
    path: "/registration",
    name: "registration",
    meta: {
      parent: "account",
      layout: "index",
    },
    component: () => import("../views/DefaultPage.vue"),
  },
  {
    path: "/lk",
    name: "lk",
    meta: {
      parent: "account",
      layout: "index",
    },
    component: () => import("../views/DefaultPage.vue"),
  },
  {
    path: "/notifications",
    name: "notifications",
    meta: {
      parent: "account",
      layout: "index",
    },
    component: () => import("../views/DefaultPage.vue"),
  },
  {
    path: "/logout",
    name: "logout",
    meta: {
      layout: "index",
      parent: "account",
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
