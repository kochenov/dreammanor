export default [
  {
    path: "/login",
    component: () => import("./layouts/MainLayout.vue"),
    children: [
      {
        path: "",
        name: "login",
        component: () => import("./pages/LoginPage.vue"),
      },
    ],
  },
];
