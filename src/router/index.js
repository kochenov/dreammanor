import { createRouter, createWebHistory } from "vue-router";
import routesImport from "./routes";

const routes = routesImport;

const router = createRouter({
  history: createWebHistory(),
  routes,
});
export default router;
