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
  {
    path: "/forgot-password",
    component: () => import("./layouts/MainLayout.vue"),
    children: [
      {
        name: "passwordReset",
        path: "",
        component: () => import("./pages/ResetPage.vue"),
      },
    ],
  },
  {
    path: "/registration",
    component: () => import("./layouts/MainLayout.vue"),
    children: [
      {
        name: "registration",
        path: "",
        component: () => import("./pages/RegistrationPage.vue"),
      },
    ],
  },
  {
    path: "/logout",
    component: () => import("./layouts/MainLayout.vue"),
    children: [
      {
        name: "logout",
        path: "",
        component: () => import("./pages/LogoutPage.vue"),
      },
    ],
  },
];
