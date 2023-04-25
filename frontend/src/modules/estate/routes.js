export default [
  {
    path: "realEstate/links/:id_component",
    name: "links",
    meta: { auth: true, title: "Список объявлений" },
    component: () => import("./pages/LinksPage.vue"),
  },
  {
    path: "realEstate",
    name: "realEstate",
    meta: {},
    redirect: (to) => {
      // the function receives the target route as the argument
      // we return a redirect path/location here.
      return { path: "/desk/realEstate/all" };
    },
  },

  {
    path: "find-home",
    name: "formFindHome",
    meta: { title: "Недвижимость", name: "realEstate" },
    component: () => import("./pages/FindHomePage.vue"),
  },
  {
    path: "find-home/:num(\\d+)?",
    name: "formFindResult",
    meta: { title: "Недвижимость", name: "realEstate" },
    component: () => import("./pages/FindHomePage.vue"),
  },
  {
    path: "realEstate/home/:id(\\d+)",
    name: "homeInfo",
    meta: {},
    component: () => import("./pages/OneHomePage.vue"),
  },
  {
    path: "realEstate/:id_component",
    name: "realEstateAds",
    meta: {},
    component: () => import("./pages/realEstatePage.vue"),
  },
];
