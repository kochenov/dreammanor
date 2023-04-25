import { routes as authRoutes } from "src/modules/auth";
import { routes as estateRoutes } from "src/modules/estate";
import { routes as newsRoutes } from "src/modules/news";
import { routes as pagesRoutes } from "src/modules/pages";

const routes = [
  {
    path: "/",
    name: "home",
    //meta: { title: "Главнwwwwwая" },
    component: () => import("layouts/MainLayout.vue"),
    children: [
      {
        path: "/",
        name: "home",
        meta: { title: "Главная" },
        component: () => import("pages/IndexPage.vue"),
      },
    ],
  },
  {
    path: "/desk",
    name: "desk",
    meta: {},
    component: () => import("layouts/MainLayout.vue"),
    children: [...estateRoutes],
  },
  {
    path: "/news",
    name: "news",
    meta: { title: "Новости" },
    component: () => import("layouts/MainLayout.vue"),
    children: [...newsRoutes],
  },

  // Always leave this as last one,
  // but you can also remove it
  {
    path: "/404",
    name: "404",
    component: () => import("pages/ErrorNotFound.vue"),
  },
  {
    path: "/:catchAll(.*)*",
    name: "404error",
    redirect: (to) => {
      // the function receives the target route as the argument
      // we return a redirect path/location here.
      return { path: "/404" };
    },
  },
];

export default [...routes, ...authRoutes, ...pagesRoutes];
