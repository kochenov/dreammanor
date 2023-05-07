export default [
  {
    path: "",
    name: "newsParent",
    redirect: (to) => {
      // the function receives the target route as the argument
      // we return a redirect path/location here.
      return { path: "/news/posts/last" };
    },
  },
  {
    path: "posts/:component(last|popular|categoryes|category)/:slug?",
    name: "posts",
    meta: {
      module: { name: "Новости", path: "news" },
      page: { name: "Список новостей", path: "posts" },
      component: [
        { name: "Последние новости", path: "last" },
        { name: "Популярные новости", path: "popular" },
        { name: "Категории ковостей", path: "categoryes" },
        { name: "Новости из категории", path: "category" },
      ]
    },
    component: () => import("./pages/postsPage.vue"),
  },
  {
    path: "post/:component(show|comments|related)/:slug",
    name: "post",
    meta: {
      module: { name: "Новости", path: "news" },
      page: { name: "Одна новость", path: "post" },
      component: [
        { name: "Содержание", path: "show" },
        { name: "Комментарии", path: "comments" },
        { name: "Похожие новости", path: "related" },
      ],
    },
    component: () => import("./pages/postPage.vue"),
  },
  /* {
    path: "actions",
    name: "actions",
    meta: {},
    component: () => import("./pages/actionPage.vue"),
  },
  {
    path: "newUsers",
    name: "newUsers",
    meta: {},
    component: () => import("./pages/newUsersPage.vue"),
  },
  {
    path: "records",
    name: "records",
    meta: {},
    component: () => import("./pages/recordsPage.vue"),
  },
  {
    path: "posts/:id_component?",
    name: "all-news",
    meta: { name: "all-news" },
    component: () => import("./pages/postsPage.vue"),
  },
  {
    path: "category/:category_id(\\d+)",
    name: "all-news-category",
    meta: { name: "postsCategory" },
    component: () => import("./pages/categoriesPage.vue"),
  },
  {
    path: "category/:category_id(\\d+)/:id_component",
    name: "all-news-category-component",
    meta: { name: "postsCategory" },
    component: () => import("./pages/categoriesPage.vue"),
  },
  {
    path: "category/:category_id(\\d+)/post/:post_id(\\d+)",
    name: "postNews",
    meta: { name: "postNews" },
    component: () => import("./pages/postPage.vue"),
  }, */
];
