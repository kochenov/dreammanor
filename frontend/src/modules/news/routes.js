export default [
  {
    path: "",
    name: "newsParent",
    redirect: (to) => {
      // the function receives the target route as the argument
      // we return a redirect path/location here.
      return { path: "/news/posts/all-posts" };
    },
  },
  {
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
  },
];
