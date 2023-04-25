import { defineStore } from "pinia";
import UserService from "./userService";
import { Notify } from "quasar";

export const useUserStore = defineStore("userStore", {
  state: () => ({
    user: null,
    error: null,
    loading: false,
  }),

  actions: {
    /**
     * @param {*} uid ID user
     * @param {*} payload  {name, email, online}
     */
    async createUser(uid, payload) {
      try {
        await UserService.createUser(uid, payload);
      } catch (error) {
        console.log(error.message);
      }
    },

    async getCurrentUser(uid) {
      try {
        let user = await UserService.getCurrentUser(uid);
        this.user = user.val() || null;
      } catch (error) {
        console.log(error);
      }
    },
  },
});
