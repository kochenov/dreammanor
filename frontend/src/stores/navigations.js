import { defineStore } from "pinia";
import { serviceNode } from "src/services/Service";

export const useNavigationsStore = defineStore("navigations", {
  state: () => ({
    breadscrumbs: [],
    curendDinamicPage: null,
    current_title: null,
    node: null,
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
    async loadNode(fullPath){
      try {
        let res = await serviceNode.get_node(fullPath);
        this.node = res.data;
      } catch (error) {
        console.log(error);
      }
    }
  },
});
