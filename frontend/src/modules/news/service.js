import { api } from "boot/axios";

/*
 * Добавьте перехватчик ответов
 */
api.interceptors.response.use(
  (response) => response,
  (error) => Promise.reject(error)
);

export const news = {
  async add_new_post(data) {
    try {
      let res = await api.post(`/news/add`, data);
      return res.status;
    } catch (error) {
      console.log(error);
      return false;
    }
  },
  async add_new_category(data) {
    try {
      let res = await api.post(`/news/add/new-category`, data);
      return res.status;
    } catch (error) {
      console.log(error);
      return false;
    }
  },
  /**
   * Получение поста
   * @param {*} post_id
   * @returns
   */
  async get_news_post(category_id, post_id) {
    try {
      let res = await api.get(`/news/category/${category_id}/post/${post_id}`);
      return res.data.data;
    } catch (error) {
      console.log(error.message);
    }
  },
  /**
   * Получение данных одной категории
   * @param {*} cat_id
   * @returns
   */
  async get_info_cat(cat_id) {
    try {
      let res = await api.get("/news/category-info/" + cat_id);
      return res.data.data;
    } catch (error) {
      console.log(error.message);
    }
  },
  /**
   * Получение списка новостей
   * @param {Number} category_id категория новости (0 по улолчанию)
   * @param {Number} limit настраивается в Store
   * @param {Number} offset количестро страниц пропустить для пагинации
   * @param {Number} popular сортировка по просмотрам
   * @returns
   */
  async get_news_posts(category_id, limit, offset, popular) {
    try {
      let res = await api.get(
        "/news?limit=" +
          limit +
          "&offset=" +
          offset +
          "&popular=" +
          popular +
          "&category=" +
          category_id
      );
      return res.data;
    } catch (error) {
      console.log(error.message);
      return False;
    }
  },
  /**
   * Получает список Категорий новостей
   * @returns
   */
  async listCategories() {
    try {
      let res = await api.get("/news/categories");
      return res.data.data;
    } catch (error) {
      console.log(error.message);
    }
  },
};
