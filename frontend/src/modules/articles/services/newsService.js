import { api } from "boot/axios";

/*
 * Добавьте перехватчик ответов
 */
api.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response && [401, 419].includes(error.response.status)) {
      console.info(
        "[401, 419]: Пользователь не авторизован, не удалось войти в систему с помощью API"
      );
    }
    return Promise.reject(error);
  }
);

export const news = {
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
  async list(category_id, limit, offset, popular) {
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
  /**
   * Получить комментарии к посту
   * @param {*} post_id
   * @returns
   */
  async comments(post_id) {
    try {
      let res = await api.get("/news.json");
      let temp = res.data.comments;
      let filtered = temp.filter((i) => i.news_post_id == post_id);
      return filtered;
    } catch (error) {
      console.log(error.message);
    }
  },
};
