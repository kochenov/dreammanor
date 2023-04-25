import { defineStore } from "pinia";
import { menu } from "./service";

export const useMenuStore = defineStore("menuStore", {
  state: () => ({
    menu_items: null, // список новостей
    active_item: null, // список комментариев
    active_parent: null, // текущая категория
    loading: false, // Пока труе, идёт загрузка
    error: null,
  }),

  actions: {
    async loadMenuItems() {
      try {
        let res = await menu.get_menu_items();
        this.menu_items = res.data;
      } catch (error) {
        console.log(error);
      }
    },
  },
  getters: {
  },
});
