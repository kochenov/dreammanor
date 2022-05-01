import { createRouter, createWebHistory } from "vue-router";
import routesImport from "./routes";

const routes = routesImport;

const router = createRouter({
  history: createWebHistory(),
  routes,
});

router.beforeEach((to, from, next) => {
  if (typeof to.meta.title !== "undefined") {
    document.title = `${to.meta.title}`;
  }
  next();
});
export default router;
