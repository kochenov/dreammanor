import { defineStore } from "pinia";

export const useNavigationsStore = defineStore("navigations", {
  state: () => ({
    breadscrumbs: [],
    curendDinamicPage: null,
    current_title: null,
  }),
  getters: {
    navBread: (state) =>
      state.curendDinamicPage
        ? [...state.breadscrumbs, ...state.curendDinamicPage]
        : state.breadscrumbs,
  },
  actions: {
    load(routes) {
      let d = routes.filter((o) => "title" in o.meta);
      /* console.log("filter: ", d);
      console.log("routs: ", routes); */
      this.breadscrumbs = d;
      this.curendDinamicPage = null;
      this.current_title = null;
    },
    addRoutes(arr) {
      this.curendDinamicPage = [{ ...arr }];
    },
  },
});
