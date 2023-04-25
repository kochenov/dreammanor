import { defineStore } from "pinia";
import { news } from "./services/newsService";
//import UserService from "./userService";
//import { Notify } from "quasar";

export const useArticlesStore = defineStore("articlesStore", {
  state: () => ({
    news: null,
    comments: null,
    cur_cat_news: null,
    categories: null,
    pages: null,
    error: null,
    loading: false,
    count_news: 0,
    limit: 3,
  }),

  actions: {
    async loadInfoCategory(cat_id) {
      try {
        this.cur_cat_news = await news.get_info_cat(cat_id);
      } catch (error) {
        console.log(error.message);
      }
    },
    async getAllNews(category_id = 0, offset = 0, popular = 0) {
      try {
        let data = await news.list(category_id, this.limit, offset, popular);

        if (category_id != 0) {
          await this.loadInfoCategory(category_id);
        }

        this.count_news = data.details.count;
        this.news = data.data;
      } catch (error) {
        console.log(error.message);
      }
    },
    async getListCategories() {
      try {
        this.categories = await news.listCategories();
      } catch (error) {
        console.log(error.message);
      }
    },

    async getPost(category_id, post_id) {
      try {
        this.news = null;
        this.news = await news.get_news_post(category_id, post_id);
      } catch (error) {
        console.log(error.message);
      }
    },
  },
  getters: {},
});
