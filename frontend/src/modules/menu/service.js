import { api } from "boot/axios";

/*
 * Добавьте перехватчик ответов
 */
api.interceptors.response.use(
  (response) => response,
  (error) => Promise.reject(error)
);

export const menu = {
  async get_menu_items() {
    try {
      let res = await api.get(`/menu/`);
      return res.data;
    } catch (error) {
      console.log(error);
      return false;
    }
  },
};
