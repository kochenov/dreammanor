export default [
  {
    path: "/about",
    name: "about",
    meta: { title: "О сайте" },
    component: () => import("layouts/MainLayout.vue"),
    children: [
      {
        path: "",
        name: "newsParent",
        redirect: (to) => {
          // the function receives the target route as the argument
          // we return a redirect path/location here.
          return { path: "/about/about" };
        },
      },
      {
        path: "about",
        name: "about",
        meta: {},
        component: () => import("./pages/aboutPage.vue"),
      },
      {
        path: "contacts",
        name: "contacts",
        meta: {},
        component: () => import("./pages/contactsPage.vue"),
      },
      {
        path: "forPartners",
        name: "forPartners",
        meta: {},
        component: () => import("./pages/forPartnersPage.vue"),
      },
      {
        path: "forAuthors",
        name: "forAuthors",
        meta: {},
        component: () => import("./pages/forAuthorsPage.vue"),
      },
      {
        path: "forEditors",
        name: "forEditors",
        meta: {},
        component: () => import("./pages/forEditorsPage.vue"),
      },
      {
        path: "feedback",
        name: "feedback",
        meta: {},
        component: () => import("./pages/feedbackPage.vue"),
      },
      {
        path: "rules",
        name: "rules",
        meta: {},
        component: () => import("./pages/rulesPage.vue"),
      },
    ],
  },
];
