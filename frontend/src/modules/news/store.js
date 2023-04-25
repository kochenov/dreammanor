import { defineStore } from "pinia";
import { news } from "./service";

export const useNewsStore = defineStore("newsStore", {
  state: () => ({
    posts: null, // список новостей
    comments: null, // список комментариев
    cur_category: null, // текущая категория
    categories: null, // список категорий
    loading: false, // Пока труе, идёт загрузка
    count_news: 0, // колисечтво постов
    limit: 9, // Количество постов
    open_add_news: false,
    open_add_news_category: false,
    error: null,
  }),

  actions: {
    /**
     * Загрузка информации о текущей категории
     * @param {*} cat_id
     */
    async loadInfoCategory(category_id) {
      try {
        this.cur_category = await news.get_info_cat(category_id);
      } catch (error) {
        console.log(error);
      }
    },
    async addNewPost(data) {
      try {
        let status = await news.add_new_post(data);
        await this.loadPosts();
        return status;
      } catch (error) {
        console.log(error);
        return false;
      }
    },
    async addNewCategory(data) {
      try {
        let status = await news.add_new_category(data);
        await this.loadCategories();
        return status;
      } catch (error) {
        console.log(error);
        return false;
      }
    },
    async loadPosts(category_id = 0, offset = 0, popular = 0) {
      try {
        this.loading = true;
        let data = await news.get_news_posts(
          category_id,
          this.limit,
          offset,
          popular
        );
        this.posts = data.data;
        this.count_news = data.details.count;
        this.loading = false;
        return true;
      } catch (error) {
        console.log(error);
        this.loading = false;
        return false;
      }
    },
    async loadCategories() {
      try {
        this.categories = await news.listCategories();
      } catch (error) {}
    },

    async getPost(category_id, post_id) {
      try {
        this.posts = await news.get_news_post(category_id, post_id);
      } catch (error) {
        console.log(error.message);
      }
    },
  },
  getters: {},
});
