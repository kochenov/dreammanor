export default [
  {
    path: "/news",
    name: "news",
    meta: { title: "Новости" },
    component: () => import("layouts/MainLayout.vue"),
    children: [
      {
        path: "",
        name: "news",
        redirect: (to) => {
          // the function receives the target route as the argument
          // we return a redirect path/location here.
          return { path: "/news/all-news" };
        },
      },
      {
        path: "all-news",
        name: "all-news",
        meta: { title: "Все новости", name: "all-news" },
        component: () => import("./pages/news/AllNewsPage.vue"),
      },
      {
        path: "category/:cat(\\d+)",
        name: "news-cats",
        meta: { title: "По категориям", name: "news-cats" },
        component: () => import("./pages/news/CategoryNewsPage.vue"),
      },
      {
        path: "category/:cat(\\d+)/post/:num(\\d+)?",
        name: "news-post",
        meta: { name: "onePostNews" },
        component: () => import("./pages/news/OnePostPage.vue"),
      },
    ],
  },
];
